%define dist Hash-Util-FieldHash-Compat
Name: perl-%dist
Version: 0.04
Release: alt1

Summary: Use Hash::Util::FieldHash or ties, depending on availability
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/E/ET/ETHER/Hash-Util-FieldHash-Compat-%{version}.tar.gz

BuildArch: noarch

# not used with perl-5.14
%add_findreq_skiplist */Hash/Util/FieldHash/Compat/Heavy.pm

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-Test-use-ok

%description
Under older perls this module provides a drop in compatible api to
Hash::Util::FieldHash using perltie.  When Hash::Util::FieldHash is
available it will use that instead.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Hash

%changelog
* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- automated CPAN update

* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.03-alt1
- initial revision
