Name: ttfautohint
Version: 1.1
Release: alt1
Summary: A tool to auto-hint TrueType fonts
License: FTL, GPLv2+
Group: File tools
Url: http://www.freetype.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: libfreetype-devel libqt4-devel libharfbuzz-devel
BuildPreReq: gcc-c++ inkscape pandoc texlive-xetex ImageMagick

%description
ttfautohint - a tool to auto-hint TrueType fonts, based on FreeType's
auto-hinting engine (still under development).

%package docs
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch

%description docs
ttfautohint - a tool to auto-hint TrueType fonts, based on FreeType's
auto-hinting engine (still under development).

This package contains documentation for %name.

%prep
%setup

%build
%autoreconf
export DISPLAY=:0.0
%configure \
	--enable-threads=posix \
	--disable-rpath \
	--enable-static=no \
	--with-qt=%_qt4dir/bin \
	--with-doc
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog COPYING *.TXT NEWS README THANKS TODO
%_bindir/*
%_man1dir/*

%files docs
%_docdir/%name

%changelog
* Fri Sep 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

