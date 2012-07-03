%define oname Sample
Name: Coin%oname
Version: 1.0
Release: alt1.svn20101031
Summary: COIN-OR Sample models
License: CPL
Group: Sciences/Mathematics
Url: http://www.coin-or.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildPreReq: zlib-devel CoinBuildTools

# https://projects.coin-or.org/svn/Data/trunk/Sample
Source: %oname-%version.tar.gz

%description
COIN-OR Sample models.

%package devel
Summary: Development files of COIN-OR Sample models
Group: Development/Other
Requires: %name-data = %version-%release
Conflicts: %name < %version-%release

%description devel
COIN-OR Sample models.

This package contains development files of COIN-OR Sample models.

%package data
Summary: Data of COIN-OR Sample models
Group: Sciences/Mathematics
BuildArch: noarch
Conflicts: %name < %version-%release
Obsoletes: %name < %version-%release
Provides: %name = %version-%release

%description data
COIN-OR Sample models.

This package contains data of COIN-OR Sample models.

%prep
%setup

%build
%autoreconf
%configure --enable-gnu-packages

%install
%makeinstall_std

rm -fR %buildroot%_datadir/coin/doc

%files data
%dir %_datadir/coin
%dir %_datadir/coin/Data
%_datadir/coin/Data/Sample

%files devel
%_pkgconfigdir/*

%changelog
* Sat Dec 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20101031
- New snapshot

* Thu Sep 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20100817.1
- Moved data into %name-data package

* Tue Aug 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20100817
- Initial build for Sisyphus

