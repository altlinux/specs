%define oname sphinxtogithub

Name: python3-module-%oname
Version: 1.1.0
Release: alt2

Summary: Script to prepare Sphinx html output for github pages
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/sphinxtogithub/
BuildArch: noarch

# https://github.com/michaeljones/sphinx-to-github.git
Source: %name-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
%py_provides %oname


%description
This project is designed to help you get around the github-pages Jekyll
behaviour of ignoring top level directories starting with an underscore.

%prep
%setup
%patch0 -p1

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests


%changelog
* Tue Feb 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.1.0-alt2
- Porting on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1.dev.git20131026.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Nov 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.dev.git20131026
- Initial build for Sisyphus

