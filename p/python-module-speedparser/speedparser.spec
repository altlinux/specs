%define _unpackaged_files_terminate_build 1

%define oname speedparser

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.2.0
Release: alt2.git20140816

Summary: feedparser but faster and worse
Group: Development/Python
License: MIT
Url: https://github.com/jmoiron/speedparser
BuildArch: noarch

%py_provides %oname
%py_requires lxml chardet

BuildRequires(pre): rpm-build-python
BuildRequires: python-dev python-module-setuptools
BuildRequires: python-module-html5lib python-module-notebook
BuildRequires: python-module-ipdb
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-html5lib python3-module-notebook
BuildRequires: python3-module-ipdb
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

%if_with python3
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
%endif

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
* Mon May 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.0-alt2.git20140816
- NMU: rebuilt to regenerate dependencies.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20140816.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.git20140816.1
- NMU: Use buildreq for BR.

* Fri Sep 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20140816
- Initial build for Sisyphus

