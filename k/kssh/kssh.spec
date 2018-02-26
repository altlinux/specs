Name: kssh
Version: 0.7
Release: alt9.1

Summary: SSH frontend for KDE with many configurable options
License: GPL
Group: Networking/Other

Packager: Repocop Q. A. Robot <repocop@altlinux.org>

URL: http://sourceforge.net/projects/kssh

Source0: %name-%version.tar.bz2

Requires: openssh-clients

BuildRequires: gcc-c++ kdelibs-devel

%description
It can work as a standard KDE application that launches ssh connections
in a terminal or as a konsole session. This means that you can press in
any konsole "New Session" and then select "Secure Shell".

%prep
%setup -q

make -f admin/Makefile.common cvs

%build
export KDEDIR=%_libdir
%add_optflags -I%_includedir/tqtinterface
%K3configure \
	--disable-debug

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%K3install
mkdir -p %buildroot/%_K3xdg_apps/
mv %buildroot/%_K3applnk/Internet/%name.desktop %buildroot/%_K3xdg_apps/
echo 'Categories=Application;Network;' >> %buildroot/%_K3xdg_apps//%name.desktop

%K3find_lang --with-kde %name

%files -f %name.lang
%_K3bindir/*
%_K3apps/konsole/*.desktop
%_kde3_iconsdir/*/*/*/*.*
%_K3xdg_apps/%name.desktop
%doc README AUTHORS

%changelog
* Sat Feb 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt9.1
- Removed bad RPATH

* Fri Apr 29 2011 Sergey V Turchin <zerg@altlinux.org> 0.7-alt9
- move to alternate place

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 0.7-alt8.1
- NMU (by repocop): the following fixes applied:
  * update_menus for kssh

* Mon May 01 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.7-alt8
- fix build on x86_64 (thanks to damir@)

* Sun Apr 02 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.7-alt7
- fix build
- remove menu file, fix desktop file
- spec cleanup

* Thu Jan 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.7-alt6.1
- Rebuilt with libstdc++.so.6.

* Sun Jun 13 2004 Yehuda Ben-Yosef <ilar@altlinux.ru> 0.7-alt6
- fix requires

* Tue Jan 27 2004 Yehuda Ben-Yosef <ilar@altlinux.ru> 0.7-alt5
- fix builrequires

* Sun Dec 14 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 0.7-alt4
- rebuilding without *.la

* Wed Oct 01 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 0.7-alt3
- new buildrequires and rebuilding in hasher

* Fri Sep 20 2002 Sergey V Turchin <zerg@altlinux.ru> 0.7-alt2
- build with gcc3.2

* Mon Jun 17 2002 Yehuda Ben-Yosef <ilar@altlinux.ru> 0.7-alt1
- 0.7

- specfile cleanup

