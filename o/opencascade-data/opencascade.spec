Name: opencascade-data
Version: 6.5.2
Release: alt1
Summary: Data for Open CASCADE
License: BSD-like
Group: Development/Documentation
Url: http://www.opencascade.org
BuildArch: noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: OpenCASCADE_src.tar

%description
Open CASCADE Technology version 6.5.0, a minor release, which introduces quite a
number of new features and improved traditional functionality along with certain
changes over the previous public release and maintenance releases exclusively
available to the customers.

This package contains data for Open CASCADE.

%prep
%setup

%install
install -d %buildroot%_datadir/%name
cp -fR * %buildroot%_datadir/%name/

%files
%_datadir/%name

%changelog
* Wed Feb 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.2-alt1
- Version 6.5.2

* Mon Oct 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.1-alt1
- Version 6.5.1

* Mon May 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.0-alt1
- Version 6.5.0

* Wed Dec 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt1
- Initial build for Sisyphus

