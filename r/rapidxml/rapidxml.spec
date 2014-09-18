Name: rapidxml
Version: 1.13
Release: alt1
Summary: Attempt to create the fastest XML parser
License: MIT
Group: Development/C++
Url: http://rapidxml.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-c++ doxygen graphviz
BuildArch: noarch

%description
RapidXml is an attempt to create the fastest XML parser possible, while
retaining useability, portability and reasonable W3C compatibility. It
is an in-situ parser with parsing speed approaching speed of strlen
function executed on the same data.

%package docs
Summary: Documentation for RapidXml
Group: Development/Documentation

%description docs
RapidXml is an attempt to create the fastest XML parser possible, while
retaining useability, portability and reasonable W3C compatibility. It
is an in-situ parser with parsing speed approaching speed of strlen
function executed on the same data.

This package contains documentation for RapidXml.

%prep
%setup

%build
pushd doc/documentation
doxygen
popd

%install
install -d %buildroot%_includedir/%name
install -p -m644 *.hpp %buildroot%_includedir/%name/

%files
%doc *.txt *.html
%_includedir/*

%files docs
%doc doc/documentation/htmlq/*

%changelog
* Thu Sep 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.13-alt1
- Initial build for Sisyphus

