Name: archway
Version: 0.2.1
Release: alt2

Summary: ArchWay is a GNU Arch GUI
License: GPL
Group: Development/Other
URL: http://www.nongnu.org/archway/

Packager: Alexey Voinov <voins@altlinux.ru>

BuildArch: noarch

Source: %name-%version.tar.bz2
Patch0: %name-0.2.0-alt-gtkinit.patch
Patch1: %name-0.2.1-alt-gtk2table.patch

# Automatically added by buildreq on Mon Jan 31 2005 (-bi)
BuildRequires: fontconfig freetype2 glib2 perl-Arch perl-Glib perl-Gtk2 xorg-x11-libs

%description 
ArchWay is a GNU Arch GUI.  It follows the unix tradition of small tools
doing their work well and cooperating nicely with each other.

Some tips: in a working tree, run "archelf" to operate on project files;
run "archmag" to manage tree merges; run "archeye ." to view tree changes;
run "archeye ,,undo-1" to view any changeset; run "archrog" to manage
registered archives; and so on.

Alternativelly, just run "archway" and choose the desired tools from there.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%install
%make install prefix=%_prefix DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%perl_vendor_privlib
mv $RPM_BUILD_ROOT%_datadir/%name/perllib/* $RPM_BUILD_ROOT%perl_vendor_privlib
rmdir $RPM_BUILD_ROOT%_datadir/%name/perllib/
rm -rf $RPM_BUILD_ROOT%perl_vendor_privlib/Arch

%files
%doc AUTHORS README TODO doc ChangeLog NEWS
%_bindir/*
%_datadir/%name
%perl_vendor_privlib/ArchWay


%changelog
* Fri Aug 08 2008 Alexey Voinov <voins@altlinux.ru> 0.2.1-alt2
- url updated
- packager tag added

* Tue Oct 11 2005 Alexey Voinov <voins@altlinux.ru> 0.2.1-alt1
- new version (0.2.1)
- gtk2table patch fixes incorrect use of Gtk2::Table

* Tue Apr 26 2005 Alexey Voinov <voins@altlinux.ru> 0.2.0-alt1
- new version (0.2.0)

* Mon Jan 31 2005 Alexey Voinov <voins@altlinux.ru> 0.1.1-alt1
- new version (0.1.1)
- perl-Arch is now separate project

* Mon Nov 01 2004 Alexey Voinov <voins@altlinux.ru> 0.1.0-alt1
- new version (0.1.0)

* Sun Oct 24 2004 Alexey Voinov <voins@altlinux.ru> 0.0.9-alt1
- initial build
