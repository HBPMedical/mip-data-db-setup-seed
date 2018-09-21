BEGIN;

-- Plan the tests
SELECT plan( 2 );

SELECT is(count(*)::INT, 1, 'Subject should be present in CUSTOM_features table')
  FROM CUSTOM_features where id='P_0001';

SELECT is(count(*)::INT, 105, 'Missing rows in CUSTOM_features table?')
  FROM CUSTOM_features;

-- Clean up
SELECT * FROM finish();
ROLLBACK;
