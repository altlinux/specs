%define _altdata_dir %_datadir/alterator

Name: alterator-notes
Version: 1.1
Release: alt9

Provides: alterator-license = %version
Obsoletes: alterator-license

Packager: Vladislav Zavjalov <slazav@altlinux.org>

BuildArch:	noarch

Source:%name-%version.tar

Summary: alterator module for view license and release notes
License: GPL
Group: System/Configuration/Other
Requires: alterator >= 3.1-alt4, alterator-sh-functions
Conflicts: alterator-browser-qt < 2.9.70
Conflicts: alterator-lookout    < 0.3

BuildPreReq: alterator >= 3.1
BuildRequires: alterator

%description
alterator module for view license and release notes

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*/
%_alterator_backend3dir/*

%changelog
* Tue Jan 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt9
- move translations to alterator-l10n

* Fri Dec 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt8
- use help from new l10n

* Tue Dec 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt7
- update help (by azol@)

* Mon Sep 22 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt6
- rebuild with new alterator-l10n

* Tue Sep 09 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt5
- rebuild with new alterator-l10n

* Thu Jul 03 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt4
- remove translations from desktop file

* Wed Jul 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt3
- remove (document:insert "/std/functions") from qt ui

* Wed Jul 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt2
- backend: use alterator_api_version=1

* Wed Jul 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt1
- remove po/*
- use module.mak

* Mon Jun 16 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt7
- fix desktop file (fix #15957)

* Thu May 15 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt6
- rebuild with new alterator-l10n

* Thu May 08 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt5
- use alterator-l10n

* Fri Mar 28 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt4
- << and >> quotes in po-file

* Fri Mar 07 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt3
- use "url" attribute of textarea
- if accesed from the next page then "agree" checked 

* Wed Mar 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt2
- add <head> section in help-files

* Fri Feb 29 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt1
- rename from alterator-license 

* Tue Jan 22 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- add help
- backend: add support for diffent licenses

* Wed Oct 10 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- fix again

* Fri Oct 05 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- fix translation

* Tue Sep 18 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- convert license to html format

* Thu Aug 16 2007 Alexey Gladkov <legion@altlinux.ru> 0.1-alt1
- Initial release
