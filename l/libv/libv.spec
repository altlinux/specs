%define origname v
%set_verify_elf_method unresolved=relaxed

Name:		libv
Version:	1.90
Release:	alt9
Summary:	V is a free, multiple platform C++ graphical user interface framework
License:	LGPL
Group:		Development/C++
Source0:	%origname-%version.tar.bz2
URL:		http://www.objectcentral.com/
Packager:	Evgeny Sinelnikov <sin@altlinux.ru>
# Automatically added by buildreq on Thu Oct 25 2007
BuildRequires: gcc-c++ libXaw-devel libXmu-devel

BuildRequires:	lesstif-devel, libXext-devel, libGLw-devel, libGLU-devel

%description
V is a free, multiple platform C++ graphical user interface framework designed
to make it the easiest way to write C++ GUI applications available -- 
commercial, shareware, or freeware. V is available for X Athena, 
X Motif/Lesstif, all Windows platforms, and now including OS/2.

%package devel
Summary:        Development header files for %name
Group:          Development/C++
Requires:       %name = %version

%description devel
Libraries, include files and other resources you can use to develop
%name applications.

%prep
%setup -q -n home/vgui

%build
perl -pi -e "s|^HOMEV\s*=.*|HOMEV=`pwd`|" Config.mk
CFLAGS=-I. make

%install
mkdir -p %buildroot%_libdir
mkdir -p %buildroot%_includedir

cp lib/lib* %buildroot%_libdir
rm -f %buildroot%_libdir/libVx.so
ln -s libVx.so.1.90 %buildroot%_libdir/libVx.so
ln -s libVxgl.so.1.90 %buildroot%_libdir/libVxgl.so

cp -r includex/* %buildroot%_includedir

perl -pi -e "s|\r\n|\n|" %buildroot%_includedir/v/*
perl -pi -e "s|\r\n|\n|"  ../help/vrefman/* Readme copying.lib

# It is the file in the package named Thumbs.db or Thumbs.db.gz, 
# which is normally a Windows image thumbnail database. 
# Such databases are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find %buildroot \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete

%files
%doc Readme copying.lib
%_libdir/*.so.*

%files devel
%doc ../help/vrefman/*
%_includedir/%origname
%_libdir/*.so

%changelog
* Mon May 02 2011 Evgeny Sinelnikov <sin@altlinux.ru> 1.90-alt9
- Rebuild with internal libGLw implementation of deprecated symbols

* Mon May 02 2011 Evgeny Sinelnikov <sin@altlinux.ru> 1.90-alt8
- Rebuilt with xorg-server-1.10
- Fixed build dependecies

* Sat Apr 03 2010 Evgeny Sinelnikov <sin@altlinux.ru> 1.90-alt7
- Fixed link problems with libVxgl

* Sun Mar 28 2010 Evgeny Sinelnikov <sin@altlinux.ru> 1.90-alt6
- Rebuild with rename symbol:
  glwDrawingAreaWidgetClass -> glwMDrawingAreaWidgetClass

* Mon Jan 04 2010 Evgeny Sinelnikov <sin@altlinux.ru> 1.90-alt5
- The following repocop fixes applied:
 * post_ldconfig for libv
 * postun_ldconfig for libv
 * windows-thumbnail-database-in-package for libv-devel

* Mon Nov 05 2007 Evgeny Sinelnikov <sin@altlinux.ru> 1.90-alt4
- Avoid patch using via gear
- Change max size of ComboBox to 64

* Wed Oct 31 2007 Evgeny Sinelnikov <sin@altlinux.ru> 1.90-alt3
- Build with lesstif-0.95-alt2 on x86_64

* Mon Oct 29 2007 Evgeny Sinelnikov <sin@altlinux.ru> 1.90-alt2
- Rebuild with lesstif-0.95-alt2

* Wed Oct 24 2007 Evgeny Sinelnikov <sin@altlinux.ru> 1.90-alt1
- Initial release

