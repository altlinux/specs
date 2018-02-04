%define oname ptpdb

%def_with python3

Name: python-module-%oname
Version: 0.17
Release: alt1.1
Summary: Python debugger (pdb) build on top of prompt_toolkit
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/ptpdb

# https://github.com/jonathanslenders/ptpdb.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel python-module-setuptools
BuildRequires: ptpython python-module-prompt_toolkit
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: ptpython3 python3-module-prompt_toolkit
%endif

%py_provides %oname
%py_requires ptpython prompt_toolkit

%description
(Still experimental) PDB replacement, build on top of prompt_toolkit and
ptpython.

%if_with python3
%package -n python3-module-%oname
Summary: Python debugger (pdb) build on top of prompt_toolkit
Group: Development/Python3
%py3_provides %oname
%py3_requires ptpython prompt_toolkit

%description -n python3-module-%oname
(Still experimental) PDB replacement, build on top of prompt_toolkit and
ptpython.
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
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.rst examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.17-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Oct 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.17-alt1
- Updated to upstream version 0.17.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7-alt1.git20150808.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.git20150808
- Initial build for Sisyphus

