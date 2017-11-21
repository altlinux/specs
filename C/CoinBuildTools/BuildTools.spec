%define oname BuildTools
Name: Coin%oname
Epoch: 1
Version: 0.8.7
Release: alt1
Summary: CoinHelp (BuildTools) project
License: EPL v1.0
Group: Development/Tools
BuildArch: noarch
Url: https://projects.coin-or.org/BuildTools

# https://projects.coin-or.org/svn/BuildTools/releases/%version
Source: %oname-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildRequires: f2c gcc-fortran gcc-c++
BuildRequires: liblapack-devel

%description
CoinHelp (BuildTools) project.

%prep
%setup -n %oname-%version
%patch1 -p1

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
* Fri Nov 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.8.7-alt1
- Updated to stable upstream version 0.8.7.

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.13-alt1.svn20131130
- Version 0.7.13

* Tue Sep 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.7-alt1.svn20121202
- Version 0.7.7

* Tue Feb 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.3-alt1.svn20120811
- Back to version 0.7.3

* Tue Feb 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.4-alt1.svn20121202
- Version 0.7.4

* Wed Sep 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.3-alt1.svn20120811
- Version 0.7.3

* Sat Aug 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt3.svn20120128
- Built with OpenBLAS instead of GotoBLAS2

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

