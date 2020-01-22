%define oname backports.test.support

Name: python3-module-%oname
Version: 0.1.1
Release: alt2

Summary: Backport of Python 3's test.support package
License: Python
Group: Development/Python3
URL: https://pypi.python.org/pypi/backports.test.support

# https://github.com/pjdelport/backports.test.support.git
Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(pytest)
BuildRequires: python3(future) python3(backports.os)
BuildRequires: python3(mock)

%py3_requires backports backports.os
%py3_provides backports.test.support


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
* Wed Jan 22 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1.1-alt2
- Porting on Python3.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1.qa1
- NMU: applied repocop patch

* Thu Mar 01 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.1-alt1
- Updated to upstream version 0.1.1.

* Mon Dec 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1-alt1
- Initial build for ALT.
