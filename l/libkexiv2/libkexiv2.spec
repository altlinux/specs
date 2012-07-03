%def_disable debug
%def_enable final
%def_disable rpath
%def_with pic
%def_enable shared
%def_disable static
%def_disable embedded
%def_enable mt
%def_enable threading

Name: libkexiv2
Version: 0.1.9
Release: alt6
Group: System/Libraries
Summary: KDE Exiv2 Interface
License: GPLv2
URL: http://www.kipi-plugins.org/ 
Source: %name-%version.tar.bz2
Patch1: libkexiv2-0.1.9-exiv2-21.patch

# Automatically added by buildreq on Mon May 07 2007
#BuildRequires: doxygen gcc-c++ graphviz imake kde-i18n-uk kdelibs-devel libdnet-devel libexiv2-devel libjpeg-devel libXext-devel libXt-devel qt3-designer qt3-doc-html qtcl xml-utils xorg-cf-files

BuildRequires: gcc-c++
BuildRequires: autoconf >= 2.5
BuildRequires: automake >= 1.7
BuildRequires: libqt3-devel >= 3.3
BuildRequires: kdelibs-devel >= 3.4
BuildRequires: libexiv2-devel >= 0.12
BuildRequires: libXext-devel libXt-devel
BuildRequires: libjpeg-devel libdnet-devel xorg-cf-files xml-utils libpng-devel

%description
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures
metadata.


%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: %name%{?_disable_shared:-devel-static} = %version-%release
Requires: libexiv2-devel >= 0.12

%description devel
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures
metadata.
This package contains the libraries and header files needed to develop
programs which make use of %name.


%if_enabled static
%package devel-static
Summary: Static %name
Group: Development/KDE and QT
Requires: %name = %version-%release

%description devel-static
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures
metadata.
This package contains the libraries and header files needed to develop
programs which make use of static %name.
%endif


%prep
%setup
%patch1 -p0


%build
%add_optflags -I%_includedir/tqtinterface
%configure \
    %{subst_enable debug} \
    %{subst_enable final} \
    %{subst_enable rpath} \
    %{subst_with pic} \
    %{subst_enable shared} \
    %{subst_enable static} \
    %{subst_enable embedded} \
    %{subst_enable mt} \
    %{subst_enable threading} \
    --without-arts \
    --enable-new-ldflags \
    --disable-gcc-hidden-visibility

%make_build


%install
%make DESTDIR=%buildroot install
bzip2 --best --keep --force ChangeLog



%if_enabled shared
%files
%doc AUTHORS NEWS README
%_libdir/*.so.*
%endif


%files devel
%doc ChangeLog.*
%{?_disable_shared:%doc AUTHORS NEWS README}
%{?_enable_shared:%_libdir/*.so}
%_pkgconfigdir/*
%_includedir/%name


%if_enabled static
%files devel-static
%_libdir/*.a
%endif


%changelog
* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 0.1.9-alt6
- fix compile with new exiv2

* Wed Nov 02 2011 Sergey V Turchin <zerg@altlinux.org> 0.1.9-alt5
- rebuilt with new exiv2

* Mon Jan 24 2011 Sergey V Turchin <zerg@altlinux.org> 0.1.9-alt4
- fix to build

* Tue Jun 01 2010 Sergey V Turchin <zerg@altlinux.org> 0.1.9-alt3
- rebuilt with new exiv2

* Mon Jan 11 2010 Sergey V Turchin <zerg@altlinux.org> 0.1.9-alt2
- rebuilt with new exiv2

* Thu Jul 23 2009 Sergey V Turchin <zerg@altlinux.org> 0.1.9-alt1
- 0.1.9

* Fri Jun 13 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.1.7-alt1.1
- Automated rebuild due to libexiv2.so.2 -> libexiv2.so.4 soname change.

* Mon May 05 2008 Led <led@altlinux.ru> 0.1.7-alt1
- 0.1.7

* Fri Apr 04 2008 Led <led@altlinux.ru> 0.1.6-alt2
- fixed License

* Sat Mar 22 2008 Led <led@altlinux.ru> 0.1.6-alt1.1
- rebuild with libexiv2.so.2

* Sat Sep 22 2007 Led <led@altlinux.ru> 0.1.6-alt1
- 0.1.6

* Mon May 14 2007 Led <led@altlinux.ru> 0.1.5-alt1
- 0.1.5

* Sat May 12 2007 Led <led@altlinux.ru> 0.1.4-alt2
- fixed %%files

* Mon May 07 2007 Led <led@altlinux.ru> 0.1.4-alt1
- 0.1.4
- updated BuildRequires

* Wed Mar 07 2007 Led <led@altlinux.ru> 0.1.1-alt1
- initial build
