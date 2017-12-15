%define _unpackaged_files_terminate_build 1
%define module FCGI

Name: perl-%module
Version: 0.78
Release: alt1.1.1

Summary: Fast CGI module for perl
License: OpenMarket
Group: Development/Perl

URL: %CPAN %module
Source: http://www.cpan.org/authors/id/E/ET/ETHER/FCGI-%{version}.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-devel

%description
This is a Fast CGI module for perl. It's based on the FCGI module that comes
with Open Market's FastCGI Developer's Kit.

See %_docdir/%name-%version/*.fpl for an examples on how to use this module.

See also the file %_docdir/%name-%version/LICENSE.TERMS for information on
usage and redistribution of this module, and for a DISCLAIMER OF ALL
WARRANTIES.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_archlib/FCGI.pm
%perl_vendor_autolib/FCGI
%doc README ChangeLog
#*.fpl

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.78-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.78-alt1.1
- rebuild with new perl 5.24.1

* Mon Mar 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.78-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.77-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.77-alt1.1
- rebuild with new perl 5.20.1

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.77-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.74-alt4
- built for perl 5.18

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.74-alt3
- rebuilt for perl-5.16

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.74-alt2
- rebuilt for perl-5.14

* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.74-alt1
- automated CPAN update

* Sat Aug 13 2011 Victor Forsiuk <force@altlinux.org> 0.73-alt1
- 0.73

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.71-alt1.1
- rebuilt with perl 5.12

* Thu Apr 08 2010 Victor Forsiuk <force@altlinux.org> 0.71-alt1
- 0.71

* Mon Jan 25 2010 Victor Forsyuk <force@altlinux.org> 0.68-alt1
- 0.68

* Mon Jul 30 2007 Victor Forsyuk <force@altlinux.org> 0.67-alt2
- Add URL.
- Spec cleanups.
- License is OpenMarket, not just simply "Free".

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.67-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Mar 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.67-alt1
- 0.67

* Sun Nov 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.66-alt2
- 0.66, built with new perl.

* Sun Mar 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.65-alt2
- build pure-perl version.

* Sat Mar 9 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.65-alt1
- First build for Sisyphus.
