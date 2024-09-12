Name:    tang
Version: 15
Release: alt1
Summary: Tang binding daemon

License: GPLv3
Group:   System/Libraries
URL:     https://github.com/latchset/tang
Source:  %name-%version.tar

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

%build
%meson
%meson_build

%install
%meson_install
rm -rf %buildroot%_datadir

%files
%doc COPYING README.md
%_bindir/tang-show-keys
%_libexecdir/tangd*
%_unitdir/tangd*

%changelog
* Thu Sep 12 2024 Alexey Shabalin <shaba@altlinux.org> 15-alt1
- update version
- delete patch with change systemd unit path

* Fri Nov 24 2023 Oleg Solovyov <mcpain@altlinux.org> 14-alt1
- update version (Fixes: CVE-2023-1672)

* Wed Nov 28 2018 Oleg Solovyov <mcpain@altlinux.org> 7-alt2
- fix description

* Mon Oct 01 2018 Oleg Solovyov <mcpain@altlinux.org> 7-alt1
- initial build

