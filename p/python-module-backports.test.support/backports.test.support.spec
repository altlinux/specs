%define oname backports.test.support

Name: python-module-%oname
Version: 0.1
Release: alt1
Summary: Backport of Python 3's test.support package
Group: Development/Python
License: Python
URL: https://pypi.python.org/pypi/backports.test.support

# https://github.com/pjdelport/backports.test.support.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-work-networkless.patch

BuildRequires: python-dev python-module-setuptools
BuildRequires: python2.7(pytest)
BuildRequires: python2.7(future) python2.7(backports.os)

%py_requires backports backports.os
%py_provides backports.test.support

%description
This backports Python 3's test.support package under the backports namespace.

This is probably only interesting if you're backporting standard library test code.

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
* Mon Dec 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1-alt1
- Initial build for ALT.
