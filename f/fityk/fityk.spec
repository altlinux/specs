# This spec file has been made for ALT Linux distribuition

%def_with docs
%def_with python3

Summary: Tool for fitting and analyzing data
Name: fityk
Version: 1.3.0
Release: alt4.git20141119.1.1
License: GPL
Group: Sciences/Other
Url: https://github.com/wojdyr/fityk
# https://github.com/wojdyr/fityk.git
Source0: %name-%version.tar.bz2
Source1: %name.desktop
Source2: x-%name.desktop
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Automatically added by buildreq on Mon Aug 04 2008
BuildRequires: gcc-c++ gcc-fortran libreadline-devel rpm-build-python

BuildPreReq: boost-devel libxylib-devel libwxGTK3.1-devel zlib-devel
BuildPreReq: liblua5.1-devel python-module-sphinx-devel swig dvipng
BuildPreReq: libcmpfit-devel
BuildPreReq: texlive-latex-recommended texmf-latex-preview gnuplot
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildPreReq: python-tools-2to3
%endif

%description
Fityk is a program for nonlinear fitting of analytical functions
(especially peak-shaped) to data (usually experimental data).
It can be also used for visualization of x-y data only.

%package -n python-module-%name
Summary: Python module for Fityk
Group: Development/Python
%py_provides fityk
Conflicts: %name < %version-%release

%description -n python-module-%name
Fityk is a program for nonlinear fitting of analytical functions
(especially peak-shaped) to data (usually experimental data).
It can be also used for visualization of x-y data only.

This package contains Python module for Fityk.

%if_with python3
%package -n python3-module-%name
Summary: Python 3 module for Fityk
Group: Development/Python3
%py3_provides fityk

%description -n python3-module-%name
Fityk is a program for nonlinear fitting of analytical functions
(especially peak-shaped) to data (usually experimental data).
It can be also used for visualization of x-y data only.

This package contains Python module for Fityk.
%endif

%package devel
Summary: Header files, libraries and development documentation for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
This package contains the header files, static libraries and development
documentation for %name. If you like to develop programs using %name,
you will need to install %name-devel.

%prep
%setup
#cp -fR %_includedir/cmpfit fityk/

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%if_with python3
export PYTHON=python3
export PYTHON_LDFLAGS="$(python3-config --ldflags) -lm"
pushd ../python3
./autogen.sh
%configure \
	--enable-python \
%if_without docs
	--without-doc \
%endif
	--enable-lua

#make_build
%make
popd
%endif

export PYTHON=python
unset PYTHON_LDFLAGS
./autogen.sh
%configure \
	--enable-python \
%if_without docs
	--without-doc \
%endif
	--enable-lua

#make_build
%make

%install
install -d 755 %buildroot%_datadir/%name/samples
#install -d 755 %buildroot%_datadir/applications/
install -d 755 %buildroot%_desktopdir
install -d 755 %buildroot%_datadir/mimelnk/application/
install -d 755 %buildroot%_niconsdir
install -d 755 %buildroot%_miconsdir

%if_with python3
pushd ../python3
%make_install DESTDIR=$PWD/build3 install
popd
%endif

