CC = cc
CFLAGS = -lm
OBJS = FFT.o Random.o SOR.o SparseCompRow.o \
	array.o MonteCarlo.o LU.o 

.SUFFIXES: .c .o

.c.o:
	$(CC) $(CFLAGS) -c $<

all: fft sor montecarlo lu  

fft: FFT.o 
	$(CC) $(CFLAGS) -o FFT FFT.o

sor: SOR.o Random.o
	$(CC) $(CFLAGS) -o SOR SOR.o Random.o

montecarlo: MonteCarlo.o Random.o
	$(CC) $(CFLAGS) -o MonteCarlo MonteCarlo.o Random.o

lu: LU.o Random.o
	$(CC) $(CFLAGS) -o LU LU.o Random.o

scimark2 : scimark2.o $(OBJS)
	$(CC) $(CFLAGS) -o scimark2 scimark2.o $(OBJS) -lm

clean:
	rm $(OBJS) scimark2
