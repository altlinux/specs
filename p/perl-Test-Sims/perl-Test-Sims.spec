%define module_name Test-Sims
# BEGIN SourceDeps(oneline):
BuildRequires: perl(DateTime.pm) perl(Exporter.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 20180103
Release: alt2
Summary: Helps build semi-random data for testing
Group: Development/Perl
License: perl
URL: http://github.com/schwern/Test-Sims

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/M/MS/MSCHWERN/%{module_name}-%{version}.tar.gz
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
%doc Changes README
%perl_vendor_privlib/T*

%changelog
* Wed Jul 13 2022 Igor Vlasenko <viy@altlinux.org> 20180103-alt2
- to Sisyphus as perl-Sub-HandlesVia build dep

* Sun Jan 21 2018 Igor Vlasenko <viy@altlinux.ru> 20180103-alt1
- regenerated from template by package builder

* Fri Sep 27 2013 Igor Vlasenko <viy@altlinux.ru> 20130412-alt1
- initial import by package builder