%makeinstall_std
rm -f samples/Makefile* doc/fitykhelp_img/Makefile* samples/*.pl \
	samples/*.o
# fityk.desktop file alrady instaled into system, therefore we should delete and 
# install our fityk.desktop file
rm -f %buildroot%_desktopdir/%name.desktop
rm -f %buildroot%_datadir/pixmaps/fityk.png

install -m 644 samples/* %buildroot%_datadir/%name/samples/
install -m 644 %SOURCE1 %buildroot%_desktopdir/
install -m 644 %SOURCE2 %buildroot%_datadir/mimelnk/application/
install -m 644 %name.png %buildroot%_niconsdir/
install -m 644 %name.png %buildroot%_miconsdir/
rm -f %buildroot%_datadir/%name/samples/*.pl

%ifarch x86_64
mv %buildroot%python_sitelibdir_noarch/* %buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3/build3
install -d %buildroot%python3_sitelibdir
mv $PWD%python3_sitelibdir/* %buildroot%python3_sitelibdir/
%ifarch x86_64
mv $PWD%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir/
%endif
popd
%endif

#check
# no check for: java, lua, perl and ruby
#make samples/hello samples/helloc
#samples/hello
#samples/helloc
#LD_LIBRARY_PATH=%buildroot%_libdir PYTHONPATH=%buildroot%python_sitelibdir samples/hello.py
#if_with python3
#pushd ../python3
#make samples/hello samples/helloc
#samples/hello
#samples/helloc
#2to3 -w samples/hello.py
#LD_LIBRARY_PATH=%buildroot%_libdir PYTHONPATH=%buildroot%python3_sitelibdir %__python3 samples/hello.py
#popd
#endif

%files
%doc COPYING NEWS TODO
%if_with docs
%doc %_datadir/%name/html
%_man1dir/*
%endif
%_bindir/*
%_datadir/%name/samples/*
%exclude %_datadir/%name/samples/*.rb
/usr/share/fityk/samples/
%_datadir/mime/packages/*
%_datadir/mimelnk/application/*.desktop
%_datadir/applications/fityk.desktop
%_niconsdir/*.png
%_miconsdir/*.png
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so

%files -n python-module-%name
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%name
%python3_sitelibdir/*
%endif

%changelog
* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt4.git20141119.1.1
- NMU: rebuild with new lua 5.1

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.0-alt4.git20141119.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sun Oct 04 2015 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt4.git20141119
- Rebuilt for new gcc5 C++11 ABI.

* Mon Jul 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt3.git20141119
- Rebuilt with gcc5

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt2.git20141119
- New snapshot

* Wed Jul 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt2.git20140615
- New snapshot

* Sat Jun 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt2.git20140516
- Rebuilt with wxGTK3.1

* Thu May 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.git20140516
- Version 1.3.0

* Wed Nov 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt2.git20130909
- Rebuilt with wxGTK3.0

* Wed Nov 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.git20130909
- New snapshot

* Fri Jun 21 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.git20130512
- New snapshot

* Mon Apr 01 2013 Aleksey Avdeev <solo@altlinux.ru> 1.2.1-alt1.git20130117
- Version 1.2.1 (12a914462f8f621ca4b21101abecd424593d96aa)

* Tue Mar 26 2013 Aleksey Avdeev <solo@altlinux.ru> 1.2.0-alt1.git20120714.1
- Rebuild with Python-3.3

* Tue Sep 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.git20120714
- Version 1.2.0

* Thu Aug 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt3
- Rebuilt with wxGTK2.9 2.9.5

* Fri May 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt2
- Rebuilt with new wxGTK 2.9
- Extracted python module into separate package
- Added module for Python 3

* Thu Dec 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Version 1.1.1
- Enabled docs

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt1.1
- Rebuild with Python-2.7

* Sun Aug 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Version 1.1.0

* Tue Jul 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt6
- Rebuilt with updated wxGTK2.9

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt5
- Rebuilt with wxGTK2.9 2.9.2-alt1.svn20110322

* Mon Mar 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt4
- Rebuilt for debuginfo

* Sat Nov 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt3
- Rebuilt with wxGTK2.9 2.9.2

* Tue Oct 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt2
- Rebuilt for soname set-versions

* Mon Oct 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1
- Version 0.9.4 (ALT #24259)

* Wed Jan 28 2009 Pavel V. Solntsev <p_solntsev@altlinux.org> 0.8.6-alt2
- Clean up spec file

* Sun Sep 21 2008 Pavel V. Solntsev <p_solntsev@altlinux.org> 0.8.6-alt1
- First build package for ALT Linux Team. 

