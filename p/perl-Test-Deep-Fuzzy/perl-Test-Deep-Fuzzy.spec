# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(Math/Round.pm) perl(Module/Build/Tiny.pm) perl(Scalar/Util.pm) perl(Test/Deep.pm) perl(Test/Deep/Cmp.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 0.01
%define module_name Test-Deep-Fuzzy
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.01
Release: alt1
Summary: fuzzy number comparison with Test::Deep
Group: Development/Perl
License: perl
URL: https://github.com/karupanerura/Test-Deep-Fuzzy

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/K/KA/KARUPA/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
Test::Deep::Fuzzy provides fuzzy number comparison with the Test::Deep manpage.


%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md LICENSE
%perl_vendor_privlib/T*

%changelog
* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

