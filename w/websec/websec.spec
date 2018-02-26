Name: websec 
Version: 1.9.0
Release: alt1.1

Summary: Web Secretary is a web page monitoring software
License: GPL
Group: Networking/WWW

URL: http://baruch.ev-en.org/proj/websec
Source: %url/websec-%version.tar.gz

BuildArch: noarch
# Automatically added by buildreq on Wed Jun 13 2007 (-bi)
BuildRequires: perl-libwww
BuildRequires: perl-Pod-Parser

Requires: /usr/sbin/sendmail

%description
Web Secretary is a web page monitoring software. However, it goes beyond
the normal functionalities offered by such software. It will detect
changes based on content analysis, making sure that it's not just HTML
that changed, but actual content. You can tell it what to ignore in the
page (hit counters and such), and it can mail you the document with the
changes highlighted or load the highlighted page in a browser.

%prep
%setup -q

%build

%install
make PREFIX=%buildroot/usr \
	DOCDIR=%buildroot/usr/share/doc/%name-%version \
	EMACSDIR=%buildroot/usr/share/doc/%name-%version \
	VIMSYNDIR=%buildroot/usr/share/doc/%name-%version \
	install

%files
%doc %_docdir/%name-%version
%_bindir/*
%_man1dir/*
%_man5dir/*

%changelog
* Mon Nov 08 2010 Vladimir Lettiev <crux@altlinux.ru> 1.9.0-alt1.1
- rebuilt with perl 5.12

* Wed Jun 13 2007 Victor Forsyuk <force@altlinux.org> 1.9.0-alt1
- 1.9.0
- Installing emacs and vim syntax files is not worth added dependancies.
  Just package them as %%doc-files.

* Mon Oct 06 2003 Egor S. Orlov <oes@altlinux.ru> 1.7.0-alt2
- Fixed package intersections in mandirs

* Fri Oct 03 2003 Egor S. Orlov <oes@altlinux.ru> 1.7.0-alt1
- fixed requires
- Russian description

* Wed Sep 17 2003 Egor S. Orlov <oes@altlinux.ru> 1.7.0-alt0.3
- Fixed buildreq using --args=-bi
- Hasher build

* Mon Sep 15 2003 Egor S. Orlov <oes@altlinux.ru> 1.7.0-alt0.2
- Fixed requires 

* Fri Sep 12 2003 Egor S. Orlov <oes@altlinux.ru> 1.7.0-alt0.1
- Initial build for ALT
