Name:		stress-ng
Version:	0.09.36
Release:	alt2
Summary:	Stress test a computer system in various ways
Group:		System/Kernel and hardware
License:	GPLv2

URL:		http://kernel.ubuntu.com/~cking/stress-ng/
Source:		%name-%version.tar

BuildRequires:	libaio-devel
BuildRequires:	libattr-devel
BuildRequires:	libbsd-devel
BuildRequires:	libcap-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libseccomp-devel
BuildRequires:	libkeyutils-devel
BuildRequires:	liblksctp-devel
BuildRequires:	zlib-devel

%description
stress-ng will stress test a computer system in various selectable ways. It was
designed to exercise various physical subsystems of a computer as well as the
various operating system kernel interfaces.

%prep
%setup -q

%build
%make_build

%install
%makeinstall_std

%files
%doc COPYING
%doc README
%{_bindir}/stress-ng
%{_datadir}/stress-ng/
%{_mandir}/man1/stress-ng.1.*

%changelog
* Sat Aug 11 2018 Vitaly Chikunov <vt@altlinux.org> 0.09.36-alt2
- First package for ALT
