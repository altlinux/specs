%define oname ImportConfig

%def_with python3

Name: python-module-%oname
Version: 0.0.4
Release: alt1.git20150108
Summary: JSON and YAML parsing with imports
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/ImportConfig/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Dinoshauer/ImportConfig.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-yaml python-module-nose
BuildPreReq: python-module-nose-watch python-module-nosexcover
BuildPreReq: python-module-pre_commit python-module-rednose
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-sphinx_rtd_theme python-modules-json
BuildPreReq: python-module-sphinxcontrib-napoleon
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-yaml python3-module-nose
BuildPreReq: python3-module-nose-watch python3-module-nosexcover
BuildPreReq: python3-module-rednose
%endif

%py_provides importconfig
%py_requires yaml json

%description
The special thing about ImportConfig is that it supports a notion of
"imports". You can import other json files in your json file by
specifying a "@file" value at any level in the config and it will be
expanded into that level.

A config file can be loaded lazily and the main config file will only be
loaded once it is called.

Note: keys/values defined in the top level document will take precedence
over those loaded in sub-documents.

%package -n python3-module-%oname
Summary: JSON and YAML parsing with imports
Group: Development/Python3
%py3_provides importconfig
%py3_requires yaml json

%description -n python3-module-%oname
The special thing about ImportConfig is that it supports a notion of
"imports". You can import other json files in your json file by
specifying a "@file" value at any level in the config and it will be
expanded into that level.

A config file can be loaded lazily and the main config file will only be
loaded once it is called.

Note: keys/values defined in the top level document will take precedence
over those loaded in sub-documents.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
The special thing about ImportConfig is that it supports a notion of
"imports". You can import other json files in your json file by
specifying a "@file" value at any level in the config and it will be
expanded into that level.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
The special thing about ImportConfig is that it supports a notion of
"imports". You can import other json files in your json file by
specifying a "@file" value at any level in the config and it will be
expanded into that level.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

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

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
export PYTHONPATH=$PWD
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.git20150108
- Initial build for Sisyphus

