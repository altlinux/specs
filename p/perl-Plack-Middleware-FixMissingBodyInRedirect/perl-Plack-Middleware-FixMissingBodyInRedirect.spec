# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp/Always.pm) perl(ExtUtils/MakeMaker.pm) perl(HTML/Entities.pm) perl(HTTP/Request/Common.pm) perl(Plack/Builder.pm) perl(Plack/Middleware.pm) perl(Plack/Test.pm) perl(Plack/Util.pm) perl(Scalar/Util.pm) perl(Test/More.pm) perl(parent.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define module_version 0.09
%define module_name Plack-Middleware-FixMissingBodyInRedirect
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.09
Release: alt1
Summary: Plack::Middleware which sets body for redirect response, if it's not already set
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/S/SW/SWEETKID/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE README
%perl_vendor_privlib/P*

%changelog
* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- uploaded to Sisyphus as dependency

