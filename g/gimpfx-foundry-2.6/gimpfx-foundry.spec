%define gimpmajor 2.0
%define gimpver 2.6

Name: gimpfx-foundry-%gimpver
Version: 1
Release: alt1

Summary: Various Gimp scripts repository
License: GPL
Group: Graphics
Packager: Fr. Br. George <george@altlinux.ru>
Url: http://gimpfx-foundry.sourceforge.net/
Source: http://dl.sourceforge.net/sourceforge/gimpfx-foundry/%name-%version.tar.gz

BuildArch: noarch
Requires: gimp >= %gimpver

%description
Repository for porting and creating GPL licensed scripts for the latest GIMP. At the moment that is %gimpver. In the future this effort can be directed towards newer versions easily while still providing a source for older versions of scripts.

%prep
%setup -cq

%build

%install
install -d %buildroot%_datadir/gimp/%gimpmajor/scripts/
install -p *.scm %buildroot%_datadir/gimp/%gimpmajor/scripts/

%files
%doc *.txt
%_datadir/gimp/%gimpmajor/scripts/*

%changelog
* Sat Nov 15 2008 Fr. Br. George <george@altlinux.ru> 1-alt1
- Initial build from scratch

