%define realname vatnumber

Name:           python3-module-%realname
Version:        1.1
Release:        alt1
Summary:        Python module to validate VAT numbers

Group:          Development/Python3
License:        GPLv3+
URL:            http://code.google.com/p/vatnumber/
Source0:        http://vatnumber.googlecode.com/files/%realname-%version.tar.gz

BuildArch:      noarch
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools

%py3_requires suds

%description
Python module to validate VAT numbers.

%prep
%setup -n %realname-%version

%build
%python3_build

%install
%python3_install

%files
%doc CHANGELOG COPYRIGHT README
%python3_sitelibdir/%realname
%python3_sitelibdir/%{realname}*.egg-info

%changelog
* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

