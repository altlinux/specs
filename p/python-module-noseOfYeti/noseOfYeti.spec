%define oname noseOfYeti

%def_with python3

Name: python-module-%oname
Version: 1.5.1
Release: alt1.git20140601
Summary: Nose plugin providing BDD dsl for python
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/noseOfYeti/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/delfick/nose-of-yeti.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six python-module-nose
BuildPreReq: python-module-fudge python-module-should_dsl
BuildPreReq: python-module-sphinx-devel python-module-pinocchio
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six python3-module-nose
BuildPreReq: python3-module-fudge python3-module-should_dsl
%endif

%py_provides %oname
%py_requires six nose fudge should_dsl

%description
Plugin for nose, inspired by http://github.com/fmeyer/yeti, which uses a
codec style to provide an RSpec style BDD dsl for python tests.

%package -n python3-module-%oname
Summary: Nose plugin providing BDD dsl for python
Group: Development/Python3
%py3_provides %oname
%py3_requires six nose fudge should_dsl

%description -n python3-module-%oname
Plugin for nose, inspired by http://github.com/fmeyer/yeti, which uses a
codec style to provide an RSpec style BDD dsl for python tests.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Plugin for nose, inspired by http://github.com/fmeyer/yeti, which uses a
codec style to provide an RSpec style BDD dsl for python tests.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Plugin for nose, inspired by http://github.com/fmeyer/yeti, which uses a
codec style to provide an RSpec style BDD dsl for python tests.

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

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
export PYTHONPATH=$PWD
python test.sh -v
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
python3 test.sh -v
popd
%endif

%files
%doc *.rst example
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst example
%python3_sitelibdir/*
%endif

%changelog
* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1.git20140601
- Initial build for Sisyphus

