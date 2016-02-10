%define _unpackaged_files_terminate_build 1
%define dist Lingua-PT-Stemmer
Name: perl-%dist
Version: 0.02
Release: alt1

Summary: Stemmers for Portuguese and Galician
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/N/NE/NEILB/Lingua-PT-Stemmer-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Jan 16 2011
BuildRequires: perl-devel

%description
This module implements a Portuguese stemming algorithm proposed in the paper
"A Stemming Algorithm for the Portuguese Language" by Moreira, V. and Huyck, C.

Galician is an endangered language spoken in northwest region of Spain.
Galician is morphologically similar to Portuguese but phonetics differs
greatly.  Due to the morphological similarity between Portuguese and Galician,
Portuguese stemming algorithm can be adopted to stem Galician texts.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%dir %perl_vendor_privlib/Lingua
%perl_vendor_privlib/Lingua/GL
%perl_vendor_privlib/Lingua/PT

%changelog
* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- automated CPAN update

* Sun Jan 16 2011 Alexey Tourbin <at@altlinux.ru> 0.01-alt1
- decoupled from perl-Lingua-Stem
