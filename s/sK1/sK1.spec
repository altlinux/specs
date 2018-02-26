%define pre pre
%define svn _rev730

Name: sK1
Version: 0.9.1
Release: alt2.1.1.1

Summary: Vector graphics editor

License: GPL
Group: Graphics
Url: http://www.sk1project.org/modules.php?name=Products&product=sk1

Packager: Vitaly Lipatov <lav@altlinux.ru>

# svn co https://sk1.svn.sourceforge.net/svnroot/sk1/trunk/sK1 sK1
#Source: %name-%version.tar.bz2
Source: http://sk1project.org/downloads/sk1/0.9.0/sk1-%version%pre%svn.tar.gz
Source1: %name.desktop
#Patch: %name.patch

# FIXME:
%add_python_req_skip Sketch _sketch pax

# Automatically added by buildreq on Sun May 17 2009
BuildRequires: libcairo-devel liblcms-devel python-devel tk-devel zlib-devel

BuildPreReq: libXext-devel

Requires: zenity python-module-lcms python-module-imaging

%description
sK1 is an open source vector graphics editor similar to CorelDRAW,
Adobe Illustrator, or Freehand.
First of all sK1 is oriented for PostScript processing.

%prep
%setup -n %name-%version%pre
#%patch

%build
%python_build

%install
%python_install
install -pDm644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

#post
#update_menus

#postun
#clean_menus

# It is the file in the package named Thumbs.db or Thumbs.db.gz, 
# which is normally a Windows image thumbnail database. 
# Such databases are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete

%files
%_bindir/sk1
%_desktopdir/%name.desktop
%python_sitelibdir/sk1/

%changelog
* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.1-alt2.1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.1-alt2.1.1
- Rebuild with Python-2.7

* Wed Aug 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt2.1
- Fixed build

* Wed Apr 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.1-alt2
- fix build

* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * windows-thumbnail-database-in-package for sK1
  * postclean-05-filetriggers for spec file

* Fri Oct 16 2009 Michael Shigorin <mike@altlinux.org> 0.9.1-alt1
- 0.9.1pre_rev730 (ALT#18891)

* Sun May 17 2009 Vitaly Lipatov <lav@altlinux.ru> 0.9.0-alt1
- release 0.9.0 (with rpmrb script)
- fix bug #18185

* Wed May 21 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt0.1rev422
- new revision 422

* Thu May 01 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt0.1rev390
- revision 390
- add zenity req
- drop python 2.4 compat patch

* Wed Jan 02 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt0.1beta2
- initial build for ALT Linux Sisyphus
