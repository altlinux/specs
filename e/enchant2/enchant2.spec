%def_disable snapshot
%define _name enchant
%define api_ver 2

%def_enable aspell
%def_disable voikko
%def_disable relocatable
%def_disable check

Name: %_name%api_ver
Version: 2.3.4
Release: alt1

Summary: An Enchanting Spell Checking Program
Group: Text tools
License: LGPL-2.1
Url: https://abiword.github.io/%_name/

%if_disabled snapshot
Source: https://github.com/AbiWord/%_name/releases/download/v%version/%_name-%version.tar.gz
%else
Vcs: https://github.com/AbiWord/enchant.git
Source: %_name-%version.tar
%endif

Requires:  lib%name = %version-%release

BuildRequires: gcc-c++ glib2-devel libdbus-glib-devel libhunspell-devel
BuildRequires: groff
%{?_enable_aspell:BuildRequires: libaspell-devel}
%{?_enable_voikko:BuildRequires: libvoikko-devel}
%{?_enable_check:BuildRequires: libunittest-cpp-devel}

%description
This package contains simple programs that wrap other spell checking backends,
including an Ispell compatible script.

%package -n lib%name
Summary: An Enchanting Spell Checking Library
Group: System/Libraries

%description -n lib%name
A library that wraps other spell checking backends.

%package -n lib%name-devel
Summary: Support files necessary to compile applications with libenchant.
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
Libraries, headers, and support files necessary to compile applications
using libenchant.

%prep
%setup -n %_name-%version
# relax autoconf version
sed -i 's|\(AC_PREREQ(\[2.\)71|\169|' configure.ac

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure --disable-static \
	--disable-gcc-warnings \
	%{subst_enable relocatable} \
	--with-hunspell-dir=%_datadir/myspell \
	%{?_enable_aspell:--with-aspell-dir=%_libdir/aspell}
%make_build pkgdatadir=%_datadir/%_name-%api_ver

%install
%makeinstall_std pkgdatadir=%_datadir/%_name-%api_ver

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%make -k check VERBOSE=1

%files
%_bindir/*
%_man1dir/*
%_man5dir/*
%doc src/*.html

%files -n lib%name
%_libdir/*.so.*
%dir %_libdir/%_name-%api_ver
%_libdir/%_name-%api_ver/*.so
%_datadir/%_name-%api_ver/
%doc AUTHORS README NEWS

%exclude %_libdir/%_name-%api_ver/*.la

%files -n lib%name-devel
%_includedir/%_name-%api_ver/
%_libdir/*.so
%_pkgconfigdir/%_name-%api_ver.pc

%changelog
* Mon Feb 20 2023 Yuri N. Sedunov <aris@altlinux.org> 2.3.4-alt1
- 2.3.4

* Sat Apr 16 2022 Yuri N. Sedunov <aris@altlinux.org> 2.3.3-alt1
- 2.3.3

* Sun Dec 05 2021 Yuri N. Sedunov <aris@altlinux.org> 2.3.2-alt1
- 2.3.2

* Wed Aug 11 2021 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt1
- 2.3.1

* Tue Jun 15 2021 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0

* Wed Dec 23 2020 Yuri N. Sedunov <aris@altlinux.org> 2.2.15-alt1
- 2.2.15

* Sun Dec 13 2020 Yuri N. Sedunov <aris@altlinux.org> 2.2.14-alt1
- 2.2.14

* Tue Nov 03 2020 Yuri N. Sedunov <aris@altlinux.org> 2.2.13-alt1
- 2.2.13

* Tue Oct 27 2020 Yuri N. Sedunov <aris@altlinux.org> 2.2.12-alt1
- 2.2.12

* Tue Sep 08 2020 Yuri N. Sedunov <aris@altlinux.org> 2.2.11-alt1
- 2.2.11

* Wed Sep 02 2020 Yuri N. Sedunov <aris@altlinux.org> 2.2.10-alt1
- 2.2.10

* Sat Aug 22 2020 Yuri N. Sedunov <aris@altlinux.org> 2.2.9-alt1
- 2.2.9

* Wed Mar 04 2020 Yuri N. Sedunov <aris@altlinux.org> 2.2.8-alt1
- 2.2.8

* Mon Sep 23 2019 Yuri N. Sedunov <aris@altlinux.org> 2.2.7-alt1
- 2.2.7

* Fri Sep 06 2019 Yuri N. Sedunov <aris@altlinux.org> 2.2.6-alt1
- 2.2.6

* Tue Jul 02 2019 Yuri N. Sedunov <aris@altlinux.org> 2.2.5-alt1
- 2.2.5

* Tue Jun 18 2019 Yuri N. Sedunov <aris@altlinux.org> 2.2.4-alt1
- 2.2.4

* Thu Sep 13 2018 Yuri N. Sedunov <aris@altlinux.org> 2.2.3-alt2
- rebuilt with hunspell-1.6.2

* Thu Feb 15 2018 Yuri N. Sedunov <aris@altlinux.org> 2.2.3-alt1
- 2.2.3

* Sat Jan 06 2018 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Fri Dec 29 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Sat Dec 09 2017 Yuri N. Sedunov <aris@altlinux.org> 2.1.4-alt0.1
- first build for Sisyphus (v2.1.3-10-g6f9d407)

