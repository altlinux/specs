# BEGIN SourceDeps(oneline):
BuildRequires: perl(Module/Build.pm) perl(Plack/Test.pm) perl(Test/More.pm) perl(URI.pm) perl(parent.pm)
# END SourceDeps(oneline)
%define module_version 0.10
%define module_name Plack-Middleware-MethodOverride
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.10
Release: alt2
Summary: Override REST methods to Plack apps via POST
Group: Development/Perl
License: perl
URL: http://search.cpan.org/dist/Plack-Middleware-MethodOverride/

Source0: http://cpan.org.ua/authors/id/D/DW/DWHEELER/%module_name-%module_version.tar.gz
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
%doc Changes README.md
%perl_vendor_privlib/P*

%changelog
* Fri Mar 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2
- moved to Sisyphus as perl update dependency

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- initial import by package builder

