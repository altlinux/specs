%define _unpackaged_files_terminate_build 1
%define dist Hash-Util-FieldHash-Compat
Name: perl-%dist
Version: 0.11
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
BuildRequires: perl-Test-use-ok perl(Module/Metadata.pm)

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
* Sun Jul 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Mon Feb 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- automated CPAN update

* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.03-alt1
- initial revision
