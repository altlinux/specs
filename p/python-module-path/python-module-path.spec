%define module_name path

%def_with python3

Name: python-module-%module_name
Version: 7.2
Release: alt1.git20150122.1

Summary: A module wrapper for os.path
License: MIT
Group: Development/Python
Url: https://github.com/jaraco/path.py

Source: python-module-%module_name-%version.tar

BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-pytest-runner
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-pytest-runner
%endif

%description
path.py implements a path objects as first-class entities, allowing
common operations on files to be invoked on those path objects directly.

%package -n python3-module-%module_name
Summary: A module wrapper for os.path
Group: Development/Python3

%description -n python3-module-%module_name
path.py implements a path objects as first-class entities, allowing
common operations on files to be invoked on those path objects directly.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
rm -f %buildroot%python3_sitelibdir/test_path.py
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
mkdir docs/_static
%make -C docs html

%files
%doc *.rst docs/_build/html
%python_sitelibdir/path*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%module_name
%doc *.rst docs/_build/html
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 7.2-alt1.git20150122.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.2-alt1.git20150122
- Version 7.2

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3-alt1.git20140823
- Version 5.3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.2.990-alt1.1
- Rebuild with Python-2.7

* Tue Jun 07 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.2.2.990-alt1
- Initial build for Sisyphus.
