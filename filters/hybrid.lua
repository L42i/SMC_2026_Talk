--[[
hybrid.lua — write a talk once, get slides and a readable page.

  ::: prose          Body text on the page; speaker notes in the slides.
  ::: slides-only    Shown only in the deck  (big numbers, terse cues).
  ::: page-only      Shown only on the page  (extra context, long captions).

  ## Title {background-image="pictures/x.jpg"}
                     Photo background in the deck; on the page the photo
                     is placed under the heading instead (pages have no
                     slide backgrounds).
]]

local slides = quarto.doc.is_format("revealjs")

local function drop_class(el, cls)
  el.classes = el.classes:filter(function(c) return c ~= cls end)
  return el
end

function Div(el)
  local c = el.classes
  if c:includes("prose") then
    if slides then
      el.classes = pandoc.List({ "notes" })
      return el
    end
    return drop_class(el, "prose")
  elseif c:includes("slides-only") then
    if slides then return drop_class(el, "slides-only") end
    return {}
  elseif c:includes("page-only") then
    if slides then return {} end
    return drop_class(el, "page-only")
  end
end

-- The abstract introduces the page; the deck's title slide stays clean.
function Meta(m)
  if slides then m.abstract = nil end
  return m
end

function Header(el)
  if slides then return nil end
  local bg = el.attributes["background-image"]
  if not bg then return nil end
  -- strip slide-only attributes so they don't leak into the page HTML
  for _, k in ipairs({ "background-image", "background-opacity",
                       "background-size", "background-position",
                       "background-color" }) do
    el.attributes[k] = nil
  end
  local img = pandoc.Image({}, bg, "", pandoc.Attr("", { "section-photo" }))
  img.attributes["alt"] = pandoc.utils.stringify(el.content)
  return { el, pandoc.Plain({ img }) }
end
