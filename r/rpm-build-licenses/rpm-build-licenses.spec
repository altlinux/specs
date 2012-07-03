# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define _name licenses

Name: rpm-build-%_name
Version: 2.0.4
Release: %branch_release alt1

Summary: RPM macros for well-known licenses
# We can't use our own macros...
License: GPLv2
Group: Development/Other
Url: http://www.altlinux.org/License

Source: %name-%version.tar

Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Requires: common-licenses

BuildRequires(pre): rpm-macros-branch

%description
This package contains RPM macros for license names commonly used in
Open Source software. Use these macros in License tags of your specfiles.

%prep
%setup -n %name-%version
ln -sf %_licensedir/GPL-2 COPYING

%install
cat <<__EOF__ >%_name.rpmmacros
%%gpl2only GPLv2
%%gpl2plus GPLv2+
%%gpl3only GPLv3
%%gpl3plus GPLv3+
%%lgpl2only LGPLv2
%%lgpl21only LGPLv2.1
%%lgpl2plus LGPLv2+
%%lgpl21plus LGPLv2.1+
%%lgpl3only LGPLv3
%%lgpl3plus LGPLv3+
%%bsd_orig BSD (original)
%%bsd BSD (revised)
%%bsdstyle BSD-style
%%mit MIT/X Consortium
%%mpl MPL
%%w3cl W3C
%%asl Apache
%%jpackage_license JPackage
%%sendmail_license Sendmail
%%artistic_license Artistic
%%artistic_license_v2 Artistic 2.0
%%perl_license Perl (GPL or Artistic)
%%fdl FDL
%%lppl LPPL
%%qpl1 QPLv1.0
%%ccbysa30 CC-BY-SA-3.0
%%ccby30 CC-BY-3.0
%%ccbysa25 CC-BY-SA-2.5
%%ccby25 CC-BY-2.5
%%epl Erlang Public License
%%pubdomain Public domain
%%distributable Distributable, non-free

# Not sure whether these ones should exist at all. Too clumsy names and vague
# semantics.
%%gpllgpl2only \
%{warning Hopefully you have read the README section about %%gpllgpl* macros.}\
GPLv2, LGPLv2
%%gpllgpl2plus \
%{warning Hopefully you have read the README section about %%gpllgpl* macros.}\
GPLv2+, LGPLv2+
%%gpllgpl3only \
%{warning Hopefully you have read the README section about %%gpllgpl* macros.}\
GPLv3, LGPLv3
%%gpllgpl3plus \
%{warning Hopefully you have read the README section about %%gpllgpl* macros.}\
GPLv3+, LGPLv3+
__EOF__
install -pD -m644 %_name.rpmmacros %buildroot%_rpmmacrosdir/%_name

%files
%_rpmmacrosdir/%_name
%doc README
%doc --no-dereference COPYING

%changelog
* Mon Apr 04 2011 Aleksey Avdeev <solo@altlinux.ru> 2.0.4-alt1
- added Qt Public License Version 1.0 (Bug #25374)
- relocated macro files to %%_rpmmacrosdir/

* Wed Jan 19 2011 Sergey Y. Afonin <asy@altlinux.ru> 2.0.3-alt1
- added Artistic License 2.0 (Bug #24921)

* Sat Jun 27 2009 Alexey Rusakov <ktirf@altlinux.org> 2.0.2-alt1
- added %distributable - a generic macro for a license not approved by OSI
  (read the README file) (closes ALT Bug 20443).

* Fri Mar 06 2009 Alexey Rusakov <ktirf@altlinux.org> 2.0.1-alt1
- %%gpllgpl* macros get back but with a warning (Bug #19079)

* Sat Feb 28 2009 Alexey Rusakov <ktirf@altlinux.org> 2.0-alt1
- added a README file with notes and Q&A on using license macros (Bug #12972)
- removed %%gpllpgl* macros (they are weird and unused)
- resolved ambiguity of the BSD license: %%bsd now only means the revised
  BSD. If you used %%bsd macro in some package, revisit it to check if it
  really is distributed under the terms of the revised BSD license
- added macros for LGPLv2.1 and LGPLv2.1+
- use GPL-2 file from common-licenses for COPYING file
- added Url tag

* Sun Feb 15 2009 Alexey Rusakov <ktirf@altlinux.org> 1.0.2-alt1
- added Erlang Public License (Bug #18635)

* Sat Jan 24 2009 Alexey Rusakov <ktirf@altlinux.org> 1.0.1-alt1
- added Creative Commons licenses (Bug #18600)
- added Packager and Url tags to favor repocop

* Sat Sep 22 2007 Alexey Rusakov <ktirf@altlinux.org> 1.0-alt2
- fixed copy-paste consequences in the package Summary (Bug #12875)

* Wed Sep 05 2007 Alexey Rusakov <ktirf@altlinux.org> 1.0-alt1
- added %%lppl macro (closing Bug #12688)
- the package lives in git.alt from now on

* Mon Aug 20 2007 Alexey Rusakov <ktirf@altlinux.org> 0.8-alt1
- Changes after discussion in devel@altlinux:
  + GPLv2 or later -> GPLv2+ (and all similar ones)
  + %%bsdlike removed - %%bsdstyle added
  + removed 'License' word from expansions ('license' in macro names stays intact)
  + reduced FDL and MPL expansions to respective abbreviations
  + replaced slashes in multilicense macros (such as GPL/LGPL) with:
    + commas in cases where package parts are covered with different licenses;
    + ' or ' in cases where package may be distributed under either of the
      given licenses (dual or triple licensing);

* Sun Aug 05 2007 Alexey Rusakov <ktirf@altlinux.org> 0.7-alt1
- no more %%gpl2, %%gpl3 etc. - they are replaced with %%gpl2only, %%gpl3only
  etc. in order to eliminate ambiguity.

* Wed Aug 01 2007 Alexey Rusakov <ktirf@altlinux.org> 0.6-alt1
- added %%artistic_license, %%perl_license, and %%fdl (Bug #12433)

* Tue Jul 31 2007 Alexey Rusakov <ktirf@altlinux.org> 0.5-alt1
- added %%sendmail_license (not %%sendmail, sorry; there's only one namespace
  for all macros and we don't want macros' names to intersect, do we?)
- fixed a typo in the GPL/LGPL v3 macro
- added 'or later' counterparts to all GPL and LGPL licenses

* Tue Jul 03 2007 Alexey Rusakov <ktirf@altlinux.org> 0.4-alt1
- fixed the package Group.

* Mon Jul 02 2007 Alexey Rusakov <ktirf@altlinux.org> 0.3-alt1
- added %%gpllgpl{2,3}, %%bsdlike, %%asl (Apache), %%jpackage_license,
  %%mpl (Mozilla), %%w3cl (W3C License).
- changed %%mit from MIT/X11 to MIT/X consortium.

* Mon Jul 02 2007 Alexey Rusakov <ktirf@altlinux.org> 0.2-alt1
- Added %%lgpl2 and %%lgpl3.

* Sun Jul 01 2007 Alexey Rusakov <ktirf@altlinux.org> 0.1-alt1
- Initial Sisyphus version
- Here we go: %%gpl2, %%gpl2plus, %%gpl3 %%bsd, %%mit and %%pubdomain are
  available. Waiting for the input from the team.
