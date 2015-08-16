%define oname zml

%def_with python3
%def_without python2

Name: python-module-%oname
Version: 0.2.3
Release: alt1.git20150816
Summary: Zero markup language
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/zml
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/babadoo/zml.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyparsing python-module-html5lib
BuildPreReq: python-module-termcolor
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyparsing python3-module-html5lib
BuildPreReq: python3-module-termcolor
%endif

%py_provides %oname
%py_requires pyparsing html5lib termcolor
Requires: /var/log

%description
Zero markup language.

Features:
* zero markup templates
* clean syntax
* extensible
* components
* namespaces
* lean code

%if_with python3
%package -n python3-module-%oname
Summary: Zero markup language
Group: Development/Python3
%py3_provides %oname
%py3_requires pyparsing html5lib termcolor
Requires: /var/log

%description -n python3-module-%oname
Zero markup language.

Features:
* zero markup templates
* clean syntax
* extensible
* components
* namespaces
* lean code
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
python setup.py test -v
export PYTHONPATH=%buildroot%python_sitelibdir
pushd %oname/test
py.test -vv *.py
popd
%endif
%if_with python3
pushd ../python3
python3 setup.py test -v
export PYTHONPATH=%buildroot%python3_sitelibdir
pushd %oname/test
py.test-%_python3_version -vv *.py
popd
popd
%endif

%if_with python2
%files
%doc %oname/examples
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc %oname/examples
%python3_sitelibdir/*
%endif

%changelog
* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt1.git20150816
- Initial build for Sisyphus

