%def_disable java
# don't use aspell as Abiword uses hanspell via libenchant
%def_disable aspell
%def_enable hunspell

%define dictdir %_datadir/myspell

Name: link-grammar
Version: 4.7.4
Release: alt1

Summary: The link grammar parsing system for Unix
License: GPL-compatible
Group: Text tools
Url: http://www.link.cs.cmu.edu/link/

Source: http://www.abisource.com/downloads/%name/%version/%name-%version.tar.gz
Requires: lib%name = %version-%release

BuildRequires: gcc-c++
%{?_enable_aspell:BuildRequires:libaspell-devel}
%{?_enable_hunspell:BuildRequires:libhunspell-devel}

%description
The link grammar parsing system for Unix

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

%prep
%setup -q
[ ! -d m4 ] && mkdir m4

%build
%autoreconf -I ac-helpers
%configure \
	--with-hunspell-dictdir=%dictdir \
	%{?_disable_java:--disable-java-bindings} \
	%{subst_enable aspell} \
	%{subst_enable hunspell}


%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/link-parser
%_man1dir/link-parser.1*
%doc LICENSE README ChangeLog

%files -n lib%name
%dir %_datadir/%name/
%_datadir/%name/*
%_libdir/*.so.*

%files -n lib%name-devel
%dir %_includedir/%name/
%_includedir/%name/*
%_libdir/*.so
%_libdir/pkgconfig/%name.pc
%exclude %_libdir/*.a

%changelog
* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 4.7.4-alt1
- 4.7.4

* Wed Nov 10 2010 Yuri N. Sedunov <aris@altlinux.org> 4.6.7-alt1
- 4.6.7

* Wed Nov 25 2009 Yuri N. Sedunov <aris@altlinux.org> 4.6.5-alt1
- 4.6.5
- spec cleanup

* Wed Nov 23 2005 Vital Khilko <vk@altlinux.ru> 4.1.3-alt1
- Initial spec 

