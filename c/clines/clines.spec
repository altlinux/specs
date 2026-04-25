# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: clines
Version: 1.0.4
Release: alt5

Summary: Curses-based Lines game

License: GPL-2
Group: Games/Other
Url: http://manticore.2y.net/prj/clines-g.html

Source0: http://manticore.2y.net/cgi-bin/dlwct.sh?f=clines/%name-%version.tar.bz2

Patch: %name-1.0.4-alt-makefile-strange_command_fix.patch

# Automatically added by buildreq on Sat Aug 12 2006
BuildRequires: libgpm-devel libncurses-devel

%description
Console Lines is a "Lines" game for the Unix terminal. After install
this program read README file about rules and scores.

%prep
%setup
%patch

%build
%autoreconf
%configure
%make_build 

%install
%make_install DESTDIR=%buildroot install

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=CLines
Comment=Curses-based Lines game
Icon=terminal
Exec=%name
Terminal=true
Categories=Game;BoardGame;
EOF

%files
%doc AUTHORS ChangeLog README TODO
%_bindir/%name
%_man6dir/%name.6.*
%_desktopdir/%name.desktop

%changelog
* Sat Apr 25 2026 Fr. Br. George <george@altlinux.org> 1.0.4-alt5
- Fix gcc15 build

* Thu Jun 07 2012 Fr. Br. George <george@altlinux.ru> 1.0.4-alt4
- Fix gcc4.6 build

* Sun Apr 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt3.qa1
- NMU: converted menu to desktop file

* Mon Nov 17 2008 Slava Semushin <php-coder@altlinux.ru> 1.0.4-alt3
- Replaced %%__autoreconf macros to %%autoreconf (noted by repocop)
- Removed obsolete %%update_menus/%%clean_menus calls (noted by repocop)

* Mon Dec 24 2007 Slava Semushin <php-coder@altlinux.ru> 1.0.4-alt2
- Fixed build with automake 1.10
- Imported into git and built with gear

* Sun Nov 26 2006 Slava Semushin <php-coder@altlinux.ru> 1.0.4-alt1
- 1.0.4
- Using -U_FORTIFY_SOURCE flag for compiler by default
- Added patch which removes strange commands from Makefile.am
- Spec cleanup: s/%%setup -q/%%setup/

* Mon Jul 31 2006 Slava Semushin <php-coder@altlinux.ru> 1.0.3-alt1
- Initial build for ALTLinux Sisyphus
- Picked up from OpenBSD
- Using -Werror flag for compiler by default

