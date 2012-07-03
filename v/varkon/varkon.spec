%define srcname Varkon
Summary: VARKON - a free CAD system
Name: varkon
Version: 1.19D
Release: alt2.1.qa1
License: GPL
Group: Editors
Packager: Boris Savelev <boris@altlinux.org>
Source: %name-%version.tar
Patch: 0001-fix-buffer_overflow.patch
Url: http://varkon.sourceforge.net/

# Automatically added by buildreq on Tue Jun 30 2009
BuildRequires: libGL-devel libXext-devel libXpm-devel libtiff-devel libunixODBC unzip
BuildPreReq: libGLU-devel
BuildRequires: desktop-file-utils

%description
VARKON - a free CAD system and high level development tool for
Engineering.

%package user-manual
Summary: %name user manual
Group: Documentation
BuildArch: noarch

%description user-manual
User manual for %name

%package programmer-manual
Summary: %name programmer manual
Group: Documentation
BuildArch: noarch

%description programmer-manual
Programmer manual for %name

%prep
%setup
%patch -p1

%build
export VARKON_ROOT="$(pwd)"
export RPM_OPT_FLAGS="%optflags"
%make -C sources

%install
mkdir -p %buildroot{%_bindir,%_desktopdir,%_pixmapsdir,%_man1dir}
mkdir -p %buildroot{%_sysconfdir,%_libdir,%_datadir}/%name
install -m755 %name.sh %buildroot%_bindir/%name
subst "s|@libdir@|%_libdir|g" %buildroot%_bindir/%name
ln -s %_libdir/%name/mbsc %buildroot%_bindir/mbsc
# Configuration
cp -a cnf %buildroot%_sysconfdir/%name
rm -Rf %buildroot%_sysconfdir/%name/cnf/Ini_win
cp -a mdf %buildroot%_sysconfdir/%name
rm -f %buildroot%_sysconfdir/%name/mdf/english/texts.INC_OLD
cp -a %{name}rc %buildroot%_sysconfdir/%name
# dummy help pages
mkdir -p %buildroot%_datadir/%name/man/{v_man,m_man}
unzip -o m_man.zip -d man
unzip -o v_man.zip -d man
cp -a man/*.htm %buildroot%_datadir/%name/man
cp -a man/v_man/* %buildroot%_datadir/%name/man/v_man
cp -a man/m_man/* %buildroot%_datadir/%name/man/m_man
# shared files
cp -a erm %buildroot%_datadir/%name
cp -a lib %buildroot%_datadir/%name
cp -a bin/* %buildroot%_libdir/%name
# icon
cp -a %name.xpm %buildroot%_pixmapsdir
cp -a %name.desktop %buildroot%_desktopdir
# man
cp -a %name.1 mbsc.1 %buildroot%_man1dir
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Engineering \
	--add-category=Electronics \
	%buildroot%_desktopdir/varkon.desktop

%files
%_sysconfdir/%name
%_bindir/*
%_libdir/%name
%dir %_datadir/%name
%_datadir/%name/erm
%_datadir/%name/lib
%dir %_datadir/%name/man
%_datadir/%name/man/*.htm
%dir %_datadir/%name/man/v_man
%_datadir/%name/man/v_man/f000.*
%_datadir/%name/man/v_man/menydoc.*
%_datadir/%name/man/v_man/partdoc.*
%_pixmapsdir/*
%_man1dir/*
%_desktopdir/*

%files programmer-manual
%_datadir/%name/man/v_man/*
%exclude %_datadir/%name/man/v_man/f000.*
%exclude %_datadir/%name/man/v_man/menydoc.*
%exclude %_datadir/%name/man/v_man/partdoc.*

%files user-manual
%_datadir/%name/man/m_man

%changelog
* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.19D-alt2.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for varkon

* Wed Dec 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.19D-alt2.1
- Fixed build

* Mon Jul 20 2009 Boris Savelev <boris@altlinux.org> 1.19D-alt2
- fix build for buffer_overflow

* Tue Jun 30 2009 Boris Savelev <boris@altlinux.org> 1.19D-alt1
- initial build for ALT Linux Sisyphus
