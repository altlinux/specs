%define _unpackaged_files_terminate_build 1
%define module Text-Template

Name: perl-Text-Template
Version: 1.50
Release: alt1

Packager: Denis Smirnov <mithraen@altlinux.ru>

Summary: Expand template text with embedded Perl
Group: Development/Perl
License: GPL or Artistic
Source0: http://www.cpan.org/authors/id/M/MS/MSCHOUT/%{module}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Feb 16 2004
BuildRequires: perl-devel

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
%doc LICENSE README Changes
#%doc README Changes FAQ ANNOUNCE scripts templates
%perl_vendor_privlib/Text*

%changelog
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
