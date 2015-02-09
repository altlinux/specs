%define oname pyjade

%def_with python3

Name: python-module-%oname
Version: 3.0.0
Release: alt1.git20150116
Summary: Jade syntax template adapter for Django, Jinja2, Mako and Tornado templates
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyjade/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/syrusakbary/pyjade.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six python-module-nose
BuildPreReq: python-module-django python-module-jinja2
BuildPreReq: python-module-tornado python-module-pyramid
BuildPreReq: python-module-mako
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six python3-module-nose
BuildPreReq: python3-module-django python3-module-jinja2
BuildPreReq: python3-module-tornado python3-module-pyramid
BuildPreReq: python3-module-mako
%endif

%py_provides %oname
%py_requires six mako

%description
PyJade is a high performance port of Jade-lang for python, that converts
any .jade source to the each Template-language (Django, Jinja2, Mako or
Tornado).

%package -n python3-module-%oname
Summary: Jade syntax template adapter for Django, Jinja2, Mako and Tornado templates
Group: Development/Python3
%py3_provides %oname
%py3_requires six mako

%description -n python3-module-%oname
PyJade is a high performance port of Jade-lang for python, that converts
any .jade source to the each Template-language (Django, Jinja2, Mako or
Tornado).

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

%check
python setup.py test
python test_jinja.py
./test.sh
%if_with python3
pushd ../python3
python3 setup.py test
python3 test_jinja.py
#sed -i 's|nosetests|nosetests3|' test.sh
#./test.sh
popd
%endif

%files
%doc AUTHORS *.md *.rst examples
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.md *.rst examples
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt1.git20150116
- Initial build for Sisyphus

