%def_disable java
# don't use aspell as Abiword uses hanspell via libenchant
%def_disable aspell
%def_enable hunspell
%def_disable perl
%def_enable system_minisat

%define dictdir %_datadir/myspell

Name: link-grammar
Version: 5.4.2
Release: alt1

Summary: The link grammar parsing system for Unix
License: GPL-compatible
Group: Text tools
Url: http://www.link.cs.cmu.edu/link/

Source: http://www.abisource.com/downloads/%name/%version/%name-%version.tar.gz
Patch: %name-5.4.2-alt-man_build.patch

Requires: lib%name = %version-%release

BuildRequires: gcc-c++ autoconf-archive swig
BuildRequires: libedit-devel libsqlite3-devel zlib-devel
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
%setup
%patch

%build
%autoreconf
%configure \
	--with-hunspell-dictdir=%dictdir \
	%{?_disable_java:--disable-java-bindings} \
	%{subst_enable aspell} \
	%{subst_enable hunspell} \
	%{?_disable_system_minisat:--enable-sat-solver=bundled}
%make_build

%install
%makeinstall_std

%files
%_bindir/link-parser
%_man1dir/link-parser.1*
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
%exclude %_libdir/*.a

%if_enabled perl
%files -n perl-%name
%perl_vendor_privlib/*
%endif

%changelog
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

