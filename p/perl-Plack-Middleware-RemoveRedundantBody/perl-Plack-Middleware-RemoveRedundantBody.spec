%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp/Always.pm) perl(ExtUtils/MakeMaker.pm) perl(HTTP/Request/Common.pm) perl(Plack/Builder.pm) perl(Plack/Middleware.pm) perl(Plack/Test.pm) perl(Plack/Util.pm) perl(Test/More.pm) perl(parent.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define module_name Plack-Middleware-RemoveRedundantBody
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.07
Release: alt1
Summary: Plack::Middleware which sets removes body for HTTP response if it's not required
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/S/SW/SWEETKID/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README LICENSE Changes
%perl_vendor_privlib/P*

%changelog
* Wed Mar 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- automated CPAN update

* Fri Mar 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- uploaded to Sisyphus as dependency

