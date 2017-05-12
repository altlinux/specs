Name: guile22
Version: 2.2.2
Release: alt1

Summary: A GNU implementation of Scheme
License: GPL
Group: Development/Scheme
Url: http://www.gnu.org/software/guile/ 

Source: %name-%version-%release.tar

Provides: /usr/bin/guile

BuildRequires: libltdl-devel libgmp-devel libunistring-devel
BuildRequires: libffi-devel libgc-devel libreadline-devel
BuildRequires: flex makeinfo

%description
Guile is an implementation of the Scheme programming language, packaged
as a library that can be linked into applications to give them their own
extension language.  Guile supports other languages as well, giving
users of Guile-based applications a choice of languages.

%package devel
Summary: A Guile development package
Group: Development/Scheme
Requires: %name = %version-%release
Conflicts: guile14-devel guile16-devel guile18-devel guile20-devel

%description devel
Guile is an implementation of the Scheme programming language, packaged
as a library that can be linked into applications to give them their own
extension language.  Guile supports other languages as well, giving
users of Guile-based applications a choice of languages.

This package provides Guile development tools, headers and libraries.

%prep
%setup
echo %version > .tarball-version

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std
mv %buildroot%_bindir/guile %buildroot%_bindir/guile22
mv %buildroot%_man1dir/guile.1 %buildroot%_man1dir/guile22.1
install -pm0644 -D guile.alternatives %buildroot%_altdir/%name
install -pm0644 -D guile.macros %buildroot%_rpmmacrosdir/guile

%add_findreq_skiplist %_bindir/guile-config

%files
%_altdir/%name
%_bindir/guile22
%_libdir/libguile-2.2.so.*
%exclude %_libdir/libguile-2.2.so.*-gdb.scm
%_libdir/guile/2.2
%_datadir/guile/2.2
%_man1dir/guile22.1*

%files devel
%_bindir/guild
%_bindir/guile-config
%_bindir/guile-snarf
%_bindir/guile-tools
%_includedir/guile/2.2
%_libdir/libguile-2.2.so
%_datadir/aclocal/guile.m4
%_pkgconfigdir/guile-2.2.pc
%_rpmmacrosdir/guile
%_infodir/*.info*

%changelog
* Fri May 12 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.2-alt1
- 2.2.2 released

* Thu Apr 20 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.1-alt1
- 2.2.1 released

* Wed Apr 12 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.0-alt2
- fix regex module

* Fri Mar 17 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.0-alt1
- initial
