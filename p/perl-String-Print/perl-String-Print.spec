%define _unpackaged_files_terminate_build 1
%define module_name String-Print
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Encode.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(Unicode/GCString.pm) perl(HTML/Entities.pm) perl(Date/Parse.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators
BuildRequires: perl-Encode-CN perl-Encode-TW perl-Encode-JP perl-Encode-KR perl-Encode-devel


Name: perl-%module_name
Version: 0.93
Release: alt1
Summary: printf extensions
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/M/MA/MARKOV/%{module_name}-%{version}.tar.gz
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
%doc ChangeLog README README.md
%perl_vendor_privlib/S*

%changelog
* Thu Feb 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.93-alt1
- automated CPAN update

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.92-alt1
- automated CPAN update

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- regenerated from template by package builder

* Thu Sep 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- initial import by package builder

