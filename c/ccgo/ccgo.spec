Name: ccgo
Version: 0.3.6.3
Release: alt1

Summary: a program for playing the game Go
License: GPL v2
Group: Games/Boards
Url: http://ccdw.org/~cjj/prog/ccgo/

Source: %url/src/%name-%version.tar.gz

# Added by buildreq2 on Wed Feb 08 2006
BuildRequires: gcc-c++ libGConf2-devel libgconfmm2-devel libgtkmm2-devel libncurses-devel libpng-devel libreadline-devel libtool-common

%description
ccgo is a program that provides a graphical interface for playing Go on
the IGS (Internet Go Server) or with GMP (Go modem protocol) programs
like GNU Go. It's also a SGF (smart game format) Go record viewer.

%prep
%setup

%build
%configure
%make

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_man6dir/%name.*
%_datadir/applications/%name.desktop
%_datadir/pixmaps/%name.xpm
%_datadir/pixmaps/%name

%changelog
* Sun Oct 25 2009 Timur Batyrshin <erthad@altlinux.org> 0.3.6.3-alt1
- 0.3.6.3

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.3.6.2-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for ccgo

* Wed Feb 08 2006 Alex V. Myltsev <avm@altlinux.ru> 0.3.6.2-alt1
- Initial build for ALT Linux Sisyphus.

