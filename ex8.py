formatter="%s%s%s%s%s"
print formatter%("靠",2,3,4,5)
print formatter%("one","two","three","four","five")
print formatter%(True,False,False,True,False)
print formatter%(formatter,formatter,formatter,formatter,formatter)
print formatter%(
"I had this things.",
"That you could type up right.",
"But it did sing.",
"so I said goodnight.",
"so I said goodmorning."
)