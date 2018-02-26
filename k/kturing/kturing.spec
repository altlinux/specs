%undefine __libtoolize

Summary: A graphical Turing machine implementation
Name:    kturing
Version: 0.4
Release: alt7

License: GPL
Group:   Education
Url:     http://kturing.sourceforge.net/
Source:  http://prdownloads.sourceforge.net/%name/%name-%version.tar.gz
Patch1:	 %name-gcc43.patch

# Automatically added by buildreq on Tue Apr 05 2011
# optimized out: fontconfig kdelibs kdelibs-devel libICE-devel libSM-devel libX11-devel libXext-devel libXt-devel libpng-devel libqt3-devel libqt3-settings libstdc++-devel libtqt-devel pkg-config xorg-xproto-devel zlib-devel
BuildRequires: chrpath gcc-c++ imake kdepim-devel kdepim-libs libjpeg-devel xml-utils xorg-cf-files

%description
KDE-based version of graphical Turing machine implementation.

%prep
%setup
#rm -f admin/config.guess admin/config.sub admin/ltmain.sh kturing/TAGS kturing/*gui*.[ch]*
%patch1 -p1
touch kturing/*ui
sed -i 's/automake\*1\.5/automake-1.5/g' admin/cvs.sh
make -f admin/Makefile.common cvs

%build
%add_optflags -I%_includedir/tqtinterface
export PATH="%_K3bindir:$PATH"
%configure --disable-rpath \
    --prefix=%prefix \
    --without-arts
%make
chrpath -d kturing/kturing

%install
%make install DESTDIR=%buildroot kde_htmldir=%_K3doc
%K3find_lang --with-kde %name

%files -f %name.lang
%doc README TODO Examples
%_bindir/%name
%_datadir/applnk/Applications/%name.desktop
%_iconsdir/*/*/apps/%name.*

%changelog
* Tue May 29 2012 Fr. Br. George <george@altlinux.ru> 0.4-alt7
Silly automake check fix

* Fri Jan 20 2012 Fr. Br. George <george@altlinux.ru> 0.4-alt6
- Fix build

* Tue Apr 05 2011 Fr. Br. George <george@altlinux.ru> 0.4-alt5
- Forbidden requires eliminated

* Fri Mar 04 2011 Sergey V Turchin <zerg@altlinux.org> 0.4-alt4.1
- fix to build

* Tue Jan 18 2011 Fr. Br. George <george@altlinux.ru> 0.4-alt4
- Resurrect from orphaned

* Tue Oct 28 2008 Fr. Br. George <george@altlinux.ru> 0.4-alt3
- GCC4.3 build fix

* Fri Oct 26 2007 Fr. Br. George <george@altlinux.ru> 0.4-alt2
- Fixed x86_64 configure

* Tue Oct 23 2007 Fr. Br. George <george@altlinux.ru> 0.4-alt1
- Initial build for ALT

