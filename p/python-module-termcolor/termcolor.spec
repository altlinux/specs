%define oname termcolor
%def_disable check

Name: python-module-%oname
Version: 1.1.0
Release: alt2.git20130510
Summary: ANSII Color formatting for output in terminal
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/termcolor/

# https://github.com/edmund-huber/termcolor.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_enabled check
PreReq: python-base
%endif

%py_provides %oname

%description
ANSII Color formatting for output in terminal.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%if_enabled check
%check
python %oname.py
%endif

%files
%doc *.rst
%python_sitelibdir/*

%changelog
* Thu Jul 28 2022 Leontiy Volodin <lvol@altlinux.org> 1.1.0-alt2.git20130510
- Returned to Sisyphus for mlnx-tools (ALT #41412, #43337).

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20130510
- Initial build for Sisyphus

