%define oname antlr4
Name: python3-module-%oname
Version: 4.5.2
Release: alt1.1.1
Summary: ANTLR 4.5 runtime for Python 3
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/antlr4-python3-runtime/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-enum34

%py3_provides %oname
Requires: python3-module-enum34

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base
BuildRequires: rpm-build-python3

%description
This is the Python 3 runtime for AntLR.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.txt
%python3_sitelibdir/*

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.5.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.5.2-alt1.1
- NMU: Use buildreq for BR.

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.2-alt1
- Version 4.5.2

* Thu Apr 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5-alt1
- Initial build for Sisyphus

