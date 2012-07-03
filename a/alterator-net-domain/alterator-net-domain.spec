%define _altdata_dir %_datadir/alterator

Name: alterator-net-domain
Version: 0.4
Release: alt11
Source:%name-%version.tar

Summary: alterator module to edit system network domain
License: GPL
Group: System/Configuration/Other
Requires: alterator >= 4.7-alt5
Requires: alterator-l10n >= 2.0-alt2
Conflicts: alterator-lookout < 1.6-alt6
Conflicts: alterator-fbi < 5.9-alt2

BuildPreReq: alterator >= 4.7-alt5

BuildArch: noarch

%description
alterator module to edit system network domain

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_altdata_dir/applications/*
%_altdata_dir/ui/*/
%_alterator_backend3dir/*
%dir %_libexecdir/alterator/hooks/net-domain.d
/etc/hooks/hostname.d/*


%changelog
* Tue May 15 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt11
- fix enabling krb5 without name change

* Wed Apr 18 2012 Mikhail Efremov <sem@altlinux.org> 0.4-alt10
- Change warning message.

* Wed Jun 15 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt9
- buttons rapaid in nonkerberos mode

* Fri Jun 10 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt8
- now module is html only

* Fri Apr 08 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt7
- hide kerberos domain status when disabled

* Tue Mar 29 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt6
- move samba restart to after all changes

* Tue Mar 29 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt5
- reread data after write
- start smbd when creating domain

* Tue Mar 29 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt4
- fix previous fix :(

* Mon Mar 28 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt3
- work in nonmaster mode fixed

* Mon Mar 28 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt2
- test for dhcpd
- checkbox for kerberos domain

* Thu Mar 24 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt1
- tests for ldap/kerberos domain status added

* Wed Dec 08 2010 Mikhail Efremov <sem@altlinux.org> 0.3-alt4
- More restrict possible domain names.

* Tue Oct 26 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt3
- always run net-domain.d hooks

* Mon Oct 25 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt2
- always run hooks

* Fri Oct 08 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- master if no role defined

* Fri Apr 16 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt5
- no roles now

* Wed Mar 03 2010 Mikhail Efremov <sem@altlinux.org> 0.2-alt4
- check hostname length.

* Fri Dec 11 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt3
- bugfix: write role before writing of domain name

* Wed Dec 09 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- restrict possible domain names

* Thu Oct 22 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- use workflow 'none', share callbacks between qt and html.

* Fri Aug 07 2009 Mikhail Efremov <sem@altlinux.org> 0.1-alt8
- write domain to /etc/net/ifaces/lo/resolv.conf.

* Thu Jun 11 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt7
- role is 'master' by default.

* Thu Apr 02 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt6
- menu file: move to group 'system'

* Mon Mar 30 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt5
- fix runhooks '#t' variant (used by firsttime)

* Wed Mar 18 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- add hook system
- add domain name to zeroconf information

* Fri Mar 13 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- fix typo

* Fri Mar 13 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- edit server role

* Wed Mar 04 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build

