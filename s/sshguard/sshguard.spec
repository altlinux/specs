Name: sshguard
Version: 2.5.1
Release: alt1
Source: %name-%version.tar.gz
Source1: sshguard.conf
Source2: sshguard.service
Patch: sshguard-autoupdate.patch
Group: Networking/Other
Summary: Protect hosts from brute-force attacks against SSH and other services
License: 0BSD
Url: https://www.sshguard.net/
VCS: https://github.com/SSHGuard/sshguard

# Automatically added by buildreq on Fri Jun 26 2026
# optimized out: bash5 glibc-kernheaders-generic glibc-kernheaders-x86 libgcc15-devel libgpg-error perl python3 python3-base sh5
BuildRequires: flex python3-module-docutils

%description
SSHGuard protects hosts from brute-force attacks against SSH and other
services. It aggregates system logs and blocks repeat offenders using
one of several firewall backends.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
install -D %SOURCE1 %buildroot/%_sysconfdir/%name.conf
install -D %SOURCE2 %buildroot/%_unitdir/%name.service

%files
%doc *.rst examples
%_man7dir/*
%_man8dir/*
%_sbindir/*
%_libexecdir/*
%_sysconfdir/*
%exclude %_libexecdir/debug

%changelog
* Fri Jun 26 2026 Fr. Br. George <george@altlinux.org> 2.5.1-alt1
- Autobuild version bump to 2.5.1

* Fri Jun 26 2026 Fr. Br. George <george@altlinux.org> 2.5.0-alt1
- Initial build for ALT
