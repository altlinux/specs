%define _unpackaged_files_terminate_build 1

Name: q6voiced
Version: 0.2.1
Release: alt1
Summary: Userspace QDSP6 voice driver daemon listing on oFono/ModemManager
License: MIT
Group: System/Kernel and hardware
Url: https://gitlab.postmarketos.org/postmarketOS/q6voiced
VCS: https://gitlab.postmarketos.org/postmarketOS/q6voiced.git
ExclusiveArch: aarch64

Source: %name-%version.tar
Patch0: fix-unit.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(alsa)

%description
q6voiced is a userspace daemon for the QDSP6 voice call audio driver.
Voice call audio is directly routed from the modem to the input/output audio
devices, but something needs to start the audio streams for that to happen.
q6voiced listens on DBus system bus for signals from oFono and ModemManager,
and opens/closes the PCM device when a DBus signal indicating that a call is
initiated/ended is received. This essentially makes voice call audio work out
of the box (provided that the audio routing, e.g. Earpiece and a microphone is
set up appropriately).

%prep
%setup
%patch -p1

%build
%meson
%meson_build -v

%install
%meson_install

%files
%doc README.md
%_bindir/%name
%_unitdir/%name.service

%changelog
* Mon Apr 20 2026 Vasiliy Doylov <neko@altlinux.org> 0.2.1-alt1
- Initial package
