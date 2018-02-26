Summary: CSS editor for web developers
Name: cssed
Version: 0.4.1
Release: alt1
Group: Development/Tools
License: GPL
Source: http://prdownloads.sourceforge.net/cssed/%name-%version.tar.gz
Url: http://cssed.sourceforge.net/
Requires: gtk2 >= 2.4 glib2 >= 2.4 cssed-common
BuildRequires: desktop-file-utils gcc-c++ libgtk+2-devel libxml2-devel

%description
cssed is a tiny GTK+ CSS editor and validator
for web developers.

%package common
Summary: common cssed files
Group: Development/Tools
BuildArch: noarch

%description common
common files for cssed. cssed is a tiny GTK+ CSS editor and validator
for web developers.

%prep
%setup -q -n cssed-0.4.1

%build
export CFLAGS="%optflags"
%configure --with-ipc-queue --prefix=/usr --mandir=%_datadir/man/ --with-freedesktop-support
make

%install
[ -n %buildroot -a %buildroot != "/" ] && rm -rf %buildroot
DESTDIR=%buildroot make install

%makeinstall
for doc in AUTHORS README COPYING INSTALL NEWS ChangeLog; do
	rm -f %buildroot%prefix/doc/cssed/$doc;
done;


%clean


%files
%_bindir/cssed

%files common
%_mandir/man1/cssed.1.gz
%_datadir/applications/*
%_datadir/application-registry/*
%_datadir/mime-info/cssed.mime
%_datadir/pixmaps/cssed_icon.png
%_datadir/cssed/data/*
%_datadir/locale/es/LC_MESSAGES/cssed.mo
%_datadir/locale/fr/LC_MESSAGES/cssed.mo
%_datadir/locale/it/LC_MESSAGES/cssed.mo
%_datadir/locale/de/LC_MESSAGES/cssed.mo
%_datadir/locale/gl/LC_MESSAGES/cssed.mo
%_datadir/locale/ca/LC_MESSAGES/cssed.mo
%_datadir/locale/cs/LC_MESSAGES/cssed.mo
%doc AUTHORS COPYING ChangeLog README INSTALL NEWS

%changelog
* Sun Apr 03 2011 Alex Negulescu <alecs@altlinux.org> 0.4.1-alt1
- initial Sisyphus build, from SVN, with small mods
* Fri Mar 25 2011 Alex Negulescu <alecs@altlinux.org> 0.4.0-alt2
- 2nd try
* Tue Sep 08 2009 Alex Negulescu <alecs@altlinux.org> 0.4.0-alt1
- initial Sisyphus build
* Sun Sep 18 2005 Iago Rubio <iago.rubio@hispalinux.es> 0.4.0-0
- Updated version tags.
* Fri Mar 09 2005 Iago Rubio <iago.rubio@hispalinux.es> 0.3.1-3
- Minimal corrections to follow the fedora extras guidelines.
* Fri Mar 09 2005 Iago Rubio <iago.rubio@hispalinux.es> 0.3.1-fc3
- Splited out development headers to a separate package.
* Fri Sep 23 2004 Iago Rubio <iago.rubio@hispalinux.es> 0.3.0-fc2
- Some changes to use GtkFileChooser on gtk+2 >= 2.4 systems.
* Mon Sep 13 2004 Iago Rubio <iago.rubio@hispalinux.es> 0.3.0
- Finished plugable interface. Lots of usability improvements.
  Added *.pc file to compile plugins with pkg-config.
* Wed Apr 07 2004 Iago Rubio <iago.rubio@hispalinux.es> 0.2.2
- Added plugable interface and some improvements.
* Wed Apr 07 2004 Iago Rubio <iago.rubio@hispalinux.es> 0.2.1
- Fixed bug that prevent open files that cannot be written.
* Tue Apr 06 2004 Iago Rubio <iago.rubio@hispalinux.es> 0.2.0
- Added doc scanner, fixed undo redo, first beta.
* Fri Feb 27 2004 Iago Rubio <iago.rubio@hispalinux.es> 0.1-5
- Fixed vte build problem.
* Thu Feb 12 2004 Iago Rubio <iago.rubio@hispalinux.es> 0.1.0-4
- Bug fixes and better highlighting
* Thu Jan 14 2004 Iago Rubio <iago.rubio@hispalinux.es> 0.1.0-3
- Updated RPM with validation support
* Mon Dec 8 2003 Iago Rubio <iago.rubio@hispalinux.es> 0.1.0-2
- Initiall RPM.

