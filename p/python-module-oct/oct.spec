%define oname oct

%def_with python3

Name: python-module-%oname
Version: 0.3.3
Release: alt1.git20150105
Summary: A library based on multi-mechanize for performances testing
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/oct/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/karec/oct.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-argparse python-module-mechanize
BuildPreReq: python-module-requests python-module-matplotlib
BuildPreReq: python-module-lxml python-module-requests-cache
BuildPreReq: python-module-celery python-module-cssselect
BuildPreReq: python-module-scipy python-module-numpy
BuildPreReq: python-module-pygal python-module-cairosvg
BuildPreReq: python-module-tinycss python-module-six
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-argparse python3-module-mechanize
BuildPreReq: python3-module-requests python3-module-matplotlib
BuildPreReq: python3-module-lxml python3-module-requests-cache
BuildPreReq: python3-module-celery python3-module-cssselect
BuildPreReq: python3-module-scipy python3-module-numpy
BuildPreReq: python3-module-pygal python3-module-cairosvg
BuildPreReq: python3-module-tinycss python3-module-six
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires cssselect pygal cairosvg tinycss six

%description
OCT stand for Open Charge Tester and his goal is simple : make a library
that give you the tools for writing performances tests on webiste. At
this time of the developpement process OCT is based on mechanize for
browsing, but we plan to replace it with a custom, more modern library.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
OCT stand for Open Charge Tester and his goal is simple : make a library
that give you the tools for writing performances tests on webiste. At
this time of the developpement process OCT is based on mechanize for
browsing, but we plan to replace it with a custom, more modern library.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A library based on multi-mechanize for performances testing
Group: Development/Python3
%py3_provides %oname
%py3_requires cssselect pygal cairosvg tinycss six

%description -n python3-module-%oname
OCT stand for Open Charge Tester and his goal is simple : make a library
that give you the tools for writing performances tests on webiste. At
this time of the developpement process OCT is based on mechanize for
browsing, but we plan to replace it with a custom, more modern library.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
OCT stand for Open Charge Tester and his goal is simple : make a library
that give you the tools for writing performances tests on webiste. At
this time of the developpement process OCT is based on mechanize for
browsing, but we plan to replace it with a custom, more modern library.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

pushd doc
sphinx-build -b html -d _build/doctrees . _build/html
popd

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc changelog.txt *.md doc/_build/html
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/testing

%files tests
%python_sitelibdir/*/testing

%if_with python3
%files -n python3-module-%oname
%doc changelog.txt *.md doc/_build/html
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/testing

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/testing
%endif

%changelog
* Tue Jan 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt1.git20150105
- Version 0.3.3

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20150102
- Initial build for Sisyphus

