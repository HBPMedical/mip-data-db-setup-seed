SET datestyle to 'European';

CREATE TABLE "CUSTOM_features"
(
    "id" char(20),
    "feature1" numeric,
    "feature2" numeric,

    CONSTRAINT pk_CUSTOM_features PRIMARY KEY (id)
)
WITH (
    OIDS=FALSE
);
