%define oname markdown-checklist

%def_with python3

Name: python-module-%oname
Version: 0.4.1
Release: alt1.git20150127.1.1
Summary: Python Markdown extension for task lists with checkboxes
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/markdown-checklist/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/FND/markdown-checklist.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-markdown python-module-figleaf
BuildPreReq: python-module-coverage
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-markdown
BuildPreReq: python3-module-coverage
BuildRequires: python3-module-pytest
%endif

%py_provides markdown_checklist
%py_requires markdown

%description
Python Markdown extension for lists of tasks with checkboxes.

%package -n python3-module-%oname
Summary: Python Markdown extension for task lists with checkboxes
Group: Development/Python3
%py3_provides markdown_checklist
%py3_requires markdown

%description -n python3-module-%oname
Python Markdown extension for lists of tasks with checkboxes.

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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.1-alt1.git20150127.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt1.git20150127.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20150127
- Initial build for Sisyphus

