%define _unpackaged_files_terminate_build 1

%define oname backports.os

Name: python-module-%oname
Version: 0.1.1
Release: alt3
Summary: Backport of new features in Python's os module
Group: Development/Python
License: Python
URL: https://pypi.org/project/backports.os/

# https://github.com/pjdelport/backports.os.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools

%py_requires backports future.utils.surrogateescape
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

%files
%doc README.rst
%python_sitelibdir/*

%changelog
* Fri Oct 16 2020 Stanislav Levin <slev@altlinux.org> 0.1.1-alt3
- Dropped dependency on tests packages.

* Mon Sep 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.1-alt2
- Updated runtime dependencies.

* Mon Dec 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.1-alt1
- Initial build for ALT.
