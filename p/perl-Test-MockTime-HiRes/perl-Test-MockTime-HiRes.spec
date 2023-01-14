%define module_name Test-MockTime-HiRes
# BEGIN SourceDeps(oneline):
BuildRequires: perl(AnyEvent.pm) perl(AnyEvent/Impl/Perl.pm) perl(Module/Build/Tiny.pm) perl(Test/Class.pm) perl(Test/MockTime.pm) perl(Test/More.pm) perl(Test/Requires.pm) perl(Time/HiRes.pm) perl(parent.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.08
Release: alt2
Summary: Replaces actual time with simulated high resolution time
Group: Development/Perl
License: perl
URL: https://github.com/tarao/perl5-Test-MockTime-HiRes

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/T/TA/TARAO/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
`Test::MockTime::HiRes' is a the Time::HiRes manpage compatible version of
the Test::MockTime manpage.  You can wait milliseconds in simulated time.

It also provides `mock_time' to restrict the effect of the simulation
in a code block.


%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE README.md Changes
%perl_vendor_privlib/T*

%changelog
* Sun Jan 15 2023 Igor Vlasenko <viy@altlinux.org> 0.08-alt2
- to Sisyphus as perl-DateTime-Format-Natural dep

* Tue Feb 13 2018 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- regenerated from template by package builder

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- regenerated from template by package builder

* Fri Feb 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- regenerated from template by package builder

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- initial import by package builder

