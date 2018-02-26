%define rver	06
%define major	0

Summary: Internet Low Bitrate Codec (iLBC) library
Name: libilbc
Version: 0.6
Release: alt6
License: Freeware
Group: System/Libraries
Url: http://www.ilbcfreeware.org/
Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: http://www.ietf.org/rfc/rfc3951.txt.bz2
Source1: http://www.ilbcfreeware.org/documentation/extract-cfile.awk.bz2
Source2: http://www.ilbcfreeware.org/documentation/gips_iLBClicense.pdf.bz2
BuildRequires: gawk

%description
iLBC (internet Low Bitrate Codec) is a FREE speech codec suitable
for robust voice communication over IP. The codec is designed for
narrow band speech and results in a payload bit rate of 13.33
kbit/s with an encoding frame length of 30 ms and 15.20 kbps with
an encoding length of 20 ms. The iLBC codec enables graceful
speech quality degradation in the case of lost frames, which
occurs in connection with lost or delayed IP packets.

%package -n %name-devel
Summary: Library and header files for the iLBC library
Group: Development/C
Requires: %name = %version

%description -n	%name-devel
iLBC (internet Low Bitrate Codec) is a FREE speech codec suitable
for robust voice communication over IP. The codec is designed for
narrow band speech and results in a payload bit rate of 13.33
kbit/s with an encoding frame length of 30 ms and 15.20 kbps with
an encoding length of 20 ms. The iLBC codec enables graceful
speech quality degradation in the case of lost frames, which
occurs in connection with lost or delayed IP packets.

This package contains the library and header files.

%package devel-static
Summary: Static library and header files for the iLBC library
Group: Development/C
Requires: %name-devel = %version

%description devel-static
iLBC (internet Low Bitrate Codec) is a FREE speech codec suitable
for robust voice communication over IP. The codec is designed for
narrow band speech and results in a payload bit rate of 13.33
kbit/s with an encoding frame length of 30 ms and 15.20 kbps with
an encoding length of 20 ms. The iLBC codec enables graceful
speech quality degradation in the case of lost frames, which
occurs in connection with lost or delayed IP packets.

This package contains the static library and header files.

%prep
%setup -q -c -T -n %name-%version
bzcat %SOURCE0 > rfc3951.txt
bzcat %SOURCE1 > extract-cfile.awk
bzcat %SOURCE2 > gips_iLBClicense.pdf

awk -f extract-cfile.awk rfc3951.txt

# please teach me indent someday...
%__subst "s|^\ \ \ ||g" *.[ch]

%build
# construct a makefile on the fly
cat > Makefile << EOF
CC=gcc
CFLAGS+=-fPIC -D_REENTRANT
LIB=libilbc.a
SHLIB=libilbc.so

OBJS=anaFilter.o iCBSearch.o packing.o \\
        constants.o gainquant.o iLBC_decode.o StateConstructW.o \\
        createCB.o getCBvec.o iLBC_encode.o StateSearchW.o doCPLC.o \\
        helpfun.o syntFilter.o enhancer.o hpInput.o LPCdecode.o \\
        filter.o hpOutput.o LPCencode.o FrameClassify.o iCBConstruct.o lsf.o

all: shared static

shared: \$(OBJS)
	\$(CC) -Wl,-soname,\$(SHLIB).%major -shared \$(CFLAGS) -o \$(SHLIB).%major.%version *.o -lm

static: \$(OBJS)
	ar cr \$(LIB) \$(OBJS)
	ranlib \$(LIB)
EOF

%make CFLAGS="%optflags -fPIC -DPIC -D_REENTRANT"

%install
install -d %buildroot%_includedir/ilbc
install -d %buildroot%_libdir

install -m0755 %name.so.%major.%version %buildroot%_libdir/
ln -snf %name.so.%major.%version %buildroot%_libdir/%name.so.%major
ln -snf %name.so.%major.%version %buildroot%_libdir/%name.so

install -m0644 %name.a %buildroot%_libdir/
install -m0644 *.h %buildroot%_includedir/ilbc/

%files -n %name
%_libdir/*.so.*

%files -n %name-devel
%doc gips_iLBClicense.pdf
%doc rfc3951.txt extract-cfile.awk
%_includedir/ilbc
%_libdir/*.so

%files -n %name-devel-static
%_libdir/*.a

%changelog
* Wed May 25 2011 Denis Smirnov <mithraen@altlinux.ru> 0.6-alt6
- rebuild

* Sun Oct 10 2010 Denis Smirnov <mithraen@altlinux.ru> 0.6-alt5
- auto rebuild

* Sat Nov 15 2008 Denis Smirnov <mithraen@altlinux.ru> 0.6-alt4
- remove post_ldconfig/pre_ldconfig
- cleanup spec
- move static library to separate package

* Wed Jan 24 2007 Denis Smirnov <mithraen@altlinux.ru> 0.6-alt3
- Cleanup spec

* Sun Mar 19 2006 Denis Smirnov <mithraen@altlinux.ru> 0.6-alt2
- fixed build with --as-needed

* Sat May 07 2005 Denis Smirnov <mithraen@altlinux.ru> 0.6-alt1
- build

* Sat May 07 2005 Motsyo Gennadi <drool_linux@pisem.net> 0.6-alt1.drool
- build for ALT Linux

* Sun Mar 13 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.6-1mdk
- 0.6 (final rfc3951)
- use the %%mkrel macro
- new S1 and S2

* Sun Sep 26 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.5-1mdk
- initial mandrake package
