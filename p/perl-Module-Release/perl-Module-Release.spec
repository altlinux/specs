%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CACertOrg/CA.pm) perl(Config.pm) perl(ConfigReader/Simple.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(IO/Null.pm) perl(Mojo/UserAgent.pm) perl(Scalar/Util.pm) perl(Test/More.pm) perl(Test/Output.pm) perl(Test/Without/Module.pm) perl(URI.pm) perl(base.pm) perl(version.pm) perl(CGI.pm)
# END SourceDeps(oneline)
%define module_version 2.123
%define module_name Module-Release
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 2.123
Release: alt1
Summary: Automate Perl distribution releases
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/B/BD/BDFOY/Module-Release-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %name = %{?epoch:%epoch:}%version-%release

%description scripts
scripts for %module_name

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc Changes README* examples
%perl_vendor_privlib/M*

%files scripts
%_bindir/*
%_man1dir/*

%changelog
* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 2.123-alt1
- automated CPAN update

* Mon Mar 21 2016 Igor Vlasenko <viy@altlinux.ru> 2.122-alt1
- automated CPAN update

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1
- automated CPAN update

* Mon Sep 15 2014 Igor Vlasenko <viy@altlinux.ru> 2.11-alt1
- automated CPAN update

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.09-alt1
- automated CPAN update

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 2.08-alt2
- moved to Sysiphus as dependency

* Tue Mar 11 2014 Igor Vlasenko <viy@altlinux.ru> 2.08-alt1
- initial import by package builder

