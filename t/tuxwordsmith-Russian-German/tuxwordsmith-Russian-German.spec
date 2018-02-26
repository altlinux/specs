%define oname Russian-German
%define pkgdata %_gamesdatadir/TuxWordSmith

Name: tuxwordsmith-%oname
Version: 1.0
Release: alt1

Summary: %oname language file for TuxWordSmith

Packager: Vitaly Lipatov <lav@altlinux.ru>

Group: Games/Educational

License: GPL
Url: http://www.asymptopia.org/staticpages/index.php?page=TuxWordSmith

Source: http://prdownloads.sourceforge.net/sourceforge/tuxwordsmith/%oname.tgz

BuildArch: noarch

Requires: tuxwordsmith

%description
%oname language file for TuxWordSmith

%prep
%setup -q -c -n %oname

%install
mkdir -p %buildroot%pkgdata
cp -R xdxf %buildroot%pkgdata

%files
%pkgdata/xdxf/%oname/

%changelog
* Thu Jan 08 2009 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Linux Sisyphus
