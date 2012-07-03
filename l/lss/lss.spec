Packager: Repocop Q. A. Robot <repocop@altlinux.org>
Name: lss
Version: 0.1.6
Release: alt1.1

Summary: LSS is a symbol browser to help creating LaTeX documents with many math symbols.
License: GNU GPL
Group: File tools

Url: http://clay.ll.pl/lss/
Source: http://clay.ll.pl/lss/%name-%version.tar.gz

# Automatically added by buildreq on Sun Apr 20 2008
BuildRequires: libgtk+2-devel libxml2-devel

%description
LSS is a symbol browser to help creating LaTeX documents with many math symbols.
 
All symbols are grouped into categories and user can copy symbol name to system-wide clipboard (or insert it directly to first running copy of gVIM) by selecting symbol icon from list. Many non-standard (and unsupported in LSS) symbols can be found in the comprehensive LATEX symbol list here.

Features
 
 * Built-in 478 LaTeX symbols
 * Most of AMS symbols are supported
 * Easy integration with gVIM editor
 * Selected symbol name can be copied into clipboard for use with your favourite editor
		 
%prep
%setup 

%build
%configure

%make

%install
%make DESTDIR=%buildroot install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/applications/*.desktop
%_pixmapsdir/*

%changelog
* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.1.6-alt1.1
- NMU (by repocop): the following fixes applied:
  * update_menus for lss

* Sun Apr 20 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.1.6-alt1
- build for ALT Linux
