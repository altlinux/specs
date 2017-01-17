%define _unpackaged_files_terminate_build 1
%define oname flask-babel

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.11.1
Release: alt1
Summary: Adds i18n/l10n support to Flask applications
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Flask-Babel/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mitsuhiko/flask-babel.git
Source0: https://pypi.python.org/packages/47/96/6013d4091fb4238e27e918aec4929f082942fa8c9489ae3aad2f18de4b5b/Flask-Babel-%{version}.tar.gz
BuildArch: noarch

BuildRequires: python-module-babel python-module-pytest
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-flask python-module-babel
#BuildPreReq: python-module-speaklater python-module-jinja2
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-flask python3-module-babel
#BuildPreReq: python3-module-speaklater python3-module-jinja2
BuildRequires: python3-module-babel python3-module-pytest
%endif

%py_provides flask_babel

%description
Adds i18n/l10n support to Flask applications with the help of the Babel
library.

%package -n python3-module-%oname
Summary: Adds i18n/l10n support to Flask applications
Group: Development/Python3
%py3_provides flask_babel

%description -n python3-module-%oname
Adds i18n/l10n support to Flask applications with the help of the Babel
library.

%prep
%setup -q -n Flask-Babel-%{version}

%if_with python3
cp -fR . ../python3
sed -i 's|python|python3|g' ../python3/Makefile
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
make test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc docs/*.rst PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc docs/*.rst PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.11.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9-alt2.git20130729.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 0.9-alt2.git20130729
- Rebuild with "def_disable check"
- Cleanup bildreq

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.git20130729
- Initial build for Sisyphus
