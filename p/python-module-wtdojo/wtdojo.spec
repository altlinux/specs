%define oname wtdojo

%def_with python3

Name: python-module-%oname
Version: 0.1.3
Release: alt1.git20141211
Summary: Dojo javascript toolkit support for WTForms
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/wtdojo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kashifpk/wtdojo.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-wtforms
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-wtforms
%endif

%py_provides %oname

%description
wtdojo (WTForms with Dojo) is a python library that allows using WTForms
with Dojo toolkit's Dijit widget set.

%package -n python3-module-%oname
Summary: Dojo javascript toolkit support for WTForms
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
wtdojo (WTForms with Dojo) is a python library that allows using WTForms
with Dojo toolkit's Dijit widget set.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
wtdojo (WTForms with Dojo) is a python library that allows using WTForms
with Dojo toolkit's Dijit widget set.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
wtdojo (WTForms with Dojo) is a python library that allows using WTForms
with Dojo toolkit's Dijit widget set.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20141211
- Initial build for Sisyphus

