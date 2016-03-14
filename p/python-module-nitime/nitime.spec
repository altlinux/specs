%define oname nitime

%def_with python3

Name: python-module-%oname
Version: 0.5
Release: alt1.1

Summary: Nitime: timeseries analysis for neuroscience data
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/nitime/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%setup_python_module %oname

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-sphinx-devel
BuildPreReq: python-module-matplotlib python-module-scipy
BuildPreReq: python-module-mpl_toolkits python-module-nibabel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildPreReq: python-tools-2to3 libnumpy-py3-devel
%endif

%description
Nitime is library of tools and algorithms for the analysis of
time-series data from neuroscience experiments. It contains a
implementation of numerical algorithms for time-series analysis both in
the time and spectral domains, a set of container objects to represent
time-series, and auxiliary objects that expose a high level interface to
the numerical machinery and make common analysis tasks easy to express
with compact and semantically clear code.

%package tests
Summary: Tests for Nitime
Group: Development/Python
Requires: %name = %EVR

%description tests
Nitime is library of tools and algorithms for the analysis of
time-series data from neuroscience experiments. It contains a
implementation of numerical algorithms for time-series analysis both in
the time and spectral domains, a set of container objects to represent
time-series, and auxiliary objects that expose a high level interface to
the numerical machinery and make common analysis tasks easy to express
with compact and semantically clear code.

This package contains tests for Nitime.

%if_with python3
%package -n python3-module-%oname
Summary: Nitime: timeseries analysis for neuroscience data
Group: Development/Python3

%description -n python3-module-%oname
Nitime is library of tools and algorithms for the analysis of
time-series data from neuroscience experiments. It contains a
implementation of numerical algorithms for time-series analysis both in
the time and spectral domains, a set of container objects to represent
time-series, and auxiliary objects that expose a high level interface to
the numerical machinery and make common analysis tasks easy to express
with compact and semantically clear code.

%package -n python3-module-%oname-tests
Summary: Tests for Nitime
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Nitime is library of tools and algorithms for the analysis of
time-series data from neuroscience experiments. It contains a
implementation of numerical algorithms for time-series analysis both in
the time and spectral domains, a set of container objects to represent
time-series, and auxiliary objects that expose a high level interface to
the numerical machinery and make common analysis tasks easy to express
with compact and semantically clear code.

This package contains tests for Nitime.

%endif

%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
pushd ../python3
#find -type f -exec sed -i 's|%_bindir/python|%_bindir/python3|' -- '{}' +
#find -type f -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +
find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

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

export PYTHONPATH=%buildroot%python_sitelibdir
#make -C doc html

%files
%doc README.txt THANKS
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/test*
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc README.txt THANKS
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/__pycache__/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/tests
%python3_sitelibdir/*/__pycache__/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1
- Version 0.5

* Fri Oct 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Initial build for Sisyphus

