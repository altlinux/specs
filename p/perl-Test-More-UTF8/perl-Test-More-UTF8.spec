%define module_name Test-More-UTF8
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(IO/Handle.pm) perl(Test/More.pm) perl(utf8.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.05
Release: alt2
Summary: Enhancing Test::More for UTF8-based projects
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/M/MO/MONS/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
use Test::More;
	use Test::More::UTF8;

	# now we can easily use flagged strings without warnings like "Wide character in print ..."
	is("\x{410}","\x{420}"); # got a failure message without warnings


%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/T*

%changelog
* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2
- to Sisyphus as perl-Text-Template dep

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- regenerated from template by package builder

* Thu Sep 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- initial import by package builder

