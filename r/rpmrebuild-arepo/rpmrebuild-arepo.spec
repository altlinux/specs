Name: rpmrebuild-arepo
Version: 3.1.3
Release: alt1

Summary: biarch repackager for Sisyphus packages
License: GPL
Group: Development/Other
BuildArch: noarch

Source: %name-%version.tar

Requires: rpmrebuild
Requires: rpm >= 4.0.4-alt100.48

%description
Arepo repackages i586 files (mostly libraries) in i586-* packages suitable
for installation on an x86_64 system. Installing these packages allows you
to emulate a biarch environment.

%package scripts
Group: Development/Other
Summary: Helper scripts for %name biarch repackager

%description scripts
Helper scripts for %name biarch repackager

%prep
%setup

%install
mkdir -p %buildroot%_bindir
install -m755 arepo_pre.py %buildroot%_bindir/
mkdir -p %buildroot%_sysconfdir
install -m644 rpmrebuild-arepo.conf %buildroot%_sysconfdir
mkdir -p %buildroot%_libexecdir/rpmrebuild/plugins/
install -m644 arepo.plug %buildroot%_libexecdir/rpmrebuild/plugins/
install -m755 arepo.sh %buildroot%_libexecdir/rpmrebuild/plugins/

%files
%config(noreplace) %_sysconfdir/rpmrebuild-arepo.conf
%_libexecdir/rpmrebuild/plugins/arepo.*

%files scripts
%_bindir/arepo_pre.py

%changelog
* Wed Jun 13 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.3-alt1
- arepo_pre.py, arepo.sh: filter out %ghost files in 'lib' mode

* Tue Apr 24 2012 Dmitry V. Levin <ldv@altlinux.org> 3.1.2-alt1
- rpmrebuild-arepo.conf: added /etc/X11/lib to lib_files.
- arepo_pre.py: changed output format to match
  $repo/files/list/arepo-x86_64-i586.list better.

* Mon Apr 02 2012 Dmitry V. Levin <ldv@altlinux.org> 3.1.1-alt1
- rpmrebuild-arepo.conf: fixed lib_files.

* Mon Apr 02 2012 Dmitry V. Levin <ldv@altlinux.org> 3.1-alt1
- rpmrebuild-arepo.conf: stuffed up lib_files.

* Sun Apr 01 2012 Dmitry V. Levin <ldv@altlinux.org> 3.0-alt1
- Changed arepo.sh interface.
- Fixed default blacklist_pkg_name regexp.
- Optimized regexps.

* Fri Mar 02 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0-alt1
- initial
