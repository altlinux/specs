%define oname peak-o-mat
Name: python-module-%oname
Version: 1.2
Release: alt1.svn20110810
Summary: A curve fitting program aimed at the fast and easy fitting of spectroscopic data
License: GPL v2
Group: Development/Python
Url: http://sourceforge.net/projects/lorentz/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://lorentz.svn.sourceforge.net/svnroot/lorentz/trunk
Source: %oname-%version.tar.gz
BuildArch: noarch

BuildPreReq: python-devel libnumpy-devel python-module-scipy-devel
BuildPreReq: python-module-wx2.9-devel

Requires: %oname-data = %version-%release
%add_python_req_skip _winreg

%description
peak-o-mat is a curve fitting program aimed at the fast and easy fitting
of spectroscopic data, especially if you face a large amount of similar
spectra.

%package -n %oname-data
Summary: Data files for peak-o-mat
Group: Sciences/Physics
BuildArch: noarch

%description -n %oname-data
peak-o-mat is a curve fitting program aimed at the fast and easy fitting
of spectroscopic data, especially if you face a large amount of similar
spectra.

This package contains data files for peak-o-mat.

%prep
%setup

%build
%python_build

%install
%python_install

install -d %buildroot%_datadir/%oname
install -p -m644 data/* %buildroot%_datadir/%oname

%files
%doc CHANGELOG COPYING DOCUMENTATION
%_bindir/*
%python_sitelibdir/*

%files -n %oname-data
%_datadir/%oname

%changelog
* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20110810
- Version 1.2

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.1-alt1.1
- Rebuild with Python-2.7

* Mon Oct 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus (ALT #24260)

