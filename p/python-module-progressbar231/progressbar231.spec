%define oname progressbar231

%def_with python3

Name: python-module-%oname
Version: 2.3.1
Release: alt1.1.1
Summary: Text progress bar library for Python
License: BSD/GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/progressbar231
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

Conflicts: python-module-progressbar2 python-module-progressbar
%py_provides %oname

%description
A text progress bar is typically used to display the progress of a long
running operation, providing a visual cue that processing is underway.

%package -n python3-module-%oname
Summary: Text progress bar library for Python
Group: Development/Python3
Conflicts: python3-module-progressbar2 python3-module-progressbar
%py3_provides %oname

%description -n python3-module-%oname
A text progress bar is typically used to display the progress of a long
running operation, providing a visual cue that processing is underway.

%prep
%setup

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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc examples.py *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc examples.py *.txt
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.3.1-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.1-alt1
- Initial build for Sisyphus

