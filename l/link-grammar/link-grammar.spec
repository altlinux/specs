%def_disable snapshot

%def_disable static
%{?_enable_static:%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}}
%def_disable java
# don't use aspell as Abiword uses hanspell via libenchant
%def_disable aspell
%def_enable hunspell
%def_disable perl
%def_disable system_minisat

%define dictdir %_datadir/myspell

Name: link-grammar
Version: 5.12.0
Release: alt1

Summary: The link grammar parsing system for Unix
License: BSD-3-Clause and LGPL-2.1
Group: Text tools
Url: https://github.com/opencog/link-grammar

%if_disabled snapshot
#Source: http://www.abisource.com/downloads/%name/%version/%name-%version.tar.gz
Source: %url/archive/%name-%version.tar.gz
%else
Vcs: https://github.com/opencog/link-grammar.git
Source: %name-%version.tar
%endif

Requires: lib%name = %version-%release

BuildRequires: gcc-c++ autoconf-archive swig flex
BuildRequires: libedit-devel libsqlite3-devel zlib-devel
BuildRequires: libpcre2-devel
%{?_enable_aspell:BuildRequires:libaspell-devel}
%{?_enable_hunspell:BuildRequires:libhunspell-devel}
%{?_enable_perl:BuildRequires: perl-devel}
%{?_enable_system_minisat:BuildRequires:libminisat-devel}

%description
The link grammar parsing system for Unix.

%package -n lib%name
Summary: Library files for %name
Group: System/Libraries

%description -n lib%name
Library files for %name

%package -n lib%name-devel
Summary: Development files needed to build applications with %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Development files needed to build applications with %name.

%package -n perl-%name
Summary: Perl bindings for %name
Group: Development/Perl
Requires: lib%name = %version-%release

%description -n perl-%name
Perl bindings for %name library.

%prep
%setup %{?_disable_snapshot:-n %name-%name-%version}

%build
%autoreconf
%add_optflags %(getconf LFS_CFLAGS)
%configure \
	%{subst_enable static} \
	--with-hunspell-dictdir=%dictdir \
	%{?_disable_java:--disable-java-bindings} \
	%{subst_enable aspell} \
	%{subst_enable hunspell} \
	%{?_disable_system_minisat:--enable-sat-solver=bundled}
%nil
%make_build

%install
%makeinstall_std

%files
%_bindir/link-parser
%_bindir/link-generator
%_man1dir/link-parser.1*
%_man1dir/link-generator.1*
%doc LICENSE README* ChangeLog

%files -n lib%name
%dir %_datadir/%name/
%_datadir/%name/*
%_libdir/*.so.*

%files -n lib%name-devel
%dir %_includedir/%name/
%_includedir/%name/*
%_libdir/*.so
%_pkgconfigdir/%name.pc
#%exclude %_libdir/*.a

%if_enabled perl
%files -n perl-%name
%perl_vendor_privlib/*
%endif

%changelog
* Tue Nov 29 2022 Yuri N. Sedunov <aris@altlinux.org> 5.12.0-alt1
- 5.12.0

* Wed Oct 12 2022 Yuri N. Sedunov <aris@altlinux.org> 5.11.0-alt1
- 5.11.0

* Fri Jul 01 2022 Yuri N. Sedunov <aris@altlinux.org> 5.10.5-alt1
- 5.10.5

* Fri Aug 27 2021 Yuri N. Sedunov <aris@altlinux.org> 5.9.1-alt1.1
- disabled build of static libraries

* Tue Jul 06 2021 Yuri N. Sedunov <aris@altlinux.org> 5.9.1-alt1
- 5.9.1

* Fri Jan 15 2021 Yuri N. Sedunov <aris@altlinux.org> 5.8.1-alt1
- 5.8.1

* Sat Sep 05 2020 Yuri N. Sedunov <aris@altlinux.org> 5.8.0-alt2
- rebuilt with bundled minisat

* Thu Mar 19 2020 Yuri N. Sedunov <aris@altlinux.org> 5.8.0-alt1
- 5.8.0
- fixed License tag

* Sat Jul 28 2018 Yuri N. Sedunov <aris@altlinux.org> 5.5.1-alt1
- updated to 5.5.1-4-g58c3121

* Sun May 13 2018 Yuri N. Sedunov <aris@altlinux.org> 5.5.0-alt1
- 5.5.0

* Sun Nov 26 2017 Yuri N. Sedunov <aris@altlinux.org> 5.4.2-alt1
- 5.4.2

* Thu Apr 27 2017 Yuri N. Sedunov <aris@altlinux.org> 5.3.16-alt1
- 5.3.16

* Tue Apr 18 2017 Yuri N. Sedunov <aris@altlinux.org> 5.3.15-alt1
- 5.3.15

* Sun Jan 22 2017 Yuri N. Sedunov <aris@altlinux.org> 5.3.14-alt1
- 5.3.14

* Mon Nov 28 2016 Yuri N. Sedunov <aris@altlinux.org> 5.3.13-alt1
- 5.3.13

* Sat Oct 01 2016 Yuri N. Sedunov <aris@altlinux.org> 5.3.11-alt1
- 5.3.11

* Sun Jun 29 2014 Yuri N. Sedunov <aris@altlinux.org> 5.0.8-alt1
- 5.0.8

* Fri Jun 06 2014 Yuri N. Sedunov <aris@altlinux.org> 4.8.6-alt1
- 4.8.6

* Wed Nov 20 2013 Yuri N. Sedunov <aris@altlinux.org> 4.8.0-alt1
- 4.8.0

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 4.7.4-alt1
- 4.7.4

* Wed Nov 10 2010 Yuri N. Sedunov <aris@altlinux.org> 4.6.7-alt1
- 4.6.7

* Wed Nov 25 2009 Yuri N. Sedunov <aris@altlinux.org> 4.6.5-alt1
- 4.6.5
- spec cleanup

* Wed Nov 23 2005 Vital Khilko <vk@altlinux.ru> 4.1.3-alt1
- Initial spec 

