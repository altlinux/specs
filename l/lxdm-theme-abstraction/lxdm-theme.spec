%define theme_name abstraction
%define theme_version 0.1

%define _unpackaged_files_terminate_build 1
%define theme_fullname lxdm-theme-%theme_name
%define themes_dir %_datadir/lxdm/themes

Name: %theme_fullname
Version: %theme_version
Release: alt6
Packager: Radik Usupov <radik@altlinux.org>
BuildArch: noarch

Summary: Provides theme for LXDM in ALT Linux
Group: Graphical desktop/Other
License: GPL

Source: %theme_name.tar.bz2

%description
Default graphics theme for LXDM in ALT Linux

%install
mkdir -p %buildroot%themes_dir
tar xvf %SOURCE0 -C %buildroot%themes_dir

mkdir -p %buildroot/etc/alternatives/packages.d/
cat > %buildroot/etc/alternatives/packages.d/%theme_fullname << __EOF__
%themes_dir/default %themes_dir/%theme_name 20
__EOF__

%files 
%config /etc/alternatives/packages.d/%theme_fullname
%themes_dir/%theme_name

%changelog
* Fri Oct 01 2010 Radik Usupov <radik@altlinux.org> 0.1-alt6
- package is now noarch

* Wed Jun 30 2010 Mykola Grechukh <gns@altlinux.ru> 0.1-alt5
- priority increased

* Tue Jun 15 2010 Mykola Grechukh <gns@altlinux.ru> 0.1-alt4
- package layout fixed

* Fri Jun 11 2010 Radik Usupov <radik@altlinux.org> 0.1-alt2
- Fixed installation directory topics

* Fri Jun 11 2010 Radik Usupov <radik@altlinux.org> 0.1-alt1
- Initial build for ALTLinux


