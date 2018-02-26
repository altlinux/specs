Name: gnome-peercast
Version: 0.5.4
Release: alt3.qa2

Summary: Graphical user interface for PeerCast

License: GPL
Group: Video

Url: http://takuo.jp/gnome-peercast/
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://ftp.debian.org/debian/pool/main/g/gnome-peercast/%{name}_%version.orig.tar.bz2
Patch: gnome-peercast-0.5.4.debian.patch
Patch1: gnome-peercast-0.5.4-fix.patch
Patch2: gnome-peercast-0.5.4-alt-DSO.patch

Requires(post): GConf2
BuildPreReq: GConf2

# manually removed: gcc-fortran 
# Automatically added by buildreq on Sun Jan 18 2009
BuildRequires: gcc-c++ libglade-devel libgnomeui-devel perl-XML-Parser

%description
Graphical user interface for PeerCast.
Core source is based on peercast v0.1217 and applied some extention patches.
So, GNOME PeerCast includes full features of PeerCast v0.1217.

%prep
%setup -q
%patch -p1
%patch1
%patch2 -p2

%build
%configure --disable-static
%make_build

%install
%makeinstall_std
%find_lang %name
rm -f %buildroot%_libdir/*.a

# The package contains a CVS/.svn/.git/.hg/.bzr/_MTN directory of revision control system.
# It was most likely included by accident since CVS/.svn/.hg/... etc. directories 
# usually don't belong in releases. 
# When packaging a CVS/SVN snapshot, export from CVS/SVN rather than use a checkout.
find $RPM_BUILD_ROOT -type d \( -name 'CVS' -o -name '.svn' -o -name '.git' -o -name '.hg' -o -name '.bzr' -o -name '_MTN' \) -print -exec rm -rf {} \; ||:
# the find below is useful in case those CVS/.svn/.git/.hg/.bzr/_MTN directory is added as %%doc
find . -type d \( -name 'CVS' -o -name '.svn' -o -name '.git' -o -name '.hg' -o -name '.bzr' -o -name '_MTN' \) -print -exec rm -rf {} \; ||:

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %name
fi

%files -f %name.lang
%doc README ChangeLog AUTHORS
%_sysconfdir/gconf/schemas/*.schemas
%_bindir/*
%_desktopdir/*
%_datadir/%name/
%_pixmapsdir/*

%changelog
* Thu Jun 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.4-alt3.qa2
- Fixed build

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.5.4-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * pkg-contains-cvs-or-svn-control-dir for gnome-peercast
  * postclean-05-filetriggers for spec file

* Sun Nov 08 2009 Vitaly Lipatov <lav@altlinux.ru> 0.5.4-alt3
- fix build

* Sun Jan 18 2009 Vitaly Lipatov <lav@altlinux.ru> 0.5.4-alt2
- update buildreqs

* Sun Mar 09 2008 Vitaly Lipatov <lav@altlinux.ru> 0.5.4-alt1
- initial build for ALT Linux Sisyphus

