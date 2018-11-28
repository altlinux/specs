Name:    tang
Version: 7
Release: alt2
Summary: Tang binding daemon

License: GPLv3
Group:   System/Libraries
URL:     https://github.com/latchset/tang
Source:  tang-%version.tar.gz

BuildRequires: openssl-devel
BuildRequires: libjose-devel
BuildRequires: libjansson-devel
BuildRequires: zlib-devel
BuildRequires: libhttp-parser-devel
BuildRequires: systemd systemd-devel

%description
Tang binding daemon

%prep
%setup

%build
%autoreconf
%configure --localstatedir=/var
%make_build

%install
%makeinstall_std

%files
%_bindir/tang-show-keys
%_libexecdir/tangd*
%_unitdir/tangd*

%changelog
* Wed Nov 28 2018 Oleg Solovyov <mcpain@altlinux.org> 7-alt2
- fix description

* Mon Oct 01 2018 Oleg Solovyov <mcpain@altlinux.org> 7-alt1
- initial build

