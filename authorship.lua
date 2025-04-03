local refs_filter = {
	Para = function(para)
		for i = 1, #para.content - 3 do
			print(para.content[i])
			this = para.content[i]
			if this.t == "Space" then
				-- skip
			elseif this.t == "Str" then
				if this.text:sub(-1) == "*" or this.text:sub(-2) == "*," then
					-- equal contribution
					para.content[i] = pandoc.Underline(pandoc.Str(this.text:gsub("*", "")))
					para.content[i + 1] = pandoc.Underline(para.content[i + 1])
					para.content[i + 2] = pandoc.Underline(para.content[i + 2])
				end
				if this.text:sub(1, 9) == "Úradník" then
					-- make it italic
					para.content[i] = pandoc.Strong(para.content[i])
					para.content[i + 2] = pandoc.Strong(para.content[i + 2])
				end
			end
		end
		return para
	end
}

return {
	{
		Div = function(div)
			if div.identifier == "refs" then
				-- apply refs_filter
				return div:walk(refs_filter)
			end
			return div
		end
	}
}
