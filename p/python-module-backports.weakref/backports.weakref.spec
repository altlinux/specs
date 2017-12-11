%define oname backports.weakref

Name: python-module-%oname
Version: 1.0
Release: alt1
Summary: Backport of new features in Python's weakref module
Group: Development/Python
License: Python
URL: https://pypi.python.org/pypi/backports.weakref

# https://github.com/pjdelport/backports.weakref.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-respect-pythonpath.patch

BuildRequires: python-dev python-module-setuptools
BuildRequires: python2.7(pytest)
BuildRequires: python2.7(future) python2.7(backports.test.support)

%py_requires backports
%py_provides backports.weakref

%description
This package provides backports of new features in Python's weakref module under the backports namespace.

%prep
%setup
%patch1 -p1

# don't use scm to determine version, just substitute it
sed -i \
	-e 's|setuptools_scm|setuptools|g' \
	-e "s|use_scm_version=.*|version='%version',|g" \
	setup.py

%build
%python_build


%install
%python_install

%if "%_lib" == "lib64"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

rm -f %buildroot%python_sitelibdir/backports/__init__.py*

%check
PYTHONPATH=$(pwd)/src py.test

%files
%doc README.rst
%python_sitelibdir/*

%changelog
* Mon Dec 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt1
- Initial build for ALT.
