%define oname CategoryTree
%define dversion MW1.16
%define revision r62678

Name: mediawiki-extensions-%oname
Version: 0.0.1
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Summary: The CategoryTree extension provides a AJAX dynamic view of the wiki's category structure as a tree
Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL

BuildPreReq: rpm-build-mediawiki >= 0.2
Requires: mediawiki-common >= 1.16

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: http://upload.wikimedia.org/ext-dist/%oname-%dversion-%revision.tar.gz
Source: %oname-%version.tar


%description
The CategoryTree extension provides a dynamic view of the wiki's
category structure as a tree. It uses AJAX to load parts of the tree
on demand.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
subst "3i\$wgUseAjax = true;" %buildroot%_mediawiki_settings_dir/50-%oname.php

%files -f %oname.files

%changelog
* Wed Jun 08 2011 Vitaly Lipatov <lav@altlinux.ru> 0.0.1-alt1
- initial build for ALT Linux Sisyphus
