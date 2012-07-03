# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

Name: cronbuild-sh-functions
Version: 0.2.1
Release: %branch_release alt1

Summary: Common shell functions for cronbuild scripts
License: %gpl2plus
Group: Development/Other

Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source: %name

BuildRequires(pre): rpm-macros-branch
BuildPreReq: rpm-build-licenses

%description
%summary

%install
install -D -m 644 %SOURCE0 %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Sat Jan 14 2012 Aleksey Avdeev <solo@altlinux.ru> 0.2.1-alt1
- Add new functions:
  + get_release_commit()

* Fri Dec 09 2011 Aleksey Avdeev <solo@altlinux.ru> 0.2.0-alt1
- Add new functions:
  + get_pullbranchmsg()
  + get_packageepochverionrel()
  + get_tagmsg()
  + get_tagname()
  + get_packageverion()
  + get_sorcetagname()
  + get_mntspecbranch()
  + get_sorcetagmsg()

* Wed Nov 30 2011 Aleksey Avdeev <solo@altlinux.ru> 0.1.1-alt1
- Fix default in functions:
  + get_mntrepohost()
  + get_mntrepopath()

* Mon Nov 28 2011 Aleksey Avdeev <solo@altlinux.ru> 0.1.0-alt1
- Add new functions:
  + get_mntname()
  + get_mntreponame()
  + get_mntrepohost()
  + get_mntrepohost()
  + get_mntrepourlpref()
  + get_mntrepourl()
  + get_mntsrpmsbranch()
  + pull_mntsrpmsbranch()

* Tue Nov 15 2011 Aleksey Avdeev <solo@altlinux.ru> 0.0.2-alt1
- Add packagespecname sets

* Wed Nov 09 2011 Aleksey Avdeev <solo@altlinux.ru> 0.0.1-alt1
- Initial build for ALT Linux Sisyphus
