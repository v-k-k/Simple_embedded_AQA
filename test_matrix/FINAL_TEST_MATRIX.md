# Final Test Matrix

| ID | Quality Risk | Level | Test / Method | Environment | Expected | Evidence | Regression? | Status |
|---|---|---|---|---|---|---|---|---|
| R01 | Button bounce creates duplicate action | System | Repeated physical input | Wokwi/real | 1 event per press | counter/log | Yes | |
| R02 | UART command parsing fails | Interface | CLI positive/negative | Wokwi + Python | structured response | Serial/Pytest | Yes | |
| R03 | I2C/SPI transaction corrupted | Protocol | protocol trace analysis | analyzer | valid frames | trace | Yes | |
| R04 | Firmware hangs | Recovery | WDT fault injection | Wokwi/real | controlled recovery | reset log | Yes | |
| R05 | Critical state corrupted | Reliability | interrupted save | Wokwi/real | valid old/new state | before/after log | Yes | |
| R06 | Network unavailable | Network | NET DOWN/UP | simulation | controlled reconnect | network log | Yes | |
| R07 | Buffer overflow loses data silently | Network | offline overflow | simulation | defined policy | IDs/counters | Yes | |
| R08 | Long-run memory degradation | Reliability | repeated stress | simulation/real | stable trend | memory log | Yes | |
