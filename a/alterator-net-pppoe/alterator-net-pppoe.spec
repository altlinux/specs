%define _altdata_dir %_datadir/alterator

Name: alterator-net-pppoe
Version: 0.9
Release: alt1

Summary: alterator module for pppoe connections configuration
License: GPL
Group: System/Configuration/Other

Packager: Stanislav Ievlev <inger@altlinux.org>
Source: %name-%version.tar
BuildArch: noarch

Requires: alterator >= 4.9-alt2
Requires: alterator-sh-functions >= 0.3-alt2
Requires: alterator-net-functions >= 0.8-alt1
Requires: alterator-hw-functions
Requires: rp-pppoe-base
Conflicts: alterator-fbi < 5.10-alt1
Conflicts: alterator-lookout < 1.6-alt8

BuildPreReq: alterator >= 4.9-alt2

%description
alterator module for pppoe connections configuration

%prep
%setup -q

%build
%make_build

%install
%makeinstall

# TODO:
# - merge up with /net-pptp -> /net-vpn,
#   move PPP-related part to separate tab (/net-pppoptions)
#   (see #11988 for comprehensive discussion of tunables)

%files
%_altdata_dir/applications/*
%_altdata_dir/ui/*
%_alterator_backend3dir/*

%changelog
* Fri Jan 15 2010 Mikhail Efremov <sem@altlinux.org> 0.9-alt1
- use setsid for ifup comand (closes #21445).

* Tue Sep 29 2009 Mikhail Efremov <sem@altlinux.org> 0.8-alt1
- fix status translations.
- join callbacks for qt and html.
- disable UI if connections do not exist (closes: #21660).

* Wed Aug 12 2009 Mikhail Efremov <sem@altlinux.org> 0.7-alt2
- fixed requires (closes: #21037)

* Mon Apr 13 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt1
- use modern form library, ajax interface and alterator-net-functions

* Tue Jan 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.6.1-alt6
- move translations and help to alterator-l10n

* Mon Jan 19 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.6.1-alt5
- merge with inger

* Fri Dec 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.6.1-alt4.2
- use help from l10n
- rebuild

* Tue Nov 11 2008 Stanislav Ievlev <inger@altlinux.org> 0.6.1-alt4.1
- minor module updates and improvements

* Wed Nov 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.6.1-alt3
- add DOCTYPE to html template

* Sat Nov 01 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.6.1-alt2
- remove title and h1 from html template

* Sat Oct 18 2008 Michael Shigorin <mike@altlinux.org> 0.6.1-alt1
- fixed a blocker typo introduced in 0.6-alt1 (#17489)

* Tue Sep 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt1
- remove unused constraints
- remove unused with-translation

* Tue Jun 17 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt2
- join to common translation database

* Thu May 15 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt1
- use alterator-sh-functions
- rewrite interface

* Mon May 12 2008 Michael Shigorin <mike@altlinux.org> 0.4.5-alt1
- add "usepeerdns" by default into pppoptions (#15603)

* Tue Mar 04 2008 Michael Shigorin <mike@altlinux.org> 0.4.4-alt3
- rebuild

* Tue Mar 04 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4.4-alt2
- Change help paths to the new style.

* Sun Mar 02 2008 Michael Shigorin <mike@altlinux.org> 0.4.4-alt1
- applied modified patch by Konstantin Uvarin (lodin@)
  to move password from chap-secrets which is shared by 
  all connections into interface-specific pppoptions (#14649)

* Fri Dec 07 2007 Michael Shigorin <mike@altlinux.org> 0.4.3-alt1
- s/1492/1476/ (as suggested by shrek@, see #11958c15)

* Thu Dec 06 2007 Michael Shigorin <mike@altlinux.org> 0.4.2-alt1
- added default MTU value (1492, as recommended in poptop docs)

* Thu Dec 06 2007 Michael Shigorin <mike@altlinux.org> 0.4.1-alt1
- added MPPE checkbox and defaultroute (partial fix for #11958)
- uk.po update

* Thu Jul 19 2007 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- use alterator-net-common common library

* Wed Jun 13 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt13
- add desktop file

* Thu May 31 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt12
- rebuild with latest standalone
- add interface status info

* Fri May 25 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt11
- switch to new card-index scripts

* Mon Apr 23 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt10
- update Ukrainian translation

* Thu Apr 19 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt9
- little CSS optimizations

* Thu Apr 05 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt8
- remove config-*

* Mon Apr 02 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt7
- add Ukrainian translation
- help improvements from kirill@

* Fri Mar 30 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt6
- improve po template generation
- add documentation

* Wed Mar 14 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt5
- assign 'Network' group

* Wed Mar 07 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt4
- more translations
- use gridbox

* Thu Feb 22 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt3
- use ifup/ifdown instead of whole network restart
- enable auto-select

* Mon Feb 19 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt2
- simplify backend
- fix ethernet device listing

* Thu Feb 08 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- add fbi data

* Mon Jan 15 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- require gettext
- add label constraints

* Wed Dec 13 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt6
- fix backend (read on /)

* Wed Dec 06 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt5
- move "first available interface" logic from UI to backend
- list all available eth interfaces itself

* Wed Nov 29 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- visualize constraints

* Tue Nov 14 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- enable constraints

* Wed Nov 08 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- use native message boxes

* Wed Nov 01 2006 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- initial release


