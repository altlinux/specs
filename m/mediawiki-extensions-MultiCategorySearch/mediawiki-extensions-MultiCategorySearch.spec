%define oname MultiCategorySearch

Name: mediawiki-extensions-%oname
Version: 1.62
Release: alt1

Summary: The MediaWiki extension lists pages included in several specified categories at once

License:  GPL
Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:Multi-Category_Search

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildPreReq: rpm-build-mediawiki >= 0.3

Requires: mediawiki-common >= 1.16

#Requires: mediawiki-extensions-StubManager

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: ftp://rudata.ru/Packages/MultiCategorySearch_%version.zip
Source: %oname-%version.tar

%description
This extension lists pages included in several specified categories
at once. By default, user can specify up to 5 such categories, and
optionally up to 3 categories to exclude from search. The maximum number
of categories is set in two corresponding variables in source code,
so you can easily change it at any time.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname

%files -f %oname.files

%changelog
* Thu May 10 2012 Vitaly Lipatov <lav@altlinux.ru> 1.62-alt1
- initial build for ALT Linux Sisyphus

