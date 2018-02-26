%define dist IPC-ShareLite
Name: perl-%dist
Version: 0.17
Release: alt1

Summary: Light-weight interface to shared memory
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# This patch is kept here for historic reasons
Patch: perl-IPC-ShareLite-fixOwl.patch

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-Test-Pod

%description
IPC::ShareLite provides a simple interface to shared memory, allowing
data to be efficiently communicated between processes.  Your operating
system must support SysV IPC (shared memory and semaphores) in order to
use this module.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/IPC
%perl_vendor_autolib/IPC

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.17-alt1
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.09-alt4.1
- rebuilt with perl 5.12

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.09-alt4
- fix directory ownership violation
- disable man packaging

* Mon Oct 03 2005 Vladimir Lettiev <crux@altlinux.ru> 0.09-alt3
- patched to work on a Owl kernel

* Sat Sep 03 2005 Vitaly Lipatov <lav@altlinux.ru> 0.09-alt2
- add changelog from obsoletes
- add some docs

* Thu Sep 01 2005 Vitaly Lipatov <lav@altlinux.ru> 0.09-alt1
- build for ALT Linux Sisyphus with cpan2rpm

* Thu Mar 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.09-alt1
- 0.09

* Tue Nov 05 2002 Stanislav Ievlev <inger@altlinux.ru> 0.08-alt2
- rebuild with new perl

* Sat Mar 9 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.08-alt1
- First build for Sisyphus.
