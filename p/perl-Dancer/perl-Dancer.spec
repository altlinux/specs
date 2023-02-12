%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Test/LongString.pm)
# END SourceDeps(oneline)
%define module_name Dancer
Name: perl-%module_name
Version: 1.3521
Release: alt1
Summary: lightweight yet powerful web application framework

Group: Development/Perl
License: Perl
Url: %CPAN Dancer

BuildArch: noarch
# Cloned from https://github.com/PerlDancer/Dancer.git
Source0: http://www.cpan.org/authors/id/Y/YA/YANICK/%{module_name}-%{version}.tar.gz

BuildRequires: perl-devel perl-Encode perl-MIME-Types perl-HTTP-Body perl-URI perl-HTTP-Server-Simple-PSGI perl-Plack perl-YAML perl-Clone perl-podlators perl-Try-Tiny perl-Test-TCP perl-Template perl-Test-Output perl-JSON perl-Test-Pod perl(Hash/Merge/Simple.pm) perl(Test/NoWarnings.pm) perl(HTTP/CookieJar.pm)
Requires: perl-Clone

%description
This project is inspired by  Ruby's Sinatra framework: a framework for
building web applications with minimal-effort, allowing a simple webapp
to be created with very few lines of code, but allowing the flexibility
to scale to much more complex applications.

%prep
%setup -q -n %{module_name}-%{version}

[ %version = "1.3520" ] && rm -f t/14_serializer/04_request_xml.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc AUTHORS CONTRIBUTORS README Changes examples
%_bindir/dancer
%_man1dir/dancer.1*
%perl_vendor_privlib/Dancer*
%dir %perl_vendor_privlib/HTTP
%dir %perl_vendor_privlib/HTTP/Tiny
%perl_vendor_privlib/HTTP/Tiny/NoProxy.pm
%doc Changes README*

%changelog
* Sun Feb 12 2023 Igor Vlasenko <viy@altlinux.org> 1.3521-alt1
- automated CPAN update

* Thu Jan 19 2023 Igor Vlasenko <viy@altlinux.org> 1.3520-alt1
- automated CPAN update

* Wed Feb 12 2020 Igor Vlasenko <viy@altlinux.ru> 1.3513-alt1
- automated CPAN update

* Tue Apr 02 2019 Igor Vlasenko <viy@altlinux.ru> 1.3512-alt1
- automated CPAN update

* Tue Mar 19 2019 Igor Vlasenko <viy@altlinux.ru> 1.3510-alt1
- automated CPAN update

* Fri Feb 22 2019 Igor Vlasenko <viy@altlinux.ru> 1.3500-alt1
- updated as official srpm;
- abandoned git due to git merge conflicts

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.3202-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 1.3142-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.3132-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.3126-alt1
- automated CPAN update

* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.3124-alt1
- automated CPAN update

* Wed Mar 12 2014 Vladimir Lettiev <crux@altlinux.ru> 1.3121-alt1
- New version 1.3121

* Fri Dec 13 2013 Vladimir Lettiev <crux@altlinux.ru> 1.3119-alt1
- New version 1.3119

* Mon Sep 16 2013 Vladimir Lettiev <crux@altlinux.ru> 1.3118-alt1
- New version 1.3118

* Tue Oct 09 2012 Vladimir Lettiev <crux@altlinux.ru> 1.3110-alt1
- New bugfix release 1.3110

* Sat Sep 22 2012 Vladimir Lettiev <crux@altlinux.ru> 1.3100-alt1
- New version 1.3100

* Sat Sep 22 2012 Vladimir Lettiev <crux@altlinux.ru> 1.3099-alt1
- New version 1.3099

* Fri Jul 06 2012 Vladimir Lettiev <crux@altlinux.ru> 1.3096-alt1
- New version 1.3096
- Added some test dependencies

* Tue Apr 10 2012 Vladimir Lettiev <crux@altlinux.ru> 1.3095-alt1
- New version 1.3095

* Sat Dec 17 2011 Vladimir Lettiev <crux@altlinux.ru> 1.3091-alt1
- New version 1.3091

* Thu Dec 15 2011 Vladimir Lettiev <crux@altlinux.ru> 1.3090-alt1
- New version 1.3090

* Mon Dec 05 2011 Vladimir Lettiev <crux@altlinux.ru> 1.3080-alt1
- New version 1.3080

* Thu Jul 28 2011 Vladimir Lettiev <crux@altlinux.ru> 1.3071-alt1
- New version 1.3071 (security release)

* Tue Jul 26 2011 Vladimir Lettiev <crux@altlinux.ru> 1.3070-alt1
- New version 1.3070

* Sat May 28 2011 Vladimir Lettiev <crux@altlinux.ru> 1.3051-alt1
- New version 1.3051.
- Security fix merged upstream

* Thu May 26 2011 Vladimir Lettiev <crux@altlinux.ru> 1.3050-alt1
- New version 1.3050

* Sun Apr 17 2011 Vladimir Lettiev <crux@altlinux.ru> 1.3030-alt1
- New version 1.3030
- Security: fixed directory traversal flaw

* Sun Feb 06 2011 Vladimir Lettiev <crux@altlinux.ru> 1.2005-alt1
- New version 1.2005

* Tue Nov 23 2010 Vladimir Lettiev <crux@altlinux.ru> 1.2000-alt1
- 1.2000, the first major stable community release
- Patch applied to fix test

* Fri Nov 19 2010 Vladimir Lettiev <crux@altlinux.ru> 1.1901-alt2
- Fixed generation of man1 pages

* Sun Sep 26 2010 Vladimir Lettiev <crux@altlinux.ru> 1.1901-alt1
- New version 1.1901

* Sun Sep 05 2010 Vladimir Lettiev <crux@altlinux.ru> 1.1811-alt1
- New version 1.1811

* Sun Aug 29 2010 Vladimir Lettiev <crux@altlinux.ru> 1.1809-alt1
- initial build
