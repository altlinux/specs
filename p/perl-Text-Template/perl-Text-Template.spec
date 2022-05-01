%define _unpackaged_files_terminate_build 1
%define module Text-Template

Name: perl-Text-Template
Version: 1.61
Release: alt1

Packager: Denis Smirnov <mithraen@altlinux.ru>

Summary: Expand template text with embedded Perl
Group: Development/Perl
License: GPL or Artistic
Url: %CPAN %module
Source0: http://www.cpan.org/authors/id/M/MS/MSCHOUT/%{module}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Feb 16 2004
BuildRequires: perl-devel perl(Test/Warnings.pm) perl(Test/More/UTF8.pm) perl(Encode.pm)

%description
This is a library for generating form letters, building HTML pages, or
filling in templates generally.  A `template' is a piece of text that
has little Perl programs embedded in it here and there.  When you `fill
in' a template, you evaluate the little programs and replace them with
their values.

You can store a template in a file outside your program.  People can
modify the template without modifying the program.  You can separate
the formatting details from the main code, and put the formatting parts
of the program into the template.  That prevents code bloat and encour-
ages functional separation.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
#%doc README Changes FAQ ANNOUNCE scripts templates
%perl_vendor_privlib/Text*

%changelog
* Sun May 01 2022 Igor Vlasenko <viy@altlinux.org> 1.61-alt1
- automated CPAN update

* Mon Sep 06 2021 Igor Vlasenko <viy@altlinux.org> 1.60-alt1
- automated CPAN update

* Sat Jul 04 2020 Igor Vlasenko <viy@altlinux.ru> 1.59-alt1
- automated CPAN update

* Sat Sep 28 2019 Igor Vlasenko <viy@altlinux.ru> 1.58-alt1
- automated CPAN update

* Wed Sep 11 2019 Igor Vlasenko <viy@altlinux.ru> 1.57-alt1
- automated CPAN update

* Wed Jul 17 2019 Igor Vlasenko <viy@altlinux.ru> 1.56-alt1
- automated CPAN update

* Tue Feb 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.55-alt1
- automated CPAN update

* Mon Jan 21 2019 Igor Vlasenko <viy@altlinux.ru> 1.54-alt1
- automated CPAN update

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.53-alt1
- automated CPAN update

* Tue Mar 20 2018 Igor Vlasenko <viy@altlinux.ru> 1.52-alt1
- automated CPAN update

* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.51-alt1.1
- NMU: added URL

* Wed Mar 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.51-alt1
- automated CPAN update

* Mon Feb 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.50-alt1
- automated CPAN update

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.47-alt1
- automated CPAN update

* Fri Oct 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.46-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.45-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Feb 05 2009 Denis Smirnov <mithraen@altlinux.ru> 1.45-alt1
- version update

* Fri Jan 09 2004 Denis Smirnov <mithraen@altlinux.ru> 1.44-alt1
- First build for Sisyphus.
