from saramin import extract_saramin_pages, extract_saramin_jobs
from save import save_to_file

last_saramin_pages = extract_saramin_pages()

saramin_jobs = extract_saramin_jobs(last_saramin_pages)

save_to_file(saramin_jobs)