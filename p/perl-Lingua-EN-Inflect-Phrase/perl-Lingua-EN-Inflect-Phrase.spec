%define dist Lingua-EN-Inflect-Phrase
Name: perl-%dist
Version: 0.10
Release: alt1

Summary: Inflect short English Phrases
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 15 2011
BuildRequires: perl-Lingua-EN-Inflect-Number perl-Lingua-EN-Tagger perl-Pod-Escapes perl-devel

%description
Attempts to pluralize or singularize short English phrases.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Lingua

%changelog
* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 0.10-alt1
- 0.04 -> 0.10

* Tue Apr 27 2010 Alexey Tourbin <at@altlinux.ru> 0.04-alt1
- initial revision
