Name: livecd-installer-features
Version: 0.3
Release: alt2

Summary: Run installer features during install from livecd
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

Requires: alterator-livecd => 0.5
Conflicts: installer-common-stage2
Conflicts: livecd-install < 0.6-alt2

%description
Run installer features during install from livecd

%prep
%setup

%install
install -pDm644 install2-init-functions %buildroot%_sbindir/install2-init-functions
for stage in initinstall preinstall postinstall; do
	live_stagedir="%_libexecdir/alterator/hooks/livecd-$stage.d"
	install2_stagedir="%_datadir/install2/$stage.d"
	mkdir -p %buildroot$live_stagedir
	sed -e "s;@LIVECD_HOOKS_STAGE_DIR@;$live_stagedir;" \
	    -e "s;@INSTALL2_HOOKS_STAGE_DIR@;$install2_stagedir;" run_install_features.sh.in > \
		%buildroot$live_stagedir/95-run_install_features.sh
	chmod 0755 %buildroot$live_stagedir/95-run_install_features.sh
done

%files
%_sbindir/install2-init-functions
%_libexecdir/alterator/hooks/livecd-*/*

%changelog
* Mon Jun 06 2011 Mikhail Efremov <sem@altlinux.org> 0.3-alt2
- Use digital prefix for hooks.

* Thu Jun 02 2011 Mikhail Efremov <sem@altlinux.org> 0.3-alt1
- Run all hooks (initinstall,preinstall,postinstall).

* Fri May 20 2011 Mikhail Efremov <sem@altlinux.org> 0.2-alt1
- Run preinstall hooks, not postinstall.

* Wed May 18 2011 Mikhail Efremov <sem@altlinux.org> 0.1-alt1
- Initial build

