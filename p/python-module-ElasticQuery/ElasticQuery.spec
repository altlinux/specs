%define oname ElasticQuery

%def_with python3

Name: python-module-%oname
Version: 0.2.0
Release: alt1.git20141125.1.1
Summary: A simple query builder for Elasticsearch
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/ElasticQuery/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Fizzadar/ElasticQuery.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python-tools-2to3
%endif

%py_provides elasticquery

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-setuptools
BuildRequires: python-module-setuptools-tests python-modules-json python3-module-pytest rpm-build-python3 time

%description
A simple query builder for Elasticsearch. Outputs json ready to be sent
to Elasticsearch via your favourite client.

%package -n python3-module-%oname
Summary: A simple query builder for Elasticsearch
Group: Development/Python3
%py3_provides elasticquery

%description -n python3-module-%oname
A simple query builder for Elasticsearch. Outputs json ready to be sent
to Elasticsearch via your favourite client.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
python test.py
#if_with python3
%if 0
pushd ../python3
python3 setup.py test
rm -fR build
python3 test.py
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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20141125.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.git20141125.1
- NMU: Use buildreq for BR.

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20141125
- Version 0.2.0

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.18-alt1.git20141106
- Version 0.1.18

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.17-alt1.git20141030
- Initial build for Sisyphus

