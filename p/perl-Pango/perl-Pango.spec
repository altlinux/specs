%define _unpackaged_files_terminate_build 1
%define dist Pango
Name: perl-%dist
Version: 1.227
Release: alt1.1.1

Summary: Layout and render international text
License: LGPL
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/X/XA/XAOC/Pango-%{version}.tar.gz

%define base_ver 1.220
Requires: perl-Glib >= %base_ver
BuildPreReq: perl-Glib-devel >= %base_ver

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: fonts-ttf-dejavu libpango-devel perl-Cairo-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig perl-Glib-devel perl-podlators

%package devel
Summary: Layout and render international text
Group: Development/Perl
Requires: %name = %version-%release
Requires: libpango-devel
# Pango/Install/Files.pm:deps
Requires: perl-Glib-devel
Requires: perl-Cairo-devel

%description
Pango is a library for laying out and rendering text, with an emphasis on
internationalization.  Pango can be used anywhere that text layout is needed,
but using Pango in conjunction with Cairo and/or Gtk2 provides a complete
solution with high quality text handling and graphics rendering.

%description devel
Pango is a library for laying out and rendering text, with an emphasis on
internationalization.  Pango can be used anywhere that text layout is needed,
but using Pango in conjunction with Cairo and/or Gtk2 provides a complete
solution with high quality text handling and graphics rendering.

%prep
%setup -q -n %dist-%version

%ifdef __buildreqs
# avoid build dependency on perl-Gtk2
rm `grep -l need_gtk t/*.t`
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	AUTHORS NEWS README
	%perl_vendor_archlib/Pango.pm
	%perl_vendor_autolib/Pango/

%files devel
%dir	%perl_vendor_archlib/Pango
%doc	%perl_vendor_archlib/Pango/*.pod
%dir	%perl_vendor_archlib/Pango/Cairo
%doc	%perl_vendor_archlib/Pango/Cairo/*.pod
%dir	%perl_vendor_archlib/Pango/Install
	%perl_vendor_archlib/Pango/Install/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.227-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.227-alt1.1
- rebuild with new perl 5.24.1

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.227-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.226-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.226-alt1.1
- rebuild with new perl 5.20.1

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.226-alt1
- automated CPAN update

* Wed Jan 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.225-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.224-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.224-alt1
- automated CPAN update

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 1.223-alt2
- rebuilt for perl-5.16

* Wed Apr 11 2012 Vladimir Lettiev <crux@altlinux.ru> 1.223-alt1
- 1.222 -> 1.223

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 1.222-alt1
- 1.221 -> 1.222
- built for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.221-alt1.1
- rebuilt with perl 5.12

* Mon Sep 28 2009 Alexey Tourbin <at@altlinux.ru> 1.221-alt1
- 1.220 -> 1.221

* Thu Mar 26 2009 Alexey Tourbin <at@altlinux.ru> 1.220-alt2
- updated dependencies

* Tue Mar 24 2009 Alexey Tourbin <at@altlinux.ru> 1.220-alt1
- initial revision (for perl-Gtk2)
