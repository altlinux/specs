Name: portsentry
Version: 1.2
Release: alt1

Summary: Advanced portscan detector
Summary(ru_RU.UTF-8): Детектор сканирования портов
Copyright: CPL
Group: System/Servers
URL: http://sourceforge.net/projects/sentrytools/
Packager: Aleksandr Blokhin 'Sass' <sass@altlinux.ru>

Source: %name-%version.tar.bz2
Source1: %name.init

Patch0: %name-1.1-alt.patch
Patch1: %name-1.1-fhs-alt.patch
Patch2: %name-1.2-alt-no_new_line.patch

%description
PortSentry is part of the Abacus Project suite of tools. The Abacus
Project is an initiative to release low-maintenance, generic, and reliable
host based intrusion detection software to the Internet community. 
PortSentry monitors TCP and UDP ports for illegal entry and port scans.
More information can be obtained from %url.

%description -l ru_RU.UTF-8
PortSentry является частью набора инструментов из Abacus Projec. 
Abacus Projec, это попытка реализации не требовательного, 
универсального и надёжного программного обеспечения 
обнаружения вторжения в систему для Интернет-сообщества. 
PortSentry следит за TCP и UDP портами, препятствуя вторжению 
и их сканированию.

%prep
%setup -q -n portsentry_beta
%patch0 -p1
%patch1 -p1
%patch2 -p1

find -type f |
	xargs %__grep -F -l /usr/local/psionic/%name/portsentry. |
	xargs %__perl -pi -e 's,/usr/local/psionic/%name/portsentry.(blocked|history),/var/log/%name/\1,g'
find -type f |
	xargs %__grep -F -l /usr/local/psionic/%name |
	xargs %__perl -pi -e 's,/usr/local/psionic/%name,%_sysconfdir/%name,g'

%build
%make_build linux

%install
%__mkdir_p $RPM_BUILD_ROOT{%_sysconfdir/%name,%_logdir/%name}

%makeinstall
%__install -m700 -D %SOURCE1 $RPM_BUILD_ROOT%_initrddir/%name

touch $RPM_BUILD_ROOT%_logdir/%name/{blocked,blocked.{atcp,audp},history}

%__cat >$RPM_BUILD_ROOT%_sysconfdir/%name/always_ignore <<EOF
# Include the host IP addresses you want %name to always ignore
127.0.0.1
EOF

%post
%post_service %name

touch %_logdir/%name/{blocked,blocked.{atcp,audp},history}
chown root.adm %_logdir/%name/{blocked,blocked.{atcp,audp},history}
chmod 640 %_logdir/%name/{blocked,blocked.{atcp,audp},history}
 
%preun
%preun_service %name

%files
%doc CHANGES CREDITS LICENSE README.* ignore.csh
%config %_initdir/%name
%_sbindir/%name
%attr(750,root,adm) %dir %_sysconfdir/%name
%attr(640,root,adm) %config(noreplace) %_sysconfdir/%name/*
%attr(750,root,adm) %dir %_logdir/%name
%attr(640,root,adm) %ghost %_logdir/%name/*

%changelog
* Fri Sep 23 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1.2-alt1
- 1.2
- Changed License

* Mon Feb 16 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1.1-alt8
- Applied initscript patch by LDV.

* Thu Feb 12 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1.1-alt7
- Updated initscript

* Sun Oct 19 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1.1-alt6
- Removed obsoleted requires

* Thu May 15 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1.1-alt5
- Replaced old initscript with new one.

* Mon Oct 21 2002 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1.1-alt4
- updated buildmacros

* Fri Oct 18 2002 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 1.1-alt3
- fixed an error, resulting to refusal in UDP-ports tracing at portsentry startup

* Sat Oct 12 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1.1-alt2
- rebuilded with gcc-3.2
- added Summary & description in russian

* Tue Jul 31 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1-alt1
- 1.1

* Thu May 24 2001 Stanislav Ievlev <inger@altlinux.ru> 1.0-ipl5mdk
- Rebuild for use new macros post_service and preun_service

* Sat Jan 13 2001 Dmitry V. Levin <ldv@fandra.org> 1.0-ipl4mdk
- RE adaptions.

* Sat Dec 30 2000 Vincent Danen <vdanen@mandrakesoft.com> 1.0-4mdk
- patch to ignore.csh to read /etc/portsentry/always_ignore so you no longer
  need to edit ignore.csh itself
- move config files to /etc/portsentry from /etc

* Thu Aug  3 2000 Vincent Danen <vdanen@mandrakesoft.com> 1.0-3mdk
- macros

* Thu Apr 27 2000 Vincent Danen <vdanen@linux-mandrake.com> 1.0-2mdk
- fix specfile for spec-helper
- fix group
- patch to ignore.csh for proper paths to config files

* Thu Dec 2 1999 Lenny Cartier <lenny@mandrakesoft.com>
- new in contribs
- used the srpm provided by Vincent Danen <vdanen@linux-mandrake.com>

* Wed Dec 1 1999 Vincent Danen <vdanen@linux-mandrake.com> 1.0-1mdk
- updated specfile for Mandrake contribs
- bzip sources
- 1.0:
-  - NeverBlock() function fixed.
-  - Updated docs.
-  - Y2K fix in WriteBlocked functions.

* Thu Nov 11 1999 Vincent Danen <vdanen@softhome.net>
- wrote patches to source files, now we can use pristine source

* Tue Nov 9 1999 Vincent Danen <vdanen@softhome.net>
- updated spec file to clean up properly
- specfile adaptations

* Tue Sep 28 1999 Vincent Danen <vdanen@softhome.net>
- updated spec file
- removed original source (you can grab it from Psionic's website anyway)

* Mon Sep 6 1999 Vincent Danen <vdanen@softhome.net>
- fixed paths in portsentry.conf
- updated spec file
- changed release number to *mdk to indicate Mandrake compliance
- Mandrake adaptions

* Sun Sep 5 1999 Vincent Danen <vdanen@softhome.net>
- adapted Makefile, portsentry-config.h, and ignore.csh to work with RPM
- wrote spec file
- included original source (unmodified)
