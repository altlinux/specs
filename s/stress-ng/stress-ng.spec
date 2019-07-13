Name: stress-ng
Version: 0.09.60
Release: alt2

Summary: Stress test a computer system in various ways
License: GPLv2
Group: System/Kernel and hardware

Url: http://kernel.ubuntu.com/~cking/stress-ng/
#Git: git://kernel.ubuntu.com/cking/stress-ng.git
Source: %name-%version.tar

BuildRequires: libaio-devel
BuildRequires: libattr-devel
BuildRequires: libbsd-devel
BuildRequires: libcap-devel
BuildRequires: libgcrypt-devel
BuildRequires: libseccomp-devel
BuildRequires: libkeyutils-devel
BuildRequires: liblksctp-devel
BuildRequires: zlib-devel

%description
stress-ng will stress test a computer system in various selectable ways. It was
designed to exercise various physical subsystems of a computer as well as the
various operating system kernel interfaces.

%prep
%setup
%ifarch %e2k
# lcc 1.23 can't do string attribute form (1.24.03 will; mcst#4061)
sed -ri 's,"-O([0123])",\1,' stress-ng.h
%endif

%build
%make_build

%install
%makeinstall_std

%files
%doc COPYING
%doc README
%_bindir/stress-ng
%_datadir/bash-completion/completions/stress-ng
%_datadir/stress-ng/
%_mandir/man1/stress-ng.1.*

%changelog
* Sat Jul 13 2019 Michael Shigorin <mike@altlinux.org> 0.09.60-alt2
- E2K: fix build with lcc 1.23

* Mon Jul 01 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.09.60-alt1
- New version
- Spec: cleanup

* Sat Aug 11 2018 Vitaly Chikunov <vt@altlinux.org> 0.09.36-alt2
- First package for ALT
