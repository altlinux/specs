Name: qalculate-kde4
Version: 0.9.7
Release: alt1.git20140210
Summary: A very versatile desktop calculator - KDE4 version
License: GPLv2
Group: Office
Url: http://sourceforge.net/projects/qalculate/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://git.code.sf.net/p/qalculate/qalculate-kde4
Source: %name-%version.tar

BuildPreReq: gcc-c++ cmake libqt4-devel kde4-devel qt4-glib-devel
BuildPreReq: libqt4-sql-sqlite2 libqt4-sql-sqlite3
BuildPreReq: libqt4-assistant-devel libXxf86misc-devel
BuildPreReq: libqalculate-devel

%description
Qalculate! is a modern multi-purpose desktop calculator for GNU/Linux
(and now ported to Mac). It is small and simple to use but with much
power underneath. Features include customizable functions, units,
arbitrary precision, plotting, and a user-friendly interface.

This is KDE4 graphical interface for Qalculate!

%prep
%setup

%build
cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_Fortran_FLAGS:STRING="%optflags" \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DKDE4_ENABLE_HTMLHANDBOOK:BOOL=ON \
	.
%make_build VERBOSE=1

pushd doc/en/qalculate_kde
%make htmlhandbook
popd

%install
%makeinstall_std

install -m644 doc/en/qalculate_kde/*.html \
	%buildroot%_docdir/HTML/en/qalculate_kde/

%files
%doc AUTHORS ChangeLog TODO
%doc %_docdir/HTML/en/qalculate_kde
%_bindir/*
%_desktopdir/*
%_datadir/apps
%_iconsdir/hicolor/*/*/*

%changelog
* Fri Sep 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt1.git20140210
- Initial build for Sisyphus

