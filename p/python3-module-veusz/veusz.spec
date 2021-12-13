%define _unpackaged_files_terminate_build 1
%define oname veusz

Name: python3-module-%oname
Version: 3.4
Release: alt1

Summary: A Scientific Plotting Package
License: GPLv2+
Group: Development/Python3
Url: http://home.gna.org/veusz/

# Source0-git: https://github.com/veusz/veusz.git
Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: /usr/bin/pod2man /usr/bin/man
BuildRequires: python3-devel libnumpy-py3-devel
BuildRequires: qt5-base-devel python3-module-PyQt5-devel
BuildRequires: python3-module-sip6

%add_python3_req_skip pyemf

%description
Veusz is a GUI scientific plotting and graphing package. It is designed
to produce publication-ready Postscript or PDF output. SVG, EMF and
bitmap export formats are also supported. The program runs under
Unix/Linux, Windows or Mac OS X, and binaries are provided. Data can be
read from text, CSV or FITS files, and data can be manipulated or
examined from within the application.

%package docs
Summary: Documentation for Veusz
Group: Development/Documentation
BuildArch: noarch

%description docs
Veusz is a GUI scientific plotting and graphing package. It is designed
to produce publication-ready Postscript or PDF output. SVG, EMF and
bitmap export formats are also supported. The program runs under
Unix/Linux, Windows or Mac OS X, and binaries are provided. Data can be
read from text, CSV or FITS files, and data can be manipulated or
examined from within the application.

This packagec contains documentation for Veusz.

%package examples
Summary: Examples for Veusz
Group: Development/Documentation
Requires: %name = %version-%release

%description examples
Veusz is a GUI scientific plotting and graphing package. It is designed
to produce publication-ready Postscript or PDF output. SVG, EMF and
bitmap export formats are also supported. The program runs under
Unix/Linux, Windows or Mac OS X, and binaries are provided. Data can be
read from text, CSV or FITS files, and data can be manipulated or
examined from within the application.

This package contains examples for Veusz.

%package -n %oname
Summary: A Scientific Plotting Package
Group: Graphics
Conflicts: %name < %version-%release
Requires: %name = %version-%release
Requires: %name-examples = %version-%release

%description -n %oname
Veusz is a GUI scientific plotting and graphing package. It is designed
to produce publication-ready Postscript or PDF output. SVG, EMF and
bitmap export formats are also supported. The program runs under
Unix/Linux, Windows or Mac OS X, and binaries are provided. Data can be
read from text, CSV or FITS files, and data can be manipulated or
examined from within the application.

This package contains main scripts for Veusz.

%prep
%setup
find ./ -type f -name '*.py' -exec \
	sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' '{}' +

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

%install
%python3_install

%files
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/examples

%files examples
%python3_sitelibdir/*/examples

%files -n %oname
%doc AUTHORS ChangeLog COPYING README.md
%_bindir/*


%changelog
* Mon Dec 13 2021 Vitaly Lipatov <lav@altlinux.ru> 3.4-alt1
- new version 3.4

* Mon Dec 13 2021 Vitaly Lipatov <lav@altlinux.ru> 3.3.1-alt3
- rebuild with sip6

* Thu Aug 26 2021 Vitaly Lipatov <lav@altlinux.ru> 3.3.1-alt2
- drop unused BR: texlive-dist

* Wed Jul 14 2021 Vitaly Lipatov <lav@altlinux.ru> 3.3.1-alt1
- new version 3.3.1, build with sip5

* Thu Mar 19 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.1-alt2
- Build for python2 disabled.

* Thu Jan 23 2020 Grigory Ustinov <grenka@altlinux.org> 3.1-alt1
- Build new version for python3.8.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.25.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.25.1-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.21-alt2.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.21-alt2
- Added module for Python 3

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.21-alt1
- Version 1.21

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.19.1-alt1
- Version 1.19.1

* Tue Nov 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.18-alt2
- Fixed build

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.18-alt1
- Version 1.18

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.17-alt1
- Version 1.17

* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14-alt3
- Extracted %oname package (ALT #28282)

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.14-alt2.1
- Rebuild to remove redundant libpython2.7 dependency

* Sat Dec 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14-alt2
- Extracted examples into separate package

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14-alt1
- Initial build for Sisyphus

