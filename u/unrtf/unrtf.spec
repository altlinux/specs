Name: unrtf
Version: 0.21.1
Release: alt1

Summary: UnRTF is a moderately complicated converter from RTF to other formats
License: GPL
Group: Text tools
Url: http://www.gnu.org/software/unrtf/unrtf.html
Packager: Ilya Mashkin <oddity@altlinux.ru>

Source: %{name}-%{version}.tar.gz

%description
The program unrtf is a converter from Rich Text Format (RTF) to a
growing number of document formats. At present it supports
Hypertext Markup Language (HTML), plain text, text with VT100 codes,
LaTeX, and PostScript. All output formats except HTML are "alpha" i.e.
limited and development has just begun. However with HTML, the program
supports tables, fonts, embedded images, hyperlinks, and paragraph alignment.
Font support includes face and size changes, as well as typical attributes
such as italic, bold, underlining, strikethrough, smallcaps, allcaps, expand,
compress and both foreground and background colors. Images are always stored
to separate files in the current directory, or they can be ignored.

%prep
%setup -q -n %{name}-%{version}
#%__rm %name *.o

%build
%configure
%make_build

%install
#%__install -pD -m755 ./%name %buildroot%_bindir/%name
#%__install -pD -m644 ./%name.1 %buildroot%_man1dir/%name.1
%makeinstall

%files
%doc NEWS README tests
%_bindir/*
%_libdir/%name/*
%_man1dir/*

%changelog
* Wed Dec 01 2010 Ilya Mashkin <oddity@altlinux.ru> 0.21.1-alt1
- 0.21.1

* Tue Oct 23 2007 Slava Semushin <php-coder@altlinux.ru> 0.20.2-alt1.1
- NMU
- Updated Url tag (#13169)

* Tue Jul 11 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.20.2-alt1
- 0.20.2

* Thu Mar 23 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.20.1-alt1
- 0.20.1

* Thu Mar 09 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.20.0-alt1
- 0.20.0

* Tue Jan 10 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.19.9-alt1
- new version

* Thu Sep 08 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.19.7-alt1
- 0.19.7

* Fri Feb 20 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.19.3-alt1
- 0.19.3
- fix bug #225592: null pointer param in convert.c

* Wed Dec 24 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.19.0-alt1
- 0.19.0
- minor fixes to prevent segmentation violations
- further special character code; minor cleanups

* Fri Dec 19 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.18.1-alt1
- First version of RPM package

