%define _unpackaged_files_terminate_build 1

%define oname pyroma

Name: python3-module-%oname
Version: 2.2
Release: alt2

Summary: Test your project's packaging friendliness
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyroma/
BuildArch: noarch

Source0: https://pypi.python.org/packages/de/f3/104ae27624982cd4b6de786d9afe23a2dc0b8c0999443ba370b3755848c7/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-docutils

%py3_provides %oname

Conflicts: python-module-%oname


%description
Pyroma rhymes with aroma, and is a product aimed at giving a rating of
how well a Python project complies with the best practices of the Python
packaging ecosystem, primarily PyPI, pip, Distribute etc, as well as a
list of issues that could be improved.

The aim of this is both to help people make a project that is nice and
usable, but also to improve the quality of Python third-party software,
making it easier and more enjoyable to use the vast array of available
modules for Python.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Pyroma rhymes with aroma, and is a product aimed at giving a rating of
how well a Python project complies with the best practices of the Python
packaging ecosystem, primarily PyPI, pip, Distribute etc, as well as a
list of issues that could be improved.

The aim of this is both to help people make a project that is nice and
usable, but also to improve the quality of Python third-party software,
making it easier and more enjoyable to use the vast array of available
modules for Python.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.txt
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*


%changelog
* Thu Feb 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.2-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1
- Initial build for Sisyphus

