CC = cc
CFLAGS = -lm -std=c99
OBJS = FFT.o Random.o SOR.o MonteCarlo.o 

.SUFFIXES: .c .o

.c.o:
	$(CC) $(CFLAGS) -c $<

all: fft sor montecarlo  

fft: FFT.o Random.o
	$(CC) $(CFLAGS) -o FFT FFT.o Random.o

sor: SOR.o Random.o
	$(CC) $(CFLAGS) -o SOR SOR.o Random.o

montecarlo: MonteCarlo.o Random.o
	$(CC) $(CFLAGS) -o MonteCarlo MonteCarlo.o Random.o

clean:
	rm $(OBJS) FFT SOR MonteCarlo
