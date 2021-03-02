Name: guile22
Version: 2.2.7
Release: alt1

Summary: A GNU implementation of Scheme
License: GPL
Group: Development/Scheme
Url: http://www.gnu.org/software/guile/ 

Source: %name-%version-%release.tar

BuildRequires: libltdl-devel libgmp-devel libunistring-devel
BuildRequires: libffi-devel libgc-devel libreadline-devel
BuildRequires: flex makeinfo
BuildRequires: /proc /dev/pts

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
# should ease transition to default devel, to be removed soon
Requires: guile-devel

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
sed -i 's,/usr/bin/guile,/usr/bin/guile22,' \
   %buildroot%_bindir/guild %buildroot%_bindir/guile-config

mv %buildroot%_bindir/guild %buildroot%_bindir/guild22
mv %buildroot%_bindir/guile %buildroot%_bindir/guile22
mv %buildroot%_bindir/guile-config %buildroot%_bindir/guile22-config
mv %buildroot%_bindir/guile-snarf %buildroot%_bindir/guile22-snarf
rm %buildroot%_bindir/guile-tools
mv %buildroot%_man1dir/guile.1 %buildroot%_man1dir/guile22.1

%add_findreq_skiplist %_bindir/guile22-config

%check
make check

%files
%_bindir/guile22
%_libdir/libguile-2.2.so.*
%exclude %_libdir/libguile-2.2.so.*-gdb.scm
%_libdir/guile/2.2
%_datadir/guile/2.2
%_man1dir/guile22.1*

%files devel
%_bindir/guild22
%_bindir/guile22-config
%_bindir/guile22-snarf
%_includedir/guile/2.2
%_libdir/libguile-2.2.so
%_datadir/aclocal/guile.m4
%_pkgconfigdir/guile-2.2.pc
%_infodir/*.info*

%changelog
* Wed Sep 09 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.7-alt1
- 2.2.7 released

* Fri Aug 10 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.4-alt3
- guile22-devel should not be included as direct BR, use guile-devel

* Thu Aug 09 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.4-alt2
- get rid of alternatives

* Mon Jul 30 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.4-alt1
- 2.2.4 released

* Fri May 12 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.2-alt1
- 2.2.2 released

* Thu Apr 20 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.1-alt1
- 2.2.1 released

* Wed Apr 12 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.0-alt2
- fix regex module

* Fri Mar 17 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.0-alt1
- initial
