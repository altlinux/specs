Name: libps
Version: 0.4.5
Release: alt1

Summary: Library for creating PostScript files
License: LGPLv2+
Group: System/Libraries

Url: http://pslib.sourceforge.net/
Source: http://download.sourceforge.net/pslib/pslib-%version.tar.gz

# Automatically added by buildreq on Mon Apr 04 2011
BuildRequires: docbook-to-man docbook-utils intltool libgif-devel libjpeg-devel libpng-devel libtiff-devel

%description
This library allows to create multi page PostScript documents. There are
functions for drawing lines, arcs, rectangles, curves, etc. PSlib also provides
very sophisticated functions for text output including hyphenation and kerning.

%package devel
Summary: Libraries, includes, etc. to develop PostScript applications
Group: System/Libraries
Requires: %name = %version-%release

%description devel
Libraries, include files, etc you can use to develop PostScript applications.

%prep
%setup -n pslib-%version

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%find_lang pslib

%files -f pslib.lang
%doc AUTHORS README data/*.ps
%_libdir/*.so.*
%_datadir/pslib

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Mon Apr 04 2011 Victor Forsiuk <force@altlinux.org> 0.4.5-alt1
- 0.4.5

* Tue Jun 16 2009 Victor Forsyuk <force@altlinux.org> 0.4.1-alt3
- Fix FTBFS due to conflicting definitions.

* Tue Dec 16 2008 Victor Forsyuk <force@altlinux.org> 0.4.1-alt2
- Remove obsolete ldconfig calls.

* Tue Jan 22 2008 Victor Forsyuk <force@altlinux.org> 0.4.1-alt1
- 0.4.1
- Build and package man pages (so build requires docbook-to-man).

* Tue Oct 30 2007 Victor Forsyuk <force@altlinux.org> 0.4.0-alt1
- 0.4.0

* Fri Jul 29 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.2.6-alt1
- 0.2.6

* Sun Jan 23 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.2.5-alt1
- 0.2.5

* Thu Jul 22 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.2.4-alt1
- new version
- free gstate resource list
- create unique template names
- check for errors when registering a resource

* Sat Jul 17 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.2.3-alt1
- new version
- encoding of images can be hex or ascii85
- renamed PS_setoverprint() PS_setoverprintmode()
- support for graphic states (PS_create_gstate(), PS_set_gstate())
- support for shading patterns (PS_shading(), PS_shfill(), PS_shading_pattern())
- fixed bug when calling PS_save(), take over old gstate
- can now read jpeg images
- image data is being ascii85 encoded to reduce file size
- fixed bug in PS_fill_stroke(), invalid PostScript because of missing space

* Sun Jul 4 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.2.2-alt1
- new version

* Fri Jun 18 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.2.1-alt1
- 0.2.1
- many man page updates

* Tue Jun 8 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.2.0-alt1
- ps_fontenc_code() returns a '?' if the glyph could not be found
- fixed many errors in handling of font encoding
- replaced unsafe strcpy() by strncpy() and enlarged buffers in  ps_afm.c
- fixed man pages
- fixed first line of postscript document

* Tue May 25 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.1.15-alt1
- First version of RPM package

