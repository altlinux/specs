Name: libaacs
Version: 0.11.1
Release: alt1

Summary: BD AACS library
License: LGPL-2.1
Group: System/Libraries
Url: https://www.videolan.org/developers/libaacs.html

Source: %name-%version-%release.tar

BuildRequires: flex libgcrypt-devel

%description
%summary

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains the headers and libraries for libaacs development.

%prep
%setup
%ifarch %e2k
# the compiler is called with "-Werror=implicit-function-declaration"
# and there's a trick in "keydbcfg-parser.c":
#   GCC diagnostic ignored "-Wimplicit-function-declaration"
# which doesn't work for EDG frontend,
# and it stops compiling with an error.
sed -i "s/-Werror/-Wno-error/" configure.ac
%endif

%build
%autoreconf
%configure
%make_build

%install
%makeinstall
rm -v %buildroot%_libdir/libaacs.a

%files
%_bindir/aacs_info
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%changelog
* Thu Dec 01 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.1-alt1
- 0.11.1 released

* Wed Jan 12 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.11.0-alt1.1
- fixed build for Elbrus

* Mon Sep 20 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.0-alt1
- 0.11.0 released

* Mon Aug 30 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.1-alt4
- unpackaged static library dropped

* Fri Jul 06 2018 Michael Shigorin <mike@altlinux.org> 0.8.1-alt3
- worked around ftbfs on e2k

* Tue Oct 06 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.1-alt2
- rebuilt with recent libgcrypt

* Wed Apr 08 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.1-alt1
- 0.8.1 released

* Tue May 27 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.1-alt1
- 0.7.1 released

* Tue Sep 11 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.0-alt1
- 0.5.0 released

* Fri May 18 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.0-alt1
- 0.4.0 released

* Wed Mar 21 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.1-alt1
- 0.3.1 released

* Fri Dec 02 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.0-alt1
- 0.3.0 released

* Tue Oct 11 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt0.1
- 0.2 released

* Wed May 11 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt0.1
- initial
