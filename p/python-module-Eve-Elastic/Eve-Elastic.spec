%define oname Eve-Elastic

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.2.5
Release: alt1.git20150209.1
Summary: Elasticsearch data layer for eve rest framework
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/Eve-Elastic/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/petrjasek/eve-elastic.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-elasticsearch python-module-arrow
#BuildPreReq: python-module-eve python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-elasticsearch python3-module-arrow
#BuildPreReq: python3-module-eve python3-module-nose
%endif

%py_provides eve_elastic

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-cryptography python-module-enum34 python-module-jinja2 python-module-pyasn1 python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-enum34 python3-module-jinja2 python3-module-ndg-httpsclient python3-module-ntlm python3-module-pycparser python3-module-setuptools
BuildRequires: python-module-ndg-httpsclient python-module-nose python-module-ntlm python-module-pytest python3-module-nose python3-module-pytest python3-module-urllib3 rpm-build-python3

%description
Eve-Elastic is elasticsearch data layer for eve REST framework.

Features:

* fulltext search
* filtering via elasticsearch filter dsl
* facets support
* aggragations support
* elasticsearch mapping generator for schema

%package -n python3-module-%oname
Summary: Elasticsearch data layer for eve rest framework
Group: Development/Python3
%py3_provides eve_elastic

%description -n python3-module-%oname
Eve-Elastic is elasticsearch data layer for eve REST framework.

Features:

* fulltext search
* filtering via elasticsearch filter dsl
* facets support
* aggragations support
* elasticsearch mapping generator for schema

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
%doc *.md *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.2.5-alt1.git20150209.1
- NMU: Use buildreq for BR.

* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1.git20150209
- Version 0.2.5

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20141124
- Initial build for Sisyphus

