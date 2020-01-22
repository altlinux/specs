%define oname backports.weakref

Name: python3-module-%oname
Version: 1.0
Release: alt2

Summary: Backport of new features in Python's weakref module
License: Python
Group: Development/Python3
URL: https://pypi.python.org/pypi/backports.weakref

# https://github.com/pjdelport/backports.weakref.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-respect-pythonpath.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(pytest)
BuildRequires: python3(future) python3(backports.test.support)

%py3_requires backports
%py3_provides backports.weakref


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
* Wed Jan 22 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0-alt2
- Porting on Python3.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1.qa1
- NMU: applied repocop patch

* Mon Dec 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt1
- Initial build for ALT.
