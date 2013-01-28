Summary: srecord programs
Name: srecord
Version: 1.61
Release: alt1
License: GPL
Group: Development/Tools
Source: http://srecord.sourceforge.net/%name-%version.tar.gz
URL: http://srecord.sourceforge.net/
BuildPrereq: boost-devel, diffutils, ghostscript, groff, libgcrypt-devel
BuildPrereq: libtool, sharutils

# Automatically added by buildreq on Mon Jan 28 2013
# optimized out: fontconfig fonts-ttf-gnu-freefont-mono fonts-ttf-gnu-freefont-sans fonts-ttf-gnu-freefont-serif fonts-type1-urw ghostscript-classic ghostscript-common groff-base libgpg-error libgpg-error-devel libstdc++-devel
BuildRequires: azenis-fonts-ttf boost-devel-headers cups-filters ghostscript-utils groff-ps libgcrypt-devel ruby ruby-stdlibs
BuildRequires: fonts-otf-oldstandard fonts-otf-stix fonts-ttf-armenian fonts-ttf-baekmuk-batang fonts-ttf-baekmuk-dotum
BuildRequires: fonts-ttf-baekmuk-gulim fonts-ttf-baekmuk-hline fonts-ttf-bengali fonts-ttf-chinese-big5 fonts-ttf-chinese-gb2312
BuildRequires: fonts-ttf-church fonts-ttf-dejavu fonts-ttf-dejavu-lgc fonts-ttf-devanagari fonts-ttf-freefont fonts-ttf-georgian
BuildRequires: fonts-ttf-gost fonts-ttf-gw fonts-ttf-java-1.6.0-sun fonts-ttf-junicode fonts-ttf-kannada fonts-ttf-latex-xft
BuildRequires: fonts-ttf-liberation fonts-ttf-malayalam fonts-ttf-ms fonts-ttf-oldstandard fonts-ttf-reduce fonts-ttf-sazanami-gothic
BuildRequires: fonts-ttf-sazanami-mincho fonts-ttf-sil-gentium fonts-ttf-syriac fonts-ttf-tamil fonts-ttf-tempora fonts-ttf-urdu
BuildRequires: fonts-ttf-vera fonts-ttf-xorg fonts-ttf-znamen fonts-type1-cm-super-pfb fonts-type1-dmtr40in fonts-type1-phonetic
BuildRequires: fonts-type1-xorg gcc-c++

%description
The srecord package is a collection of powerful tools for manipulating EPROM
load files. It reads and writes numerous EPROM file formats, and can perform
many different manipulations.

%package -n lib%name
Summary: srecord libraries
Group: Development/Tools

%description -n lib%name
This package contains the shared libraries for programs that manipulate EPROM
load files.

%package devel
Summary: srecord development files
Group: Development/Tools

%description devel
This package contains static libraries and header files for compiling programs
that manipulate EPROM load files.

%prep
%setup -q

%build
%configure
%make_build

%install
%makeinstall DESTDIR=%buildroot
%__rm -f $RPM_BUILD_ROOT/usr/lib/*.la

%check
%make sure

%files
%doc LICENSE BUILDING README
%_datadir/doc/srecord/*
%_bindir/srec_cat
%_bindir/srec_cmp
%_bindir/srec_info
%_man1dir/*
%_man5dir/*

%files -n lib%name
%_libdir/libsrecord.so.*

%files devel
%dir %_includedir/srecord
%_includedir/srecord/*
%_libdir/pkgconfig/srecord.pc
%_libdir/libsrecord.a
%_libdir/libsrecord.so
%_man3dir/*

%changelog
* Mon Jan 28 2013 Grigory Milev <week@altlinux.ru> 1.61-alt1
- Initial build for ALTLinux

