BEGIN;

-- Plan the tests
SELECT plan( 6 );

SELECT is(count(*)::INT, 1, 'Subject should be present in mip_cde_features table')
  FROM mip_cde_features where subjectcode='P_0001';

SELECT is(count(*)::INT, 105, 'Missing rows in mip_cde_features table?')
  FROM mip_cde_features;

SELECT is(count(*)::INT, 1, 'Subject should be present in CUSTOM_features table')
  FROM CUSTOM_features where subjectcode='P_0001';

SELECT is(count(*)::INT, 105, 'Missing rows in CUSTOM_features table?')
  FROM CUSTOM_features;

SELECT is(count(*)::INT, 1, 'Subject should be present in mip_local_features table')
  FROM mip_local_features where subjectcode='P_0001';

SELECT is(count(*)::INT, 105, 'Missing rows in mip_local_features table?')
  FROM mip_local_features;

-- Clean up
SELECT * FROM finish();
ROLLBACK;
