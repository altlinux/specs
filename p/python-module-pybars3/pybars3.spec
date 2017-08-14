%define oname pybars3

%def_with python3

Name: python-module-%oname
Version: 0.9.3
Release: alt1
Summary: Handlebars.js templating for Python 3 and 2
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/pybars3/

# https://github.com/wbond/pybars3.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-module-pymeta3 python-module-pytest python-module-testtools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-html5lib python3-module-pymeta3 python3-module-pytest python3-module-testtools
%endif

%py_provides %oname pybars

%description
Handlebars.js template support for Python 3 and 2.

%if_with python3
%package -n python3-module-%oname
Summary: Handlebars.js templating for Python 3 and 2
Group: Development/Python3
%py3_provides %oname pybars

%description -n python3-module-%oname
Handlebars.js template support for Python 3 and 2.
%endif

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
py.test -vv

%if_with python3
pushd ../python3
py.test3 -vv
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.3-alt1
- Updated to upstream version 0.9.3.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.2-alt1.git20150123.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.2-alt1.git20150123.1
- NMU: Use buildreq for BR.

* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1.git20150123
- Initial build for Sisyphus

