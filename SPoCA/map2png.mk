CC=g++
TRACKINGLFLAGS=-lpthread
IDLLFLAGS=-L /usr/local/idl/idl706/bin/bin.linux.x86_64 -lpthread -lidl -lXp -lXpm -lXmu -lXext -lXt -lSM -lICE  -lXinerama -lX11 -ldl -ltermcap -lrt -lm /usr/lib/libXm.a
MAGICKLFLAGS=`Magick++-config --ldflags --libs`
MAGICKCFLAGS=`Magick++-config --cppflags`
CFLAGS=-Wall -fkeep-inline-functions -g -O3 $(MAGICKCFLAGS) 
LFLAGS=-lcfitsio $(MAGICKLFLAGS) 
DFLAGS= -DMAGICK 

all:bin/map2png.x
clean: rm bin/map2png.x objects/map2png.o objects/MagickImage.o objects/ColorMap.o objects/SunImage.o objects/FitsFile.o objects/Coordinate.o objects/WCS.o objects/Image.o objects/Header.o objects/ArgParser.o objects/mainutilities.o objects/SUVIImage.o objects/HMIImage.o objects/SWAPImage.o objects/AIAImage.o objects/EUVIImage.o objects/EITImage.o objects/EUVImage.o objects/FeatureVector.o objects/tools.o


bin/map2png.x : map2png.mk objects/map2png.o objects/MagickImage.o objects/ColorMap.o objects/SunImage.o objects/FitsFile.o objects/Coordinate.o objects/WCS.o objects/Image.o objects/Header.o objects/ArgParser.o objects/mainutilities.o objects/SUVIImage.o objects/HMIImage.o objects/SWAPImage.o objects/AIAImage.o objects/EUVIImage.o objects/EITImage.o objects/EUVImage.o objects/FeatureVector.o objects/tools.o | bin
	$(CC) $(CFLAGS) $(DFLAGS) objects/map2png.o objects/MagickImage.o objects/ColorMap.o objects/SunImage.o objects/FitsFile.o objects/Coordinate.o objects/WCS.o objects/Image.o objects/Header.o objects/ArgParser.o objects/mainutilities.o objects/SUVIImage.o objects/HMIImage.o objects/SWAPImage.o objects/AIAImage.o objects/EUVIImage.o objects/EITImage.o objects/EUVImage.o objects/FeatureVector.o objects/tools.o $(LFLAGS) -o bin/map2png.x

objects/map2png.o : map2png.mk programs/map2png.cpp classes/tools.h classes/constants.h classes/mainutilities.h classes/ArgParser.h classes/ColorMap.h classes/MagickImage.h| objects
	$(CC) -c $(CFLAGS) $(DFLAGS) programs/map2png.cpp -o objects/map2png.o

objects/MagickImage.o : map2png.mk classes/MagickImage.cpp classes/constants.h| objects
	$(CC) -c $(CFLAGS) $(DFLAGS) classes/MagickImage.cpp -o objects/MagickImage.o

objects/ColorMap.o : map2png.mk classes/ColorMap.cpp classes/Header.h classes/SunImage.h classes/gradient.h classes/MagickImage.h| objects
	$(CC) -c $(CFLAGS) $(DFLAGS) classes/ColorMap.cpp -o objects/ColorMap.o

objects/SunImage.o : map2png.mk classes/SunImage.cpp classes/Image.h classes/WCS.h classes/Header.h classes/Coordinate.h classes/FitsFile.h| objects
	$(CC) -c $(CFLAGS) $(DFLAGS) classes/SunImage.cpp -o objects/SunImage.o

objects/FitsFile.o : map2png.mk classes/FitsFile.cpp classes/tools.h classes/constants.h classes/Header.h classes/Coordinate.h| objects
	$(CC) -c $(CFLAGS) $(DFLAGS) classes/FitsFile.cpp -o objects/FitsFile.o

