%define _name ibus-qt

Name: %{_name}4
Version: 1.3.1
Release: alt1

Summary: Qt IBus library and Qt input method plugin
License: GPLv2+
Group: System/Libraries
Url: http://code.google.com/p/ibus/
Source: http://ibus.googlecode.com/files/%_name-%version-Source.tar.gz

Patch: ibus-qt-HEAD.patch
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
%setup -n %_name-%version-Source
%patch -p1
%patch1

%build
%cmake -DLIBDIR=%_libdir

pushd BUILD
%make_build VERBOSE=1

%make docs

%install
pushd BUILD
%make DESTDIR=%buildroot install

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
* Tue Jan 17 2012 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- first build for Sisyphus

