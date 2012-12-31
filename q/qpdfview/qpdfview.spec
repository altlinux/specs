Name: qpdfview
Version: 0.3.7
Release: alt1
Summary: Tabbed PDF viewer using the poppler library
License: GPLv2
Group: Office
Url: https://launchpad.net/qpdfview
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: libpoppler-devel libqt4-devel libcups-devel
BuildPreReq: libpoppler-qt4-devel gcc-c++

%description
qpdfview is a tabbed PDF viewer using the poppler library.

%prep
%setup

%build
export PATH=%_qt4dir/bin:$PATH
qmake
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

install -d %buildroot%_liconsdir
install -d %buildroot%_miconsdir
install -d %buildroot%_niconsdir

ln -s %_datadir/%name/%name.svg \
	%buildroot%_liconsdir
ln -s %_datadir/%name/%name.svg \
	%buildroot%_miconsdir
ln -s %_datadir/%name/%name.svg \
	%buildroot%_niconsdir

%files
%doc CHANGES CONTRIBUTORS README TODO
%_bindir/*
%_man1dir/*
%_desktopdir/*
%_datadir/%name
%_liconsdir/*
%_miconsdir/*
%_niconsdir/*

%changelog
* Mon Dec 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.7-alt1
- Version 0.3.7 (ALT #28294)

* Sat Dec 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt1
- Version 0.3.6 (ALT #28153)

* Fri Oct 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1
- Initial build for Sisyphus (ALT #27871)

