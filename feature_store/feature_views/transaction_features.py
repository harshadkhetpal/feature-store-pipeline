# Author: Harshad Khetpal <harshadkhetpal@gmail.com>
from datetime import timedelta
from feast import Entity, FeatureView, Field, PushSource, BigQuerySource
from feast.types import Float32, Int64, String, Bool

customer = Entity(name="customer_id", description="Customer identifier", join_keys=["customer_id"])

transaction_source = BigQuerySource(
    name="transactions",
    table="harshad-ml.features.transactions",
    timestamp_field="event_timestamp",
)

transaction_features = FeatureView(
    name="transaction_features",
    entities=[customer],
    ttl=timedelta(days=7),
    schema=[
        Field(name="tx_amount_last_1h", dtype=Float32),
        Field(name="tx_count_last_24h", dtype=Int64),
        Field(name="merchant_risk_score", dtype=Float32),
        Field(name="is_foreign_tx", dtype=Bool),
    ],
    online=True,
    source=transaction_source,
)
