%define module_version 0.15
%define module_name String-Print
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Encode.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(Unicode/GCString.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators
BuildRequires: perl-Encode-CN perl-Encode-TW perl-Encode-JP perl-Encode-KR perl-Encode-devel


Name: perl-%module_name
Version: 0.15
Release: alt1
Summary: printf extensions
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/M/MA/MARKOV/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_privlib/S*

%changelog
* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- regenerated from template by package builder

* Thu Sep 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- initial import by package builder

