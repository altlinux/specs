Name: deroff
Version: 2.0
Release: alt1

Summary: Deroff removes roff constructs from documents
License: GPL
Group: Text tools
URL: http://www.moria.de/~michael/deroff
Source: %url/deroff-%version.tar.gz

%description
Deroff removes roff constructs from documents for the purpose of indexing,
spell checking etc.

%prep
%setup -q

%build
%configure
%make_build

%install
%__install -pD -m755 deroff $RPM_BUILD_ROOT%_bindir/deroff
%__install -pD -m644 deroff.1.en $RPM_BUILD_ROOT%_man1dir/deroff.1
%__install -pD -m644 de.mo $RPM_BUILD_ROOT%_datadir/locale/de/deroff.mo

%find_lang deroff

%files -f deroff.lang
%_bindir/*
%_man1dir/*

%changelog
* Mon Apr 04 2005 Victor Forsyuk <force@altlinux.ru> 2.0-alt1
- New version (now deroff supports tbl).
- Cleaning spec: parallel make, etc.

* Sat Feb 08 2003 Ott Alex <ott@altlinux.ru> 1.8-alt3
- fixing spec

* Sat Nov 02 2002 Ott Alex <ott@altlinux.ru> 1.8-alt1
- Initial build
