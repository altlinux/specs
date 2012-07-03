%define _name gimplensfun
%define gimpplugindir %(gimptool-2.0 --gimpplugindir)

Name: gimp-plugin-lensfun
Version: 0.2.1
Release: alt2

Summary: lens distortion correction plugin for Gimp
License: GPLv3
Group: Graphics

Url: http://lensfun.sebastiankraft.net/
Source: %url%_name-%version.tar.gz
Patch: %_name-0.2.1-alt-makefile.patch

Requires: gimp >= 2.6
BuildRequires: gcc-c++ libexiv2-devel libgimp-devel libgomp-devel liblensfun-devel

%description
GimpLensfun is a Gimp plugin to correct lens distortion using the
lensfun library and database.

%prep
%setup -n %_name-%version
rm -rf bin
%patch -p1 -b .makefile

%build
%make

%install
install -pD %_name %buildroot%gimpplugindir/plug-ins/%_name

#export DESTDIR=%buildroot
#gimptool-2.0 --install-admin-bin %_name

%files
%gimpplugindir/plug-ins/%_name
%doc README.txt CHANGES.txt

%changelog
* Wed May 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt2
- fixed install for gimp-2.8

* Mon Nov 14 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- 0.2.1

* Tue Nov 01 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2-alt2
- rebuilt against libexiv2.so.11

* Fri Sep 23 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2-alt1
- 0.2

* Mon Jan 31 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt1
- first build for Sisyphus

