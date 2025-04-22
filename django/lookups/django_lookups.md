[ Django ORM - Queries & Lookups ]
|
├── 🎯 1. Basic Filters (Where)
|    ├── exact          → field=value
|    ├── iexact         → case-insensitive exact
|    ├── contains       → field contains value
|    ├── icontains      → case-insensitive contains
|    ├── in             → field in list
|    ├── isnull         → field IS NULL
|    ├── regex / iregex → regex matching
|
├── 🔢 2. Comparison Operators
|    ├── gt  → greater than
|    ├── gte → greater than or equal
|    ├── lt  → less than
|    ├── lte → less than or equal
|    └── Example:
|         Product.objects.filter(price__gt=100)
|
├── 🔗 3. Relationship Lookups (Join via __)
|    ├── author__name='Ahmed'
|    ├── book__title__icontains='Python'
|    ├── category__parent__name='Tech'
|    └── Used to filter across ForeignKey / OneToOne / ManyToMany
|
├── 💣 4. F() Expressions (Column vs Column)
|    ├── Compare two fields → stock__gt=F('sold')
|    ├── Update value based on itself → stock = F('stock') + 5
|    └── Useful in filters & updates
|
├── 🧮 5. Aggregation (Summary – one value)
|    ├── Sum('field')
|    ├── Avg('field')
|    ├── Count('field')
|    ├── Max / Min
|    └── Example:
|         Book.objects.aggregate(Sum('pages'))
|
├── 🧩 6. Annotation (Add field per row)
|    ├── Add calculated field for each row
|    ├── Example:
|         Author.objects.annotate(book_count=Count('book'))
|    └── Can combine with filters/order_by etc.
|
├── ⚡ 7. select_related (1-to-1 or ForeignKey)
|    ├── Optimizes by JOIN
|    ├── Example:
|         Book.objects.select_related('author')
|    └── Works with single-value relationships
|
├── 🕸 8. prefetch_related (Reverse / ManyToMany)
|    ├── Optimizes via 2 queries
|    ├── Example:
|         Author.objects.prefetch_related('book_set')
|    └── Used for many-related objects
|
└── 🧠 Bonus: Q objects (OR / complex filters)
     ├── from django.db.models import Q
     ├── Product.objects.filter(Q(price__gt=100) | Q(sale=True))
     └── Useful when using OR / NOT
