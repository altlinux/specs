Name: altlinux-repos
Version: 0.1
Release: alt1

Summary: A set of ALT repos desktop files
License: GPL
Group: System/Configuration/Packaging
BuildArch: noarch

Source: %name-%version.tar

Conflicts: apt-conf-branch < 7.0.0-alt3
Conflicts: apt-conf-sisyphus < 7.0-alt2

%description
A set of desktop files describing ALTLinux repositories and mirrors

%prep
%setup

%install
mkdir -p %buildroot%_sysconfdir/apt
cp -a mirrors repositories %buildroot%_sysconfdir/apt/


%files
%_sysconfdir/apt/repositories
%_sysconfdir/apt/mirrors

%changelog
* Mon Jun 10 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1-alt1
- Create separate package for altlinux repos desktop files
