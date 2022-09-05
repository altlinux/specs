%define oname hatch-fancy-pypi-readme
%define modname hatch_fancy_pypi_readme

Name: python3-module-%oname
Version: 22.3.0
Release: alt1

Summary: Fancy PyPI READMEs with Hatch.

License: MIT
Group: Development/Python3
Url: https://github.com/hynek/hatch-fancy-pypi-readme

Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-setuptools_scm
BuildRequires: python3-module-wheel
BuildRequires: python3-module-hatchling

%description
hatch-fancy-pypi-readme is a Hatch metadata plugin for everyone who cares
about the first impression of their project's PyPI landing page.

%prep
%setup -n %oname-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/%oname
%python3_sitelibdir/%modname/
%python3_sitelibdir/%modname-*.dist-info

%changelog
* Mon Sep 5 2022 Vladimir Didenko <cow@altlinux.ru> 22.3.0-alt1
- Initial build for Sisyphus
