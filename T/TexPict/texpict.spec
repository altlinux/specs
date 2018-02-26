%define shortname texpict
Name: TexPict
Version: 1.3
Release: alt3

Summary: Tex Pictures is a drawing program for latex documents
Summary(ru_RU.UTF-8): Tex Pictures - программа рисования рисунков LaTeX.
License: BSD like
Group: Graphics
Url: http://gatxan.cimne.upc.es/texpict/

Packager: Igor Vlasenko <viy@altlinux.ru>
Source: http://gatxan.cimne.upc.es/texpict/%name.tar.gz

BuildArch: noarch

# It is tcl file; findreq treat it as shell :(
%add_findreq_skiplist %_bindir/*
Requires: tk >= 8.0
BuildRequires: recode

%description
Tex Pictures is a program to create easy drawings to include in latex documents in both Unix and MS Windows. It is possible also to save them as postscript.
- One latex file.
Pictures are included inside the latex document. They are VERY small and 
avoid too many files. 
- Annotate images.
Useful to annotate one EPS or GIF image and  include the figure and the 
annotations inside the latex document. 
- Later edition.
You can edit later the figure that you have pasted in your latex document. 
Just select it, and paste inside TexPict. In this way, one drawing from 
3 month ago can be edited. With a EPS or GIF file it would be no possible. 

%prep
%setup -q -c -n %name-%version
#%patch -p1

%build
recode /CRLF.. TexPict.tcl

%install
%__install -d %buildroot%_bindir/
%__install -m755 TexPict.tcl %buildroot%_bindir/%shortname
ln -s %shortname %buildroot%_bindir/%name

mkdir -p $RPM_BUILD_ROOT%_desktopdir
cat > $RPM_BUILD_ROOT%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=%{name}
Comment=Tex Pictures is a drawing program for latex documents
Comment[ru]=Tex Pictures - программа рисования рисунков LaTeX
Icon=%{name}
Exec=%{name}
Terminal=false
Categories=Graphics;2DGraphics;VectorGraphics;X-ALTLinux-TeX;
EOF

%files
%doc README TexPict.html
#doc eepic.sty eepicemu.sty epic.sty
%_bindir/%shortname
%_bindir/%name
%_desktopdir/%{name}.desktop

%changelog
* Sat Apr 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.3-alt3
- desktop file cleanup

* Sat Mar 26 2011 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2
- converted debian menu to freedesktop

* Wed Nov 19 2008 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1.1
- NMU (by repocop): the following fixes applied:
 * update_menus for TexPict

* Tue Dec 20 2005 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1
- initial build
