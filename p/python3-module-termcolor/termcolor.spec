%define oname termcolor

Name: python3-module-%oname
Version: 1.1.0
Release: alt2.git20130510
Summary: ANSII Color formatting for output in terminal
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/termcolor/

# https://github.com/edmund-huber/termcolor.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%py3_provides %oname

%description
ANSII Color formatting for output in terminal.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
python3 %oname.py

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Wed Jul 14 2021 Alexey Shabalin <shaba@altlinux.org> 1.1.0-alt2.git20130510
- Build python3 module only

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20130510
- Initial build for Sisyphus
