%define oname graphcanvas

Name: python3-module-%oname
Version: 4.1.0
Release: alt2

Summary: Interactive graph (network) visualization

License: BSD
Group: Development/Python3
Url: https://github.com/enthought/graphcanvas

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%description
graphcanvas is an library for interacting with visualizations of complex
graphs. The aim is to allow the developer to declare the graph by the
simplest means and be able to visualize the graph immediately.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc *.rst examples
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info

%changelog
* Fri May 20 2022 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt2
- Fixed BuildRequires.

* Mon Oct 21 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.1.0-alt1
- Version updated to 4.1.0
- python2 -> python3

* Mon May 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1.git20130328
- Version 4.0.2

* Mon Oct 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.git20120221
- New snapshot

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.git20110627
- Initial build for Sisyphus

