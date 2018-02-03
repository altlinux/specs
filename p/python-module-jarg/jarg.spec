%define oname jarg

%def_with python3

Name: python-module-%oname
Version: 0.3.0
Release: alt1.git20141127.1.1
Summary: Shorthand JSON and form encoding syntax in the shell 
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/jarg/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jdp/jarg.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-modules-json
BuildPreReq: python-devel python-module-setuptools
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
BuildRequires: python3-module-pytest
%endif

%py_provides %oname

%description
jarg is an encoding shorthand for your shell. It is a command-line
utility that wants to make writing things like JSON and form-encoded
values easier in the shell.

%package -n python3-module-%oname
Summary: Shorthand JSON and form encoding syntax in the shell
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
jarg is an encoding shorthand for your shell. It is a command-line
utility that wants to make writing things like JSON and form-encoded
values easier in the shell.

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
%doc *.rst man/*
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst man/*
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1.git20141127.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt1.git20141127.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20141127
- Initial build for Sisyphus

