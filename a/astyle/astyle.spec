Name: astyle
Version: 2.06
Release: alt1

Summary: A small, fast automatic indentation filter for C/C++/Java code
License: GPL
Group: Development/Other

Url: http://%name.sourceforge.net/
Source: %{name}_%{version}_linux.tar.gz

BuildRequires: gcc-c++

%package -n lib%name
Group: Development/C++
Summary: Separated dynamc library for linking with astyle
%description -n lib%name
Separated dynamc library for linking with astyle

%package -n lib%name-devel
Group: Development/C++
Summary: Separated dynamc library for linking with astyle (development environment)
%description -n lib%name-devel
Separated dynamc library for linking with astyle (development environment)

%description
Artistic Style is a reindenter and reformatter of C++, C and Java source code.

When indenting source code, we as programmers have a tendency to use
both spaces and tab characters to create the wanted
indentation. Moreover, some editors by default insert spaces instead
of tabs when pressing the tab key. Since the NUMBER of space
characters showed on screen for each tab character in the source code
changes between editors (until the user sets up the number to his
liking...), one of the standard problems facing programmers when
moving from one source code editor to another is that code containing
both spaces and tabs that was up to now perfectly indented, suddently
becomes a mess to look at when changing to another editor.

Artistic Style solves this problem by providing a series of filters,
written in C++, that automatically reindent & reformat C/C++/Java
source files. These can be used from a command line, or it can be
incorporated as classes in another C++ program.

%prep
%setup -n %name

%build
%make_build CFLAGS=-O2 -C src -f ../build/gcc/Makefile shareddebug astyled

%install
install -D src/bin/%{name}d %buildroot%_bindir/%name
install -d %buildroot%_libdir/
install src/bin/lib* %buildroot%_libdir/
( cd %buildroot%_libdir; ln -s lib* lib%name.so )
install -D src/%name.h %buildroot%_includedir/%name.h

%files
%doc doc/*
%_bindir/%name

%files -n lib%name
%_libdir/lib*.*.so

%files -n lib%name-devel
%_libdir/lib%name.so
%_includedir/%name.h

%changelog
* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 2.06-alt1
- Autobuild version bump to 2.06

* Wed Dec 14 2016 Fr. Br. George <george@altlinux.ru> 2.05.1-alt2
- Build isolated shared library (closes: #32855)

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 2.05.1-alt1
- Autobuild version bump to 2.05.1

* Sun Jan 12 2014 Fr. Br. George <george@altlinux.ru> 2.04-alt1
- Autobuild version bump to 2.04

* Mon May 20 2013 Fr. Br. George <george@altlinux.ru> 2.03-alt1
- Autobuild version bump to 2.03

* Wed Apr 25 2012 Fr. Br. George <george@altlinux.ru> 2.02.1-alt1
- Autobuild version bump to 2.02.1
- Skip a lot of version upgrades

* Fri May 30 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 1.22-alt1
- 1.22

* Tue Jan 25 2005 Stanislav Ievlev <inger@altlinux.org> 1.15.3-alt7
- really apply previous fix

* Thu Jan 13 2005 Stanislav Ievlev <inger@altlinux.org> 1.15.3-alt6
- ready for gcc3.4

* Mon Apr 14 2003 Stanislav Ievlev <inger@altlinux.ru> 1.15.3-alt5
- added patch from Alexey Voinov <voins at altlinux dot ru>

* Fri Mar 21 2003 Stanislav Ievlev <inger@altlinux.ru> 1.15.3-alt4
- remove special processing for: lock,set,get

* Wed Jan 15 2003 Stanislav Ievlev <inger@altlinux.ru> 1.15.3-alt3
- added buildreq

* Wed Sep 04 2002 Stanislav Ievlev <inger@altlinux.ru> 1.15.3-alt2
- rebuild with gcc3

* Fri Aug 02 2002 Stanislav Ievlev <inger@altlinux.ru> 1.15.3-alt1
- 1.15.3

* Thu Nov 29 2001 Stanislav Ievlev <inger@altlinux.ru> 1.14.1-alt1
- 1.14.1

* Mon Oct 16 2000 Dmitry V. Levin <ldv@fandra.org> 1.11.6-ipl1mdk
- 1.11.6

* Tue Sep 16 1999 Dmitry V. Levin <ldv@fandra.org>
- initial revision
