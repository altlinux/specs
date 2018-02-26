Name: xfdiff
Version: 4.5.0
Release: alt4.2

Summary: Patch Manager and Difference Viewer
Group: Text tools
License: GPL

Url: http://xffm.sourceforge.net/xfdiff.html

Source: %name-%version.tar.gz

Packager: Eugene Ostapets <eostapets@altlinux.ru>

BuildPreReq: gtk-doc intltool chrpath
# Automatically added by buildreq on Tue Nov 07 2006
BuildRequires: gcc-c++ libgtk+2-devel libtubo-devel perl-XML-Parser

%description
Xfdiff 4.5.0 is graphic interface to the GNU diff and patch commands. With this utility, 
you can view differences side by side for files or directories. You can also view differences 
that applying a patch file would imply, without applying the patch. You can also apply 
patches to the hard disc or create patch files for differences between files or directories. 
All-in-all, a handy utility for lazy chaps who don't want to type the diff command. 

%prep
%setup -q

%build
intltoolize --force
libtoolize --force --copy
aclocal -I m4
automake -f -a -c
autoconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

chrpath -d %buildroot%_bindir/xfdiff4

%find_lang %name

%files -f %name.lang
%doc AUTHORS
%_bindir/*
%dir %_datadir/xffm/xfdiff/
%_datadir/xffm/xfdiff/
%_desktopdir/Xfdiff.desktop
%_pkgconfigdir/xfdiff.pc
%_pixmapsdir/xfdiff-icon.png

%changelog
* Tue Feb 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.0-alt4.2
- Removed bad RPATH

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 4.5.0-alt4.1
- NMU (by repocop): the following fixes applied:
  * update_menus for xfdiff

* Wed Jan 09 2008 Eugene Ostapets <eostapets@altlinux.ru> 4.5.0-alt4
- fix build with new autotools

* Mon Nov 06 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.5.0-alt3
- cleanup spec

* Mon Jul 24 2006 Igor Zubkov <icesik@altlinux.ru> 4.5.0-alt2
- add url

* Mon Jul 17 2006 Igor Zubkov <icesik@altlinux.ru> 4.5.0-alt1
- Initial build for Sisyphus
