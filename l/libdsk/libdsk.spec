# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define sname         dsk

%define major         5
%define libname       lib%{sname}%{major}
%define libname_devel lib%{sname}-devel

Name:           lib%sname
Summary:        A library for accessing floppy drives and disk images transparently
Version:        1.5.19
Release:        alt1_1
License:        LGPLv2+
Group:          System/Libraries
URL:            https://www.seasip.info/Unix/LibDsk/index.html
Source:         https://www.seasip.info/Unix/LibDsk/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  lyx
Source44: import.info

%description
LibDsk is a library intended to give transparent access to floppy drives and
to the "disc image files" used by emulators to represent floppy drives.

%package -n %{libname}
Summary:        A library for accessing floppy drives and disk images transparently
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}

%description -n %{libname}
LibDsk is a library intended to give transparent access to floppy drives and
to the "disc image files" used by emulators to represent floppy drives.

Install the libdsk package if you need to manipulate DSK files. You should
also install the libdsk-progs package.

%package -n %{libname_devel}
Summary:        Development files for programs which will use the libdsk library
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:       %name-devel = %{version}-%{release}
Obsoletes:      %{_lib}dsk-static-devel < 1.4.2-2

%description -n %{libname_devel}
This package contains the header files and documentation necessary for
development of programs that will use the libdsk library to load and save
DSK format disc image files.

You should install this package if you need to develop programs which will
use the libdsk library functions for loading and saving DSK format disc
image files. You'll also need to install the libdsk package.

%package progs
Summary:        Programs for manipulating DSK format disc image files
Group:          Emulators

%description progs
The libdsk-progs package contains various programs for manipulating
DSK format disc image files.

Install this package if you need to manipulate DSK format disc image
files. You'll also need to install the libdsk package.

%prep
%setup -q


# make autoreconf happy
%define automake_opts foreign
sed -i -e 's,\(^AM_INIT_AUTOMAKE\)\((\[\(.*\)\])\|(\(.*\))\|.*\),\1([%{automake_opts} \3\4]),' configure.ac

%build
# fix build on aarch64
autoreconf -vfi

%configure --disable-static
%make_build

%install
%makeinstall_std

# we don't want these
find %{buildroot} -name '*.la' -delete

%files -n %{libname}
%doc ChangeLog doc/COPYING doc/README doc/TODO
%{_libdir}/lib*.so.%{major}*

%files -n %{libname_devel}
%doc doc/COPYING doc/cfi.html doc/libdsk.*
%{_libdir}/lib*.so
%{_includedir}/*.h

%files progs
%doc doc/COPYING
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*


%changelog
* Wed Apr 19 2023 Igor Vlasenko <viy@altlinux.org> 1.5.19-alt1_1
- update by mgaimport

* Thu Mar 25 2021 Igor Vlasenko <viy@altlinux.org> 1.5.15-alt1_1
- update by mgaimport

* Wed Jan 13 2021 Igor Vlasenko <viy@altlinux.ru> 1.5.14-alt1_1
- update by mgaimport

* Thu Nov 05 2020 Igor Vlasenko <viy@altlinux.ru> 1.5.12-alt1_2
- picked up from orphaned

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.2.1-alt2.qa2
- NMU: rebuilt for debuginfo.

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Wed Nov 18 2009 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt2
- cleanup spec

* Tue Nov 04 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version 1.2.1 (with rpmrb script)

* Sun Jul 29 2007 Vitaly Lipatov <lav@altlinux.ru> 1.1.14-alt1
- new version 1.1.14 (with rpmrb script)

* Sun May 27 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- restored from orphaned
- fix Source Url, add packager, remove COPYING, INSTALL

* Mon Dec 15 2003 Sir Raorn <raorn@altlinux.ru> 1.1.0-alt2
- devel-static and *.la fixes

* Mon Sep 29 2003 Sir Raorn <raorn@altlinux.ru> 1.1.0-alt1
- Built for Sisyphus

