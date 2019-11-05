%define oname anywho

Name: python3-module-%oname
Version: 1.0.0
Release: alt2

Summary: whois in pure Python
License: WTFPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/anywho
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

Requires: whois

%py3_provides %oname


%description
whois in pure Python.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc PKG-INFO
%python3_sitelibdir/*


%changelog
* Tue Nov 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.0-alt2
- disable python2, enable python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

