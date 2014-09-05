%define oname speedparser

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.2.0
Release: alt1.git20140816

Summary: feedparser but faster and worse
Group: Development/Python
License: MIT
Url: https://github.com/jmoiron/speedparser
BuildArch: noarch

%py_provides %oname
%py_requires lxml chardet

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-lxml python-module-chardet
BuildPreReq: python-modules-json python-module-ipdb
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-lxml python3-module-chardet
BuildPreReq: python3-module-ipdb python-tools-2to3
%endif

# https://github.com/jmoiron/speedparser.git
Source: %name-%version.tar

%description
Speedparser is a black-box "style" reimplementation of the Universal
Feed Parser. It uses some feedparser code for date and authors, but
mostly re-implements its data normalization algorithms based on
feedparser output. It uses lxml for feed parsing and for optional HTML
cleaning. Its compatibility with feedparser is very good for a strict
subset of fields, but poor for fields outside that subset.
See tests/speedparsertests.py for more information on which fields are
more or less compatible and which are not.

%package -n python3-module-%oname
Summary: feedparser but faster and worse
Group: Development/Python3
%py3_provides %oname
%py3_requires lxml chardet

%description -n python3-module-%oname
Speedparser is a black-box "style" reimplementation of the Universal
Feed Parser. It uses some feedparser code for date and authors, but
mostly re-implements its data normalization algorithms based on
feedparser output. It uses lxml for feed parsing and for optional HTML
cleaning. Its compatibility with feedparser is very good for a strict
subset of fields, but poor for fields outside that subset.
See tests/speedparsertests.py for more information on which fields are
more or less compatible and which are not.

%prep
%setup
tar -xf tests/feeds.tar.bz2

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
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
PYTHONPATH=%buildroot%python_sitelibdir python setup.py test
%if_with python3
pushd ../python3
PYTHONPATH=%buildroot%python3_sitelibdir python3 setup.py test
popd
%endif

%files
%doc *.rst docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Sep 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20140816
- Initial build for Sisyphus

