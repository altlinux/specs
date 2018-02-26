%define module Text-WagnerFischer
%define m_name Text::WagnerFischer
%define _enable_test 1

Name: perl-Text-WagnerFischer
Version: 0.04
Release: alt1

Summary: Text::WagnerFischer is an implementation of the Wagner-Fischer edit distance in Perl.

License: GPL or Artistic
Group: Development/Perl
Url: http://www.cpan.org

BuildArch: noarch
Source: http://search.cpan.org/CPAN/authors/id/D/DA/DAVIDEBE/%module-%version.tar.gz

# Automatically added by buildreq on Wed Jan 21 2009
BuildRequires: perl-devel

%description
This module implements the Wagner-Fischer dynamic programming technique,
used here to calculate the edit distance of two strings.
The edit distance is a measure of the degree of proximity between two strings,
based on "edits": the operations of substitutions, deletions or insertions
needed to transform the string into the other one (and vice versa).

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf %buildroot%perl_vendor_man3dir/

%files
%perl_vendor_privlib/Text/*

%changelog
* Wed Jan 21 2009 Grigory Milev <week@altlinux.ru> 0.04-alt1
- Initial build for ALT Linux
