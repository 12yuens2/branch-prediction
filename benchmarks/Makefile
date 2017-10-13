CC = cc
CFLAGS = -lm -std=c99
OBJS = FFT.o Random.o SOR.o MonteCarlo.o Loop.o LoopCondition.o BubbleSort.o
OUT = prog

.SUFFIXES: .c .o

.c.o:
	$(CC) $(CFLAGS) -c $<

all: setup fft sor montecarlo loop loopcond sort

setup:
	mkdir -p $(OUT)

fft: FFT.o Random.o
	$(CC) $(CFLAGS) -o $(OUT)/FFT FFT.o Random.o

sor: SOR.o Random.o
	$(CC) $(CFLAGS) -o $(OUT)/SOR SOR.o Random.o

montecarlo: MonteCarlo.o Random.o
	$(CC) $(CFLAGS) -o $(OUT)/MonteCarlo MonteCarlo.o Random.o

loop: Loop.o
	$(CC) $(CFLAGS) -o $(OUT)/Loop Loop.o

loopcond: LoopCondition.o
	$(CC) $(CFLAGS) -o $(OUT)/LoopCondition LoopCondition.o

sort: BubbleSort.o
	$(CC) $(CFLAGS) -o $(OUT)/BubbleSort BubbleSort.o

clean:
	rm -rf $(OBJS) $(OUT)