objects/Coordinate.o : map2png.mk classes/Coordinate.cpp classes/constants.h| objects
	$(CC) -c $(CFLAGS) $(DFLAGS) classes/Coordinate.cpp -o objects/Coordinate.o

objects/WCS.o : map2png.mk classes/WCS.cpp classes/constants.h classes/Coordinate.h classes/FitsFile.h| objects
	$(CC) -c $(CFLAGS) $(DFLAGS) classes/WCS.cpp -o objects/WCS.o

objects/Image.o : map2png.mk classes/Image.cpp classes/tools.h classes/constants.h classes/Coordinate.h classes/FitsFile.h| objects
	$(CC) -c $(CFLAGS) $(DFLAGS) classes/Image.cpp -o objects/Image.o

objects/Header.o : map2png.mk classes/Header.cpp classes/constants.h| objects
	$(CC) -c $(CFLAGS) $(DFLAGS) classes/Header.cpp -o objects/Header.o

objects/ArgParser.o : map2png.mk classes/ArgParser.cpp | objects
	$(CC) -c $(CFLAGS) $(DFLAGS) classes/ArgParser.cpp -o objects/ArgParser.o

objects/mainutilities.o : map2png.mk classes/mainutilities.cpp classes/FeatureVector.h classes/EUVImage.h classes/EITImage.h classes/EUVIImage.h classes/AIAImage.h classes/SWAPImage.h classes/HMIImage.h classes/SUVIImage.h classes/ColorMap.h classes/Header.h classes/Coordinate.h| objects
	$(CC) -c $(CFLAGS) $(DFLAGS) classes/mainutilities.cpp -o objects/mainutilities.o

objects/SUVIImage.o : map2png.mk classes/SUVIImage.cpp classes/EUVImage.h classes/Header.h| objects
	$(CC) -c $(CFLAGS) $(DFLAGS) classes/SUVIImage.cpp -o objects/SUVIImage.o

objects/HMIImage.o : map2png.mk classes/HMIImage.cpp classes/EUVImage.h classes/Header.h| objects
	$(CC) -c $(CFLAGS) $(DFLAGS) classes/HMIImage.cpp -o objects/HMIImage.o

objects/SWAPImage.o : map2png.mk classes/SWAPImage.cpp classes/EUVImage.h classes/Header.h| objects
	$(CC) -c $(CFLAGS) $(DFLAGS) classes/SWAPImage.cpp -o objects/SWAPImage.o

objects/AIAImage.o : map2png.mk classes/AIAImage.cpp classes/EUVImage.h classes/Header.h| objects
	$(CC) -c $(CFLAGS) $(DFLAGS) classes/AIAImage.cpp -o objects/AIAImage.o

objects/EUVIImage.o : map2png.mk classes/EUVIImage.cpp classes/EUVImage.h classes/Header.h| objects
	$(CC) -c $(CFLAGS) $(DFLAGS) classes/EUVIImage.cpp -o objects/EUVIImage.o

objects/EITImage.o : map2png.mk classes/EITImage.cpp classes/EUVImage.h classes/Header.h| objects
	$(CC) -c $(CFLAGS) $(DFLAGS) classes/EITImage.cpp -o objects/EITImage.o

objects/EUVImage.o : map2png.mk classes/EUVImage.cpp classes/Coordinate.h classes/SunImage.h classes/MagickImage.h| objects
	$(CC) -c $(CFLAGS) $(DFLAGS) classes/EUVImage.cpp -o objects/EUVImage.o

objects/FeatureVector.o : map2png.mk classes/FeatureVector.cpp classes/constants.h| objects
	$(CC) -c $(CFLAGS) $(DFLAGS) classes/FeatureVector.cpp -o objects/FeatureVector.o

objects/tools.o : map2png.mk classes/tools.cpp classes/constants.h| objects
	$(CC) -c $(CFLAGS) $(DFLAGS) classes/tools.cpp -o objects/tools.o

objects : 
	 mkdir -p objects

bin : 
	 mkdir -p bin
