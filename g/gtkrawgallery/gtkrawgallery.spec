Name: gtkrawgallery
Version: 0.9.61
Release: alt1.qa1.1

Summary: A photo manager and camera raw file processor
License: GPLv2
Group: Graphics

Url: http://sourceforge.net/projects/gtkrawgallery/
Source: http://downloads.sourceforge.net/gtkrawgallery/gtkrawgallery-%version.tar.bz2

BuildArch: noarch

# Automatically added by buildreq on Thu Apr 14 2011 (-bi)
BuildRequires: python-devel

Requires: dcraw, perl-Image-ExifTool

%description
GTKRawGallery is an image viewer with support for camera raw files. It is
also an album manager and conversion tool.

%prep
%setup
subst 's/\r//g' gtkrg_loader.py gtkrg_profiles.py gtkrg_smtp.py uninstall_gtkrawgallery.py

%build

%install
%python_build_install
rm -f %buildroot%_datadir/gtkrawgallery/liblcms*
rm -f %buildroot%python_sitelibdir/uninstall*

# It is the file in the package named Thumbs.db or Thumbs.db.gz, 
# which is normally a Windows image thumbnail database. 
# Such databases are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete

%files
%_bindir/gtkrawgallery
%_datadir/gtkrawgallery
%_desktopdir/*
%_pixmapsdir/*
%python_sitelibdir/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.61-alt1.qa1.1
- Rebuild with Python-2.7

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.61-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * windows-thumbnail-database-in-package for gtkrawgallery

* Thu Apr 14 2011 Victor Forsiuk <force@altlinux.org> 0.9.61-alt1
- 0.9.61

* Mon Sep 27 2010 Victor Forsiuk <force@altlinux.org> 0.9.6-alt1
- 0.9.6

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt1.1
- Rebuilt with python 2.6

* Fri Nov 13 2009 Victor Forsyuk <force@altlinux.org> 0.9.5-alt1
- Initial build.
