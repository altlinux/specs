%def_enable snapshot
%define _name mmsd

Name: %_name-tng
Version: 2.6.4
Release: alt1

Summary: Multimedia Messaging Service Daemon
License: GPL-2.0-or-later
Group: System/Servers
Url: https://gitlab.com/kop316/mmsd

%if_disabled snapshot
Source: https://gitlab.com/kop316/mmsd/-/archive/%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif
Source1: mmsd-tng.service

Requires: ModemManager

BuildRequires(pre): rpm-macros-meson rpm-macros-systemd
BuildRequires: meson gcc-c++
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(json-c) >= 0.15
BuildRequires: pkgconfig(libcares) >= 1.18
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(mm-glib) >= 1.14
BuildRequires: libphonenumber-devel
BuildRequires: pkgconfig(mobile-broadband-provider-info)

%description
mmsd-tng is a lower level daemon that transmits and recieves MMSes. It works with
both the Modem Manager stack.

%prep
%setup -n %_name-%version

%build
%meson -Dbuild-mmsctl=true
%meson_build

%install
%meson_install
mkdir -p %buildroot%_userunitdir
install -pDm644 %SOURCE1 %buildroot%_userunitdir

%check
%__meson_test

%preun
%systemd_user_preun mmsd-tng.service

%post
%systemd_user_post mmsd-tng.service

%files
%_bindir/%{_name}tng
%_bindir/mmsctl
%_userunitdir/mmsd-tng.service
%doc README

%changelog
* Sat Jul 05 2025 Yuri N. Sedunov <aris@altlinux.org> 2.6.4-alt1
- 2.6.4

* Wed May 07 2025 Yuri N. Sedunov <aris@altlinux.org> 2.6.3-alt1
- first build for Sisyphus (2.6.3-1-g4b3582d)
- adapted fc spec with stuffed mmsd-tng.service

