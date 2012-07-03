%define sname gits
# for backports/branches:
%define tdir %_datadir/X11/icewm/themes

Name: icewm-theme-gits
Version: 0.2
Release: alt1
License: GPL
Group: Graphical desktop/Icewm
URL: http://www.crash-override.net
Summary: Theme inspired by Masamune Shirow's Ghost in the Shell
BuildArch: noarch
Requires: icewm-light
Provides: design-icewm
Source: icewm_%sname-0.2.tar.gz.gz

%description
Theme inspired by Masamune Shirow's Ghost in the Shell

%prep
%install
mkdir -p %buildroot%tdir
tar xfz %SOURCE0 -C %buildroot%tdir/
mv %buildroot%tdir/ghost_in_the_shell/{ChangeLog,ReadMe,TODO} .
mv %buildroot%tdir/ghost_in_the_shell %buildroot%tdir/%sname

%files
%tdir/%sname
%doc ChangeLog ReadMe TODO

%changelog
* Fri Aug 15 2008 Terechkov Evgenii <evg@altlinux.ru> 0.2-alt1
- Initial build for ALT Linux Sisyphus
