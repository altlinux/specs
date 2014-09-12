Name: guitone
Version: 1.0
Release: alt1.dev.mtn20111125
Summary: Qt-based, cross-platform graphical user interface for monotone
License: LGPLv3+
Group: Development/Tools
Url: https://guitone.thomaskeller.biz/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# get: mtn clone mtn://code.monotone.ca/guitone?net.venge.monotone.guitone
# update: mtn pull --update
Source: %name-%version.tar

BuildPreReq: libqt4-devel libgraphviz-frozen-devel monotone gcc-c++
BuildPreReq: libexpat-devel libltdl-devel

Requires: monotone

%description
Guitone is a Qt-based, cross-platform graphical user interface for the
distributed version control system monotone. It aims towards a full
implementation of the monotone automation interface and is especially
targeted at beginners.

%prep
%setup

%build
export PATH=$PATH:%_qt4dir/bin
qmake \
	QMAKE_CXXFLAGS="%optflags" \
	%name.pro
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

%files
%doc NEWS README* notes/*
%_bindir/*
%_desktopdir/*
%_datadir/mime/packages/*
%_pixmapsdir/*

%changelog
* Fri Sep 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.dev.mtn20111125
- Initial build for Sisyphus

