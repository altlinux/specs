Summary: GNOME Manpages Editor
Name: gmanedit
Version: 0.4.2
Release: alt3
License: GPL
Group: Development/Other
URL: http://sourceforge.net/projects/gmanedit2
Source0: %{name}-%{version}.tar.gz
 
# Automatically added by buildreq on Mon Jan 05 2009
BuildRequires: libgtk+2-devel
BuildRequires: zlib-devel

%description
Gmanedit is an GNOME/Gtk Editor for Manual pages on Linux/Unix
systems. The original code was written in 2001 by Sergio Rua and
the program would run on the GNOME version 1 desktop environment.

Nothing happened since then and Sergio seemed to be unreachable,
so I decided to port the program to the GNOME version 2 and revive
the project. What you see is a second version which has the same
functionality as the old version, there were many code cleanups and
the program is now GTK+ only.

%prep
%setup

%build
export LIBS=-lz
%configure
%make

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/*
%_desktopdir/*.desktop
%_man1dir/*
%_pixmapsdir/*.png

%changelog
* Fri Jun 01 2012 Andrey Cherepanov <cas@altlinux.org> 0.4.2-alt3
- Add -lz to linker command line

* Wed Apr 20 2011 Andrey Cherepanov <cas@altlinux.org> 0.4.2-alt2
- Add zlib support

* Mon Jan 05 2009 Eugene Ostapets <eostapets@altlinux.ru> 0.4.2-alt1
- First build for ALTLinux
