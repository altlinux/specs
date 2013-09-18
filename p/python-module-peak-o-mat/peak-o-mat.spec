%define oname peak-o-mat
Name: python-module-%oname
Epoch: 1
Version: 1.1.9
Release: alt1.svn20130614
Summary: A curve fitting program aimed at the fast and easy fitting of spectroscopic data
License: GPL v2
Group: Development/Python
Url: http://sourceforge.net/projects/lorentz/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# svn://svn.code.sf.net/p/lorentz/code/trunk
Source: %oname-%version.tar.gz
BuildArch: noarch

BuildPreReq: python-devel libnumpy-devel python-module-scipy-devel
BuildPreReq: python-module-wx2.9-devel
BuildPreReq: python-module-sphinx-devel

Requires: %oname-data = %EVR
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

%package pickles
Summary: Pickles for peak-o-mat
Group: Development/Python

%description pickles
peak-o-mat is a curve fitting program aimed at the fast and easy fitting
of spectroscopic data, especially if you face a large amount of similar
spectra.

This package contains pickles for peak-o-mat.

%package doc
Summary: Documentation for peak-o-mat
Group: Development/Python
BuildArch: noarch

%description doc
peak-o-mat is a curve fitting program aimed at the fast and easy fitting
of spectroscopic data, especially if you face a large amount of similar
spectra.

This package contains documentation for peak-o-mat.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build

%make -C doc pickle
%make -C doc html

%install
%python_install

install -d %buildroot%_datadir/%oname
install -p -m644 data/* %buildroot%_datadir/%oname

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/peak_o_mat/

%files
%doc CHANGELOG COPYING
#_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files -n %oname-data
%_datadir/%oname

%files pickles
%python_sitelibdir/*/pickle

%files doc
%doc doc/_build/html/*

%changelog
* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.1.9-alt1.svn20130614
- Version 1.1.9

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20121202
- New snapshot

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20110810
- Version 1.2

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.1-alt1.1
- Rebuild with Python-2.7

* Mon Oct 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus (ALT #24260)

