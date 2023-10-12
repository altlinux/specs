%define node_module typescript

%filter_from_requires /^nodejs.engine./d
%{?nodejs_find_provides_and_requires}

Name: node-typescript
Version: 5.2.2
Release: alt1

Summary: TypeScript is a language for application scale JavaScript development

License: Apache License 2.0
Group: Development/Other
Url: http://www.typescriptlang.org

# Source-url: https://github.com/Microsoft/TypeScript/archive/v%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: rpm-build-nodejs node
BuildRequires(pre): rpm-macros-nodejs

# due /usr/bin/env in bin scripts
Requires: node

Provides: nodejs-%node_module = %version-%release
Obsoletes: nodejs-%node_module < %version
Provides: %node_module = %version-%release
Obsoletes: %node_module < %version

%description
TypeScript is a free and open source programming language developed by Microsoft.
 It is a strict superset of JavaScript, and essentially adds optional static
typing and class-based object oriented programming to the language.
%prep
%setup

%build
%check

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%nodejs_sitelib/%node_module
chmod a+x bin/*
cp -rp bin lib package.json %buildroot/%nodejs_sitelib/%node_module

ln -s %nodejs_sitelib/%node_module/bin/tsc %buildroot%_bindir
ln -s %nodejs_sitelib/%node_module/bin/tsserver %buildroot%_bindir

%nodejs_symlink_deps

%files
%doc LICENSE.txt CONTRIBUTING.md README.md ThirdPartyNoticeText.txt
%_bindir/tsc
%_bindir/tsserver
%nodejs_sitelib/%node_module/

%changelog
* Thu Oct 12 2023 Vitaly Lipatov <lav@altlinux.ru> 5.2.2-alt1
- new version 5.2.2 (with rpmrb script)

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 4.6.3-alt1
- new version 4.6.3 (with rpmrb script)

* Fri Sep 03 2021 Vitaly Lipatov <lav@altlinux.ru> 4.4.2-alt1
- new version 4.4.2 (with rpmrb script)

* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 4.2.4-alt1
- new version 4.2.4 (with rpmrb script)

* Sun Apr 18 2021 Vitaly Lipatov <lav@altlinux.ru> 4.2.3-alt1
- new version 4.2.3 (with rpmrb script)

* Wed Feb 24 2021 Vitaly Lipatov <lav@altlinux.ru> 4.1.5-alt1
- new version 4.1.5 (with rpmrb script)

* Mon Oct 12 2020 Vitaly Lipatov <lav@altlinux.ru> 4.0.3-alt1
- new version 4.0.3 (with rpmrb script)

* Wed Aug 26 2020 Vitaly Lipatov <lav@altlinux.ru> 3.9.7-alt1
- new version 3.9.7 (with rpmrb script)

* Fri Jun 26 2020 Vitaly Lipatov <lav@altlinux.ru> 3.9.5-alt2
- drop rpm-build-nodejs from Requires

* Wed Jun 24 2020 Vitaly Lipatov <lav@altlinux.ru> 3.9.5-alt1
- new version 3.9.5 (with rpmrb script)

* Fri May 29 2020 Vitaly Lipatov <lav@altlinux.ru> 3.9.3-alt1
- new version 3.9.3 (with rpmrb script)

* Fri Feb 28 2020 Vitaly Lipatov <lav@altlinux.ru> 3.8.2-alt1
- new version 3.8.2 (with rpmrb script)

* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 3.7.5-alt1
- new version 3.7.5 (with rpmrb script)

* Tue Oct 29 2019 Vitaly Lipatov <lav@altlinux.ru> 3.6.4-alt1
- new version 3.6.4 (with rpmrb script)

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 2.8.3-alt1
- new version 2.8.3 (with rpmrb script)

* Tue May 30 2017 Vitaly Lipatov <lav@altlinux.ru> 2.3.3-alt1
- new version 2.3.3 (with rpmrb script)

* Wed Jul 27 2016 Vitaly Lipatov <lav@altlinux.ru> 1.8.10-alt1
- new version 1.8.10 (with rpmrb script)

* Thu Feb 11 2016 Vitaly Lipatov <lav@altlinux.ru> 1.7.5-alt1
- new version 1.7.5 (with rpmrb script)

* Sat Jul 27 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.9.0.1-alt1
Initial build
