# branch-prediction
Branch prediction simulation and experiments

# TODO

## benchmarks
- echo program as basic baseline program

## benchmark properties
- echo and loop condition have shorter traces

## experiments

### two bit
- overall improvement as table size increases as expected
- compared to over 30% for other benchmarks
- loop causing saturating counters to be overwritten lead to low prediction because cannot recognise branches
- scimark programs not achieving high growth in prediction rate

### correlating
- overall behaviour -> good as table size increases
- benchmarks begin with high prediction rate
- has more memory to deal with collisions

- at low table size, benchmarks still have a peak performance before dropping in history bits

### gshare
- change graph to include 2 table size
- does poorly in beginning -> trying to spread collisions on already tiny address space -> more overwriting addresses/collisions than two bit
- make comparison graph of loop benchmark

### comparison
- get averages to plot 'best' version of predictor strategies together to compare

## conclusion
- cost of branch prediction -> hardware and cost of prediction
