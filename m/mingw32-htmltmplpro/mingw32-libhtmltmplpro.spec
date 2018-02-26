%define __strip %_mingw32_strip
%define __objdump %_mingw32_objdump

%define libname mingw32-libhtmltmplpro
%define origname htmltmplpro
%def_disable static

Name: mingw32-%origname
Version: 0.9509
Release: alt1

Summary: Windows MinGW HTML::Template compatible HTML template library
License: GPL2+ or Artistic
Group: System/Libraries
Url: http://sf.net/projects/html-tmpl-pro
Packager: Igor Vlasenko <viy@altlinux.org>

Source: htmltmplpro-%version.tar.gz

BuildArch: noarch
#BuildRequires: doxygen graphviz
BuildRequires(pre): rpm-build-mingw32
BuildRequires: mingw32-gcc
#BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-binutils
BuildRequires: mingw32-libpcre-devel-static


%package -n %libname
Summary: Windows MinGW HTML::Template compatible HTML template shared library
Summary(ru_RU.UTF-8): Windows MinGW Разделяемая библиотека для работы с шаблонами HTML::Template
Group: System/Libraries
Provides: %name = %version
Obsoletes: %name < %version

%package -n %libname-devel
Summary: Windows MinGW HTML::Template compatible HTML template library development environment
Group: Development/C
Provides: %name-devel = %version
Obsoletes: %name-devel < %version
Requires: %libname = %version-%release

%package -n %libname-devel-static
Summary: Windows MinGW HTML::Template compatible HTML template static library
Summary(ru_RU.UTF-8): Windows MinGW Вариант библиотеки htmltemplpro для статической компоновки
Group: Development/C
Provides: %name-devel-static = %version
Obsoletes: %name-devel-static < %version
Requires: %libname-devel = %version-%release

%description
The HTML::Template::Pro library is a portable template engine for templates 
that use syntax of known perl modules HTML::Template, HTML::Template::Expr 
and HTML::Template::Pro.

%_mingw32_description

%description -n %libname
The HTML::Template::Pro library is a portable template engine for templates 
that use syntax of known perl modules HTML::Template, HTML::Template::Expr 
and HTML::Template::Pro.

This package contains shared libraries.

%_mingw32_description

%description -n %libname-devel
The HTML::Template::Pro library is a portable template engine for templates 
that use syntax of known perl modules HTML::Template, HTML::Template::Expr 
and HTML::Template::Pro.

This package contains development libraries, include files and development
documentation required for developing applications which use perl-style
regular expressions.

%_mingw32_description

%description -n %libname-devel-static
The HTML::Template::Pro library is a portable template engine for templates 
that use syntax of known perl modules HTML::Template, HTML::Template::Expr 
and HTML::Template::Pro.

This package contains static development libraries required for developing
statically linked applications which use perl-style regular expressions.

%_mingw32_description

%prep
%setup -q -n %origname-%version

%build
autoreconf -fisv

%_mingw32_configure \
	--includedir=%_mingw32_includedir/%origname \
	%{subst_enable static} \
	--enable-static-libpcre \
	#
%make_build

%install
%make_install install DESTDIR=%buildroot

%files -n %libname
%_mingw32_bindir/lib%origname-*.dll

%files -n %libname-devel
#%doc doc/html
%doc API README
%_mingw32_includedir/%origname
%_mingw32_libdir/*.la
%_mingw32_libdir/lib%origname.dll.a
%_mingw32_libdir/pkgconfig/*.pc

%if_enabled static
%files -n %libname-devel-static
%_mingw32_libdir/lib%origname.a
%endif

%changelog
* Tue Feb 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.9509-alt1
- new version; see Changes

* Mon Dec 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.9508-alt1
- new version; see Changes

* Fri Dec 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.9507-alt1
- new version; see Changes

* Tue Oct 04 2011 Igor Vlasenko <viy@altlinux.ru> 0.9506-alt1
- new version; see Changes

* Fri Jul 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.9505-alt1
- new version; see Changes

* Tue Sep 28 2010 Igor Vlasenko <viy@altlinux.ru> 0.9504-alt1
- new version; see Changes

* Sat Aug 28 2010 Igor Vlasenko <viy@altlinux.ru> 0.9503-alt1
- new version; see Changes

* Thu Jun 17 2010 Igor Vlasenko <viy@altlinux.ru> 0.9502-alt1
- new version; see Changes

* Wed Jun 09 2010 Igor Vlasenko <viy@altlinux.ru> 0.9501-alt1
- new version; see Changes

* Fri May 21 2010 Igor Vlasenko <viy@altlinux.ru> 0.95-alt1
- new version; see Changes

* Tue Feb 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.94-alt1
- new version; see Changes

* Sun Nov 15 2009 Igor Vlasenko <viy@altlinux.ru> 0.93-alt1
- new version; see Changes

* Sun Nov 15 2009 Igor Vlasenko <viy@altlinux.ru> 0.92-alt1
- new version; see Changes

* Sat Oct 03 2009 Igor Vlasenko <viy@altlinux.ru> 0.92-alt2
- disabled static 

* Tue Sep 29 2009 Igor Vlasenko <viy@altlinux.ru> 0.92-alt1
- new version; see Changes

* Tue Sep 22 2009 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1
- new version; see Changes

* Sat Sep 12 2009 Igor Vlasenko <viy@altlinux.ru> 0.90-alt3
- release

* Fri Sep 11 2009 Igor Vlasenko <viy@altlinux.ru> 0.90-alt2
- rc2

* Mon Aug 31 2009 Igor Vlasenko <viy@altlinux.ru> 0.90-alt1
- new version; see Changes

* Sat Aug 29 2009 Igor Vlasenko <viy@altlinux.ru> 0.87-alt1
- new version; see Changes

* Sat Aug 22 2009 Igor Vlasenko <viy@altlinux.ru> 0.86-alt1
- new version; see Changes
