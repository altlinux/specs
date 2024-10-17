%define git %nil
%def_enable tests
%def_enable systemd

Name: libratbag
Version: 0.18
Release: alt1
Summary: Programmable input device library
Group: System/Libraries
License: MIT
Url: https://github.com/libratbag/libratbag
Source0: https://github.com/libratbag/%name/archive/v%version/%name-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires(pre): meson
BuildRequires: pkgconfig gcc-c++ libevdev-devel libudev-devel libunistring-devel
BuildRequires: glib2-devel python3-dev swig libjson-glib-devel
%if_enabled systemd
BuildRequires: libsystemd-devel
%else
BuildRequires: libelogind-devel
%endif
%{?_enable_tests:BuildRequires: check python3-module-pygobject3 python3-module-lxml python3-module-evdev}

%description
libratbag is a library that allows to configure programmable
mice.

%package -n liblur
Summary: Logitech Unifying Receiver library
Group: System/Libraries

%description -n liblur
The liblur package contains libraries and tools to access and
configure the Logitech Unifying Receivers. The functionality
are mainly listing, pairing and un-pairing Logitech devices
attached to a receiver.

%package -n liblur-devel
Summary: Development files for liblur
Group: Development/C
Requires: liblur = %EVR

%description -n liblur-devel
The liblur-devel package contains libraries and header files for
developing applications that use liblur.

%package -n ratbagd
Summary: System daemon to introspect and modify configurable mice
Group: System/Configuration/Hardware
Requires: %name-data = %EVR

%description -n ratbagd
System daemon to introspect and modify configurable mice using libratbag.

%package tools
Summary: Mice configuration tools using libratbag
Group: System/Configuration/Hardware
Requires: ratbagd = %EVR

%description tools
Mice configuration tools using libratbag.

%package data
Summary: Libratbag mice configuration data
Group: System/Configuration/Hardware
BuildArch: noarch
Requires: ratbagd = %EVR

%description data
Libratbag mice configuration data.

%prep
%setup
%patch -p1

%build
%meson \
    -Ddocumentation=false \
%if_enabled tests
    -Dtests=false \
%endif
%if_enabled systemd
    -Dsystemd-unit-dir=%_unitdir
%else
    -Dlogind-provider=elogind \
    -Dsystemd=false
%endif
%meson_build

%if_enabled tests
%check
%meson_test
%endif

%install
%meson_install

%files -n liblur
%_libdir/liblur.so.*

%files -n liblur-devel
%_includedir/liblur.h
%_libdir/liblur.so
%_pkgconfigdir/liblur.pc

%files -n ratbagd
%doc COPYING README* TODO
%_sbindir/ratbagd
%_datadir/dbus-1/system.d/*.conf
%_datadir/dbus-1/system-services/*.service
%if_enabled systemd
%_unitdir/*.service
%endif
%_man8dir/*.8*

%files tools
%_bindir/ratbagctl
%_bindir/lur-command
%_man1dir/ratbagctl.1*
%_man1dir/lur-command.1*

%files data
%dir %_datadir/libratbag
%_datadir/libratbag

%changelog
* Thu Oct 17 2024 L.A. Kostis <lakostis@altlinux.ru> 0.18-alt1
- 0.18.

* Tue Jun 25 2024 L.A. Kostis <lakostis@altlinux.ru> 0.17-alt2.g1c96620
- v0.17-334-g1c96620.

* Fri Dec 30 2022 L.A. Kostis <lakostis@altlinux.ru> 0.17-alt1
- 0.17.

* Fri Sep 23 2022 L.A. Kostis <lakostis@altlinux.ru> 0.16-alt0.3.gc335b2b
- GIT c335b2b.

* Mon May 23 2022 L.A. Kostis <lakostis@altlinux.ru> 0.16-alt0.2.g3ea0d44
- v0.16-159-g3ea0d44.

* Mon Jul 19 2021 L.A. Kostis <lakostis@altlinux.ru> 0.16-alt0.1
- 0.16.

* Wed Nov 04 2020 L.A. Kostis <lakostis@altlinux.ru> 0.15-alt0.1
- v0.15.

* Sat Mar 21 2020 L.A. Kostis <lakostis@altlinux.ru> 0.13-alt0.16.g1dff6f2
- v0.13-16-g1dff6f2.

* Fri Sep 13 2019 L.A. Kostis <lakostis@altlinux.ru> 0.10-alt0.1
- v0.10-30-g07567ac.

* Mon Apr 30 2018 L.A. Kostis <lakostis@altlinux.ru> 0.9.901-alt0.2
- GIT 7fe4d6f.
- build -data as noarch.

* Thu Jan 04 2018 L.A. Kostis <lakostis@altlinux.ru> 0.9.901-alt0.1
- Updated to v0.9.901.
- Added SteelSeries Rival 95 mice (very similar to Rival 310 but without any LEDs).

* Wed Oct 25 2017 L.A. Kostis <lakostis@altlinux.ru> 0.9.900-alt0.1.git9c75a7c
- GIT 9c75a7c.
- initial build for ALTLinux.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Benjamin Tissoires <benjamin.tissoires@redhat.com> 0.9-2
- disable tests on s390x because they seem to fail without good reasons

* Tue Jun 06 2017 Benjamin Tissoires <benjamin.tissoires@redhat.com> 0.9-1
- libratbag v0.9
- new manpage for lur-command

* Tue May 09 2017 Benjamin Tissoires <benjamin.tissoires@redhat.com> 0.8-1
- libratbag v0.8

* Tue May 09 2017 Benjamin Tissoires <benjamin.tissoires@redhat.com> 0.7-3
- add a hack for F24 and F25 to compile

* Fri May 05 2017 Benjamin Tissoires <benjamin.tissoires@redhat.com> 0.7-2
- Remove the generation of the documentation, we don't ship it

* Thu May 04 2017 Benjamin Tissoires <benjamin.tissoires@redhat.com> 0.7-1
- Initial Fedora packaging (rhbz#1309703)
