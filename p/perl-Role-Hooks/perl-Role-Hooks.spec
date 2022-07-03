%define module_name Role-Hooks
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Class/Method/Modifiers.pm) perl(Class/Tiny.pm) perl(Devel/GlobalDestruction.pm) perl(ExtUtils/MakeMaker.pm) perl(List/Util.pm) perl(Moo.pm) perl(Moo/HandleMoose.pm) perl(Moo/Role.pm) perl(Moose.pm) perl(Moose/Meta/Role.pm) perl(Moose/Role.pm) perl(Moose/Util.pm) perl(Mouse.pm) perl(Mouse/Meta/Role.pm) perl(Mouse/Role.pm) perl(Mouse/Util.pm) perl(Package/Variant.pm) perl(Role/Basic.pm) perl(Role/Tiny.pm) perl(Role/Tiny/With.pm) perl(Test/More.pm) perl(Test/Requires.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.006
Release: alt2
Summary: role callbacks
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/Role-Hooks

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/T/TO/TOBYINK/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
This module allows a role to run a callback when it is applied to a class or
to another role.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CREDITS COPYRIGHT LICENSE README Changes
%perl_vendor_privlib/R*

%changelog
* Sun Jul 03 2022 Igor Vlasenko <viy@altlinux.org> 0.006-alt2
- to Sisyphus as perl-Sub-HandlesVia build dep

* Sat Jul 02 2022 Igor Vlasenko <viy@altlinux.org> 0.006-alt1
- updated by package builder

* Mon Jun 20 2022 Igor Vlasenko <viy@altlinux.org> 0.005-alt1
- updated by package builder

* Wed Jun 08 2022 Igor Vlasenko <viy@altlinux.org> 0.004-alt1
- updated by package builder

* Sun Nov 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- updated by package builder

* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- initial import by package builder

