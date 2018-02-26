%define modulename FormEncode

Name: python3-module-%modulename
Version: 1.2.3
Release: alt1.git20100904

Summary: HTML form validation, generation, and convertion package for Python 3
License: PSF
Group: Development/Python3

URL: https://github.com/davidfraser/FormEncode
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
BuildArch: noarch

# https://github.com/davidfraser/FormEncode.git
Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-distribute
BuildPreReq: python3-module-docutils

%description
FormEncode validates and converts nested structures. It allows for
a declarative form of defining the validation, and decoupled processes
for filling and generating forms.

%package doc
Summary: This package contains documentation and examples for FormEncode.
Group: Development/Python

%description doc
FormEncode validates and converts nested structures. It allows for
a declarative form of defining the validation, and decoupled processes
for filling and generating forms.

%prep
%setup

%build
%python3_build

pushd docs
./build
popd

%install
%python3_install

%files
%python3_sitelibdir/*

%files doc
%doc docs/* examples

%changelog
* Fri Apr 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1.git20100904
- Initial build for Sisyphus

