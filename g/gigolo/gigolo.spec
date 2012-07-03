Name:           gigolo
Version:        0.4.1
Release:        alt1
Summary:        frontend to manage connections to remote filesystems using GIO/GVfs
Group:          File tools
License:        GPL
URL:            http://www.uvena.de/gigolo/
Source:         %name-%version.tar
#Patch1:		%name-%version-%release.patch

# Automatically added by buildreq on Wed Oct 21 2009
BuildRequires: intltool libgtk+2-devel

%description
Gigolo is a frontend to easily manage connections to remote filesystems
using GIO/GVfs. It allows you to quickly connect/mount a remote filesystem
and manage bookmarks of such.

%prep
%setup
#patch1 -p1

%build
autoreconf -fisv
%configure
%make

%install
%makeinstall

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%_bindir/%name
%_datadir/applications/gigolo.desktop
%_man1dir/%name.*

%changelog
* Thu Jun 02 2011 Mykola Grechukh <gns@altlinux.ru> 0.4.1-alt1
- new version

* Wed Oct 21 2009 Mykola Grechukh <gns@altlinux.ru> 0.3.2-alt1
- initial build for ALT Linux
