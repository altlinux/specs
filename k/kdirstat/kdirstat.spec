Name: 	kdirstat
Version: 2.5.3
Release: alt3.1
Summary: Graphical Directory Statistics for Used Disk Space
License: GPLv2
Group: File tools
URL: http://kdirstat.sourceforge.net/
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source0: %name-%version.tar.bz2
Patch0:           kdirstat-2.5.3-desktop.patch
Patch1:           kdirstat-2.5.3-gcc43.patch


BuildPreReq: perl-Encode perl-URI

# Automatically added by buildreq on Sun Feb 17 2008
BuildRequires: gcc-c++ imake kdelibs-devel libjpeg-devel libqt3-devel
BuildRequires: xml-utils xorg-cf-files perl-Encode desktop-file-utils

%description
KDirStat (KDE Directory Statistics) is a utility program that sums up
disk usage for directory trees - very much like the Unix 'du' command.
It can also help you clean up used space.

%prep
%setup -q -n %name-%version

%patch0 -p0 -b kdirstat.desktop
%patch1 -p1 -b .gcc43


%build
%configure --without-arts
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build CXXFLAGS="-I%_includedir/tqtinterface"

%install
rm -rf %buildroot
%makeinstall

%find_lang --with-kde %name

%files -f %name.lang

%doc COPYING AUTHORS ChangeLog TODO README
%_bindir/kdirstat
%_bindir/kdirstat-cache-writer
%_datadir/apps/kdirstat
%_datadir/appl*/*/kdirstat*
%_datadir/doc/HTML/*/kdirstat/
#%dir %_datadir/icons/hicolor/16x16
#%dir %_datadir/icons/hicolor/16x16/apps
#%dir %_datadir/icons/hicolor/32x32
#%dir %_datadir/icons/hicolor/32x32/apps
#%dir %_datadir/icons/locolor/16x16/apps
#%dir %_datadir/icons/locolor/32x32/apps
%_datadir/icons/??color/??x??/*/kdirstat*
%dir %_datadir/apps/kconf_update
%_datadir/apps/kconf_update/kdirstat.upd
%_datadir/apps/kconf_update/fix_move_to_trash_bin.pl
# TODO: How to use %find_lang here?
%_datadir/locale/??/LC_MESSAGES/kdirstat.mo

%changelog
* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.3-alt3.1
- Removed bad RPATH

* Sun Apr 17 2011 Ilya Mashkin <oddity at altlinux dot ru> 2.5.3-alt3
- fix build

* Mon Dec 22 2008 Ilya Mashkin <oddity@altlinux.ru> 2.5.3-alt2
- fix build gcc4.3
- fix desktop file
- add find_lang macro

* Sun Feb 17 2008 Eugine V. Kosenko <maverik@altlinux.ru> 2.5.3-alt1
- Initial Build

