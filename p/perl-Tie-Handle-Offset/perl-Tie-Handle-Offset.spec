%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_name Tie-Handle-Offset
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.004
Release: alt1
Summary: Tied handle that hides the beginning of a file
Group: Development/Perl
License: apache
URL: https://github.com/dagolden/tie-handle-offset

Source0: http://www.cpan.org/authors/id/D/DA/DAGOLDEN/%{module_name}-%{version}.tar.gz
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
%doc LICENSE README Changes
%perl_vendor_privlib/T*

%changelog
* Wed Apr 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- automated CPAN update

* Sat Dec 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.003-alt2
- moved to Sisyphus as dependency

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- initial import by package builder

