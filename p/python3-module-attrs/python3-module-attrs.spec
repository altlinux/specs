%define oname attr
%define newoname attrs
%define pkgname attrs

Name: python3-module-%pkgname
Version: 22.2.0
Release: alt1

Summary: Python attributes without boilerplate

License: MIT
Group: Development/Python3
Url: https://attrs.readthedocs.io

Source: %pkgname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3


%description
attrs is an MIT-licensed Python package with class decorators that ease the
chores of implementing the most common attribute-related object protocols.

%prep
%setup -n %pkgname-%version

%build
%python3_build

%install
%python3_install

%files
%doc CHANGELOG.md LICENSE README.md
%python3_sitelibdir/%oname/
%python3_sitelibdir/%newoname/
%python3_sitelibdir/*.egg-info

%changelog
* Tue Jan 10 2023 Vladimir Didenko <cow@altlinux.org> 22.2.0-alt1
- New version

* Mon Sep 5 2022 Vladimir Didenko <cow@altlinux.org> 22.1.0-alt1
- New version

* Thu Jan 1 2022 Vladimir Didenko <cow@altlinux.org> 21.4.0-alt1
- New version

* Tue Jun 1 2021 Vladimir Didenko <cow@altlinux.org> 21.2.0-alt1
- New version

* Mon Nov 23 2020 Vladimir Didenko <cow@altlinux.org> 20.3.0-alt1
- New version

* Wed Sep 30 2020 Vladimir Didenko <cow@altlinux.org> 20.2.0-alt1
- New version

* Fri Sep 4 2020 Vladimir Didenko <cow@altlinux.org> 20.1.0-alt1
- New version
- Build Python 3 version as separate package

* Wed Nov 13 2019 Vladimir Didenko <cow@altlinux.org> 19.3.0-alt1
- New version

* Wed Mar 13 2019 Vladimir Didenko <cow@altlinux.org> 19.1.0-alt1
- New version

* Tue Oct 9 2018 Vladimir Didenko <cow@altlinux.org> 18.2.0-alt1
- New version

* Wed Jul 4 2018 Vladimir Didenko <cow@altlinux.org> 18.1.0-alt1
- New version

* Wed Mar 14 2018 Vladimir Didenko <cow@altlinux.org> 17.4.0-alt1
- New version

* Fri Jun 9 2017 Vladimir Didenko <cow@altlinux.org> 17.2.0-alt1
- New version

* Fri Dec 16 2016 Vladimir Didenko <cow@altlinux.org> 16.3.0-alt1
- New version

* Wed Oct 12 2016 Vladimir Didenko <cow@altlinux.org> 16.2.0-alt1
- Initial build for Sisyphus

* Mon Jul 24 2016 Vladimir Didenko <cow@altlinux.org> 16.0.0-alt1
- Initial build for Sisyphus
