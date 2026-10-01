Name: cpulimit
Epoch: 1
Version: 3.2
Release: alt1

Summary: CPU Usage Limiter

Packager: Vitaly Lipatov <lav@altlinux.ru>

Url: https://limitcpu.sourceforge.net
License: GPL-2.0-only
Group: Monitoring

# Source-url: https://downloads.sourceforge.net/limitcpu/cpulimit-%version.tar.gz
Source: %name-%version.tar
Patch0: cpulimit-0.2-compat.patch

%description
cpulimit is a tool which limits the CPU usage of a process (expressed in
percentage, not in CPU time). It is useful to control batch jobs, when you
don't want them to eat too many CPU cycles. It does not change the nice value
or other scheduling priority settings, but the real CPU usage. Also, it is
able to adapt itself to the overall system load, dynamically and quickly.
The control of the used CPU amount is done sending SIGSTOP and SIGCONT
POSIX signals to processes.

%prep
%setup
%patch0 -p1

%build
%make_build CFLAGS="%optflags"

%install
install -Dp -m 755 %name %buildroot%_bindir/%name
install -Dp -m 644 %name.1 %buildroot%_man1dir/%name.1

%files
%doc README CHANGELOG
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Thu Oct 01 2026 Vitaly Lipatov <lav@altlinux.ru> 1:3.2-alt1
- new version 3.2
- switch upstream to limitcpu (continuation of the original cpulimit 1.x),
  opsengine/cpulimit is abandoned since 2015
- add compatibility with opsengine cpulimit 0.2 command line:
  -i/--include-children as alias for -m, stop option parsing at the command

* Thu Mar 12 2026 Vitaly Lipatov <lav@altlinux.ru> 1:0.2-alt1
- new version 0.2, switched upstream to GitHub (opsengine/cpulimit)
- applied Fedora patches for modern Linux kernel compatibility

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.1-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Jul 06 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- initial release for ALT Linux Sisyphus

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.1-3mdv2009.0
+ Revision: 243724
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.1-1mdv2008.1
+ Revision: 136345
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jul 27 2007 Nicolas Vigier <nvigier@mandriva.com> 1.1-1mdv2008.0
+ Revision: 56274
- Import cpulimit
