# BEGIN SourceDeps(oneline):
BuildRequires: perl(B.pm) perl(Data/Dumper.pm) perl(Module/Build.pm) perl(Storable.pm) perl(Test/More.pm) perl(Try/Tiny.pm)
# END SourceDeps(oneline)
%define module_version 0.13
%define module_name Role-Basic
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.13
Release: alt2
Summary: Just roles. Nothing else.
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/O/OV/OVID/%module_name-%module_version.tar.gz
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
%doc README Changes examples
%perl_vendor_privlib/R*

%changelog
* Fri Mar 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2
- moved to Sisyphus by lav@ request

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- initial import by package builder

