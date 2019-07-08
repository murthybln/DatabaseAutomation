import query, database_results

"""Query returns no rows said to be a good test"""
def test_validate_query_pass():
    assert database_results.get_db_data(query.db_conn, query.query_pass) == 0


"""Query returns few rows said to be a failed test and need to be notified"""
def test_validate_query_fail():
    assert database_results.get_db_data(query.db_conn, query.query_fail) == 0, "query_fail script failed with errors"
