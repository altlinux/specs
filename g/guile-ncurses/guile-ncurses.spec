Name: guile-ncurses
Version: 3.1
Release: alt1

Summary: GNU Guile-Ncurses is a library for the Guile Scheme interpreter
License: GPLv3
Group: System/Libraries
Url: http://www.gnu.org/software/guile-ncurses/

Source: %name-%version.tar

BuildRequires: guile-devel libncursesw-devel libunistring-devel texinfo

%package -n lib%name
Summary: GNU Guile-Ncurses is a library for the Guile Scheme interpreter
Group: System/Libraries
License: LGPLv3

%package shell
Summary: XTerm based dedicated window for the Guile Scheme interpreter 
Group: Development/Scheme
Requires: lib%name = %version-%release
Requires: xterm

%description
GNU Guile-Ncurses is a library for the Guile Scheme interpreter that
provides functions for creating text user interfaces. The text user
interface functionality is built on the ncurses libraries: curses, form,
panel, and menu.

%description -n lib%name
GNU Guile-Ncurses is a library for the Guile Scheme interpreter that
provides functions for creating text user interfaces. The text user
interface functionality is built on the ncurses libraries: curses, form,
panel, and menu.

%description shell
Xterm based dedicated window for interactive Guile Scheme interpreter
for easy interactive development with GNU Guile-Ncurses library.

%prep
%setup

%build
%autoreconf
%configure --with-ncursesw
%make_build

%install
%makeinstall_std

%check
make check

%define guile_sitedir %(guile-config info sitedir)

%files -n lib%name
%guile_ccachedir/ncurses
%guile_extensiondir/libguile-ncurses.so*
%guile_sitedir/ncurses

%_infodir/guile-ncurses.info*

%files shell
%_bindir/guile-ncurses-shell

%changelog
* Tue Feb 07 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1-alt1
- 3.1 released

* Mon Jan 25 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0-alt1
- 3.0 released

* Mon Aug 13 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2-alt1
- 2.2

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1.1
- NMU: added BR: texinfo

* Tue Jun 04 2013 Ivan Ovcherenko <asdus@altlinux.org> 1.4-alt1
- Initial build
