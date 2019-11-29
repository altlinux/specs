%define oname transitions

Name: python3-module-%oname
Version: 0.2.3
Release: alt2

Summary: A lightweight, object-oriented Python state machine implementation
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/transitions/
BuildArch: noarch

# https://github.com/tyarkoni/transitions.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose

%py3_provides %oname


%description
A lightweight, object-oriented finite state machine implementation in
Python.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.md
%python3_sitelibdir/*


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.3-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.3-alt1.git20150114.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.3-alt1.git20150114.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt1.git20150114
- Initial build for Sisyphus

