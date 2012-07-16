Name: pdf2djvu
Version: 0.7.13
Release: alt1

Summary: PDF to DjVu converter
License: GPLv2
Group: Office
Url: http://pdf2djvu.googlecode.com/
# http://pdf2djvu.googlecode.com/files/%{name}_%version.tar.gz
Source: %name-%version.tar
Requires: djvu-utils
# Automatically added by buildreq on Fri Nov 19 2010
BuildRequires: djvu-utils fontconfig-devel gcc-c++ libGraphicsMagick-c++-devel libdjvu-devel libgomp-devel libpoppler-devel libxslt-devel pstreams

%description
pdf2djvu creates DjVu files from PDF files. It's able to extract:
- graphics,
- text layer,
- hyperlinks,
- document outline (bookmarks),
- metadata (including XMP metadata).

%prep
%setup
%configure
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc COPYING doc/changelog
%_bindir/*
%_man1dir/*

%changelog
* Mon Jul 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.13-alt1
- Version 0.7.13

* Sat Nov 26 2011 L.A. Kostis <lakostis@altlinux.ru> 0.7.11-alt1
- Updated to 0.7.11.

* Tue Apr 26 2011 Dmitry V. Levin <ldv@altlinux.org> 0.7.7-alt1
- Updated to 0.7.7.

* Fri Nov 19 2010 Dmitry V. Levin <ldv@altlinux.org> 0.7.4-alt1
- Enabled OpenMP support.
- Updated build requirements.
- Rebuilt for libpoppler.so.7.

* Mon Aug 16 2010 L.A. Kostis <lakostis@altlinux.ru> 0.7.4-alt0.1
- 0.7.4.

* Sat Jan 23 2010 L.A. Kostis <lakostis@altlinux.ru> 0.6.0-alt0.1.1
- Rebuild w/ new GraphicsMagick.

* Thu Nov 05 2009 L.A. Kostis <lakostis@altlinux.ru> 0.6.0-alt0.1
- 0.6.0.
- Optimize buildrequires, .spec cleanup.
- Change packager.

* Sun Mar 15 2009 L.A. Kostis <lakostis@altlinux.ru> 0.4.12-alt2.1
- NMU: rebuild with new libdjvu.

* Thu Mar 12 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.4.12-alt2
- Rebuild with new libdjvu

* Sat Sep 20 2008 Vladimir Scherbaev <vladimir@altlinux.org> 0.4.12-alt1
- Initial build
