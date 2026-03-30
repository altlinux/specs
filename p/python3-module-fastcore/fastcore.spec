%define _unpackaged_files_terminate_build 1
%define pypi_name fastcore
%define mod_name fastcore

Name: python3-module-%pypi_name
Version: 1.8.5
Release: alt1.1

Summary: Library that uses customization flexibility to add features to Python

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/fastcore/
VCS: https://github.com/AnswerDotAI/fastcore/

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
Fastcore is an utility library created as a part of the fastai ecosystem.
It provides advanced Python capabilities, enhanced classes, decorators,
collection utilities, types, and metaprogramming.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/py2pyi
%_bindir/replace_wildcards
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.8.5-alt1.1
- Demodernized packaging.

* Tue Jul 08 2025 Anastasia Doronina <swaggyglice@altlinux.org> 1.8.5-alt1
- Update to 1.8.5.

* Tue Jun 24 2025 Anastasia Doronina <swaggyglice@altlinux.org> 1.8.4-alt1
- Update to 1.8.4.

* Tue May 20 2025 Anastasia Doronina <swaggyglice@altlinux.org> 1.8.2-alt1
- Update to 1.8.2.

* Wed Apr 02 2025 Anastasia Doronina <swaggyglice@altlinux.org> 1.8.0-alt1
- Update to 1.8.0.

* Tue Feb 18 2025 Anastasia Doronina <swaggyglice@altlinux.org> 1.7.29-alt1
- Initial Build for Sisyphus.
