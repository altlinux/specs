%define oname mozrunner

Name: python3-module-%oname
Version: 7.7.0
Release: alt1

Summary: Reliable start/stop/configuration of Mozilla Applications (Firefox, Thunderbird, etc.)
License: MPLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/mozrunner/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
# BuildPreReq: python-module-mozcrash python-module-mozdevice
# BuildPreReq: python-module-mozfile python-module-mozinfo
# BuildPreReq: python-module-mozlog python-module-mozprocess
# BuildRequires: python3-module-mozprofile

%py3_provides %oname


%description
Reliable start/stop/configuration of Mozilla Applications (Firefox,
Thunderbird, etc.).

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
# %%__python3 setup.py test

%files
%doc PKG-INFO
%_bindir/*
%python3_sitelibdir/*


%changelog
* Tue Jan 21 2020 Andrey Bychkov <mrdrew@altlinux.org> 7.7.0-alt1
- Version updated to 7.7.0
- porting on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 6.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.6-alt1
- Initial build for Sisyphus

