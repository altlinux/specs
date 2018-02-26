Name: astyle
Version: 2.02.1
Release: alt1

Summary: A small, fast automatic indentation filter for C/C++/Java code
License:: GPL
Group: Development/Other

Url: http://%name.sourceforge.net/
Source: %{name}_%{version}_linux.tar.gz

# Automatically added by buildreq on Tue Apr 24 2012
# optimized out: libstdc++-devel
BuildRequires: gcc-c++

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
%make_build -C src -f ../build/gcc/Makefile

%install
install -p -m755 -D src/bin/%name %buildroot%_bindir/%name

%files
%doc doc/*
%_bindir/%name

%changelog
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
