%define oname Miplib3
Name: Coin%oname
Version: 1.0
Release: alt1.svn20101103.1
Summary: COIN-OR miplib3
License: Boost Software License, Version 1.0
Group: Sciences/Mathematics
Url: http://www.coin-or.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildPreReq: CoinBuildTools zlib-devel

# https://projects.coin-or.org/svn/Data/trunk/miplib3
Source: %oname-%version.tar.gz

%description
COIN-OR miplib3.

%package data
Summary: COIN-OR miplib3 data
Group: Sciences/Mathematics
BuildArch: noarch

%description data
COIN-OR miplib3.

This package contains data of COIN-OR miplib3.

%package devel
Summary: Development files of COIN-OR miplib3
Group: Development/Other
Requires: %name-data = %version-%release

%description devel
COIN-OR miplib3.

This package contains development files of COIN-OR miplib3.

%prep
%setup

%build
#autoreconf
%configure --enable-gnu-packages
%make_build

%install
%makeinstall_std

rm -fR %buildroot%_datadir/coin/doc

%files data
%dir %_datadir/coin
%dir %_datadir/coin/Data
%_datadir/coin/Data/miplib3

%files devel
%_pkgconfigdir/*

%changelog
* Fri Apr 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20101103.1
- Fixed build

* Sat Dec 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20101103
- New snapshot

* Thu Sep 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20100619
- Initial build for Sisyphus

