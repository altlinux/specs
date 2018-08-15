%def_enable snapshot
%define _name ibus-qt

Name: %{_name}4
Version: 1.3.3
Release: alt2

Summary: Qt IBus library and Qt input method plugin
License: GPLv2+
Group: System/Libraries
Url: https://github.com/ibus/%_name

%if_disabled snapshot
Source: %url/releases/download/%version/%_name-%version-Source.tar.gz
%else
#VCS: https://github.com/ibus/ibus-qt.git
Source: %_name-%version.tar
%endif
Patch1: ibus-qt-alt-build.patch

%define ibus_ver 1.3.7
%define qt_ver 4.5

Requires: ibus >= %ibus_ver

BuildRequires: cmake gcc-c++
BuildRequires: libqt4-devel >= %qt_ver
BuildRequires: libibus-devel >= %ibus_ver
BuildRequires: libdbus-devel libicu-devel doxygen

%description
Qt IBus library and Qt input method plugin.

%package devel
Summary: Development files for iBus Qt
Group: Development/C++
Requires: %name = %version-%release

%description devel
This package provides header and development library for iBus Qt
library.

%package devel-doc
Summary: Development documentation for iBus Qt
Group: Development/C++
Requires: %name = %version-%release

%description devel-doc
This package provides development documentation for iBus Qt
library.

%prep
%if_disabled snapshot
%setup -n %_name-%version-Source
%else
%setup -n %_name-%version
%endif
%patch1

%build
%cmake -DLIBDIR=%_libdir
%cmake_build VERBOSE=1
%make docs

%install
%cmakeinstall_std

%files
%_libdir/lib%{_name}.so.*
%_libdir/qt4/plugins/inputmethods/libqtim-ibus.so
%doc AUTHORS README

%files devel
%_includedir/*
%_libdir/lib%{_name}.so

#%files devel-doc
#%doc docs/html

%changelog
* Wed Aug 15 2018 Yuri N. Sedunov <aris@altlinux.org> 1.3.3-alt2
- updated to 1.3.3-1-gdc8f7cb
- build against libicu*.so.62

* Thu Feb 11 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.3-alt1
- 1.3.3

* Wed Nov 14 2012 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt2
- rebuild against libicu-5.1

* Tue Jan 17 2012 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- first build for Sisyphus

