%define _unpackaged_files_terminate_build 1
Name: rng-tools
Version: 6.7
Release: alt3

Summary: Random number generator related utilities
License: GPLv2+
Group: System/Kernel and hardware

URL: https://github.com/nhorman/rng-tools
#Git: https://github.com/nhorman/rng-tools.git
Source0: %name-%version.tar
Source1: %name.init
Source2: %name.default
Source3: %name.service

# latest upstream fixes, remove after version > 6.7
# get rid of compiler warning on unused variables
Patch100: 0002-Remove-superfluous-variables.patch
# Urandom test may fail, but this may happen periodically as urandom
# is best-effort source of random data
# https://github.com/nhorman/rng-tools/issues/48
Patch101: 0001-Don-t-fail-on-urandom-test-failures.patch

# Automatically added by buildreq on Wed Apr 03 2019
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config
# libsasl2-3 libssl-devel perl pkg-config python-base sh4
BuildRequires: libcurl-devel
BuildRequires: libxml2-devel
BuildRequires: libp11-devel
BuildRequires: libsysfs-devel
BuildRequires: jitterentropy-devel
# Systems that support RDRAND but not AES-NI will require libgcrypt
# in order to use RDRAND as an entropy source.
BuildRequires: libgcrypt-devel

Obsoletes: kernel-utils

%description
Hardware random number generation tool.
It monitors a set of entropy sources, and supplies entropy from them
to the system kernel's /dev/random machinery.

%prep
%setup

%patch100 -p1
%patch101 -p1

%build
./autogen.sh
%configure
%make_build

%install
%makeinstall_std
mkdir -p %buildroot{%_initdir,%_sysconfdir/sysconfig,%_unitdir}
install -m755 %SOURCE1 %buildroot%_initdir/rngd
install -m644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/rngd
install -m644 %SOURCE3 %buildroot%_unitdir/rngd.service

%check
make check

%post
%post_service rngd

%preun
%preun_service rngd

%files
%config(noreplace) %_sysconfdir/sysconfig/rngd
%_initdir/rngd
%_unitdir/rngd.service
%_bindir/rngtest
%_sbindir/rngd
%_man1dir/rngtest.1*
%_man8dir/rngd.8*

%changelog
* Tue May 28 2019 Nikolai Kostrigin <nickel@altlinux.org> 6.7-alt3
- add upstream patch skipping periodical urandom test failures

* Thu Apr 04 2019 Nikolai Kostrigin <nickel@altlinux.org> 6.7-alt2
- add libgcrypt-devel to BR
- switch auto tests on

* Wed Apr 03 2019 Nikolai Kostrigin <nickel@altlinux.org> 6.7-alt1
- Version 6.7
- rearrange package git repo

* Sat Sep 01 2018 Sergey Y. Afonin <asy@altlinux.ru> 5-alt1
- Version 5
- added LSB init header to init script
- added example with /dev/urandom to /etc/sysconfig/rngd
- do not pack deprecated modutils.d/rng-tools

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Oct 25 2010 Victor Forsiuk <force@altlinux.org> 3-alt1
- Version 3.

* Thu Feb 02 2006 LAKostis <lakostis at altlinux.org> 2.0-alt2
- add some improvements from debian package (init.d script, defaults).

* Thu Feb 02 2006 LAKostis <lakostis at altlinux.org> 2.0-alt1
- rebuild for ALTLinux.

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Apr 13 2005 Florian La Roche <laroche@redhat.com>
- remove empty scripts

* Tue Mar  1 2005 Dave Jones <davej@redhat.com>
- Rebuild for gcc4

* Wed Feb  9 2005 Dave Jones <davej@redhat.com>
- Use $RPM_OPT_FLAGS

* Sat Dec 18 2004 Dave Jones <davej@redhat.com>
- Initial packaging, based upon kernel-utils.
