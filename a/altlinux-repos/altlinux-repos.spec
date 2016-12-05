Name: altlinux-repos
Version: 0.7
Release: alt1

Summary: A set of ALT repos desktop files
License: GPL
Group: System/Configuration/Packaging
BuildArch: noarch

Source: %name-%version.tar

Conflicts: apt-conf-branch < 8.0.0-alt3
Conflicts: apt-conf-sisyphus < 7.1-alt1

%description
A set of desktop files describing ALTLinux repositories and mirrors

%prep
%setup

%install
mkdir -p %buildroot%_sysconfdir/apt
cp -a mirrors repositories vendors.list vendors.list.d %buildroot%_sysconfdir/apt/

%files
%_sysconfdir/apt/mirrors
%_sysconfdir/apt/repositories
%_sysconfdir/apt/vendors.list
%_sysconfdir/apt/vendors.list.d/alt.list

%changelog
* Mon Dec 05 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7-alt1
- Added mirror.datacenter.by mirror.

* Wed Jun 22 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.6-alt1
- Droped ibiblio.org mirror.
- Moved vendors.list.d/alt.list from apt-conf-{branch,sisyphus}.

* Thu Apr 14 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5-alt1
- Add p8 branch.

* Wed Dec 24 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4-alt1
- Dropped ftp.linux.kiev.ua mirror (ALT#30104, #30598).

* Wed Feb 19 2014 Andrey Cherepanov <cas@altlinux.org> 0.3-alt1
- Informika mirror is dead, remove it

* Wed Sep 04 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2-alt1
- Sisyphus has arepo.
- Add t6 and t7 branches.

* Mon Jun 10 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1-alt1
- Create separate package for altlinux repos desktop files
