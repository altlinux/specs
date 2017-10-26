%define _unpackaged_files_terminate_build 1
%define oname sphinx-celery

%def_with python3

Name: python-module-%oname
Version: 1.3.1
Release: alt1
Summary: Sphinx Celery Theme
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://github.com/celery/sphinx_celery

# https://github.com/celery/sphinx_celery.git
Source: %name-%version.tar
Patch1: %oname-%version-upstream-refdomain.patch

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-sphinx
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-sphinx
%endif

%py_requires sphinx

%description
This project provides the Celery sphinx theme and common Sphinx utilities.

%if_with python3
%package -n python3-module-%oname
Summary: Sphinx Celery Theme
Group: Development/Python3
%py3_requires sphinx

%description -n python3-module-%oname
This project provides the Celery sphinx theme and common Sphinx utilities.
%endif

%prep
%setup
%patch1 -p1

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc README.rst
%python_sitelibdir/sphinx_celery
%python_sitelibdir/sphinx_celery-%version-py*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc README.rst
%python3_sitelibdir/sphinx_celery
%python3_sitelibdir/sphinx_celery-%version-py*.egg-info
%endif

%changelog
* Wed Oct 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.1-alt1
- Initial build for ALT.
