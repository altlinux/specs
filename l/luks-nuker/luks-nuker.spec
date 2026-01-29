%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: luks-nuker
Version: 0.1.0
Release: alt1

Summary: Add support to a password that nukes your cryptsetup.
License: GPL-3.0-or-later
Group: System/Base
URL: http://git.altlinux.org/people/ved/public/luks-nuker.git
VCS: git://git.altlinux.org/people/ved/public/luks-nuker.git

Source: %name-%version.tar

Requires: cryptsetup

BuildRequires: libblkid-devel
BuildRequires: libcrypt-devel

%description
Add support to a password that nukes your cryptsetup everywhere you want.

%prep
%setup

%build
%make_build

%install
%makeinstall_std SBINDIR=%_sbindir SYSCONFDIR=%_sysconfdir

%files
%_sbindir/luks-nuker
%config(noreplace) %_sysconfdir/luks-nuker.conf
%doc README

%changelog
* Wed Jan 28 2026 Egor Shestakov <ved@altlinux.org> 0.1.0-alt1
- Initial build.
