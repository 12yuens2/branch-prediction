CC = cc
CFLAGS = -lm -std=c99
OBJS = FFT.o Random.o SOR.o MonteCarlo.o
OUT = prog

.SUFFIXES: .c .o

.c.o:
	$(CC) $(CFLAGS) -c $<

all: setup fft sor montecarlo  

setup:
	mkdir -p $(OUT)

fft: FFT.o Random.o
	$(CC) $(CFLAGS) -o $(OUT)/FFT FFT.o Random.o

sor: SOR.o Random.o
	$(CC) $(CFLAGS) -o $(OUT)/SOR SOR.o Random.o

montecarlo: MonteCarlo.o Random.o
	$(CC) $(CFLAGS) -o $(OUT)/MonteCarlo MonteCarlo.o Random.o

clean:
	rm -rf $(OBJS) $(OUT)
