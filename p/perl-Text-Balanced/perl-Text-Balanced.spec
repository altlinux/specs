%define dist Text-Balanced
Name: perl-%dist
Version: 2.02
Release: alt1

Summary: Extract delimited text sequences from strings
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Dec 18 2010
BuildRequires: perl-devel

%description
The various subroutines may be used to extract a delimited substring,
possibly after skipping a specified prefix string.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Text*

%changelog
* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 2.02-alt1
- 2.01 -> 2.02

* Tue Jul 28 2009 Alexey Tourbin <at@altlinux.ru> 2.01-alt1
- 2.0.0 -> 2.01

* Tue Apr 10 2007 Alexey Tourbin <at@altlinux.ru> 2.0.0-alt1
- 1.98 -> 2.0.0
- replaced qv('2.0.0') version object with v2.0.0 v-string

* Mon May 22 2006 Alexey Tourbin <at@altlinux.ru> 1.98-alt1
- 1.96 -> 1.98

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.95-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Mon Nov 08 2004 Alexey Tourbin <at@altlinux.ru> 1.95-alt1
- initial revision (perl-base offset; required only by perl-PDL
  and perl-Parse-RecDescent)
