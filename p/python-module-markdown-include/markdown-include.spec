%define oname markdown-include

%def_with python3

Name: python-module-%oname
Version: 0.4.2
Release: alt1.git20150126.1.1.1
Summary: Provides an "include" function, similar to that found in LaTeX
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/markdown-include/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/cmacmackin/markdown-include.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-markdown python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-markdown
%endif

%py_provides markdown_include
%py_requires markdown json

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-markdown python-module-setuptools python3-module-markdown python3-module-setuptools rpm-build-python3

%description
This is an extension to Python-Markdown which provides an "include"
function, similar to that found in LaTeX (and also the C pre-processor
and Fortran).

%package -n python3-module-%oname
Summary: Provides an "include" function, similar to that found in LaTeX
Group: Development/Python3
%py3_provides markdown_include
%py3_requires markdown

%description -n python3-module-%oname
This is an extension to Python-Markdown which provides an "include"
function, similar to that found in LaTeX (and also the C pre-processor
and Fortran).

%prep
%setup

ln -s README.md README.rst

%if_with python3
cp -fR . ../python3
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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.2-alt1.git20150126.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.2-alt1.git20150126.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt1.git20150126.1
- NMU: Use buildreq for BR.

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20150126
- Version 0.4.2

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20150120
- Initial build for Sisyphus

