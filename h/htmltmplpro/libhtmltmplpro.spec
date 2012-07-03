%def_disable static
#def_enable debug

%define libname libhtmltmplpro
Name: htmltmplpro
Version: 0.9509
Release: alt1

Summary: HTML::Template compatible HTML template library
License: GPL2+ or Artistic
Group: System/Libraries
Url: http://sf.net/projects/html-tmpl-pro
Packager: Igor Vlasenko <viy@altlinux.org>

Source: htmltmplpro-%version.tar.gz

BuildRequires: gcc libpcre-devel doxygen graphviz

%package -n %libname
Summary: HTML::Template compatible HTML template shared library
Summary(ru_RU.UTF-8): Разделяемая библиотека для работы с шаблонами HTML::Template
Group: System/Libraries
Provides: %name = %version
Obsoletes: %name < %version

%package -n lib%name-devel
Summary: HTML::Template compatible HTML template library development environment
Group: Development/C
Provides: %name-devel = %version
Obsoletes: %name-devel < %version
Requires: %libname = %version-%release

%package -n lib%name-devel-static
Summary: HTML::Template compatible HTML template static library
Summary(ru_RU.UTF-8): Вариант библиотеки htmltemplpro для статической компоновки
Group: Development/C
Provides: %name-devel-static = %version
Obsoletes: %name-devel-static < %version
Requires: lib%name-devel = %version-%release

%package -n %name-testsuite
Summary: HTML template library common testsuite
Group: Development/C
Requires: %libname = %version-%release

%description
The HTML::Template::Pro library is a portable template engine for templates 
that use syntax of known perl modules HTML::Template, HTML::Template::Expr 
and HTML::Template::Pro.

%description -n %libname
The HTML::Template::Pro library is a portable template engine for templates 
that use syntax of known perl modules HTML::Template, HTML::Template::Expr 
and HTML::Template::Pro.

This package contains shared libraries.

%description -n lib%name-devel
The HTML::Template::Pro library is a portable template engine for templates 
that use syntax of known perl modules HTML::Template, HTML::Template::Expr 
and HTML::Template::Pro.

This package contains development libraries, include files and development
documentation required for developing applications which use perl-style
regular expressions.

%description -n lib%name-devel-static
The HTML::Template::Pro library is a portable template engine for templates 
that use syntax of known perl modules HTML::Template, HTML::Template::Expr 
and HTML::Template::Pro.

This package contains static development libraries required for developing
statically linked applications which use perl-style regular expressions.

%description -n %name-testsuite
The HTML::Template::Pro library is a portable template engine for templates 
that use syntax of known perl modules HTML::Template, HTML::Template::Expr 
and HTML::Template::Pro.

This package contains library's test suite to test its bindings.

%prep
%setup -q

%build
autoreconf -fisv
%define docdir %_docdir/%name-%version
%configure --includedir=%_includedir/%name \
	--docdir=%docdir \
	%{subst_enable static} \
	#
%make_build
#%{?!__buildreqs:%{?!_without_check:%{?!_disable_check:%make_build check}}}

%install
%make_install install DESTDIR=%buildroot

# install testsuite
mkdir -p %buildroot%_datadir/%name/
cp -a tests/templates-Pro %buildroot%_datadir/%name/

%check
make check

%files -n %libname
/%_libdir/lib*.so.*
#%dir %docdir
#%docdir/[ACLN]*

%files -n lib%name-devel
%doc doc/html
%doc API README
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%files testsuite
%_datadir/%name

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
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

* Tue Sep 29 2009 Igor Vlasenko <viy@altlinux.ru> 0.92-alt1
- new version; see Changes

* Tue Sep 22 2009 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1
- new version; see Changes

* Sat Sep 12 2009 Igor Vlasenko <viy@altlinux.ru> 0.90-alt3
- release

* Mon Aug 31 2009 Igor Vlasenko <viy@altlinux.ru> 0.90-alt1
- new version; see Changes

* Sat Aug 29 2009 Igor Vlasenko <viy@altlinux.ru> 0.87-alt1
- new version; see Changes

* Sat Aug 22 2009 Igor Vlasenko <viy@altlinux.ru> 0.86-alt1
- new version; see Changes

* Sun Aug 09 2009 Igor Vlasenko <viy@altlinux.ru> 0.85-alt1
- new version; see Changes

* Fri Aug 07 2009 Igor Vlasenko <viy@altlinux.ru> 0.84-alt1
- new version; see Changes

* Wed Aug 05 2009 Igor Vlasenko <viy@altlinux.ru> 0.83-alt1
- new version; see Changes

* Wed Jul 29 2009 Igor Vlasenko <viy@altlinux.ru> 0.82-alt1
- new version; see Changes

