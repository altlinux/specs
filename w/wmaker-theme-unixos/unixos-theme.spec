Name: wmaker-theme-unixos
Version: 0.60.0
Release: alt9

Packager: Alexey Voinov <voins@altlinux.ru> 

Summary: WindowMaker theme
Summary(ru_RU.KOI8-R): Тема для WindowMaker
License: GPL
Group: Graphical desktop/Window Maker
Source: UnixOS-%version.tar.bz2
Patch: unixos-theme-0.60.0-voins1.patch.bz2
Requires: WindowMaker >= 0.60.0
Url: http://themes.freshmeat.net/projects/unixos/

Provides: unixos-theme = %version-%release
Obsoletes: unixos-theme

BuildArch: noarch

%description
WindowMaker theme

%description -l ru_RU.KOI8-R
Тема для WindowMaker

%prep
%setup -q -n UnixOS.themed
%patch -p2

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/WindowMaker/Themes/UnixOS.themed/
install -m644 * $RPM_BUILD_ROOT%_datadir/WindowMaker/Themes/UnixOS.themed/

%files
%_datadir/WindowMaker/Themes/UnixOS.themed/

%changelog
* Wed Jan 03 2007 Alexey Voinov <voins@altlinux.ru> 0.60.0-alt9
- package renamed [#9313]

* Sun Dec 10 2006 Alexey Voinov <voins@altlinux.ru> 0.60.0-alt8
- url fixed
- license fixed
- spec cleanup
- /usr/X11R6 -> /usr [#9294]

* Mon Nov 11 2002 Stanislav Ievlev <inger@altlinux.ru> 0.60.0-alt7
- rebuild

* Fri May  4 2001 Alexey Voinov <voins@voins.program.ru>
- translated Summary & description

* Mon Apr 30 2001 Alexey Voinov <voins@voins.program.ru>
- conditional NoSource. build nosrc.rpm with --define 'nosource 1'

* Wed Apr 18 2001 Alexey Voinov <voins@voins.program.ru>
- Spring2001 build

* Sun Feb 18 2001 Alexey Voinov <voins@voins.program.ru>
- spec cleanup

