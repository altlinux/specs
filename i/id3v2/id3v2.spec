Name: id3v2
Version: 0.1.12
Release: alt2

Summary:Command line id3v2 tag editor
Summary(ru_RU.UTF-8): Утилита редактирования ID3 тэгов v2

License: GPLv2+
Group: Sound
Url: http://id3v2.sourceforge.net

Source: http://prdownloads.sf.net/%name/%version/%name-%version.tar

BuildPreReq: id3lib-devel

# Automatically added by buildreq on Sun Jan 12 2003
BuildRequires: gcc-c++ help2man id3lib-devel libstdc++-devel zlib-devel

%description
id3v2 is a command line tool to add, modify, remove, or view ID3v2
tags, as well as convert or list ID3v1 tags.  ID3 tags are commonly
embedded in compressed music files and are the standard way to more
fully describe the work than would normally be allowed by putting the
information in the filename.

%description -l ru_RU.UTF-8
%name - утилита командной строки, предназначенная для редактирования ID3
тэгов v2 (http://www.id3v2.org).

%prep
%setup

%build
# a strange person released source code with built binaries
make clean

CXXFLAGS="$RPM_OPT_FLAGS" %make_build

%install
%__install -pD -m755 %name %buildroot/%_bindir/%name
%__install -pD -m644 %name.1 %buildroot/%_man1dir/%name.1

%files
%_bindir/%name
%_man1dir/*
%doc README

%changelog
* Mon Mar 31 2014 Vitaly Lipatov <lav@altlinux.ru> 0.1.12-alt2
- build to ALT Linux Sisyphus again
- cleanup spec

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.12-alt1_7
- update to new release by fcimport

* Fri Mar 08 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.12-alt1_6
- update to new release by fcimport

* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.12-alt1_5
- initial fc import

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.1.9-alt1.1
- Rebuilt with libstdc++.so.6.

* Fri Mar 07 2003 Andrey Astafiev <andrei@altlinux.ru> 0.1.9-alt1
- 0.1.9.

* Mon Jan 13 2003 Andrey Astafiev <andrei@altlinux.ru> 0.1.7-alt4
- rebuilt with id3lib-3.8.2.

* Wed Nov 13 2002 Andrey Astafiev <andrei@altlinux.ru> 0.1.7-alt3
- rebuilt with id3lib-3.8.1.

* Tue Sep 24 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.1.7-alt2
- rebuild with gcc-3.2, id3lib-3.8.0-alt3 requires.

* Tue Apr 23 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.1.7-alt1
- new version.

* Wed Jan 9 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.1.4-alt1
- First build for Sisyphus.
