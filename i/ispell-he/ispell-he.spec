Summary: Hebrew dictionary for of ispell
Name: ispell-he
Version: 0.1
Release: alt5
Group: System/Internationalization
Source: ftp://ftp.ivrix.org/pub/ivrix/src/cmdline/spell/ispell-he-0.1.tar.bz2
Copyright: distributable
Requires: ispell
BuildRequires: ispell
Provides: ispell-dictionary
Packager: Igor Vlasenko <viy@altlinux.org>


%description
Hebrew Dictionaries for ispell. 
To check spelling in hebrew text use command:
ispell -d hebrew <file_name>

%prep
%setup  -q

%build
buildhash -s combined.txt hebrew.aff hebrew.hash
%install
mkdir -p $RPM_BUILD_ROOT%_libdir/ispell/
cp -avf hebrew.aff $RPM_BUILD_ROOT%_libdir/ispell
cp -avf hebrew.hash $RPM_BUILD_ROOT%_libdir/ispell


%files
%doc README
%_libdir/ispell/*

%changelog
* Mon May 12 2008 Igor Vlasenko <viy@altlinux.ru> 0.1-alt5
- fixed to be arch

* Fri Jul 14 2006 Igor Vlasenko <viy@altlinux.ru> 0.1-alt4
- fixed build for x86_64

* Tue Jul 11 2006 Igor Vlasenko <viy@altlinux.ru> 0.1-alt3
- rebuild with new ispell (fixes #7662 )

* Mon Feb 03 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 0.1-alt2
- rebuild

* Wed Jul 11 2001 AEN <aen@logic.ru> 0.1-alt1
- first build
