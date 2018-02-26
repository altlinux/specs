Packager: Repocop Q. A. Robot <repocop@altlinux.org>
%define dvddev /dev/dvd
%define dvdsize 4590208

#%%define cvsdate 20080229

%define lname tkdvd
%define Name TkDVD
Name: %lname
Version: 4.0.9
%define rel 1
Release: alt%{?cvsdate:0.}%rel.1
Summary: TCL/Tk GUI for dvd+rw-tools
Summary(uk_UA.CP1251): TCL/Tk GUI для dvd+rw-tools
Summary(ru_RU.CP1251): TCL/Tk GUI для dvd+rw-tools
License: GPL
Group: Archiving/Cd burning
URL: http://savannah.nongnu.org/projects/%lname
%ifdef cvsdate
Source0: %lname-cvs-%cvsdate.tar
%else
Source0: %lname-%version.tar
%endif
Source1: %Name-i18n-uk-4.0.8.tcl
Source2: %Name-i18n-ru-4.0.8.tcl
Patch0: %lname-4.0.5-width.patch
Patch1: %lname-4.0.7-shebang.patch
BuildArch: noarch
Provides: %Name = %version-%release
Obsoletes: %Name
Requires: tk >= 8.4 mkisofs dvd+rw-tools cdrecord

# Automatically added by buildreq on Fri Feb 29 2008
BuildRequires: ImageMagick tcl

%description
%Name is a GUI for growisfs which is a part of dvd+rw-tools programmed
in TCL/Tk.
Features:
  - burn DVD+R/RW -R/W and DVD+R DL
  - burn from iso images
  - create ISO images from files
  - can overburn DVD
  - support multi-sessions DVD
  - add/delete/view/exclude files/directory to burn
  - can keep directory structure
  - size control of selected files
  - show burning command line
  - extra burning options (like iso9660 extensions or dvd compatibility
    option)
  - choose volume id
  - show growisofs/mkisofs output


%prep
%setup -n %lname%{?cvsdate:-cvs-%cvsdate}
%patch0 -p1
%patch1 -p1
sed -i -r -e 's/^([ \t]*wm[ \t]+geometry[ \t]+\.[ \t]+)[[:digit:]]+(x[[:digit:]]+)/\1900\2/' %Name.sh
sed -i -r -e '/^[ \t]*button[ \t]/ s/[ \t]+-width[ \t]+[^ \t]+//' src/*.tcl
# fix lapsus
sed -i -r -e 's/([Ll]ang)(age)/\1u\2/g' FAQ doc/config_file src/*.tcl
cat %SOURCE1 %SOURCE2 >> src/internationalization.tcl
sed -i -e 's|/dev/[[:alnum:]]*|%dvddev|g' src/*.tcl %Name.sh
sed -i -r -e 's/4[[:digit:]]{6}/%dvdsize/g' src/*.tcl %Name.sh doc/config_file


%build
./configure --prefix=%_bindir
%make_build
convert -resize 16x16 icons/%lname-2-{48,16}.png


%install
install -d -m 0755 %buildroot{%_bindir,%_liconsdir,%_niconsdir,%_miconsdir,%_docdir/%name-%version,%_desktopdir}
install -m 0755 %lname-install.sh %buildroot/%_bindir/%Name.tcl
ln -s %Name.tcl %buildroot/%_bindir/%lname
install -m 0644 icons/%lname-2-48.png %buildroot%_liconsdir/%name.png
install -m 0644 icons/%lname-2-32.png %buildroot%_niconsdir/%name.png
install -m 0644 icons/%lname-2-16.png %buildroot%_miconsdir/%name.png
install -m 0644 icons/README %buildroot%_docdir/%name-%version/README.icons
install -m 0644 FAQ README TODO doc/config_file %buildroot%_docdir/%name-%version/
bzip2 --best --stdout ChangeLog > %buildroot%_docdir/%name-%version/ChangeLog.bz2
iconv -f cp1251 -t utf-8 > %buildroot%_desktopdir/%name.desktop <<__MENU__
[Desktop Entry]
Version=1.0
Name=%Name
Exec=%name
Comment=GUI for growisfs
Comment[uk]=GUI для dvd+rw-tools
Comment[ru]=GUI для dvd+rw-tools
X-MultipleArgs=true
Icon=%name
Terminal=false
Type=Application
StartupNotify=true
Categories=AudioVideo;DiscBurning;
__MENU__


%files
%doc %_docdir/%name-%version
%_bindir/*
%_niconsdir/*
%_liconsdir/*
%_miconsdir/*
%_desktopdir/*


%changelog
* Tue Nov 03 2009 Igor Vlasenko <viy@altlinux.ru> 4.0.9-alt1.1
- NMU (by repocop): the following fixes applied:
  * update_menus for tkdvd

* Tue Sep 02 2008 Led <led@altlinux.ru> 4.0.9-alt1
- 4.0.9

* Sun Aug 10 2008 Led <led@altlinux.ru> 4.0.8-alt2
- fixed %name.desktop

* Sat Jul 12 2008 Led <led@altlinux.ru> 4.0.8-alt1
- 4.0.8
- updated Ukrainian internationalization
- updated Russian internationalization

* Fri Feb 29 2008 Led <led@altlinux.ru> 4.0.8-alt0.20080229.1
- updated from CVS (4.0.8 prereliase):
  + can detect cdrkit presence and use it instead of cdrtools
  + allows to burn files with a size > 4GB using UDF filesystem
- added 16x16 icon
- added %lname-4.0.7-shabang.patch

* Mon Oct 29 2007 Led <led@altlinux.ru> 4.0.7-alt1
- 4.0.7

* Fri Mar 16 2007 Led <led@altlinux.ru> 4.0.6-alt1
- 4.0.6
- fixed %name.desktop

* Sat Feb 17 2007 Led <led@altlinux.ru> 4.0.5-alt2
- rename package from %Name to %lname
- added %lname-4.0.5-width.patch
- cleaned up spec

* Fri Feb 16 2007 Led <led@altlinux.ru> 4.0.5-alt1
- 4.0.5:
  + Eject CD option is now saved in config file
  + Burn speed option is saved in config file

* Fri Aug 11 2006 Led <led@altlinux.ru> 4.0.3-alt1
- 4.0.3
- updated Ukrainian internationalization
- updated Russian internationalization

* Wed Jul 05 2006 Led <led@altlinux.ru> 4.0.2-alt1
- 4.0.2
- fixed and updated Ukrainian internationalization
- updated Russian internationalization
- replaced %name-*-button.patch with sed
- replased subst with sed
- fixed menu file

* Thu Jun 29 2006 Led <led@altlinux.ru> 4.0.0-alt1
- 4.0.0
- updated Ukrainian internationalization
- updated Russian internationalization

* Thu Jun 08 2006 Led <led@altlinux.ru> 3.10.1-alt1
- initial build
- fixed DVD device and DVD size
- added Ukrainian internationalization
- added Russian internationalization
