%define oname FreeMind
%define dversion MW1.16

Name: mediawiki-extensions-%oname
Version: 0.0.1
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Summary: This extension is for FreeMind-Users. It displays the FreeMind-MindMap (user does not have to install FreeMind).
Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Denis Baranov <baraka@altlinux.ru>

License: GPL

BuildPreReq: rpm-build-mediawiki >= 0.2
Requires: mediawiki-common >= 1.16

Source: %oname-%version.tar


%description
Displays FreeMind MindMaps as flash or java applet with full navigation.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname

%files -f %oname.files

%changelog
* Sat Mar 10 2012 Denis Baranov <baraka@altlinux.ru> 0.0.1-alt1
- Initial build for ALTLinux

