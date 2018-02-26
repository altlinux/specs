%define lib_name	libaiksaurus
%define lib_namegtk	%{lib_name}-gtk

Name: aiksaurus
Version: 1.2.1
Release: alt4.qa4

Summary: An English-language thesaurus library

License: GPL
Group: Text tools
Url: http://sourceforge.net/projects/aiksaurus/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%name-%version.tar.bz2
Source1: %name.png
Source2: %name.desktop
Patch: %name-gcc43.patch

Requires: %name-data

# manually removed: gcc-g77
# Automatically added by buildreq on Sun Jun 22 2008
BuildRequires: gcc-c++ libgtk+2-devel
BuildRequires: desktop-file-utils

%description
Aiksaurus is an English-language thesaurus library that can be
embedded in word processors, email composers, and other authoring
software to provide thesaurus capabilities.
This package contains a basic command line thesaurus program.

Install Aiksaurus if you want to have a thesaurus available on
your computer.

%package -n %name-data
Summary: An English-language thesaurus library
Group: Text tools

%description -n %name-data
Aiksaurus is an English-language thesaurus library that can be
embedded in word processors, email composers, and other authoring
software to provide thesaurus capabilities.
This package contains the datafiles.

%package -n %lib_name
Summary: An English-language thesaurus library
Group: Text tools
Requires: %name-data

%description -n %lib_name
Aiksaurus is an English-language thesaurus library that can be
embedded in word processors, email composers, and other authoring
software to provide thesaurus capabilities.
This package contains these libraries.

Install Aiksaurus if you want to have a thesaurus available on
your computer.

%package -n %lib_name-devel
Summary: Libraries and include files for Aiksuarus
Group: Development/C
Requires: %lib_name = %version-%release

%description -n %lib_name-devel
Aiksaurus is an English-language thesaurus library that can be
embedded in word processors, email composers, and other authoring
software to provide thesaurus capabilities.
This package contains the libraries and includes files necessary to develop
applications with Aiksaurus.

%package -n %{name}-gtk
Summary: A GTK+ thesaurus application
Group: Text tools

%description -n %{name}-gtk
Aiksaurusgtk is a GTK+ interface to the Aiksaurus library.
It provides an attractive thesaurus interface, and can be embedded
in GTK+ projects, notably AbiWord.
This package provides the standalone GTK+ interface.

%package -n %lib_namegtk
Summary: Libraries for aiksaurusgtk
Group: Text tools

%description -n %lib_namegtk
Aiksaurusgtk is a GTK+ interface to the Aiksaurus library.
It provides an attractive thesaurus interface, and can be embedded
in GTK+ projects, notably AbiWord.
This package provides the library files for aiksaurusgtk.

%package -n %lib_namegtk-devel
Summary: A GTK+ thesaurus library
Group: Development/C
Requires: %lib_namegtk = %version-%release

%description -n %lib_namegtk-devel
This package contains the libraries and includes files necessary to develop
applications with Aiksaurusgtk.

%prep
%setup -q
%patch

%build
%configure
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall_std

install -D -m644 %SOURCE1 %buildroot%_niconsdir/%name.png
install -D -m644 %SOURCE2 %buildroot%_desktopdir/g%name.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Utility \
	--remove-category=Application \
	--add-category=Office \
	--add-category=TextTools \
	--add-category=Dictionary \
	%buildroot%_desktopdir/gaiksaurus.desktop

%files
%doc ChangeLog README AUTHORS
%_bindir/aiksaurus
%_bindir/caiksaurus

%files -n %name-data
%dir %_datadir/aiksaurus
%_datadir/aiksaurus/*.dat

%files -n %lib_name
%_libdir/libAiksaurus-*.so.*

%files -n %lib_name-devel
%_libdir/libAiksaurus.so
%_pkgconfigdir/aiksaurus-1.0.pc
%dir %_includedir/Aiksaurus
%_includedir/Aiksaurus/Aiksaurus.h
%_includedir/Aiksaurus/AiksaurusC.h

%files -n %{name}-gtk
%_bindir/gaiksaurus
%_desktopdir/g%name.desktop
%_niconsdir/%name.png

%files -n %lib_namegtk
%_libdir/libAiksaurusGTK-*.so.*

%files -n %lib_namegtk-devel
%_libdir/libAiksaurusGTK.so
%_pkgconfigdir/gaiksaurus-1.0.pc
%_includedir/Aiksaurus/AiksaurusGTK*.h

%changelog
* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt4.qa4
- Removed bar RPATH

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.1-alt4.qa3
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for aiksaurus-gtk

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt4.qa2
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Sun Nov 29 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.1-alt4.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libaiksaurus-gtk
  * postun_ldconfig for libaiksaurus-gtk
  * update_menus for aiksaurus-gtk
  * post_ldconfig for libaiksaurus
  * postun_ldconfig for libaiksaurus
  * pixmap-in-deprecated-location for aiksaurus
  * postclean-05-filetriggers for spec file

* Tue Nov 04 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt4
- fix build with gcc 4.3
- replace menu with desktop file (thanks Fedora)

* Sun Jun 22 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt3
- update buildreq

* Sun Jan 29 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt2
- fix libdir using (bug #8604)

* Tue Sep 14 2004 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- first build for ALT Linux Sisyphus
- add menu and icon for gtk-version

* Mon Aug 09 2004 Marcel Pol <mpol@mandrake.org> 1.2.1-1mdk
- 1.2.1
- increase api version
- no need to run aclocal anymore

* Wed Jun 09 2004 Marcel Pol <mpol@mandrake.org> 1.0.2-0.cvs20040609.1mdk
- cvs snapshot

* Wed Dec 16 2003 Marcel Pol <mpol@mandrake.org> 1.0.1-5mdk
- use better 64bit (build)requires

* Sun Oct 19 2003 Marcel Pol <mpol@gmx.net> 1.0.1-4mdk
- buildrequires

* Fri Aug 29 2003 Marcel Pol <mpol@gmx.net> 1.0.1-3mdk
- buildrequires

* Mon Jul 21 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 1.0.1-2mdk
- Rebuild

* Wed Jul 16 2003 Marcel Pol <mpol@gmx.net> 1.0.1-1mdk
- rebuild for provides/requires
- s/Aiksaurus/aiksaurus
- new url
- source now includes gtk frontend
- drop patch0
- run aclocal to avoid libtool problems
- new soname

* Thu May 22 2003 Marcel Pol <mpol@gmx.net> 0.15-2mdk
- rebuild for provides/requires

* Mon Mar 10 2003 Marcel Pol <mpol@gmx.net> 0.15-1mdk
- initial mandrake release
