%def_with xql

Name: libxbsql
Version: 0.11
Release: alt5.1

Summary: An SQL wrapper for Xbase
Summary(uk_UA.UTF-8): SQL-обгортка для Xbase
Summary(ru_RU.UTF-8): SQL-обёртка для Xbase

License: LGPL
Group: Databases
Url: http://www.quaking.demon.co.uk/xbsql

Packager: Vitaly Lipatov <lav@altlinux.ru>

# FIXME: where is sources really?
Source: %name-%version.tar
Patch0: %name-0.11-configure.patch
Patch1: %name-0.11-namespace.patch

# Automatically added by buildreq on Tue Aug 15 2006
BuildRequires: gcc-c++ libncurses-devel libreadline-devel awk
BuildRequires: libxbase-devel >= 1.8.1

%description
%name is a wrapper library which provides an SQL-subset interface to
Xbase DBMS.

%description -l uk_UA.UTF-8
%name - це бібліотека-обгортка, яка забезпечує інтерфейс підмножини SQL
для Xbase DBMS.

%description -l ru_RU.UTF-8
%name - это библиотека-обёртка, которая обеспечивает интерфейс
подмножества SQL для Xbase DBMS.

%if_with xql
%package -n xql
Summary: CLI client for %name
Summary(uk_UA.UTF-8): CLI-клієнт для %name
Summary(ru_RU.UTF-8): CLI-клиент для %name
Group: Databases
Provides: %name-xql = %version-%release
Obsoletes: xbsql
Conflicts: xbsql

%description -n xql
This package contains a simple command-line client xql which can be
used as an example.

%description -n xql -l uk_UA.UTF-8
Цей пакет містить простий клієнт командного рядка xql, що може
використовуватись в якості зразка.

%description -n xql -l ru_RU.UTF-8
Этот пакет содержит простой клиент командной строки xql, который может
использоваться в качестве примера.
%endif

%package devel
Summary: Headers for %name
Summary(uk_UA.UTF-8): Заголовки для %name
Summary(ru_RU.UTF-8): Заголовки для %name
Group: Development/Other
Requires: libxbase-devel >= 1.8.1
Requires: %name = %version-%release

%description devel
This package contains headers for %name.

%description devel -l uk_UA.UTF-8
Цей пакет містить заголовки для %name.

%description devel -l ru_RU.UTF-8
Этот пакет содержит заголовки для %name.

%prep
%setup
%patch0 -p1 -b .orig
%patch1 -p1
touch -r configure.in.orig configure.in

%build
%configure \
    --enable-shared --disable-static \
    --with-pic

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build CFLAGS="%optflags" CXXFLAGS="%optflags"

%install
%makeinstall_std
%{?_without_xql:rm -rf %buildroot%_bindir}

%if_with xql
%files -n xql
%_bindir/*
%endif

%files
%_libdir/*.so.*

%files devel
%doc doc/* README AUTHORS TODO Announce
%_includedir/*
%_libdir/*.so

%changelog
* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt5.1
- Removed bad RPATH

* Sat Jun 26 2010 Vitaly Lipatov <lav@altlinux.ru> 0.11-alt5
- rewrite spec, rename main package to libxbsql

* Wed Mar 10 2010 Vitaly Lipatov <lav@altlinux.ru> 0.11-alt4
- cleanup spec, rebuild with libxbase 2.1.1

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.11-alt3.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libxbsql
  * postun_ldconfig for libxbsql

* Wed Sep 13 2006 Led <led@altlinux.ru> 0.11-alt3
- replaced xbsql-0.11-ncurses64.patch and dumb
  xbsql-0.11-ncurses64.patch with xbsql-0.11-configure.patch

* Tue Sep 12 2006 Led <led@altlinux.ru> 0.11-alt2
- fixed/cleaned up spec
- fixed License
- added xbsql-0.11-ncurses64.patch (from FC5)
- added xbsql-0.11-namespace.patch
- added xbsql-0.11-version.patch
- fixed Summaries and descriptions
- added ukrainian and russian Summaries and descriptions
- replaced package %name with xql

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.11-alt1.1
- Rebuilt with libreadline.so.5.

* Sat Jun 18 2005 Vitaly Lipatov <lav@altlinux.ru> 0.11-alt1
- first build for ALT Linux Sisyphus

* Sat Jun 5 2004 Spencer Anderson <sdander@oberon.ark.com> 0.11-5mdk
- correct %%Summary

* Sat Jun 5 2004 Spencer Anderson <sdander@oberon.ark.com> 0.11-4mdk
- rebuild
- spec cleaning

* Sun Jan 4 2004 Spencer Anderson <sdander@oberon.ark.com> 0.11-3mdk
- buildrequires libreadline-devel
- move some libs

* Thu Dec 25 2003 Spencer Anderson <sdander@oberon.ark.com> 0.11-2mdk
- include missing libraries
- buildrequires and requires

* Tue Nov 18 2003 Spencer Anderson <sdander@oberon.ark.com> 0.11-1mdk
- initial Mandrake release
- needed by rekall
