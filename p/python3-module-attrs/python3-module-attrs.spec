%define oname attr
%define newoname attrs
%define pkgname attrs

Name: python3-module-%pkgname
Version: 24.2.0
Release: alt2

Summary: Python attributes without boilerplate

License: MIT
Group: Development/Python3
Url: https://attrs.readthedocs.io

Source: %pkgname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(hatchling)
BuildRequires: python3(hatch-fancy-pypi-readme)
BuildRequires: python3(hatch-vcs)
BuildRequires: git

%description
attrs is an MIT-licensed Python package with class decorators that ease the
chores of implementing the most common attribute-related object protocols.

%prep
%setup -n %pkgname-%version

%build
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi
%pyproject_build

%install
%pyproject_install

%files
%doc CHANGELOG.md LICENSE README.md
%python3_sitelibdir/%oname/
%python3_sitelibdir/%newoname/
%python3_sitelibdir/%newoname-%version.dist-info/

%changelog
* Tue Aug 20 2024 Vladimir Didenko <cow@altlinux.org> 24.2.0-alt2
- Return back non-packed dist-info

* Tue Aug 20 2024 Vladimir Didenko <cow@altlinux.org> 24.2.0-alt1
- New version

* Wed Jan 24 2024 Vladimir Didenko <cow@altlinux.org> 23.2.0-alt1
- New version

* Thu May 25 2023 Vladimir Didenko <cow@altlinux.org> 23.1.0-alt1
- New version

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
