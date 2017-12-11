%define oname backports.os

Name: python-module-%oname
Version: 0.1.1
Release: alt1
Summary: Backport of new features in Python's os module
Group: Development/Python
License: Python
URL: https://pypi.python.org/pypi/backports.os

# https://github.com/pjdelport/backports.os.git
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools
BuildRequires: python2.7(pytest)
BuildRequires: python2.7(future) python2.7(hypothesis)

%py_requires backports
%py_provides backports.os

%description
This package provides backports of new features in Python's os module under the backports namespace.

%prep
%setup

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
* Mon Dec 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.1-alt1
- Initial build for ALT.
