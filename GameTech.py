class Page:
    def __init__(self, page_id, process_name=None):
        self.page_id = page_id
        self.process_name = process_name  # Which process owns this page

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
        self.pages = [Page(i) for i in range(num_pages)]  # Initialize memory as empty
        self.total_allocated_pages = 0

    def allocate_memory(self, process_name, num_pages_requested):
        free_pages = [page for page in self.pages if page.process_name is None]

        if len(free_pages) < num_pages_requested:
            return False  # Not enough free memory

        # Allocate consecutive pages to the process
        allocated_pages = free_pages[:num_pages_requested]
        for page in allocated_pages:
            page.allocate(process_name)

        self.total_allocated_pages += num_pages_requested
        return True

    def print_memory_status(self):
        print("\nCurrent Memory Allocation Status:")
        for page in self.pages:
            if page.process_name:
                print(f"Page {page.page_id} -> {page.process_name}")
            else:
                print(f"Page {page.page_id} -> Free")
        print("-" * 50)

    def print_total_memory_used(self):
        total_units = self.total_allocated_pages * self.page_size
        print(f"\nTotal Pages Allocated: {self.total_allocated_pages}")
        print(f"Total Memory Utilized: {total_units} units")


# Driver Code
memory_manager = MemoryManager(num_pages=256, page_size=16)

requests = [
    ("Game Session 1", 32),
    ("Game Session 2", 20),
    ("Game Session 3", 40),
    ("Game Session 4", 18),
    ("Game Session 5", 25)
]

for request in requests:
    process_name, num_pages_requested = request
    allocated = memory_manager.allocate_memory(process_name, num_pages_requested)
    if allocated:
        print(f"\nAllocated {num_pages_requested} pages for {process_name}")
        memory_manager.print_memory_status()
    else:
        print(f"\nNot enough memory available for {process_name} (requested {num_pages_requested} pages)")

memory_manager.print_total_memory_used()
