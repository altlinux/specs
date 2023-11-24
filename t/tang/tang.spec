Name:    tang
Version: 14
Release: alt1
Summary: Tang binding daemon

License: GPLv3
Group:   System/Libraries
URL:     https://github.com/latchset/tang
Source:  tang-%version.tar.gz
Patch1:  alt-fix-paths.patch

BuildRequires: openssl-devel
BuildRequires: libjose-devel
BuildRequires: libjansson-devel
BuildRequires: zlib-devel
BuildRequires: libhttp-parser-devel
BuildRequires: systemd systemd-devel

BuildRequires: meson

%description
Tang binding daemon

%prep
%setup
%patch1 -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%doc COPYING
%_bindir/tang-show-keys
%_libexecdir/tangd*
%_unitdir/tangd*

%changelog
* Fri Nov 24 2023 Oleg Solovyov <mcpain@altlinux.org> 14-alt1
- update version (Fixes: CVE-2023-1672)

* Wed Nov 28 2018 Oleg Solovyov <mcpain@altlinux.org> 7-alt2
- fix description

* Mon Oct 01 2018 Oleg Solovyov <mcpain@altlinux.org> 7-alt1
- initial build

