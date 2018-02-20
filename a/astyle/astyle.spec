Name: astyle
Version: 3.1
Release: alt1

%global majorversion    3
%global soversion       %version

Summary: A small, fast automatic indentation filter for C/C++/Java code
License: GPL
Group: Development/Other

Url: http://%name.sourceforge.net/
Source: %{name}_%{version}_linux.tar.gz

BuildRequires: gcc-c++ java-devel-default

# Make the astyle-lib usable for arduino
Patch0: astyle-arduino.patch

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
%patch0 -p1

%build
chmod a-x src/*
chmod a-x doc/*

pushd src
    # it's much easier to compile it here than trying to fix the Makefile
    g++ $RPM_OPT_FLAGS -DASTYLE_LIB -DASTYLE_JNI -fPIC -I/usr/lib/jvm/java/include -I/usr/lib/jvm/java/include/linux -c ASBeautifier.cpp ASEnhancer.cpp ASFormatter.cpp ASResource.cpp astyle_main.cpp
    g++ -shared -o libastyle.so.%soversion *.o -Wl,-soname,libastyle.so.%majorversion
    ln -s libastyle.so.%soversion libastyle.so
    g++ $RPM_OPT_FLAGS -c ASLocalizer.cpp astyle_main.cpp
    g++ $RPM_OPT_FLAGS -o astyle ASLocalizer.o astyle_main.o -L. -lastyle
popd

%install
pushd src
    mkdir -p $RPM_BUILD_ROOT{%_bindir,%_libdir,%_includedir}

    install -p -m 755 astyle $RPM_BUILD_ROOT%_bindir
    install -p -m 755 libastyle.so.%soversion $RPM_BUILD_ROOT%_libdir
    cp -P libastyle.so $RPM_BUILD_ROOT%_libdir
    install -p -m 644 astyle.h $RPM_BUILD_ROOT%_includedir
popd

# hardcoded path! for --help
mkdir -p %buildroot%_datadir/doc/%name/html
install -m 644 doc/*.html %buildroot%_datadir/doc/%name/html/

%files
%doc %_datadir/doc/%name
%_bindir/%name

%files -n lib%name
%_libdir/lib*.so.*

%files -n lib%name-devel
%_libdir/lib%name.so
%_includedir/%name.h

%changelog
* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 3.1-alt1
- Autobuild version bump to 3.1

* Sun Nov 26 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt2
- NMU:
- fixed bug: astyle --help files not found (hardcoded path to html doc)
- added JNI support for arduino (closes: #34238)
- library should be named lib%name.so.* (closes: #34235)

* Tue Aug 15 2017 Fr. Br. George <george@altlinux.ru> 3.0.1-alt1
- Autobuild version bump to 3.0.1

* Mon May 29 2017 Fr. Br. George <george@altlinux.ru> 3.0-alt1
- Autobuild version bump to 3.0
- Fix build

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

* Thu Sep 16 1999 Dmitry V. Levin <ldv@fandra.org>
- initial revision
