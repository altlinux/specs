# TODO -- create initscript
%define origname op_panel

%def_without snapshot

Name: asterisk-op_panel
Summary: Flash Operators Panel
Version: 0.30
Release: alt5.1
License: GPL
Group: System/Servers

BuildArch: noarch

Url: http://www.asternic.org/

Patch1: %name-configs.patch
Patch2: %name-daemonize.patch

Requires: webserver-common

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %origname-%version.tar
Source1: op_panel-alt.sh

Requires(pre): asterisk-base

BuildRequires: perl-Pod-Parser

%description
Flash Operators Panel

%prep
%setup -n %origname-%version
%patch1 -p1
%patch2 -p1

%build
%install
mkdir -p %buildroot/var/www/html/%name
mkdir -p %buildroot%_sysconfdir/%name
mkdir -p %buildroot%_initdir/
mkdir -p %buildroot/var/run/%name

cp -a flash/* %buildroot/var/www/html/%name

install -D op_server.pl %buildroot%_sbindir/op_panel
install *.cfg %buildroot%_sysconfdir/%name
install -m 0755 %SOURCE1 %buildroot%_initdir/op_panel

%preun
%preun_service op_panel
%post
%post_service op_panel

%files
%attr(0700,_asterisk,_asterisk)	%dir /var/run/%name
%attr(0570,_asterisk,pbxadmin)	%dir %_sysconfdir/%name/
%attr(0460,_asterisk,pbxadmin)	%config(noreplace)	%_sysconfdir/%name/*.cfg
%attr(0750,root,asterisk) 		%_sbindir/op_panel
%_initdir/op_panel
%attr(0755,_asterisk,_asterisk)	%dir /var/www/html/%name/
%attr(0644,_asterisk,_asterisk)	/var/www/html/%name/*
%doc CHANGES FAQ LICENSE README RECIPES TODO UPGRADE
%changelog
* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.30-alt5.1
- rebuilt with perl 5.12

* Thu Dec 03 2009 Denis Smirnov <mithraen@altlinux.ru> 0.30-alt5
- build as noarch

* Thu Dec 03 2009 Denis Smirnov <mithraen@altlinux.ru> 0.30-alt4
- fix configs for russian fonts support

* Mon Oct 19 2009 Denis Smirnov <mithraen@altlinux.ru> 0.30-alt3
- remove execution access from configs

* Tue Oct 06 2009 Denis Smirnov <mithraen@altlinux.ru> 0.30-alt2
- add requires to webserver-common
- fix config directory packaging

* Tue Jul 07 2009 Denis Smirnov <mithraen@altlinux.ru> 0.30-alt1
- update to 0.30

* Tue Sep 02 2008 Denis Smirnov <mithraen@altlinux.ru> 0.29-alt1
- update to 0.29 (thanks to Alex Radetsky)

* Mon Nov 19 2007 Denis Smirnov <mithraen@altlinux.ru> 0.28-alt0.svn20071114
- Update to last svn snapshot
- Russian language support added

* Wed Mar 21 2007 Denis Smirnov <mithraen@altlinux.ru> 0.27-alt1
- update to 0.27 (fixes for asterisk 1.4 support)

* Sun Aug 20 2006 Denis Smirnov <mithraen@altlinux.ru> 0.26-alt3
- move service to %_sbindir
- fix x86_64 build

* Fri Aug 18 2006 Denis Smirnov <mithraen@altlinux.ru> 0.26-alt2
- cleanup spec

* Sun Aug 13 2006 Denis Smirnov <mithraen@altlinux.ru> 0.26-alt1
- first build for Sisyphus
