%define oname pyfunc

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt1.20150101.1
Summary: Call python functions from your shell
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/pyfunc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/saurabh-hirani/pyfunc.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
Call python functions from your shell.

%package -n python3-module-%oname
Summary: Call python functions from your shell
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Call python functions from your shell.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%python_build_debug

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.20150101.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.20150101
- Initial build for Sisyphus

