Name: firestarter
Version: 1.0.3
Release: alt4
Summary: The Firestarter firewall GUI tool
Packager:       Mikhail Pokidko <pma@altlinux.ru>
Group: Security/Networking
License: GPL2+
Url: http://www.fs-security.com
Source0: %name-%version.tar.gz
Source1: %name.README.ALT
Patch0: %name.patch

# Automatically added by buildreq on Fri Feb 29 2008
BuildRequires: fontconfig gcc-c++ GConf libavahi-glib libdbus-glib libgnomeui-devel perl-XML-Parser libglade-devel

Requires: iptables
Requires: gtk2 >= 2.4.0
Requires: gnome-vfs2 => 2.6.0

%description
Firestarter is an easy-to-use, yet powerful, Linux firewall tool for GNOME.
Use it to quickly set up a secure environment using the firewall creation
wizard, or use it's monitoring and administrating features with your old
firewall scripts.

%prep
%setup -q
%patch0 -p1 

%build
%configure
make %{?_smp_mflags}

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_sbindir
mkdir -p %buildroot%_sysconfdir/%name/{inbound,outbound}
mkdir -p %buildroot%_sysconfdir/gconf/schemas/
mkdir -p %buildroot%_datadir/applications/
mkdir -p %buildroot%_datadir/pixmaps/
mkdir -p %buildroot%_datadir/%name/xpm/
mkdir -p %buildroot%_datadir/%name/glade/
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=%buildroot

mv %buildroot/%_bindir/firestarter %buildroot/%_sbindir
ln -fs %_bindir/consolehelper %buildroot%_bindir/%name
mv %name.desktop.in %buildroot%_datadir/applications/%name.desktop
mv %name.schemas %buildroot%_sysconfdir/gconf/schemas/%name.schemas
mv pixmaps/%name.png %buildroot%_datadir/pixmaps/
mv scripts/non-routables %buildroot%_sysconfdir/%name/
mv src/xpm/* %buildroot%_datadir/%name/xpm/
mv src/preferences.glade %buildroot%_datadir/%name/glade/

touch %buildroot/%_sysconfdir/%name/configuration
touch %buildroot/%_sysconfdir/%name/events-filter-hosts
touch %buildroot/%_sysconfdir/%name/events-filter-ports
touch %buildroot/%_sysconfdir/%name/%name.sh
touch %buildroot/%_sysconfdir/%name/firewall
touch %buildroot/%_sysconfdir/%name/sysctl-tuning
touch %buildroot/%_sysconfdir/%name/user-pre
touch %buildroot/%_sysconfdir/%name/user-post
#touch %buildroot/%_sysconfdir/%name/non-routables
touch %buildroot/%_sysconfdir/%name/inbound/allow-from
touch %buildroot/%_sysconfdir/%name/inbound/allow-service
touch %buildroot/%_sysconfdir/%name/inbound/forward
touch %buildroot/%_sysconfdir/%name/inbound/setup
touch %buildroot/%_sysconfdir/%name/outbound/allow-from
touch %buildroot/%_sysconfdir/%name/outbound/allow-service
touch %buildroot/%_sysconfdir/%name/outbound/allow-to
touch %buildroot/%_sysconfdir/%name/outbound/deny-from
touch %buildroot/%_sysconfdir/%name/outbound/deny-service
touch %buildroot/%_sysconfdir/%name/outbound/deny-to
touch %buildroot/%_sysconfdir/%name/outbound/setup

%find_lang %name

install -p -D -m0644 %name.pam %buildroot%_sysconfdir/pam.d/%name
install -p -D -m0644 %name.console  %buildroot%_sysconfdir/security/console.apps/%name
install -p -D -m0755 fedora.init %buildroot%_initdir/%name
install -p -D -m0644 %SOURCE1 ./README.ALT


%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %_sysconfdir/gconf/schemas/%name.schemas &>/dev/null
if [ "$1" = "1" ]; then
        /sbin/chkconfig --level 0123456 iptables off 2>/dev/null || :
        /sbin/chkconfig --add firestarter
        /sbin/chkconfig firestarter on
fi

%preun
if [ "$1" = "0" ]; then
	export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
	gconftool-2 --makefile-uninstall-rule %_sysconfdir/gconf/schemas/%name.schemas &>/dev/null

	/sbin/chkconfig iptables reset 2>/dev/null || :
	/sbin/service firestarter stop >/dev/null 2>&1
	/sbin/chkconfig --del firestarter
fi

%postun
if [ "$1" = "0" ]; then
    if [ -e /etc/dhclient-exit-hooks ]; then
        grep -v 'sh %_sysconfdir/firestarter/firewall.sh start' < /etc/dhclient-exit-hooks > /etc/dhclient-exit-hooks.tmp
        mv /etc/dhclient-exit-hooks.tmp /etc/dhclient-exit-hooks
    fi
fi

%files -f %name.lang
%doc README* ChangeLog AUTHORS TODO COPYING CREDITS
%_bindir/*
%_sbindir/*
%config %_initdir/*
%_sysconfdir/gconf/schemas/*
%_sysconfdir/pam.d/*
%_sysconfdir/security/console.apps/%name
%_sysconfdir/%name/*
%_datadir/applications/firestarter.desktop
%_datadir/pixmaps/%name.png
%_datadir/firestarter/*

%changelog
* Wed May 23 2012 Mikhail Pokidko <pma@altlinux.org> 1.0.3-alt4
- Fixed build error

* Thu Jan 14 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.3-alt3.1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for firestarter
  * postclean-05-filetriggers for spec file

* Sat Feb 14 2009 Alexey Rusakov <ktirf@altlinux.org> 1.0.3-alt3.1
- NMU: added libglade-devel to buildreqs

* Thu Apr 03 2008 Mikhail Pokidko <pma@altlinux.org> 1.0.3-alt3
- repocop fix

* Fri Sep 28 2007 Mikhail Pokidko <pma@altlinux.org> 1.0.3-alt2
- .desktop fix

* Wed Aug 15 2007 Mikhail Pokidko <pma@altlinux.org> 1.0.3-alt1
- Initial ALT build

