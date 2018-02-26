%define realname htmltmplpro-sharp
%define namespace HTML.Template.Pro

%define vmajor 0.95
%define vminor 4

Summary: C# htmpltmplpro binding
Name: lib%{realname}
Version: %vmajor.%vminor
Release: alt1
License: LGPL2+ or Artistic
Group: System/Libraries
#?Packager: Mono Maintainers Team <mono@packages.altlinux.org>
Packager: Igor Vlasenko <viy@altlinux.org>

Url: http://sf.net/projects/html-tmpl-pro
Source: %realname-%version.tar.gz

BuildRequires: libhtmltmplpro-devel >= %vmajor mono-mcs mono-devel

BuildRequires: rpm-build-mono
BuildRequires: /proc

Requires: libhtmltmplpro >= %vmajor


%description
The HTML::Template::Pro library is a portable template engine for templates 
that use syntax of known perl modules HTML::Template, HTML::Template::Expr 
and HTML::Template::Pro.
This library provides a C# .NET interface to the HTML::Template::Pro.

%package devel
Summary: Development files %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
This package includes development files for the %name.

%prep
%setup -n htmltmplpro-sharp-%version

%build
./configure
%make CSFLAGS=" -debug"

%install
mkdir -p %buildroot%_monodir/%{namespace}
gacutil -i bin/%{namespace}.dll -f -package %{namespace} -root %buildroot/usr/lib

mkdir -p %buildroot%_pkgconfigdir
install -m 644 pkgconfig/%realname.pc %buildroot%_pkgconfigdir/%realname.pc

%check
make test

%files
%doc README ChangeLog
%_monodir/%{namespace}
%_monogacdir/*

%files devel
%_pkgconfigdir/*

%changelog
* Tue Feb 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.95.4-alt1
- new version; see Changes

* Mon Dec 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.95.3-alt1
- new version; see Changes

* Tue Dec 13 2011 Igor Vlasenko <viy@altlinux.ru> 0.95.2-alt1
- updated tests for 0.9507 compliance

* Sat Aug 28 2010 Igor Vlasenko <viy@altlinux.ru> 0.95.1-alt1
- new version; see Changes

* Tue Feb 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.94.1-alt1
- new version; see Changes

* Sun Nov 15 2009 Igor Vlasenko <viy@altlinux.ru> 0.93.1-alt1
- new version; see Changes

* Tue Sep 29 2009 Igor Vlasenko <viy@altlinux.ru> 0.92.1-alt1
- new version; see Changes

* Tue Sep 22 2009 Igor Vlasenko <viy@altlinux.ru> 0.91.1-alt1
- new version; see Changes

* Sat Sep 12 2009 Igor Vlasenko <viy@altlinux.ru> 0.90.1-alt3
- release

* Mon Aug 31 2009 Igor Vlasenko <viy@altlinux.ru> 0.90.1-alt1
- new version; see Changes

* Sat Aug 29 2009 Igor Vlasenko <viy@altlinux.ru> 0.87.1-alt1
- new version; see Changes

* Sat Aug 22 2009 Igor Vlasenko <viy@altlinux.ru> 0.86.1-alt1
- new version

* Sun Aug 09 2009 Igor Vlasenko <viy@altlinux.ru> 0.85.1-alt1
- new version

* Fri Aug 07 2009 Igor Vlasenko <viy@altlinux.ru> 0.84.1-alt1
- new version

* Thu Aug 06 2009 Igor Vlasenko <viy@altlinux.ru> 0.83.3-alt1
- new version

* Thu Aug 06 2009 Igor Vlasenko <viy@altlinux.ru> 0.83.2-alt1
- new version

* Wed Aug 05 2009 Igor Vlasenko <viy@altlinux.ru> 0.83.1-alt1
- Inital release for ALTLinux
