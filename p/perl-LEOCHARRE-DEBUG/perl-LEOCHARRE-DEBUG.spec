%define module_version 1.14
%define module_name LEOCHARRE-DEBUG
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Data/Dumper.pm) perl(ExtUtils/MakeMaker.pm) perl(Term/ANSIColor.pm) perl(Test/Simple.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.14
Release: alt2
Summary: deprecated
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/L/LE/LEOCHARRE/%module_name-%module_version.tar.gz
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
%doc Changes README
%perl_vendor_privlib/L*

%changelog
* Fri Oct 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.14-alt2
- regenerated from template by package builder

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1
- initial import by package builder

