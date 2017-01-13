%define _unpackaged_files_terminate_build 1
%define oname sed3

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.1.34
Release: alt1
Summary: 3D viewer and editor of color seeds
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sed3
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mjirik/sed3.git
Source0: https://pypi.python.org/packages/bc/b1/7c56e45f4aafd260e5472772a5ca0b4536faa84be1ae522b92ecd82c59aa/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: python-module-coverage python-module-matplotlib python-module-nose python-module-pbr python-module-pygobject3 python-module-pytest python-module-pytz python-module-scipy python-module-unittest2 python-module-yaml
#BuildPreReq: python-devel python-module-setuptools-tests xvfb-run
#BuildPreReq: python-module-matplotlib-qt4 python-module-yaml
#BuildPreReq: python-module-scipy python-module-nose
#BuildPreReq: python-module-mock python-module-PyQt4
#BuildPreReq: python-module-pytz python-module-pygobject3
#BuildPreReq: python-module-pycairo python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-matplotlib-qt4 python3-module-yaml
#BuildPreReq: python3-module-scipy python3-module-nose
#BuildPreReq: python3-module-mock python3-module-PyQt4
#BuildPreReq: python3-module-pytz python3-module-pygobject3
#BuildPreReq: python3-module-pycairo python3-module-coverage
BuildRequires: python3-module-coverage python3-module-html5lib python3-module-matplotlib python3-module-nose python3-module-pbr python3-module-pycairo python3-module-pygobject3 python3-module-pytest python3-module-pytz python3-module-scipy python3-module-unittest2 python3-module-yaml
%endif

%py_provides %oname
#%py_requires matplotlib yaml scipy PyQt4
#%py_requires matplotlib.backends.backend_qt4agg

%description
3D viewer and editor of color seeds.

%if_with python3
%package -n python3-module-%oname
Summary: 3D viewer and editor of color seeds
Group: Development/Python3
%py3_provides %oname
#%py3_requires matplotlib yaml scipy PyQt4
#%py3_requires matplotlib.backends.backend_qt4agg

%description -n python3-module-%oname
3D viewer and editor of color seeds.
%endif

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
python setup.py test -v
xvfb-run nosetests -vv --with-coverage --cover-package=%oname
%if_with python3
pushd ../python3
python3 setup.py test -v
xvfb-run nosetests3 -vv --with-coverage --cover-package=%oname
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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.34-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.10-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 1.1.10-alt2
- Rebuild with "def_disable check"
- Cleanup buildreq

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.10-alt1
- Initial build for Sisyphus

