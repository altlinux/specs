%define oname sphinx-celery

Name: python3-module-%oname
Version: 2.1.3
Release: alt1

Summary: Sphinx Celery Theme

License: BSD
Group: Development/Python3
URL: https://pypi.org/project/sphinx-celery
VCS: https://github.com/celery/sphinx_celery

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-sphinx

%py3_requires sphinx

%description
This project provides the Celery sphinx theme and common Sphinx utilities.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst
%python3_sitelibdir/sphinx_celery
%python3_sitelibdir/sphinx_celery-%version.dist-info

%changelog
* Tue Oct 22 2024 Grigory Ustinov <grenka@altlinux.org> 2.1.3-alt1
- Automatically updated to 2.1.3.

* Tue Jun 01 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.1-alt2
- Drop python2 support.

* Wed Oct 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.1-alt1
- Initial build for ALT.
