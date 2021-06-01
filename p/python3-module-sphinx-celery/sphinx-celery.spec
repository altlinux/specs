%define _unpackaged_files_terminate_build 1
%define oname sphinx-celery

Name: python3-module-%oname
Version: 1.3.1
Release: alt2
Summary: Sphinx Celery Theme
License: BSD
Group: Development/Python3
BuildArch: noarch
Url: https://github.com/celery/sphinx_celery

# https://github.com/celery/sphinx_celery.git
Source: %name-%version.tar
Patch1: %oname-%version-upstream-refdomain.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx

%py3_requires sphinx

%description
This project provides the Celery sphinx theme and common Sphinx utilities.

%prep
%setup
%patch1 -p1

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/sphinx_celery
%python3_sitelibdir/sphinx_celery-%version-py*.egg-info

%changelog
* Tue Jun 01 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.1-alt2
- Drop python2 support.

* Wed Oct 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.1-alt1
- Initial build for ALT.
