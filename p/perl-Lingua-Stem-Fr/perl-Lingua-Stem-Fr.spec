%define dist Lingua-Stem-Fr
Name: perl-%dist
Version: 0.02
Release: alt1

Summary: Porter's stemming algorithm for French
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Jan 16 2011
BuildRequires: perl-devel

%description
This module is an implementation of the Porter Stemming Algorithm:
http://snowball.tartarus.org/french/stemmer.html
with some improvement.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_privlib/Lingua

%changelog
* Sun Jan 16 2011 Alexey Tourbin <at@altlinux.ru> 0.02-alt1
- decoupled from perl-Lingua-Stem
