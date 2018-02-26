Name: wmaker-theme-gnustep_penguin
Version: 0.60.0
Release: alt8

Packager: Alexey Voinov <voins@altlinux.ru> 

Summary: WindowMaker theme
Summary(ru_RU.KOI8-R): Тема для WindowMaker
License: GPL
Group: Graphical desktop/Window Maker
Source: GNUstep-Penguin-%version.tar.bz2
Requires: WindowMaker >= 0.60.0
Url: http://themes.freshmeat.net/projects/gnusteppenguin/

Provides: gnustep_penguin-theme = %version-%release
Obsoletes: gnustep_penguin-theme

BuildArch: noarch

%description
WindowMaker theme

%description -l ru_RU.KOI8-R
Тема для WindowMaker

%prep
%setup -q -n GNUstep-Penguin.themed

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/WindowMaker/Themes/GNUstep-Penguin.themed
install -m644 * $RPM_BUILD_ROOT%_datadir/WindowMaker/Themes/GNUstep-Penguin.themed

%files
%_datadir/WindowMaker/Themes/GNUstep-Penguin.themed/

%changelog
* Thu Jan 04 2007 Alexey Voinov <voins@altlinux.ru> 0.60.0-alt8
- package renamed [#9313]

* Sun Dec 10 2006 Alexey Voinov <voins@altlinux.ru> 0.60.0-alt7
- url fixed
- license fixed
- spec cleanup
- /usr/X11R6 -> /usr

* Mon Nov 11 2002 Stanislav Ievlev <inger@altlinux.ru> 0.60.0-alt6
- rebuild

* Sat May  5 2001 Alexey Voinov <voins@voins.program.ru>
- translated Summary & description

* Mon Apr 30 2001 Alexey Voinov <voins@voins.program.ru>
- conditional NoSource. build nosrc.rpm with --define 'nosource 1'

* Wed Apr 18 2001 Alexey Voinov <voins@voins.program.ru>
- Spring2001 build

* Sun Feb 18 2001 Alexey Voinov <voins@voins.program.ru>
- initial build

