Name: cunit
Version: 0.7.5
Release: alt7

Summary: C Unit Tester
License: LGPL
Group: Development/C
Url: http://www.gethos.net/opensource/cunit


Source0: %url/%name-%version.tar
Patch0: %name-%version-alt-makefile.patch
Patch1: %name-%version-alt-trivial.patch
Patch2: %name-%version-alt-pedantic.patch

%description 
This is a Unit Test framework for 'C'.

The emphasis in this framework is to make test writing as simple as possible.
As such all the developer needs to do is write test functions, define the
suite layout and compile the code into a shared object with a name of the form
libtest_*.so.

The unit test runner finds all libtest_*.so files under the directory it is
run from, compiles a list of tests defined in the corresponding suites and
runs all the tests. The output is displayed directly to the console using
colours for added readability. It shows the progress, results and bottom line.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure
make

%install
%__mkdir_p $RPM_BUILD_ROOT%_includedir $RPM_BUILD_ROOT%_bindir $RPM_BUILD_ROOT%_libdir
%__install -m755 bin/cunit $RPM_BUILD_ROOT%_bindir
%__install -m644 src/libcunit/unittester.h $RPM_BUILD_ROOT%_includedir
%__install -m644 build/libcunit/libcunit.a $RPM_BUILD_ROOT%_libdir
%__install -m644 build/statictester/libcunitstatic.a $RPM_BUILD_ROOT%_libdir


%files
%doc CHANGELOG INSTALL README src/trivsuite/trivsuite.c
%_bindir/*
%_includedir/*
%_libdir/lib*


%changelog
* Tue Apr 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.5-alt7
- fix build

* Wed Mar 26 2008 Alexey Voinov <voins@altlinux.ru> 0.7.5-alt6
- use -fPIC for compiling

* Tue Mar 25 2008 Alexey Voinov <voins@altlinux.ru> 0.7.5-alt5
- don't try strip debug info from header files

* Thu Dec 27 2007 Alexey Voinov <voins@altlinux.ru> 0.7.5-alt4
- libraries for creating statically-linked test-runners included

* Tue Sep 19 2007 Alexey Voinov <voins@altlinux.ru> 0.7.5-alt3
- fixed warning for tests compiled with -pedantic

* Tue Sep 18 2007 Alexey Voinov <voins@altlinux.ru> 0.7.5-alt2
- fixed build problem
- fixed example testsuite

* Sun Jul 24 2005 Alexey Voinov <voins@altlinux.ru> 0.7.5-alt1
- new version (0.7.5)

* Sun Mar 13 2005 Alexey Voinov <voins@altlinux.ru> 0.7.3-alt1
- new version (0.7.3)

* Thu Oct 07 2004 Alexey Voinov <voins@altlinux.ru> 0.6.9-alt1
- new version (0.6.9)

* Wed Sep 15 2004 Alexey Voinov <voins@altlinux.ru> 0.6.8-alt1
- initial build
