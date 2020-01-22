%define oname mozhttpd

Name: python3-module-%oname
Version: 0.7
Release: alt3

Summary: Python webserver intended for use with Mozilla testing
License: MPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/mozhttpd/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-moznetwork
BuildRequires: python-tools-2to3 python3-module-six

Conflicts: python-module-%oname


%description
Python webserver intended for use with Mozilla testing.

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc PKG-INFO
%_bindir/*
%python3_sitelibdir/*


%changelog
* Wed Jan 22 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.7-alt3
- Porting on Python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt2
- Enabled testing

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1
- Initial build for Sisyphus

