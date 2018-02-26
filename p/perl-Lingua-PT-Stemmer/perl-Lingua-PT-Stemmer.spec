%define dist Lingua-PT-Stemmer
Name: perl-%dist
Version: 0.01
Release: alt1

Summary: Stemmers for Portuguese and Galician
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

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
* Sun Jan 16 2011 Alexey Tourbin <at@altlinux.ru> 0.01-alt1
- decoupled from perl-Lingua-Stem
