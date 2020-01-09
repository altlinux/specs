%define oname portal

Name: python3-module-%oname
Version: 0.3.1
Release: alt2

Summary: Portal - Apple's Provisioning Portal API and CLI
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/portal/
BuildArch: noarch

# https://github.com/jlopez/portal.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_provides %oname


%description
Portal is a Python module that hooks to Apple's undocumented
provisioning portal developer services as well as a command line utility
that allows you to perform tasks without suffering CTS from all the
clicking.

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
%doc AUTHORS CHANGES *.rst
%_bindir/*
%python3_sitelibdir/*


%changelog
* Thu Jan 09 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.3.1-alt2
- porting on python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.1-alt1.git20130627.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Oct 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20130627
- Initial build for Sisyphus

