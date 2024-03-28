%global pypi_name sphinx_basic_ng
%define _unpackaged_files_terminate_build 1
%define stage .beta2

Name: sphinx-basic-ng
Version: 1.0.0
Release: alt0.1%{stage}
Summary: A modernised skeleton for Sphinx themes
Group: Development/Python

License: MIT
Url: https://sphinx-basic-ng.readthedocs.io/en/latest/
# https://github.com/pradyunsg/sphinx-basic-ng/archive/refs/tags/%version%{stage}.tar.gz
Source0: %name-%version.tar

BuildRequires: python3-devel python3-module-sphinx
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

%package -n python3-module-%{pypi_name}
Summary: %summary
Group: Development/Python

%description
%summary

%description -n python3-module-%{pypi_name}
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files -n python3-module-%{pypi_name}
%python3_sitelibdir_noarch/%{pypi_name}
%python3_sitelibdir_noarch/%{pypi_name}-%{version}b2.dist-info/

%changelog
* Thu Mar 28 2024 L.A. Kostis <lakostis@altlinux.ru> 1.0.0-alt0.1.beta2
- Initial build for ALTLinux.


