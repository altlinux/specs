%define module_version 1.10
%define module_name WordPress-API
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Cwd.pm) perl(Date/Manip.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Type.pm) perl(LEOCHARRE/DEBUG.pm) perl(MIME/Base64.pm) perl(Smart/Comments.pm) perl(Test/Simple.pm) perl(WordPress/XMLRPC.pm) perl(YAML.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.10
Release: alt2
Summary: perl module %module_name
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
%perl_vendor_privlib/W*

%changelog
* Fri Oct 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2
- regenerated from template by package builder

* Tue Sep 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1
- initial import by package builder

