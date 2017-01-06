%define oname ptpython

%def_with python3

Name: %oname
Version: 0.36
Release: alt1
Summary: Python REPL build on top of prompt_toolkit
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/ptpython
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jonathanslenders/ptpython.git
Source0: https://pypi.python.org/packages/00/bf/eca5caf726c8b773dbafeed5bda65e95214bd626b31bbbaae535a7752844/%{name}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests ipython
BuildPreReq: python-module-prompt_toolkit python-module-jedi
BuildPreReq: python-module-docopt
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests ipython3
BuildPreReq: python3-module-prompt_toolkit python3-module-jedi
BuildPreReq: python3-module-docopt
%endif

%py_provides %oname
%py_requires prompt_toolkit jedi docopt IPython
%add_python_req_skip asyncio asyncssh

%description
ptpython is an advanced Python REPL built on top of the prompt_toolkit
library.

%if_with python3
%package -n %{oname}3
Summary: Python REPL build on top of prompt_toolkit
Group: Development/Python3
%py3_provides %oname
%py3_requires prompt_toolkit jedi docopt IPython

%description -n %{oname}3
ptpython is an advanced Python REPL built on top of the prompt_toolkit
library.
%endif

%prep
%setup -q 

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
	mv $i ${i}3
done
popd
%endif

%python_install

%check
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc CHANGELOG *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*3
%endif
%python_sitelibdir/*

%if_with python3
%files -n %{oname}3
%doc CHANGELOG *.rst
%_bindir/*3
%python3_sitelibdir/*
%endif

%changelog
* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.20-alt1.git20150808.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20-alt1.git20150808
- Initial build for Sisyphus

