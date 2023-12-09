# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Crypt/OpenSSL/RSA.pm) perl(Crypt/PK/Ed25519.pm) perl(Data/Dumper.pm) perl(ExtUtils/MakeMaker.pm) perl(Getopt/Long/Descriptive.pm) perl(MIME/Base64.pm) perl(MIME/Lite.pm) perl(Mail/Address.pm) perl(Mail/AuthenticationResults/Header/AuthServID.pm) perl(Net/DNS.pm) perl(Net/DNS/Resolver.pm) perl(Net/DNS/Resolver/Mock.pm) perl(Pod/Usage.pm) perl(Test/More.pm) perl(Test/Pod.pm) perl(Test/RequiresInternet.pm) perl(Test/Simple.pm) perl(YAML/XS.pm) perl(base.pm) perl(lib.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define module_name Mail-DKIM
%define _unpackaged_files_terminate_build 1
# network is disabled :(
%def_disable test
%define module Mail-DKIM

Name: perl-%module
Version: 1.20230911
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Perl module for DKIM-based mail-signing and -verifying
License: perl
Group: Development/Perl

URL: %CPAN %module
Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/M/MB/MBRADSHAW/%{module_name}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 16 2010
BuildRequires: perl-Crypt-OpenSSL-RSA perl-MailTools perl-Net-DNS perl-devel perl(Digest/SHA.pm) perl(Mail/AuthenticationResults/Parser.pm)

%description
This module implements the various components of the DKIM message-signing and
verifying standard for Internet mail.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes LICENSE TODO README.md doc
%perl_vendor_privlib/Mail

%changelog
* Fri Dec 08 2023 Igor Vlasenko <viy@altlinux.org> 1.20230911-alt1
- updated by package builder

* Tue Jun 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.20200513.1-alt1
- automated CPAN update

* Tue Nov 19 2019 Igor Vlasenko <viy@altlinux.ru> 0.58-alt1
- automated CPAN update

* Sun Oct 13 2019 Igor Vlasenko <viy@altlinux.ru> 0.57-alt1
- automated CPAN update

* Thu Aug 22 2019 Igor Vlasenko <viy@altlinux.ru> 0.56-alt1
- automated CPAN update

* Mon Apr 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1
- automated CPAN update

* Wed Oct 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1
- automated CPAN update

* Mon May 28 2018 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1
- automated CPAN update

* Tue Jan 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1
- automated CPAN update

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1
- automated CPAN update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1
- automated CPAN update

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.40-alt2
- NMU: fixed build

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1
- automated CPAN update

* Sun Oct 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.39-alt2
- fixed build (disabled tests because network is disabled)

* Tue Nov 16 2010 Victor Forsiuk <force@altlinux.org> 0.39-alt1
- 0.39

* Mon Jun 21 2010 Victor Forsiuk <force@altlinux.org> 0.38-alt1
- 0.38

* Fri Feb 12 2010 Victor Forsiuk <force@altlinux.org> 0.37-alt1
- 0.37

* Thu Jun 19 2008 Victor Forsyuk <force@altlinux.org> 0.32-alt1
- 0.32

* Tue Mar 04 2008 Victor Forsyuk <force@altlinux.org> 0.30.1-alt1
- 0.30.1

* Wed Dec 12 2007 Victor Forsyuk <force@altlinux.org> 0.29-alt1
- 0.29

* Fri Oct 26 2007 Victor Forsyuk <force@altlinux.org> 0.28-alt1
- 0.28

* Fri Jun 01 2007 Victor Forsyuk <force@altlinux.org> 0.26-alt1
- 0.26

* Thu Mar 22 2007 Victor Forsyuk <force@altlinux.org> 0.24-alt1
- 0.24

* Thu Aug 31 2006 Victor Forsyuk <force@altlinux.ru> 0.18-alt1
- 0.18
- Refresh BuildRequires.

* Wed Jun 07 2006 Victor Forsyuk <force@altlinux.ru> 0.16-alt1
- Initial build.
