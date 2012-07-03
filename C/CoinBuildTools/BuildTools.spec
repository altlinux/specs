%define oname BuildTools
Name: Coin%oname
Version: 0.7.2
Release: alt2.svn20120128
Summary: CoinHelp (BuildTools) project
License: Public domain
Group: Development/Tools
Url: http://www.coin-or.org/projects/BuildTools.xml
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://projects.coin-or.org/svn/BuildTools/trunk
Source: %oname-%version.tar.gz
BuildArch: noarch

BuildPreReq: f2c gcc-fortran gcc-c++
BuildPreReq: liblapack-devel

%description
CoinHelp (BuildTools) project.

%prep
%setup

%install
install -d %buildroot%_bindir
install -p -m755 run_autotools %buildroot%_bindir

install -d %buildroot%_includedir
install -p -m644 headers/* %buildroot%_includedir

install -d %buildroot%_datadir/libtool
install -p -m644 share/config.site \
	%buildroot%_datadir
install -p -m644 coin.m4 \
	%buildroot%_datadir/libtool
install -p -m644 %_datadir/libtool-2.4/aclocal/libtool.m4 \
	%buildroot%_datadir/libtool

install -d %buildroot%_datadir/%oname
for i in config.guess config.sub depcomp \
	install-sh ltmain.sh missing Makemain.inc
do
	install -p -m755 $i %buildroot%_datadir/%oname
done
ln -s ../%oname/ltmain.sh %buildroot%_datadir/libtool

%files
%_bindir/*
%_includedir/*
%_datadir/%oname
%_datadir/libtool/*
%_datadir/config.site

%changelog
* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt2.svn20120128
- Rebuilt with libtool_2.4

* Sun Feb 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1.svn20120128
- Version 0.7.2

* Sun Sep 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.svn20110903
- Version 0.7.0

* Sun Sep 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.svn20110903
- New snapshot

* Sat Aug 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.svn20110716
- New snapshot

* Sat Apr 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.svn20110417
- New snapshot

* Sat Apr 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.svn20101205.2
- Built with GotoBLAS2 instead of ATLAS

* Sun Dec 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.svn20101205.1
- Added libtinfo in list where find 'tputs'

* Thu Dec 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.svn20101205
- Version 0.6.1

* Wed Sep 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.svn20100915
- New snapshot

* Tue Aug 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.svn20100819.1
- Fixed Makemain.inc

* Tue Aug 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.svn20100819
- Version 0.6

* Wed Feb 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.29-alt1.svn20090726.1
- Rebuilt as noarch

* Wed Feb 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.29-alt1.svn20090726
- Initial build for Sisyphus

