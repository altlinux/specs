%define oname pypandoc

%def_with python3

Name: python-module-%oname
Version: 0.9.3
Release: alt3.git20150226.1
Summary: Thin wrapper for pandoc
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pypandoc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bebraw/pypandoc.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools pandoc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname
Requires: pandoc

%description
Thin wrapper for "pandoc" (MIT).

%package -n python3-module-%oname
Summary: Thin wrapper for pandoc
Group: Development/Python3
%py3_provides %oname
Requires: pandoc

%description -n python3-module-%oname
Thin wrapper for "pandoc" (MIT).

%prep
%setup

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.3-alt3.git20150226.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 31 2016 Denis Medvedev <nbr@altlinux.org> 0.9.3-alt3.git20150226
- Recompile for changed site-packages for python3.5

* Wed Feb 24 2016 Denis Medvedev <nbr@altlinux.org> 0.9.3-alt2.git20150226
- back to sisyphus

* Fri Feb 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1.git20150226
- Version 0.9.3

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.git20150204
- Version 0.9.1

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20140529
- Initial build for Sisyphus

