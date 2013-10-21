Name: firewalld
Version: 0.3.7
Release: alt1

Summary: A firewall daemon with D-BUS interface providing a dynamic firewall
License: %gpl2plus
Group: System/Configuration/Networking

URL: http://fedorahosted.org/firewalld
# git://git.fedorahosted.org/firewalld.git
Source: %name-%version.tar
Source1: %name.init
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses rpm-build-xdg
BuildRequires: intltool xsltproc docbook-style-xsl docbook-dtds glib2-devel python-devel libgio-devel

Requires: python-module-slip-dbus iptables ebtables iptables-ipv6

%description
firewalld is a firewall service daemon that provides a dynamic
customizable firewall with a D-BUS interface.

%package -n firewall-applet
Summary: Firewall panel applet
Group: System/Configuration/Networking
Requires: %name = %version-%release
Requires: python-module-pygtk-libglade

%description -n firewall-applet
The firewall panel applet provides a status information of firewalld and
also the firewall settings.

%prep
%setup
%patch -p1

# create po/POTFILES.in
#for i in $(cat po/POTFILES.in.in); do echo $i>>po/POTFILES.in; done

# create po/LINGUAS
ls po/*.po | sed -e 's/.po//' | sed -e 's/po\///' > po/LINGUAS

%build
%autoreconf
%configure \
	--enable-systemd \
	--with-systemd-unitdir=%systemd_unitdir
%make

%install
%makeinstall_std
%find_lang %name
install -pDm755 %SOURCE1 %buildroot%_initdir/%name

%post
%post_service %name

%preun
%preun_service %name

%files -f %name.lang
%_sbindir/*
%_bindir/firewall-cmd
%_bindir/firewall-offline-cmd
%attr(0750,root,root) %config(noreplace) %_sysconfdir/firewalld
%attr(0640,root,root) %config(noreplace) %_sysconfdir/firewalld/firewalld.conf
%config(noreplace) %_sysconfdir/sysconfig/firewalld
%_initdir/%name
%_usr/lib/firewalld
%systemd_unitdir/firewalld.service
%config(noreplace) %_sysconfdir/dbus-1/system.d/FirewallD.conf
%_datadir/polkit-1/actions/org.fedoraproject.FirewallD1.policy
%_datadir/bash-completion/completions/*
%python_sitelibdir_noarch/firewall
%_man1dir/*
%_man5dir/*

%files -n firewall-applet
%_bindir/firewall-applet
%_desktopdir/firewall-*.desktop
%_xdgconfigdir/autostart/firewall-applet.desktop
%_iconsdir/hicolor/*/apps/firewall-*.*
%_datadir/glib-2.0/schemas/org.fedoraproject.*.gschema.xml
%_bindir/firewall-config
%_datadir/firewalld/

%changelog
* Mon Oct 21 2013 Mikhail Efremov <sem@altlinux.org> 0.3.7-alt1
- Updated to 0.3.7.

* Tue Oct 08 2013 Mikhail Efremov <sem@altlinux.org> 0.3.6.2-alt1
- Updated to 0.3.6.2.

* Thu Oct 03 2013 Mikhail Efremov <sem@altlinux.org> 0.3.6.1-alt1
- Updated to 0.3.6.1.

* Mon Sep 30 2013 Mikhail Efremov <sem@altlinux.org> 0.3.5-alt1
- Updated to 0.3.5.

* Tue Aug 13 2013 Mikhail Efremov <sem@altlinux.org> 0.3.4-alt1
- Use autoconf-2.68.
- Updated to 0.3.4.

* Mon Jun 17 2013 Mikhail Efremov <sem@altlinux.org> 0.3.3-alt1
- Updated to 0.3.3.

* Tue May 14 2013 Mikhail Efremov <sem@altlinux.org> 0.3.2-alt1
- Updated to 0.3.2.

* Thu Jan 24 2013 Mikhail Efremov <sem@altlinux.org> 0.2.12-alt1
- Patch from upstream git:
  + default zone in firewalld.conf was set to public with every
    restart
- Updated to 0.2.12.

* Fri Dec 14 2012 Mikhail Efremov <sem@altlinux.org> 0.2.11-alt1
- Updated to 0.2.11.

* Wed Aug 29 2012 Mikhail Efremov <sem@altlinux.org> 0.2.7-alt1
- Updated to 0.2.7.

* Mon Jun 04 2012 Mikhail Efremov <sem@altlinux.org> 0.2.5-alt1
- Updated to 0.2.5.

* Wed Mar 14 2012 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt2
- Fix firewalld.conf permissions.
- Fix URL.

* Mon Mar 12 2012 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1
- Initial build (based on Fedora spec).
