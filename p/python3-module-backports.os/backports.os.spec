%define _unpackaged_files_terminate_build 1

%define oname backports.os

Name: python3-module-%oname
Version: 0.1.1
Release: alt3

Summary: Backport of new features in Python's os module
License: Python
Group: Development/Python3
URL: https://pypi.org/project/backports.os/

# https://github.com/pjdelport/backports.os.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(pytest)
BuildRequires: python3(future) python3(hypothesis)

%py3_requires backports future.utils.surrogateescape
%py3_provides backports.os


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
%python3_build


%install
%python3_install

%if "%_lib" == "lib64"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

rm -f %buildroot%python3_sitelibdir/backports/__init__.py*

%check
PYTHONPATH=$(pwd)/src py.test3

%files
%doc README.rst
%python3_sitelibdir/*


%changelog
* Wed Jan 22 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1.1-alt3
- Porting on Python3.

* Mon Sep 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.1-alt2
- Updated runtime dependencies.

* Mon Dec 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.1-alt1
- Initial build for ALT.
