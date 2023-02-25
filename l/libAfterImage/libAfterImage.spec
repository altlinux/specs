# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ imake libXpm-devel libXt-devel libglvnd-devel xorg-cf-files
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libAfterImage
Version:        1.20
Release:        alt1_31
Summary:        A generic image manipulation library

License:        LGPLv2+
URL:            http://www.afterstep.org/afterimage/index.php
Source0:        ftp://ftp.afterstep.org/stable/%{name}/%{name}-%{version}.tar.bz2
Source1:        %{name}-COPYING
#               Don't call ldconfig as part of "make install"
Patch0:         %{name}-Makefile-ldconfig.patch
#               Port to libpng 1.5 and later (patch from gentoo)
Patch1:         %{name}-libpng15.patch
#               Port to giflib version 5 and allow unbundling of giflib
Patch2:         %{name}-unbundle-libgif.patch
#               Link the shared library with its dependencies
Patch3:         %{name}-link.patch
#               Patch configure script for C99 compatibility.
Patch4:         %{name}-configure-c99.patch

BuildRequires:  gcc
BuildRequires:  libfreetype-devel
BuildRequires:  zlib-devel
BuildRequires:  libtiff-devel libtiffxx-devel
BuildRequires:  libpng-devel libpng17-tools
BuildRequires:  libgif-devel
BuildRequires:  libjpeg-devel
BuildRequires:  librsvg-devel librsvg-gir-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  gawk
Source44: import.info

%description
libAfterImage is a generic image manipulation library. It was initially
implemented to address AfterStep Window Manager's needs for image handling,
but it evolved into extremely powerful and flexible software, suitable for
virtually any project that has needs for loading, manipulating, displaying
images, as well as writing images in files. Most of the popular image formats
are supported using standard libraries, with XCF, XPM, PPM/PNM, BMP, ICO and
TGA being supported internally.

GIF, PNG, JPEG, TIFF and SVG formats are supported via standard libraries.

Powerful text rendering capabilities included, providing support for
TrueType fonts using FreeType library, and anti-aliasing of standard fonts
from X window system. 

%package devel
Group: Development/Other
Summary:        Files needed for software development with %{name}
Requires:       %{name} = %{version}-%{release}
#               Package split (apps split out from devel)

%description devel
The %{name}-devel package contains the files needed for development with
%{name}.

%package apps
Group: System/Libraries
Summary:        Sample programs using %{name}
Requires:       %{name} = %{version}-%{release}
#               Package split (apps split out from devel)
Obsoletes:      %{name}-devel < 1.20-21

%description apps
The %{name}-apps package contains sample programs using %{name}.

%prep
%setup -q
%patch0 
%patch1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# Delete bundled sources
rm libjpeg/*
rm libpng/*
rm libungif/*
rm zlib/*

sed /zlib/d -i .depend
# copies
rm -rf libjpeg/ libpng/ libungif/ zlib/
sed -i -e '/zlib\/zlib\.h/d' .depend


%build
%configure --enable-i18n --disable-staticlibs --enable-sharedlibs \
--disable-mmx-optimization --without-builtin-gif --without-afterbase \
--x-includes=%{_includedir} --x-libraries=%{_libdir}

%make_build CCFLAGS="-DNO_DEBUG_OUTPUT -fPIC %{optflags}" AR="ar cq"

%install
%makeinstall_std CCFLAGS="-DNO_DEBUG_OUTPUT -fPIC %{optflags}" AR="ar cq"

cp %{SOURCE1} COPYING



%files
%doc README ChangeLog
%doc --no-dereference COPYING
%{_libdir}/*.so.*

%files devel
%{_bindir}/afterimage-*
%{_includedir}/%{name}
%{_libdir}/*.so

%files apps
%{_bindir}/as*

%changelog
* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 1.20-alt1_31
- update to new release by fcimport

* Thu Mar 25 2021 Igor Vlasenko <viy@altlinux.org> 1.20-alt1_26
- update to new release by fcimport

* Wed Sep 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1_24
- fixed build

* Sat Mar 28 2020 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1_23
- update

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1_17
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1_15
- update to new release by fcimport

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

