Name: design-icewm-themes
Version: 1.0
Release: alt6

Summary: Themes collection for IceWM
License: GPL-2.0
Group: Graphical desktop/Icewm

Source: icewm-themes.tar
Requires: design-icewm >= 1.0-alt12
AutoReqProv: no
BuildArch: noarch

Summary(ru_RU.UTF-8): Коллекция тем для IceWM

%define themedir %_x11x11dir/icewm/themes

%description
Themes collection for IceWM

%description -l ru_RU.UTF-8
Коллекция тем для IceWM

%prep

%build

%install
mkdir -p %buildroot%themedir
tar xf %SOURCE0 -C %buildroot$(dirname %themedir)

find %buildroot%themedir -type f -print0 | xargs -r0 chmod 0644
find %buildroot%themedir -type d -print0 | xargs -r0 chmod 0755

# remove .xvpics
find %buildroot%themedir -type d -name .xvpics -print0 | xargs -r0 rm -rf
# remove *.bak
find %buildroot%themedir -type f -name '*.bak' -print0 | xargs -r0 rm -rf

# It is the file in the package whose name matches the format emacs or vim uses 
# for backup and autosave files. It may have been installed by  accident.
find %buildroot \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete
# failsafe cleanup if the file is declared as %%doc
find . \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete

%files
%themedir/*

%changelog
* Sat Apr 09 2022 Dmitriy Khanzhin <jinn@altlinux.org> 1.0-alt6
- removed themes that included to the main package, this themes Helix,
  Infadel2, Natural are now provided in a package icewm-themes
- fixed license to GPL-2.0

* Sun Mar 31 2013 Dmitriy Khanzhin <jinn@altlinux.org> 1.0-alt5
- fixed and restored dropped themes
- added several new themes from http://box-look.org

* Fri Mar 22 2013 Michael Shigorin <mike@altlinux.org> 1.0-alt4
- dropped a bunch of themes exposing bugs with icewm-1.3 (closes: #28733)
- fixed permissions in the archive
- spec cleanup

* Mon Aug 27 2012 Repocop Q. A. Robot <repocop@altlinux.org> 1.0-alt3.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * backup-file-in-package for design-icewm-themes

* Sat Jun 10 2006 Damir Shayhutdinov <damir@altlinux.ru> 1.0-alt3
- Files relocated from %_x11libdir to %_x11datadir

* Mon Oct 21 2002 Rider <rider@altlinux.ru> 1.0-alt2
- fix permissons

* Fri Oct 18 2002 Rider <rider@altlinux.ru> 1.0-alt1
- first build
