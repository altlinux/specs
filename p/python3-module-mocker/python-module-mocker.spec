Name: python3-module-mocker
Version: 1.1.1
Release: alt1.bzr20130910
Summary: graceful creation of test doubles (mocks, stubs, fakes and dummies)

Group: Development/Python3
License: BSD
Url: http://labix.org/mocker

# bzr branch lp:mocker
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
BuildPreReq: python3-module-setuptools python3-module-distutils-extra
BuildPreReq: intltool python-tools-2to3

%description
%summary

%prep
%setup
find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*
%doc NEWS LICENSE README.md

%changelog
* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.bzr20130910
- Initial build for Sisyphus

