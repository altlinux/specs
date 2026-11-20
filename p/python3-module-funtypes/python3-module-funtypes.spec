%define pypi_name funtypes

Name: python3-module-funtypes
Version: 0.2.1
Release: alt1

Summary: Functional types for Python

License: MIT
Group: Development/Python3
URL: https://github.com/timoniq/fntypes
# Source-url: https://files.pythonhosted.org/packages/a2/59/dc2bcf2bdacbd45b964bc8f588c87c8684f7d1828251eaaa46248b78bbc1/funtypes-0.2.1.tar.gz
Source: %name-%version.tar
# Omitted from the PyPI sdist; MIT license of the original fntypes project.
# Source1-url: https://raw.githubusercontent.com/timoniq/kungfu/b05186365941f89c621b491afca12f0ca13134b4/LICENSE
Source1: fntypes-LICENSE

BuildArch: noarch
BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-poetry-core

%description
Functional types for Python.

%prep
%setup
cp %SOURCE1 LICENSE
# The sdist has a lowercase readme filename.
sed -i 's/README.md/readme.md/' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%files
%doc readme.md
%doc LICENSE
%python3_sitelibdir/fntypes/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Nov 19 2026 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt1
- initial build for Sisyphus.

