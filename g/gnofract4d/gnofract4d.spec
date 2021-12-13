%define _unpackaged_files_terminate_build 1

Name: gnofract4d
Version: 4.3
Release: alt1

Summary: Gnofract 4D is a Gnome-based program to draw fractals

License: GPLv2
Group: Sciences/Mathematics
Url: http://gnofract4d.sourceforge.net/

# Source-git: https://github.com/edyoung/gnofract4d.git
Source: %name-%version.tar

# This *really* requires gcc at runtime!
Requires: gcc

# Typical environment for GNOME program
#Requires(post): GConf2
#Requires(post,postun): scrollkeeper
#Requires(post,postun): desktop-file-utils
#BuildPreReq: GConf2
#BuildPreReq: desktop-file-utils 

#add_python_req_skip fract4d _lsprof cProfile fractutils frm_docbook kid
%add_python3_req_skip frm_docbook

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ libGConf-devel libjpeg-devel libpng-devel
BuildRequires: python3-devel

%description
Gnofract 4D is a Gnome-based program to draw fractals. What sets it apart from
other fractal programs (and makes it "4D") is the way that it treats the
Mandelbrot and Julia sets as different views of the same four-dimensional
fractal object. This allows you to generate images which are a cross between
the two sets and explore their inter-relationships.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

# drop all tests
rm -rf %buildroot%python3_sitelibdir/fract*/test*

rm -rf %buildroot/usr/share/doc/gnofract4d

%find_lang %name --with-gnome

%files -f %name.lang
%doc README.md
%_bindir/%name
%python3_sitelibdir/fract4d/
%python3_sitelibdir/fract4d_compiler/
%python3_sitelibdir/fract4dgui/
%python3_sitelibdir/*.egg-info
%_datadir/%name/
%_datadir/mime/packages/*
%_pixmapsdir/*
%_iconsdir/hicolor/*/apps/*.png
%_desktopdir/*

%changelog
* Mon Dec 13 2021 Vitaly Lipatov <lav@altlinux.ru> 4.3-alt1
- new version 4.3 (with rpmrb script)

* Fri Sep 14 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.1-alt1
- Updated to upstream version 4.0.1.

* Sun Feb 25 2018 Vitaly Lipatov <lav@altlinux.ru> 3.14.1-alt2.git201802025
- Snapshot from git
- drop all tests and python gst using

* Thu Aug 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.14.1-alt1.git20130402
- Snapshot from git

* Fri Jun 21 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.14.1-alt1
- Version 3.14.1

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.14-alt2
- Rebuilt with libpng15

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.14-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.14-alt1.1
- Rebuild with Python-2.7

* Mon Sep 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.14-alt1
- Version 3.14

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 3.13-alt5.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * altlinux-policy-obsolete-buildreq for gnofract4d

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13-alt5
- Rebuilt for debuginfo

* Sat Nov 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13-alt4
- Fixed categories in desktop file (thnx viy@)

* Thu Nov 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13-alt3
- Fixed desktop file

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13-alt2
- Disabled build with rpm-build-compat

* Fri Oct 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13-alt1
- Version 3.13

* Sat Mar 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10-alt2
- Rebuilt for pygtk_git instead of pygtk

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10-alt1.1
- Rebuilt with python 2.6

* Sun Dec 21 2008 Vitaly Lipatov <lav@altlinux.ru> 3.10-alt1
- new version 3.10 (with rpmrb script)
- remove post/preun scripts (fixes bug#18273 too)

* Sat Jul 05 2008 Vitaly Lipatov <lav@altlinux.ru> 3.9-alt1
- new version 3.9 (with rpmrb script)
- add rpm-build-compat requires

* Mon Feb 18 2008 Vitaly Lipatov <lav@altlinux.ru> 3.8-alt1
- new version 3.8
- update buildreq
- build with python 2.5

* Sun Dec 24 2006 Vitaly Lipatov <lav@altlinux.ru> 3.2-alt0.1
- new version 3.2, fix packager
- cleanup spec, remove Debian menu

* Mon Jun 19 2006 Vitaly Lipatov <lav@altlinux.ru> 2.14-alt0.2
- fix requires

* Mon May 29 2006 Vitaly Lipatov <lav@altlinux.ru> 2.14-alt0.1
- new version 2.14
- update buildreq

* Mon Sep 05 2005 Vitaly Lipatov <lav@altlinux.ru> 2.9-alt1
- first build for ALT Linux Sisyphus

* Sun Feb 13 2005 Throsten Leemhuis <fedora at leemhuis dot info> 0:2.6-2
- "sed -i s|%_libdir/|%%{_libdir}|g setup.cfg" on x86_64

* Tue Feb 01 2005 Panu Matilainen <pmatilai@welho.com> 0:2.6-1
- update to 2.6
- drop epoch 0 and fedora.us release tag
- run update-desktop-database on post+postun

* Sun Oct 03 2004 Panu Matilainen <pmatilai@welho.com> 0:2.1-0.fdr.1
- update to 2.1

* Tue Jul 06 2004 Panu Matilainen <pmatilai@welho.com> 0:2.0-0.fdr.1
- update to 2.0
- quite a few dependency changes because of switch to python etc

* Mon May 31 2004 Panu Matilainen <pmatilai@welho.com> 0:1.9-0.fdr.3
- fix build against newer gtk (gtk-buildfix patch)

* Tue Dec 23 2003 Panu Matilainen <pmatilai@welho.com> 0:1.9-0.fdr.2
- address issues in #1114
- huh, this requires g++ to run...

* Mon Dec 15 2003 Panu Matilainen <pmatilai@welho.com> 0:1.9-0.fdr.1
- update to 1.9
- drop patch (no longer needed to build)
- add translations now that there is one

* Sun Dec 07 2003 Panu Matilainen <pmatilai@welho.com> 0:1.8-0.fdr.1
- Initial Fedora packaging.
