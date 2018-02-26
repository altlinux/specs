Summary: Belarusian dictionary for of ispell

Name: ispell-be
Version: 0.2
Release: alt1

Packager: Igor Vlasenko <viy@altlinux.ru>

Group: System/Internationalization
Source: http://www.mova.org/bellinux/ispell-be-0.2.tar.gz
URL: http://mova.linux.by/
License: GPL
Requires: ispell
BuildRequires: ispell
#ENDIAN dependent!
#NO BuildArchitectures: noarch
Provides: ispell-dictionary

%description
Belarusian Dictionaries for ispell.
To check spelling in belarusian text (in cp1251) use command:
ispell -d belarusian <file_name>

%prep
%setup -q -n ispell-be

%build
cat belarusian.stems belarusian.lemmas >belarusian.sml
buildhash belarusian.sml belarusian.aff belarusian.hash

%install
mkdir -p $RPM_BUILD_ROOT%_libdir/ispell/
cp -avf belarusian.aff $RPM_BUILD_ROOT%_libdir/ispell/belarusian.aff
cp -avf belarusian.hash $RPM_BUILD_ROOT%_libdir/ispell/belarusian.hash

%files
%doc CREDITS INSTALL ispell.el
%_libdir/ispell/*

%changelog
* Mon Apr 14 2008 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1
- new version

* Thu Jul 07 2005 Igor Vlasenko <viy@altlinux.org> 0.1-ipl6mdk
- rebuild with ispell-3.2

* Mon Nov 11 2002 Stanislav Ievlev <inger@altlinux.ru> 0.1-ipl5mdk
- rebuild

* Wed Jun 19 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.1-ipl4mdk
- Removed requires to locales-be
- Some spec cleanup

* Wed Jun 13 2001 AEN <aen@logic.ru> 0.1-ipl3mdk
- provides ispell-dictionary

* Wed Dec 06 2000 AEN <aen@logic.ru>
- build for RE

* Mon Oct 9 2000 AEN <aen@logic.ru>
- first build
