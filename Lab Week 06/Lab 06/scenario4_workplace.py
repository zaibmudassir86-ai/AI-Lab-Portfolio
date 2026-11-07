from lab6_search import Retriever, show_hits
records = [{'id': 'remote:staff', 'audience': 'employee', 'text': 'Employees may request remote work with manager approval.'}, {'id': 'remote:contractor', 'audience': 'contractor', 'text': 'Contractors may work remotely only when the signed contract explicitly permits remote work.'}]
engine = Retriever(records)
show_hits(engine.search('contractor remote work eligibility', k=1, filters={"audience": "contractor"}))
