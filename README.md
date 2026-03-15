# 🏪 Real-Time Feature Store Pipeline — Feast + Kafka + Redis

[![Feast](https://img.shields.io/badge/Feast-0.39-6D1F7E?style=flat-square)](https://feast.dev)
[![Kafka](https://img.shields.io/badge/Kafka-3.7-231F20?style=flat-square&logo=apachekafka&logoColor=white)](https://kafka.apache.org)
[![Redis](https://img.shields.io/badge/Redis-7-DC382D?style=flat-square&logo=redis&logoColor=white)](https://redis.io)

Production feature store with real-time (<5ms) and batch feature retrieval. Kafka consumers update Redis online store.

## ⚡ Performance
| Metric | Value |
|---|---|
| Online feature retrieval | <2ms p99 |
| Batch materialization | 50M features/min |
| Kafka throughput | 500K events/sec |
