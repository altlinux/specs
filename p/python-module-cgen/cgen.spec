%define _unpackaged_files_terminate_build 1

%define oname cgen

%def_with python3

Name: python-module-%oname
Version: 2017.1
Release: alt1
Summary: C/C++ source generation from an AST
License: MIT
Group: Development/Python
BuildArch: noarch
Url: http://pypi.python.org/pypi/cgen/

# https://github.com/inducer/cgen.git
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
%endif

%py_requires decorator

%description
C/C++ source generation from an AST.

%if_with python3
%package -n python3-module-%oname
Summary: C/C++ source generation from an AST (Python 3)
Group: Development/Python3
%py3_requires decorator

%description -n python3-module-%oname
C/C++ source generation from an AST.
%endif

%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
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
%doc LICENSE README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon May 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2017.1-alt1
- Updated to upstream version 2017.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2013.1.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2013.1.2-alt1.1
- NMU: Use buildreq for BR.

* Mon Sep 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.1.2-alt1
- Version 2013.1.2

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2012.1-alt2
- Use 'find... -exec...' instead of 'for ... $(find...'

* Sun Mar 24 2013 Aleksey Avdeev <solo@altlinux.ru> 2012.1-alt1.1
- Rebuild with Python-3.3

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2012.1-alt1
- Initial build for Sisyphus

