CC=gcc
OBJDIR = ./obj
SRCDIR = ./src
IDIR = ./include
LIBDIR = ./lib
TESTDIR = ./test
#TOBJDIR = ./src/test/obj

SRC = $(wildcard $(SRCDIR)/*.c)
DEPS := $(wildcard $(IDIR)/*.h)
OBJ = $(SRC:.c=.o)
OBJ := $(OBJ:$(SRCDIR)/=$(OBJDIR)/)
TESTS = $(wildcard $(TESTDIR)/*.c)
TOBJ = $(TESTS:.c=.o)
TOBJ := $(TOBJ:$(TESTDIR)/=$(OBJDIR))

#OBJ = $(patsubst %,$(OBJDIR)/%,$(_OBJ))
CFLAGS = -I$(IDIR) -Wall -g
LDFLAGS = -lwiringPi -lwiringPiDev

all: $(OBJ)

$(OBJDIR)/%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS) $(LDFLAGS)

lcd: $(OBJ)
	$(CC) -o $@ $^ $(LDFLAGS)

perf: $(TOBJ) $(OBJ) 
	$(CC) -o $@ $^ $(CFLAGS) $(LDFLAGS)

.PHONY: clean
clean:
	rm -f $(OBJ) $(TOBJ) lcd perf