# rt-tests is taken by perl tests for RT
Name:     linux-rt-tests
Version:  1.5
Release:  alt1

Summary:  Programs that test various rt-linux features
License:  GPL-2.0-or-later
Group:    System/Kernel and hardware
# git://git.kernel.org/pub/scm/utils/rt-tests/rt-tests.git
Url:      https://wiki.linuxfoundation.org/realtime/documentation/howto/tools/rt-tests

ExclusiveArch: %ix86 x86_64
Source:   %name-%version.tar
BuildRequires: libnuma-devel

%description
rt-tests is a test suite, that contains programs (such as cyclictest) to test
various Real Time Linux features.

%prep
%setup

%build
%make_build prefix=/usr

%install
%makeinstall_std prefix=/usr

%files
%_bindir/*
%_man8dir/*
%doc COPYING MAINTAINERS README.markdown

%changelog
* Fri Sep 06 2019 Vitaly Chikunov <vt@altlinux.org> 1.5-alt1
- First build of rt-tests.
