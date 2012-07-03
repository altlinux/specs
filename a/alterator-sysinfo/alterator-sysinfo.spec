%define _altdata_dir %_datadir/alterator

Name: alterator-sysinfo
Version: 0.8
Release: alt5

Packager: Vladislav Zavjalov <slazav@altlinux.org>

BuildArch: noarch

Source:%name-%version.tar

Summary: alterator module to view general system information
License: GPL
Group: System/Configuration/Other
Requires: alterator >= 2.9 gettext

BuildPreReq: alterator >= 2.9-alt0.10
BuildPreReq: alterator-fbi >= 5.22-alt2
BuildPreReq: alterator-lookout

# Automatically added by buildreq on Mon Jul 11 2005 (-bi)
BuildRequires: alterator

%description
alterator module to view general system information

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_altdata_dir/applications/*
%_altdata_dir/ui/*/*
%_alterator_backend3dir/*

%changelog
* Mon Jun 04 2012 Andriy Stepanov <stanv@altlinux.ru> 0.8-alt5
- Don't print "ALT Linux" keywords

* Mon Jun 04 2012 Andriy Stepanov <stanv@altlinux.ru> 0.8-alt4
- Add release info

* Fri Dec 04 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.8-alt3
- move MHz from table header to values (closes: #22306)

* Tue Oct 13 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.8-alt2
- update translations in sysinfo.desktop

* Tue Oct 13 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.8-alt1
- html ui: use wf=none
- change memory usage tables
- don't show /dev and /dev/shm fs

* Thu Apr 23 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt1
- use enumref instead of optionlist in html tables

* Wed Mar 11 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt2
- fix spec

* Wed Mar 11 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt1
- move help and translations to alterator-l10n
- add table borders in html (fix #11640)
- move html template to ui dir

* Fri Dec 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt5
- update help and pt_BR.po

* Tue Dec 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt4
- update help (by azol@)

* Wed Nov 26 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt3
- capital letters in table headers

* Tue Nov 18 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt2
- remove cron job (#14927)

* Tue Nov 18 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt1
- add cpuinfo (#15303)

* Mon Nov 17 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt3
- add ru help (by azol@)

* Thu Nov 06 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt2
- fix translations

* Thu Nov 06 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt1
- add qt ui
- join disk_used and disk_percent columns

* Wed Nov 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt1
- update for new alterator
  + remove template backend
  + move html template to common place
  + use alterator-sh-functions (api-version=1)

* Thu Jun 14 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt6
- switch to new menu system

* Mon Apr 23 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt5
- add Ukrainian translation

* Thu Apr 19 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- little CSS improvements

* Wed Apr 18 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- add disk usage statistics generation

* Mon Apr 09 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- fix df usage (#11404)

* Tue Apr 03 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial release
