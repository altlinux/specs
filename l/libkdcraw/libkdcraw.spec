%def_disable debug
%def_disable profile
%def_enable final
%def_disable rpath
%def_with pic
%def_enable shared
%def_enable static
%def_disable embedded
%def_enable mt
%def_enable threading

%define bname kdcraw
Name: lib%bname
Version: 0.1.5
Release: alt3.1
Group: System/Libraries
Summary: C++ interface around dcraw binary program
License: %gpl2plus
URL: http://www.kipi-plugins.org/ 
Source: %name-%version.tar
Patch: %name-0.1.0-makefile.patch
Patch1: %name-0.1.5-alt-DSO.patch
Conflicts: %bname < 0.1.1-alt1
Provides: %bname = %version-%release
Obsoletes: %bname

# Automatically added by buildreq on Sat Mar 15 2008
#BuildRequires: doxygen gcc-c++ graphviz imake kdepim-devel libXt-devel libdnet-devel libjpeg-devel liblcms-devel qt3-designer qt3-doc-html xml-utils xorg-cf-files

BuildRequires: doxygen gcc-c++ imake libdnet-devel xml-utils
BuildRequires: libXt-devel xorg-cf-files symlinks rpm-build-licenses
BuildRequires: autoconf >= 2.5
BuildRequires: automake >= 1.7
BuildRequires: libqt3-devel >= 3.3
BuildRequires: kdelibs-devel >= 3.4
BuildRequires: libjpeg-devel
BuildRequires: liblcms-devel >= 1.14

%description
%name is a C++ interface around dcraw binary program used to decode
RAW picture files.
This library is used by kipi-plugins, digiKam and others kipi host
programs.


%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: %name%{?_disable_shared:-devel-static} = %version-%release
Requires: libexiv2-devel >= 0.12

%description devel
Libkdcraw is a C++ interface around dcraw binary program used to decode
RAW picture files.
This package contains the libraries and header files needed to develop
programs which make use of %name.


%if_enabled static
%package devel-static
Summary: Static %name
Group: Development/KDE and QT
Requires: %name-devel = %version-%release

%description devel-static
Libkdcraw is a C++ interface around dcraw binary program used to decode
RAW picture files.
This package contains the library needed to develop programs which make
use of static %name.
%endif


%prep
%setup
%patch1 -p2


%build
%add_optflags %optflags_shared -I%_includedir/tqtinterface
#for // comments in lcms.h:
%K3configure \
    %{subst_enable debug} \
    %{subst_enable profile} \
    %{subst_enable final} \
    %{subst_enable rpath} \
    %{subst_with pic} \
    %{subst_enable shared} \
    %{subst_enable static} \
    %{subst_enable embedded} \
    %{subst_enable mt} \
    %{subst_enable threading} \
    --enable-new-ldflags \
    --disable-gcc-hidden-visibility

%make_build

bzip2 --best --keep --force ChangeLog


%install
%K3install
install -d -m 0755 %buildroot%_K3bindir
ln -sf %buildroot%_K3libdir/%name[[:digit:]]*/%bname %buildroot%_K3bindir/
symlinks -scd %buildroot%_K3bindir
install -pD -m 0644 %name/dcraw/%bname.1 %buildroot%_man1dir/%bname.1
%K4find_lang %name


%files -f %name.lang
%doc AUTHORS NEWS README %name/dcraw/CAMERALIST
%_libdir/%name[[:digit:]]*
%_K3bindir/*
%_man1dir/*
%{?_enable_shared:%_libdir/*.so.*}
%_kde3_iconsdir/hicolor/*/apps/%bname.png


%files devel
%doc ChangeLog.*
%{?_enable_shared:%_libdir/lib*.so}
%_pkgconfigdir/*
%_K3includedir/%name


%if_enabled static
%files devel-static
%_libdir/*.a
%endif


%changelog
* Fri Jun 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt3.1
- Fixed build

* Tue Feb 22 2011 Sergey V Turchin <zerg@altlinux.org> 0.1.5-alt3
- move to alternate place

* Mon Nov 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt2
- Fixed build

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 0.1.5-alt1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libkdcraw
  * postun_ldconfig for libkdcraw

* Sun Sep 14 2008 Led <led@altlinux.ru> 0.1.5-alt1
- 0.1.5

* Sat Mar 15 2008 Led <led@altlinux.ru> 0.1.4-alt1
- 0.1.4
- updated BuildRequires
- fixed License

* Wed Jan 16 2008 Led <led@altlinux.ru> 0.1.3-alt1
- 0.1.3

* Sat Sep 22 2007 Led <led@altlinux.ru> 0.1.2-alt1
- 0.1.2

* Thu Jun 14 2007 Led <led@altlinux.ru> 0.1.1-alt1
- 0.1.1
- removed %bname subpackage
- fixed %%description

* Sat May 12 2007 Led <led@altlinux.ru> 0.1.0-alt1
- initial build
