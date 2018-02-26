%define _altdata_dir %_datadir/alterator

Name: alterator-ltsconf
Version: 0.4.1
Release: alt2

Summary: Alterator module for ALTSP terminal management
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/LTSP
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

Requires: alterator >= 2.9 gettext
Requires: nmap
Requires: ltsp-server >= 5.1.2-alt0.2.M40.3

BuildArch: noarch
BuildPreReq: alterator >= 2.9-alt0.10, alterator-standalone >= 2.5-alt0.3

%description
%summary

%prep
%setup

%build
%make_build libdir=%_libdir

%install
%makeinstall
#find_lang %name

#files -f %name.lang
%files
%_altdata_dir/applications/*
%_altdata_dir/ui/*/
%_alterator_backend3dir/*
%_altdata_dir/images/ltsconf

%changelog
* Tue Jul 13 2010 Michael Shigorin <mike@altlinux.org> 0.4.1-alt2
- dropped localization (belongs to alterator-l10n now)

* Tue Jan 05 2010 Michael Shigorin <mike@altlinux.org> 0.4.1-alt1
- backend fixup (closes: #22634)
- micro ui cleanup

* Thu Dec 17 2009 Michael Shigorin <mike@altlinux.org> 0.4.0-alt1
- backend update/cleanup by slazav@, thanks a lot!
- added an Url:
- minor spec cleanup

* Fri Jun 20 2008 Michael Shigorin <mike@altlinux.org> 0.3.1-alt1
- updated translation

* Fri Jun 20 2008 Michael Shigorin <mike@altlinux.org> 0.3.0-alt1
- added manual X resolution setup for thin clients

* Mon Apr 14 2008 Michael Shigorin <mike@altlinux.org> 0.2.7-alt1
- moved from System to Network submenu

* Fri Apr 11 2008 Michael Shigorin <mike@altlinux.org> 0.2.6-alt1
- fixed to work with current builds of ltsp-5.1
  (/var/lib/ltsp5/ -> /var/lib/ltsp/)

* Thu Apr 10 2008 Michael Shigorin <mike@altlinux.org> 0.2.5-alt1
- merged fixes by slazav@

* Fri Mar 28 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2.0-alt3
- add X-Alterator-UI=qt to ltsconf.default

* Mon Mar 24 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2.0-alt2
- remove children-align and layout-policy attributes from ui (bug #14945)

* Fri Dec 14 2007 Michael Shigorin <mike@altlinux.org> 0.2.4-alt1
- we should also install images then *probably* :)

* Wed Dec 12 2007 Michael Shigorin <mike@altlinux.org> 0.2.3-alt1
- 0.2.3:
  + visualize true/false values

* Wed Dec 12 2007 Michael Shigorin <mike@altlinux.org> 0.2.2-alt1
- 0.2.2:
  + *added* Russian translation
  + removed --open nmap option which is too new (4.20+) 
    but not critical at all

* Tue Dec 11 2007 Michael Shigorin <mike@altlinux.org> 0.2.1-alt1
- 0.2.1:
  + added Russian translation

* Fri Nov 30 2007 Michael Shigorin <mike@altlinux.org> 0.2.0-alt1
- 0.2.0:
  + added realtime network portscan to determine terminal IPs

* Fri Nov 30 2007 Michael Shigorin <mike@altlinux.org> 0.1.1-alt1
- 0.1.1:
  + is able to switch on/off sound and localdev support,
    nothing really more for now

* Tue Nov 06 2007 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial implementation (somewhat based on net-pptp-0.4-alt1)
- great many thanks for advice and hints to:
  + Stanislav Ievlev
  + Sergey Bolshakov
  + Victor Sovetov
  + Wad Mashckoff

