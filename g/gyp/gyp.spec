Name: gyp
Version: 0.15.1
Release: alt1

Summary: A fork of the GYP build system for use in the Node.js projects
License: BSD
Group: Development/Tools

Url: https://github.com/nodejs/gyp-next.git

BuildArch: noarch

# Source-url: https://github.com/nodejs/gyp-next/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
#BuildRequires: python3-devel >= 3.6

# it is a command, but a module
AutoProv:no

%description
A fork of the GYP build system for use in the Node.js projects.

GYP is a tool to generates native Visual Studio, Xcode and SCons and/or
make build files from a platform-independent input format. Its syntax
is a universal cross-platform build representation that still allows
sufficient per-platform flexibility to accommodate irreconcilable
differences.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
rm -v %buildroot/%python3_sitelibdir/%name/*_test.py
rm -v %buildroot/%python3_sitelibdir/%name/generator/*_test.py

%files
%doc AUTHORS LICENSE README.md
%_bindir/%name
%python3_sitelibdir/%name
%python3_sitelibdir/*.dist-info

%changelog
* Fri Oct 20 2023 Anton Vyatkin <toni@altlinux.org> 0.15.1-alt1
- NMU: new version 0.15.1

* Fri Jul 28 2023 Vitaly Lipatov <lav@altlinux.ru> 0.15.0-alt1
- new version 0.15.0 (with rpmrb script)

* Mon Mar 13 2023 Vitaly Lipatov <lav@altlinux.ru> 0.14.1-alt1
- new version 0.14.1 (with rpmrb script)

* Mon Jan 24 2022 Vitaly Lipatov <lav@altlinux.ru> 0.10.1-alt1
- new version 0.10.1 (with rpmrb script)

* Fri Dec 17 2021 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt1
- switch to gyp-next (a maintained fork of gyp)

* Thu Jan 16 2020 Vitaly Lipatov <lav@altlinux.ru> 0.1.h.e87d37d6-alt1
- new version (0.1.h.e87d37d6) with rpmgs script
- switch to python3

* Sun Dec 11 2016 Vitaly Lipatov <lav@altlinux.ru> 0.1.g940a15e-alt2
- add cmake_precompiled_header support from tdesktop project patch

* Sun Dec 11 2016 Vitaly Lipatov <lav@altlinux.ru> 0.1.g940a15e-alt1
- build lastest commit from git

* Sat Jun 16 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.1-alt1.r1415
- Update to SVN r1415

* Tue Mar 13 2012 Vladimir Lettiev <crux@altlinux.ru> 0.1-alt1.r1241
- initial build for Sisyphus

