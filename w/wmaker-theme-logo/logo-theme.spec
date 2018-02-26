Name: wmaker-theme-logo
Version: 0.52
Release: alt9

Packager: Alexey Voinov <voins@altlinux.ru> 

Summary: WindowMaker theme
Summary(ru_RU.KOI8-R): Тема для WindowMaker
License: GPL
Group: Graphical desktop/Window Maker
Source: Logo-%version.tar.bz2
Patch: logo-theme-0.52-voins2.patch.bz2
Requires: WindowMaker >= 0.52
Url: http://themes.freshmeat.net/projects/logo/

Provides: logo-theme = %version-%release
Obsoletes: logo-theme

BuildArch: noarch

%description
A theme designed around the Logo that won the Linux Logo T-Shirt contest.
You can find more about that at http://poledra.coyote.org:8080/~fullung/

%description -l ru_RU.KOI8-R
Тема для WindowMaker, на осонове логотипа - победителя конкурса.
Подробнее на http://poledra.coyote.org:8080/~fullung/

%prep
%setup -q -n Logo-%version
%patch -p0

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/WindowMaker/Themes/Logo.themed
install -m644 Backgrounds/* Pixmaps/* $RPM_BUILD_ROOT%_datadir/WindowMaker/Themes/Logo.themed/
install -m644 Themes/Logo $RPM_BUILD_ROOT%_datadir/WindowMaker/Themes/Logo.themed/style

%files
%_datadir/WindowMaker/Themes/Logo.themed

%changelog
* Wed Jan 03 2007 Alexey Voinov <voins@altlinux.ru> 0.52-alt9
- package renamed [#9313]

* Sun Dec 10 2006 Alexey Voinov <voins@altlinux.ru> 0.52-alt8
- url fixed
- license fixed
- spec cleanup
- /usr/X11R6 -> /usr

* Mon Nov 11 2002 Stanislav Ievlev <inger@altlinux.ru> 0.52-alt7
- rebuild

* Sat May  5 2001 Alexey Voinov <voins@voins.program.ru>
- translated Summary & description

* Mon Apr 30 2001 Alexey Voinov <voins@voins.program.ru>
- conditional NoSource. build nosrc.rpm with --define 'nosource 1'

* Wed Apr 18 2001 Alexey Voinov <voins@voins.program.ru>
- Spring2001 build

* Sun Feb 18 2001 Alexey Voinov <voins@voins.program.ru>
- spec cleanup
