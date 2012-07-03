%define dist Snowball-Swedish
Name: perl-%dist
Version: 1.2
Release: alt1

Summary: Porters stemming algorithm for Swedish
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Jan 16 2011
BuildRequires: perl-Module-Build perl-Test-Pod

%description
The stem function takes a scalar as a parameter and stems the word
according to Martin Porters Swedish stemming algorithm, which can be
found at the Snowball website: http://snowball.tartarus.org

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
rm %buildroot%_bindir/stemmer-se.pl

%files
%doc Changes README
%perl_vendor_privlib/Lingua

%changelog
* Sun Jan 16 2011 Alexey Tourbin <at@altlinux.ru> 1.2-alt1
- decoupled from perl-Lingua-Stem
