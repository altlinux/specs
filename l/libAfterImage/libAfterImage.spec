# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/find /usr/bin/perl /usr/bin/pkg-config /usr/bin/xargs gcc-c++ libXpm-devel libgif-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           libAfterImage
Version:        1.20
Release:        alt1_14
Summary:        A generic image manipulation library

Group:          System/Libraries
License:        LGPLv2+
URL:            http://www.afterstep.org/afterimage/index.php
Source0:        ftp://ftp.afterstep.org/stable/libAfterImage/libAfterImage-1.20.tar.bz2
Source1:        libAfterImage-COPYING
Patch0:         libAfterImage-Makefile-ldconfig.patch
Patch1:         libAfterImage-afterimage-config.patch
Patch2:         libAfterImage-multiarch.patch

# use gentoo patch to fix some issues with libpng
Patch100:       http://sources.gentoo.org/cgi-bin/viewvc.cgi/gentoo-x86/media-libs/libafterimage/files/libafterimage-libpng15.patch

BuildRequires:  libfreetype-devel
BuildRequires:  zlib-devel
BuildRequires: libtiffxx-devel libtiff-devel
BuildRequires:  libpng-devel
BuildRequires:  libungif-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libGL-devel
BuildRequires:  gawk
Source44: import.info
Patch33: libAfterImage-1.20-alt-fix-linkage.patch

%description
libAfterImage   is a generic image manipulation library. It was initially
implemented to address AfterStep Window Manager's needs for image handling,
but it evolved into extremely powerful and flexible software, suitable for
virtually any project that has needs for loading, manipulating, displaying
images, as well as writing images in files. Most of the popular image formats
are supported using standard libraries, with XCF, XPM, PPM/PNM, BMP, ICO,
TGA and GIF being supported internally.

PNG, JPEG and TIFF formats are supported via standard libraries.

Powerful text rendering capabilities included, providing support for
TrueType fonts using FreeType library, and anti-aliasing of standard fonts
from X window system. 

%package devel
Summary:  Files needed for software development with %{name}
Group:    Development/C
Requires: %{name} = %{version}

%description devel
The %{name}-devel package contains the files needed for development with
%{name}

%prep
%setup -q
%patch0 
%patch1
%patch2 -b multiarch
%patch100 -b libpng15
%patch33 -p1
# copies
rm -rf libjpeg/ libpng/ libungif/ zlib/
sed -i -e '/zlib\/zlib\.h/d' .depend


%build
%configure --enable-i18n --enable-sharedlibs \
--with-xpm --without-builtin-ungif --disable-staticlibs --enable-glx \
--without-afterbase --disable-mmx-optimization \
--x-includes=%{_includedir} --x-libraries=%{_libdir}

make CCFLAGS="-DNO_DEBUG_OUTPUT -fPIC $RPM_OPT_FLAGS" %{?_smp_mflags} \
LIBAFTERIMAGE_PATH=../


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}
make install DESTDIR=$RPM_BUILD_ROOT LIBAFTERIMAGE_PATH=../

cp %{SOURCE1} %{_builddir}/%{name}-%{version}/COPYING

touch -r ChangeLog $RPM_BUILD_ROOT%{_bindir}/afterimage-{config,libs}

%files
%doc README ChangeLog COPYING
%{_libdir}/*.so.*

%files devel
%{_bindir}/*
%{_includedir}/libAfterImage/
%{_libdir}/*.so

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1_14
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1_13
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1_11
- update to new release by fcimport

* Thu Oct 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1_10
- Sisyphus build

