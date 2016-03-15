%define oname pybars3

%def_with python3

Name: python-module-%oname
Version: 0.7.2
Release: alt1.git20150123.1.1
Summary: Handlebars.js templating for Python 3 and 2
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/pybars3/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/wbond/pybars3.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-pymeta3 python-module-fixtures
#BuildPreReq: python-module-testtools
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-pymeta3 python3-module-fixtures
#BuildPreReq: python3-module-testtools
%endif

%py_provides %oname pybars
%py_requires pymeta3

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-cryptography python-module-enum34 python-module-extras python-module-linecache2 python-module-mimeparse python-module-pbr python-module-pluggy python-module-py python-module-pyasn1 python-module-serial python-module-setuptools python-module-six python-module-traceback2 python-module-twisted-core python-module-unittest2 python-module-zope.interface python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-extras python3-module-genshi python3-module-linecache2 python3-module-mimeparse python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pluggy python3-module-py python3-module-pycparser python3-module-setuptools python3-module-six python3-module-traceback2 python3-module-unittest2 xz
BuildRequires: python-module-pymeta3 python-module-pytest python-module-testtools python3-module-html5lib python3-module-pymeta3 python3-module-pytest python3-module-testtools rpm-build-python3 time

%description
Handlebars.js template support for Python 3 and 2.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Handlebars.js template support for Python 3 and 2.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Handlebars.js templating for Python 3 and 2
Group: Development/Python3
%py3_provides %oname pybars
%py3_requires pymeta3

%description -n python3-module-%oname
Handlebars.js template support for Python 3 and 2.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Handlebars.js template support for Python 3 and 2.

This package contains tests for %oname.

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
rm -fR build
py.test -vv
%if_with python3
pushd ../python3
rm -fR build
py.test-%_python3_version -vv
popd
%endif

%files
%doc NEWS *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc NEWS *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.2-alt1.git20150123.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.2-alt1.git20150123.1
- NMU: Use buildreq for BR.

* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1.git20150123
- Initial build for Sisyphus

