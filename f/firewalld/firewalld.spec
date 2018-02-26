Name: firewalld
Version: 0.2.5
Release: alt1

Summary: A firewall daemon with D-BUS interface providing a dynamic firewall
License: %gpl2plus
Group: System/Configuration/Networking

URL: http://fedorahosted.org/firewalld
# git://git.fedorahosted.org/firewalld.git
Source: %name-%version.tar
Source1: %name.init
#Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses
BuildRequires: intltool glib2-devel python-devel libgio-devel

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
#patch -p1

# create po/POTFILES.in
for i in $(cat po/POTFILES.in.in); do echo $i>>po/POTFILES.in; done

# create po/LINGUAS
ls po/*.po | sed -e 's/.po//' | sed -e 's/po\///' > po/LINGUAS

%build
%autoreconf
%configure \
	--enable-systemd
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
%attr(0750,root,root) %config(noreplace) %_sysconfdir/firewalld
%attr(0640,root,root) %config(noreplace) %_sysconfdir/firewalld/firewalld.conf
%config(noreplace) %_sysconfdir/sysconfig/firewalld
%_initdir/%name
%_usr/lib/firewalld
%systemd_unitdir/firewalld.service
%config(noreplace) %_sysconfdir/dbus-1/system.d/FirewallD.conf
%_datadir/polkit-1/actions/org.fedoraproject.FirewallD1.policy
%python_sitelibdir_noarch/firewall
%_man1dir/*
%_man5dir/*

%files -n firewall-applet
%_bindir/firewall-applet
%_desktopdir/firewall-applet.desktop
%_iconsdir/hicolor/*/apps/firewall-applet*.*
%_datadir/glib-2.0/schemas/org.fedoraproject.FirewallApplet.gschema.xml

%changelog
* Mon Jun 04 2012 Mikhail Efremov <sem@altlinux.org> 0.2.5-alt1
- Updated to 0.2.5.

* Wed Mar 14 2012 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt2
- Fix firewalld.conf permissions.
- Fix URL.

* Mon Mar 12 2012 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1
- Initial build (based on Fedora spec).
