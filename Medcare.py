class Page:
    def __init__(self, page_id, process_name=None):
        self.page_id = page_id
        self.process_name = process_name  # Department currently using the page

    def allocate(self, process_name):
        self.process_name = process_name

    def deallocate(self):
        self.process_name = None

    def __str__(self):
        if self.process_name:
            return f"Page {self.page_id} -> {self.process_name}"
        else:
            return f"Page {self.page_id} -> Free"


class MemoryManager:
    def __init__(self, num_pages, page_size):
        self.num_pages = num_pages
        self.page_size = page_size
        self.pages = [Page(i) for i in range(num_pages)]  # Initialize memory pages
        self.total_allocated_pages = 0

    def allocate_memory(self, process_name, num_pages_requested):
        free_pages = [page for page in self.pages if page.process_name is None]

        if len(free_pages) < num_pages_requested:
            return False  # Not enough memory available

        # Allocate consecutive pages
        allocated_pages = free_pages[:num_pages_requested]
        for page in allocated_pages:
            page.allocate(process_name)

        self.total_allocated_pages += num_pages_requested
        return True

    def print_memory_status(self):
        print("\nCurrent Memory Allocation Status:")
        for page in self.pages:
            print(str(page))
        print("-" * 50)

    def print_total_memory_used(self):
        total_units = self.total_allocated_pages * self.page_size
        print(f"\nTotal Pages Allocated: {self.total_allocated_pages}")
        print(f"Total Memory Utilized: {total_units} units")


# Driver Code
memory_manager = MemoryManager(num_pages=300, page_size=1)

requests = [
    ("Emergency Department", 50),
    ("Radiology Department", 35),
    ("Laboratory Department", 45),
    ("Patient Records System", 60),
    ("Surgery Department", 40)
]

for request in requests:
    process_name, num_pages_requested = request
    allocated = memory_manager.allocate_memory(process_name, num_pages_requested)
    if allocated:
        print(f"\nAllocated {num_pages_requested} pages for {process_name}")
        memory_manager.print_memory_status()
    else:
        print(f"\nNot enough memory available for {process_name} (requested {num_pages_requested} pages)")

# Final memory utilization
memory_manager.print_total_memory_used()
