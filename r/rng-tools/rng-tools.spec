Name: rng-tools
Version: 3
Release: alt1

Summary: Random number generator related utilities
License: GPLv2+
Group: System/Kernel and hardware

URL: http://sourceforge.net/projects/gkernel/
Source0: http://download.sourceforge.net/project/gkernel/rng-tools/%version/rng-tools-%version.tar.gz
Source1: %name.init
Source2: %name.default
Source3: %name.modprobe

Obsoletes: kernel-utils

%description
Hardware random number generation tools.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std
mkdir -p %buildroot{%_initdir,%_sysconfdir/sysconfig,%_sysconfdir/modutils.d}
install -m755 %SOURCE1 %buildroot%_initdir/rngd
install -m644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/rngd
install -m644 %SOURCE3 %buildroot%_sysconfdir/modutils.d/%name

%post
%post_service rngd

%preun
%preun_service rngd

%files
%config(noreplace) %_sysconfdir/sysconfig/rngd
%_sysconfdir/modutils.d/%name
%_initdir/rngd
%_bindir/rngtest
%_sbindir/rngd
%_man1dir/rngtest.1*
%_man8dir/rngd.8*

%changelog
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
