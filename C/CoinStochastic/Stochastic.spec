%define oname Stochastic
Name: Coin%oname
Version: 1.0
Release: alt1.svn20100718
Summary: COIN-OR Stochastic data
License: CLP
Group: Sciences/Mathematics
Url: https://www.coin-or.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/Data/trunk/Stochastic
Source: %oname-%version.tar.gz

BuildPreReq: zlib-devel CoinBuildTools

%description
COIN-OR Stochastic data.

%package data
Summary: COIN-OR Stochastic data
Group: Sciences/Mathematics
BuildArch: noarch

%description data
COIN-OR Stochastic data.

%prep
%setup

%build
%autoreconf
%configure --enable-gnu-packages

%install
%makeinstall_std

%files data
%dir %_datadir/coin
%dir %_datadir/coin/Data
%_datadir/coin/Data/Stochastic

%changelog
* Sat Sep 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20100718
- Initial build for Sisyphus

