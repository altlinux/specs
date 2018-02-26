Name: CBFlib
Version: 0.9.2.3
Release: alt2

Summary: Crystallographic Binary File and Image Library
# library files (*.so*) are LGPLv2+, all else is GPLv2+
License: GPLv2+ and (GPLv2+ or LGPLv2+)
Group: System/Libraries

Url: http://www.bernstein-plus-sons.com/software/CBF
Source: http://downloads.sourceforge.net/cbflib/%name-%version.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-fortran

%description
CBFlib (Crystallographic Binary File library) is a library of ANSI-C
functions providing a simple mechanism for accessing Crystallographic
Binary Files (CBF files) and Image-supporting CIF (imgCIF) files.
The CBFlib API is loosely based on the CIFPARSE API for mmCIF files.
Like CIFPARSE, CBFlib does not perform any semantic integrity checks;
rather it simply provides functions to create, read, modify and write
CBF binary data files and imgCIF ASCII data files.

%package -n lib%name
Summary: Shared library for programs that use CBF.
License: LGPLv2+
Group: System/Libraries

%description -n lib%name
This package includes the shared library files for running
applications that use Crystallographic Binary File.

%package -n lib%name-devel
Summary: Header files and library for developing programs with cbf
License: LGPLv2+ and GPLv2+
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains libraries and header files needed for program
development using the crystallographic binary file and image library.

%package utils
Summary: CBF utilities
License: GPLv2+
Group: Sciences/Chemistry

%description utils
This package contains CBF (Crystallographic Binary File) utilities.

%prep
%setup
# various cleanups
iconv -f iso8859-15 -t utf-8 doc/cif_img_1.5.3_8Jul07.dic \
> doc/cif_img_1.5.3_8Jul07.dic.conv \
&& mv -f doc/cif_img_1.5.3_8Jul07.dic.conv doc/cif_img_1.5.3_8Jul07.dic
rm doc/.symlinks
rm doc/.undosymlinks
mv doc/gpl.txt .

%build
cd src
gcc -fPIC -DCBF_DONT_USE_LONG_LONG -D_USE_XOPEN_EXTENDED %optflags \
	-c *.c ../examples/img.c -I../include/ -I../examples/
gcc -shared -Wl,-soname,libcbf.so.0 -o libcbf.so.0.0.0 *.o -lm
rm *.o
gfortran -fPIC -fno-range-check %optflags -c *.f90 -I../include/
gfortran -shared -Wl,-soname,libfcb.so.0 -o libfcb.so.0.0.0 *.o

cd ../examples
utilsublist="adscimg2cbf
cbf2adscimg
adscimg2cbf"
for i in $utilsublist; do
	gcc $i.c ${i}_sub.c -I../include ../src/libcbf.so.0.0.0 -o $i
done
utillist="convert_image
convert_minicbf
makecbf
img2cif
cif2cbf
cif2c"
for i in $utillist; do
	gcc $i.c -I../include ../src/libcbf.so.0.0.0 -o $i -lm
done

%install
mkdir -p %buildroot%_libdir
install -pm644 src/*.so* %buildroot%_libdir/
pushd %buildroot%_libdir
ln -sf libcbf.so.* libcbf.so
ln -sf libfcb.so.* libfcb.so
popd

mkdir -p %buildroot%_bindir
utilsublist="adscimg2cbf
cbf2adscimg
adscimg2cbf"
for i in $utilsublist; do
	install -pm755 examples/$i %buildroot%_bindir/
done
utillist="convert_image
convert_minicbf
makecbf
img2cif
cif2cbf
cif2c"
for i in $utillist; do
	install -pm755 examples/$i %buildroot%_bindir/
done

mkdir -p %buildroot%_includedir/cbf
install -pm644 include/* %buildroot%_includedir/cbf/
install -pm644 examples/img.h %buildroot%_includedir/cbf/

%files -n lib%name
%doc README gpl.txt
# LGPLv2+
%_libdir/libcbf.so.*
%_libdir/libfcb.so.*

%files -n lib%name-devel
# GPLv2+
%doc doc
# LGPLv2+
%_libdir/libcbf.so
%_libdir/libfcb.so
# GPLv2+
%_includedir/cbf

%files utils
# GPLv2+
%_bindir/adscimg2cbf
%_bindir/cbf2adscimg
%_bindir/adscimg2cbf
%_bindir/convert_image
%_bindir/convert_minicbf
%_bindir/makecbf
%_bindir/img2cif
%_bindir/cif2cbf
%_bindir/cif2c

%changelog
* Fri Sep 23 2011 Michael Shigorin <mike@altlinux.org> 0.9.2.3-alt2
- drop empty package

* Fri Sep 23 2011 Michael Shigorin <mike@altlinux.org> 0.9.2.3-alt1
- initial build for ALT Linux Sisyphus based on
  http://www.stanford.edu/~fenn/packs/CBFlib.spec
- libraries and utilities moved to subpackages
- considerable spec cleanup

* Fri Jul 01 2011 Tim Fenn <fenn@stanford.edu> - 0.9.2.1-1
- update to 0.9.2.2 (removes pycifrw dependency)

* Mon Nov 15 2010 Tim Fenn <fenn@stanford.edu> - 0.9.1-1
- update to 0.9.1rc2
- add lm to linker for utils

* Mon Mar 08 2010 Tim Fenn <fenn@stanford.edu> - 0.9.0-1
- update to 0.9.0
- include examples

* Wed Dec 09 2009 Tim Fenn <fenn@stanford.edu> - 0.8.1-2
- add a define to cflags
- fix up doc
- license update

* Wed Sep 16 2009 Tim Fenn <fenn@stanford.edu> - 0.8.1-1
- initial build
