%define module_name MooX-StrictConstructor
# BEGIN SourceDeps(oneline):
BuildRequires: perl(B.pm) perl(Class/Method/Modifiers.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Moo.pm) perl(Moo/Role.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(constant.pm) perl(strict.pm) perl(strictures.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires(pre): rpm-build-licenses
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.011
Release: alt2
Summary: Make your Moo-based object constructors blow up on unknown attributes.
Group: Development/Perl
License: %perl_license
URL: https://metacpan.org/release/MooX-StrictConstructor

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/H/HA/HARTZELL/%{module_name}-%{version}.tar.gz
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
%doc Changes LICENSE
%perl_vendor_privlib/M*

%changelog
* Tue Mar 07 2023 L.A. Kostis <lakostis@altlinux.ru> 0.011-alt2
- fix License.

* Thu Mar 12 2020 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1
- updated by package builder

* Thu Nov 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- regenerated from template by package builder

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1.1
- rebuild to restore role requires

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- regenerated from template by package builder

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- initial import by package builder

