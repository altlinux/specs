%def_enable shared
%def_enable static
%def_disable debug
%def_enable libpng
%def_with pic
%def_with doc

%define bname gavl
Name: lib%bname
Version: 1.2.0
Release: alt1.0
Summary: Library for handling uncompressed audio- and video data
License: %gpl2plus
Group: System/Libraries
URL: http://gmerlin.sourceforge.net/
Source: %bname-%version.tar.gz
Patch: %bname-1.1.2-config.patch
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses

## Automatically added by buildreq on Sat Apr 24 2010
#BuildRequires: doxygen glibc-devel-static libpng-devel

BuildRequires: gcc-c++
%{?_enable_libpng:BuildRequires: libpng-devel}
%{?_with_doc:BuildRequires: doxygen}

%description
Gavl is short for Gmerlin Audio Video Library. It defines generic types
for audio and video formats, which are applicable to a wide range of
multimedia applications. In addition, it provides conversion functions
from all possible formats to all other formats.


%package devel
Group: Development/C
Summary: Development files for %name
Requires: %name%{?_disable_shared:-devel-static} = %version-%release

%description devel
Gavl is short for Gmerlin Audio Video Library. It defines generic types
for audio and video formats, which are applicable to a wide range of
multimedia applications. In addition, it provides conversion functions
from all possible formats to all other formats.

If you want to write a multimedia application, gavl will help you a
lot: You don't have to mess around with the large varieties of
pixelformats, interleaving modes, audio sample formats and so on.

This package contains header files and documentation needed to develop
applications with %name.


%if_enabled static
%package devel-static
Summary: Static %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Gavl is short for Gmerlin Audio Video Library. It defines generic types
for audio and video formats, which are applicable to a wide range of
multimedia applications. In addition, it provides conversion functions
from all possible formats to all other formats.

This package contains static library to develop applications with
%name.
%endif


%package doc
Summary: %name documentation
Group: Documentation
BuildArch: noarch

%description doc
Gavl is short for Gmerlin Audio Video Library. It defines generic types
for audio and video formats, which are applicable to a wide range of
multimedia applications. In addition, it provides conversion functions
from all possible formats to all other formats.

If you want to write a multimedia application, gavl will help you a
lot: You don't have to mess around with the large varieties of
pixelformats, interleaving modes, audio sample formats and so on.

This package contains API Reference for develop with %name.


%prep
%setup -n %bname-%version
%patch -p1


%build
%define _optlevel 3
%autoreconf
%configure \
    %{subst_enable shared} \
    %{subst_enable static} \
    %{subst_enable libpng} \
    %{subst_enable debug} \
    %{subst_with pic} \
    %{?_without_doc:--without-doxygen} \
    --without-cpuflags
%make_build


%install
%make_install DESTDIR=%buildroot docdir=%_docdir/%name-devel-%version install
install -d -m 0755 %buildroot%_docdir/%name-%version
install -m 0644 AUTHORS README TODO %buildroot%_docdir/%name-%version/


%if_enabled shared
%files
%dir %_docdir/%name-%version
%_docdir/%name-%version/*
%_libdir/*.so.*
%endif


%files devel
%if_disabled shared
%dir %_docdir/%name-%version
%_docdir/%name-%version/*
%endif
%{?_enable_shared:%_libdir/*.so}
%_includedir/*
%_pkgconfigdir/*


%if_enabled static
%files devel-static
%_libdir/*.a
%endif


%if_with doc
%files doc
%dir %_docdir/%name-devel-%version
%_docdir/%name-devel-%version/apiref
%endif


%changelog
* Thu Sep 22 2011 Hihin Ruslan <ruslandh@altlinux.ru> 1.2.0-alt1.0
- New version

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.2
- Rebuilt for debuginfo

* Wed Nov 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.1
- Rebuilt for soname set-versions

* Sat Apr 24 2010 Hihin Ruslan <ruslandh@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Sun Dec 28 2008 Led <led@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Sat Aug 02 2008 Led <led@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Wed May 28 2008 Led <led@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Sat Mar 15 2008 Led <led@altlinux.ru> 0.2.7-alt1
- initial build

