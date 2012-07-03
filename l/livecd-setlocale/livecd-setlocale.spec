Name: livecd-setlocale
Version: 0.1.1
Release: alt1

Summary: Automatically set locale from /proc/cmdline
License: GPL
Group: System/Configuration/Other

Source0: %name.tar
BuildArch: noarch
# NB: alterator-sysconfig's kbd data is required
Requires: service chkconfig alterator-sysconfig

%description
Service to automatically set locale from /proc/cmdline
(when specified as e.g. lang=ru_RU).

%prep
%setup -c

%install
mkdir -p %buildroot%_initdir/
install -pDm755 {livecd-setlocale,%buildroot%_initdir}/livecd-setlocale

%files 
%_initdir/livecd-setlocale

%changelog
* Wed Apr 18 2012 Michael Shigorin <mike@altlinux.org> 0.1.1-alt1
- don't require indexhtml-common (but use it if available)
- added ru_UA special handling
- start in runlevels 3/4/5
- cleanups

* Sun Feb 19 2012 Radik Usupov <radik@altlinux.org> 0.1-alt9
- Added hook to langmap from tt_RU

* Wed Feb 15 2012 Andrey Cherepanov <cas@altlinux.org> 0.1-alt8
- Set Russian as fallback language for tt_RU (closes: #26931)

* Fri Sep 30 2011 Andrey Cherepanov <cas@altlinux.org> 0.1-alt7
- Set correct language for default indexhtml

* Wed Jan 12 2011 Andrey Cherepanov <cas@altlinux.org> 0.1-alt6
- completely rewrite startup script without alterator-cmdline call

* Mon May 25 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt5
- Don't anything at runlevel change

* Mon Feb 23 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt4
- change syntax to call new alterator backends

* Wed Nov 07 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt3
- alterator-syskbd changed to alterator-sysconfig

* Fri Jun 29 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt2
- added keyboard setting

* Thu May 31 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- first build
