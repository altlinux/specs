
%define modname flask
%def_with python3
%def_disable check

Name: python-module-%modname
Version: 0.10.1
Release: alt1.1
Summary: A micro-framework for Python based on Werkzeug, Jinja 2 and good intentions

Group: Development/Python
License: BSD
URL: http://flask.pocoo.org/

BuildArch: noarch

%setup_python_module %modname

Source: Flask-%version.tar
Patch1: flask-0.9-alt-tests-in-usr-src.patch

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-jinja2 python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: python-module-pytest python3-module-pytest rpm-build-python3

#BuildRequires: python-module-setuptools-tests
#BuildRequires: python-module-jinja2 python-module-werkzeug python-module-simplejson
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%description
Flask is called a "micro-framework" because the idea to keep the core
simple but extensible. There is no database abstraction layer, no form
validation or anything else where different libraries already exist that
can handle that.  However Flask knows the concept of extensions that can
add this functionality into your application as if it was implemented in
Flask itself. There are currently extensions for object relational
mappers, form validation, upload handling, various open authentication
technologies and more.

%package -n python3-module-%modname
Summary: A micro-framework for Python based on Werkzeug, Jinja 2 and good intentions
Group: Development/Python3

%description -n python3-module-%modname
Flask is called a "micro-framework" because the idea to keep the core
simple but extensible. There is no database abstraction layer, no form
validation or anything else where different libraries already exist that
can handle that.  However Flask knows the concept of extensions that can
add this functionality into your application as if it was implemented in
Flask itself. There are currently extensions for object relational
mappers, form validation, upload handling, various open authentication
technologies and more.

%prep
%setup -n Flask-%version

%patch1 -p 1

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install --record=INSTALLED_FILES

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python ./setup.py test
%if_with python3
pushd ../python3
python3 ./setup.py test
popd
%endif

%files -f INSTALLED_FILES
%doc AUTHORS README LICENSE
%exclude %python_sitelibdir_noarch/flask/testsuite

%if_with python3
%files -n python3-module-%modname
%doc AUTHORS README LICENSE
%python3_sitelibdir_noarch/*
%exclude %python3_sitelibdir_noarch/flask/testsuite
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.10.1-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt1
- Version 0.10.1
- Added module for Python 3

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt2.1
- Fixed build

* Sun Jan 06 2013 Ivan A. Melnikov <iv@altlinux.org> 0.9-alt2
- Don't package testsuite.

* Sun Jan 06 2013 Ivan A. Melnikov <iv@altlinux.org> 0.9-alt1
- Initial build for Sisyphus.

