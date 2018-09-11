BEGIN;

-- Plan the tests
SELECT plan( 4 );

SELECT has_table( 'CUSTOM_features' );

SELECT has_column( 'CUSTOM_features', 'id' );
SELECT col_is_pk(  'CUSTOM_features', 'id' );
SELECT has_column( 'CUSTOM_features', 'feature1' );
SELECT has_column( 'CUSTOM_features', 'feature2' );

-- Clean up
SELECT * FROM finish();
ROLLBACK;
