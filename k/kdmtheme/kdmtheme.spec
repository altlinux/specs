
Name:		kdmtheme
Version:	1.2.2
Release:	alt4
Summary:	Theme Manager for KDM

License:	GPL
Group:		System/Configuration/Other
URL:		http://beta.smileaf.org

Packager:   	Andrey Cherepanov <cas@altlinux.ru>

Source0:	%name-%version.tar.bz2
Patch0:		kdmtheme-1.2.2-alt-libs-fix.patch
Patch1:		kdmtheme-1.2.2-alt-desktop-fix.patch
Patch2:		kdmtheme-1.2.2-l10n-ru.patch
Patch3:		kdmtheme-1.2.2-kubuntu_11_replace_qlist.patch
Patch4:		kdmtheme-1.2.2-alt-info-update.patch

BuildRequires: gcc-c++ kdelibs-devel, desktop-file-utils, kdebase-devel kdelibs-devel xmllint

%description
KDM Theme manager is just what it says a theme Manager for KDM.
This control module allows you to easily add, remove and select
any KDM theme you want.

%prep
%setup -q
%patch0 -p1
%patch1 -p2
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%set_automake_version 1.7
%set_autoconf_version 2.5
%add_optflags -I%_includedir/tqtinterface
%configure --without-arts
%make_build

%install
%makeinstall

%find_lang --with-kde --with-man %name

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog README
%_datadir/applications/kde/*.desktop
%_libdir/kde3/kcm_%name.so
%_libdir/kde3/kcm_%name.la

%changelog
* Tue Feb 01 2011 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt4
- Disable aRts support, fix build

* Wed Nov 19 2008 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt3
- Fix Categories (bug #16870)
- Remove deprecated update-desktop-database and update-menus macros
- Remove deprecated Encoding in group "Desktop Entry"
- Add xmllint requirement for documentation build
- Add missed file kcm_kdmtheme.la

* Mon May 19 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.2.2-alt1.eter1
- Fixed crash wheh click out of theme at themes list
  + Added kdmtheme-1.2.2-alt-info-update.patch
- Added simple patch from kubuntu

* Tue May 06 2008 Andrey Cherepanov <cas@altlinux.ru> 1.2.2-alt1
- Version 1.2.2

* Fri Oct 27 2006 Alexey Gladkov <legion@altlinux.ru> 1.1.2-alt1
- Initial release.

