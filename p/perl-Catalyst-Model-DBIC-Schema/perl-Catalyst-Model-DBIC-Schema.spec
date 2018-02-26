%define dist Catalyst-Model-DBIC-Schema
Name: perl-%dist
Version: 0.59
Release: alt1

Summary: DBIx::Class::Schema Model Class
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 15 2011
BuildRequires: perl-Catalyst-Component-InstancePerContext perl-Catalyst-Devel perl-CatalystX-Component-Traits perl-Class-C3 perl-DBD-SQLite perl-DBIx-Class-Schema-Loader perl-SQL-Abstract perl-Test-Exception perl-Test-Pod perl-Test-Requires perl-Tie-IxHash

%description
This is a Catalyst Model for DBIx::Class::Schema-based Models.  See the
documentation for Catalyst::Helper::Model::DBIC::Schema for information
on generating these Models via Helper scripts.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Catalyst

%changelog
* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 0.59-alt1
- 0.55 -> 0.59

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1
- automated CPAN update

* Wed Apr 21 2010 Alexey Tourbin <at@altlinux.ru> 0.40-alt2
- rebuilt with rpm-build-perl 0.72

* Tue Apr 20 2010 Alexey Tourbin <at@altlinux.ru> 0.40-alt1
- 0.21 -> 0.40

* Mon Sep 08 2008 Michael Bochkaryov <misha@altlinux.ru> 0.21-alt1
- 0.21 version build
- fix directory ownership violation

* Mon Jun 30 2008 Michael Bochkaryov <misha@altlinux.ru> 0.20-alt1
- 0.20 version build
  + small bugfixes
  + requirements update
  + switch to Module::Install
- spec file sleanup

* Thu Mar 22 2007 Sir Raorn <raorn@altlinux.ru> 0.18-alt1
- first build for ALT Linux Sisyphus
