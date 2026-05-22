Name:     wayvnc
Version:  0.10.0
Release:  alt1
Summary:  A VNC server for wlroots based Wayland compositors
Group:    Graphical desktop/Other
License:  ISC
Url:      https://github.com/any1/wayvnc
Vcs:      https://github.com/any1/wayvnc.git
Source:   %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(neatvnc)
BuildRequires: pam-devel
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(jansson)
BuildRequires: pkgconfig(aml1)
BuildRequires: pkgconfig(gbm)
BuildRequires: scdoc

%description
This is a VNC server for wlroots based Wayland compositors. It
attaches to a running Wayland session, creates virtual input devices
and exposes a single display via the RFB protocol. The Wayland session
may be a headless one, so it is also possible to run wayvnc without a
physical display attached.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_bindir/%name
%_bindir/%{name}ctl
%doc README.md FAQ.md COPYING
%_man1dir/%name.1.*
%_man1dir/%{name}ctl.1.*

%changelog
* Thu May 21 2026 Anton Midyukov <antohami@altlinux.org> 0.10.0-alt1
- New version 0.10.0.

* Wed Jun 18 2025 Anton Midyukov <antohami@altlinux.org> 0.9.1-alt2
- add build dependency on pkgconfig(gbm)
- enable check

* Thu Mar 27 2025 Anton Midyukov <antohami@altlinux.org> 0.9.1-alt1
- initial build
