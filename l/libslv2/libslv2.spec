Name: libslv2
Version: 0.6.6
Release: alt3
License: GPLv2+
Url: http://drobilla.net/software/slv2/
Packager: Egor Glukhov <kaman@altlinux.org>
Source0: %name-%version.tar
BuildRequires: gcc-c++ rasqal-devel libredland-devel lv2core rasqal-devel
BuildRequires: python-modules-compiler python-modules-logging

Summary: A library for simple use of LV2 plugins
Group: System/Libraries

%description
SLV2 is a library for LV2 hosts intended to make using LV2 Plugins as simple
as possible (without sacrificing capabilities).

%package -n slv2
Requires: %name = %version-%release
Group: Sound
Summary: Tools for SLV2 library

%description -n slv2
SLV2 is a library for LV2 hosts intended to make using LV2 Plugins as simple
as possible (without sacrificing capabilities).

This package contains tools for SLV2 library.

%package devel
Requires: %name = %version-%release
Group: Development/C
Summary: Includes to develop with SLV2 library

%description devel
SLV2 is a library for LV2 hosts intended to make using LV2 Plugins as simple
as possible (without sacrificing capabilities).

This package contains includes to develop with SLV2 library.

%prep
%setup

%build
./waf configure --prefix=%_prefix/ --libdir=%_libdir/
./waf

%install
DESTDIR=%buildroot ./waf install

%files
%doc AUTHORS COPYING ChangeLog README
%_libdir/%{name}*

%files -n slv2
%_bindir/*
%_man1dir/*

%files devel
%_includedir/slv2
%_pkgconfigdir/slv2.pc

%changelog
* Thu Sep 08 2011 Egor Glukhov <kaman@altlinux.org> 0.6.6-alt3
- Fixed build

* Tue Nov 16 2010 Egor Glukhov <kaman@altlinux.org> 0.6.6-alt2
- Fixed BuildRequires

* Thu Jul 15 2010 Egor Glukhov <kaman@altlinux.org> 0.6.6-alt1
- initial build for Sisyphus
