%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Clone.pm) perl(Test/Needs.pm)
# END SourceDeps(oneline)
%define dist HTTP-Message
Name: perl-%dist
Version: 6.45
Release: alt1

Summary: HTTP style messages
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/O/OA/OALDERS/%{dist}-%{version}.tar.gz

Conflicts: perl-libwww < 6

BuildArch: noarch

# Automatically added by buildreq on Mon Feb 20 2012
BuildRequires: perl-Encode-Locale perl-HTML-Parser perl-HTTP-Date perl-IO-Compress perl-LWP-MediaTypes perl-devel perl(IO/HTML.pm) perl(Try/Tiny.pm)

%description
An HTTP::Message object contains some headers and a content body.
The following methods are available:

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes CONTRIBUTORS README.md CONTRIBUTING.md
%perl_vendor_privlib/HTTP

%changelog
* Sun Oct 01 2023 Igor Vlasenko <viy@altlinux.org> 6.45-alt1
- automated CPAN update

* Fri Oct 28 2022 Igor Vlasenko <viy@altlinux.org> 6.44-alt1
- automated CPAN update

* Sat Oct 22 2022 Igor Vlasenko <viy@altlinux.org> 6.42-alt1
- automated CPAN update

* Fri Oct 14 2022 Igor Vlasenko <viy@altlinux.org> 6.41-alt1
- automated CPAN update

* Wed Oct 12 2022 Igor Vlasenko <viy@altlinux.org> 6.39-alt1
- automated CPAN update

* Sat Oct 08 2022 Igor Vlasenko <viy@altlinux.org> 6.38-alt1
- automated CPAN update

* Wed Jun 15 2022 Igor Vlasenko <viy@altlinux.org> 6.37-alt1
- automated CPAN update

* Sat Jan 08 2022 Igor Vlasenko <viy@altlinux.org> 6.36-alt1
- automated CPAN update

* Wed Nov 17 2021 Igor Vlasenko <viy@altlinux.org> 6.35-alt1
- automated CPAN update

* Thu Nov 11 2021 Igor Vlasenko <viy@altlinux.org> 6.34-alt1
- automated CPAN update

* Thu Jul 01 2021 Igor Vlasenko <viy@altlinux.org> 6.33-alt1
- automated CPAN update

* Thu May 27 2021 Igor Vlasenko <viy@altlinux.org> 6.32-alt1
- automated CPAN update

* Sun May 16 2021 Igor Vlasenko <viy@altlinux.org> 6.31-alt1
- automated CPAN update

* Sat Mar 06 2021 Igor Vlasenko <viy@altlinux.org> 6.29-alt1
- automated CPAN update

* Sun Feb 21 2021 Igor Vlasenko <viy@altlinux.org> 6.28-alt1
- automated CPAN update

* Wed Jan 06 2021 Igor Vlasenko <viy@altlinux.ru> 6.27-alt1
- automated CPAN update

* Wed Nov 11 2020 Igor Vlasenko <viy@altlinux.ru> 6.26-alt2
- cleaned up deprecated provides (closes:#39248)

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 6.26-alt1
- automated CPAN update

* Sat Jul 04 2020 Igor Vlasenko <viy@altlinux.ru> 6.25-alt1
- automated CPAN update

* Tue Jun 09 2020 Igor Vlasenko <viy@altlinux.ru> 6.24-alt1
- automated CPAN update

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 6.22-alt1
- automated CPAN update

* Wed Jun 06 2018 Igor Vlasenko <viy@altlinux.ru> 6.18-alt1
- automated CPAN update

* Thu Mar 29 2018 Igor Vlasenko <viy@altlinux.ru> 6.16-alt1
- automated CPAN update

* Fri Mar 16 2018 Igor Vlasenko <viy@altlinux.ru> 6.15-alt1
- automated CPAN update

* Tue Dec 26 2017 Igor Vlasenko <viy@altlinux.ru> 6.14-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 6.13-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 6.11-alt1
- automated CPAN update

* Tue Oct 15 2013 Igor Vlasenko <viy@altlinux.ru> 6.06-alt2
- updated provides

* Tue Oct 23 2012 Igor Vlasenko <viy@altlinux.ru> 6.06-alt1
- automated CPAN update

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 6.04-alt1
- automated CPAN update

* Mon Feb 20 2012 Alexey Tourbin <at@altlinux.ru> 6.03-alt1
- 6.02 -> 6.03

* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 6.02-alt3
- rebuilt as plain src.rpm

* Tue Mar 22 2011 Alexey Tourbin <at@altlinux.ru> 6.02-alt2
- HTTP/Headers.pm: enabled explicit dependency on Sotrable

* Mon Mar 21 2011 Alexey Tourbin <at@altlinux.ru> 6.02-alt1
- initial revision
