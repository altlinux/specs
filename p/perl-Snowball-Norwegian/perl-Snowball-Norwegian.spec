%define dist Snowball-Norwegian
Name: perl-%dist
Version: 1.2
Release: alt1

Summary: Porters stemming algorithm for Norwegian
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Jan 16 2011
BuildRequires: perl-Module-Build perl-Test-Pod

%description
Lingua::Stem::Snowball::No is a perl port of the norwegian
stemmer at http://snowball.tartarus.org

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
rm %buildroot%_bindir/stemmer-no.pl

%files
%doc Changes README
%perl_vendor_privlib/Lingua

%changelog
* Sun Jan 16 2011 Alexey Tourbin <at@altlinux.ru> 1.2-alt1
- decoupled from perl-Lingua-Stem
