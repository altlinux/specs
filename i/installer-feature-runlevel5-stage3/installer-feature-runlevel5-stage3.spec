Name: installer-feature-runlevel5-stage3
Version: 0.4
Release: alt1

Summary: Provide a system with graphical boot
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Requires: /sbin/init

%description
%summary

%prep

%post
if [ -f /etc/inittab ]; then
	sed -ri 's,^id:[^:]+:initdefault,id:5:initdefault,' /etc/inittab
fi

# https://wiki.archlinux.org/index.php/Systemd#Running_DEs_under_systemd
rm -f /etc/systemd/system/default.target

%files

%changelog
* Mon Nov 19 2012 Michael Shigorin <mike@altlinux.org> 0.4-alt1
- systemd adaptation (that's called "intuitive" by now probably)

* Tue Jun 19 2012 Michael Shigorin <mike@altlinux.org> 0.3-alt2
- dropped extra installer-common-stage3 dependency
- spec update/cleanup

* Mon Nov 21 2011 Michael Shigorin <mike@altlinux.org> 0.3-alt1
- systemd compatibility

* Tue Oct 13 2009 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- rewritten from stage2 to stage3
- added an Url:

* Thu Sep 18 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.1-alt2
- remove Requires: portmap > 1:4.0-alt2

* Wed Apr 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
