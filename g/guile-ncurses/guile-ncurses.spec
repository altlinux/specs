Name: guile-ncurses
Version: 1.4
Release: alt1.1

Summary: GNU Guile-Ncurses is a library for the Guile Scheme interpreter
License: %gpl3only
Group: System/Libraries
Url: http://www.gnu.org/software/guile-ncurses/
Packager: Ivan Ovcherenko <asdus@altlinux.org>

Source: %name-%version.tar
Patch0: %name-%version-alt-texinfo.patch

BuildPreReq: rpm-build-licenses
BuildPreReq: libncursesw-devel
BuildPreReq: libunistring-devel
BuildPreReq: guile18-devel
# explicitly added texinfo for info files
BuildRequires: texinfo

%package -n lib%name
Summary: GNU Guile-Ncurses is a library for the Guile Scheme interpreter
Group: System/Libraries
License: %lgpl3only

%package -n guile-ncurses-shell
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

%description -n guile-ncurses-shell
Xterm based dedicated window for interactive Guile Scheme interpreter
for easy interactive development with GNU Guile-Ncurses library.

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure \
	--with-ncursesw \
	--with-guilesitedir=%_datadir/guile/1.8
%make_build

%install
%makeinstall_std

%files -n lib%name
%_libdir/*.so*
%_datadir/guile/1.8/ncurses/*
%_infodir/*

%files -n guile-ncurses-shell
%_bindir/*

%changelog
* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1.1
- NMU: added BR: texinfo

* Tue Jun 04 2013 Ivan Ovcherenko <asdus@altlinux.org> 1.4-alt1
- Initial build
