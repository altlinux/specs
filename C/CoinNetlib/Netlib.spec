%define oname Netlib
Name: Coin%oname
Version: 1.0
Release: alt1.svn20101103.1
Summary: COIN-OR Netlib models
License: CPL
Group: Sciences/Mathematics
Url: http://www.coin-or.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/Data/trunk/Netlib
Source: %oname-%version.tar.gz

BuildPreReq: CoinBuildTools zlib-devel

%description
COIN-OR Netlib models.

%package devel
Summary: Development files of COIN-OR Netlib models
Group: Development/Other
Requires: %name-data = %version-%release
Conflicts: %name < %version-%release

%description devel
COIN-OR Netlib models.

This package contains development files of COIN-OR Netlib models.

%package data
Summary: Data of COIN-OR Netlib models
Group: Sciences/Mathematics
BuildArch: noarch
Conflicts: %name < %version-%release
Obsoletes: %name < %version-%release
Provides: %name = %version-%release

%description data
COIN-OR Netlib models.

This package contains data of COIN-OR Netlib models.

%prep
%setup

%build
#autoreconf
%configure \
	--enable-gnu-packages
%make_build

%install
%makeinstall_std

rm -fR %buildroot%_datadir/coin/doc

%files data
%dir %_datadir/coin
%dir %_datadir/coin/Data
%_datadir/coin/Data/Netlib

%files devel
%_pkgconfigdir/*

%changelog
* Fri Apr 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20101103.1
- Fixed build

* Sat Dec 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20101103
- New snapshot

* Thu Sep 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20100619.1
- Moved data into %name-data package

* Tue Aug 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20100619
- Initial build for Sisyphus

