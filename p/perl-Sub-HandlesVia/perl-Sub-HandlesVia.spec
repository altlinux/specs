%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Class/Method/Modifiers.pm) perl(Class/Tiny.pm) perl(Eval/TypeTiny.pm) perl(Exporter/Shiny.pm) perl(ExtUtils/MakeMaker.pm) perl(List/Util.pm) perl(Moo.pm) perl(Moo/Role.pm) perl(MooX/TypeTiny.pm) perl(Moose.pm) perl(Moose/Role.pm) perl(Moose/Util.pm) perl(Moose/Util/TypeConstraints.pm) perl(MooseX/ArrayRef.pm) perl(MooseX/InsideOut.pm) perl(Mouse.pm) perl(Mouse/Role.pm) perl(Mouse/Util.pm) perl(Mouse/Util/TypeConstraints.pm) perl(Role/Hooks.pm) perl(Role/Tiny.pm) perl(Scope/Guard.pm) perl(Test/Fatal.pm) perl(Test/Moose.pm) perl(Test/More.pm) perl(Test/Requires.pm) perl(Type/Params.pm) perl(Types/Standard.pm) perl(Object/Pad.pm) perl(XS/Parse/Keyword.pm) perl(XS/Parse/Sublike.pm) perl(experimental.pm)
# END SourceDeps(oneline)
%define module_name Sub-HandlesVia
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.045
Release: alt1
Summary: alternative handles_via implementation
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/Sub-HandlesVia

Source0: http://www.cpan.org/authors/id/T/TO/TOBYINK/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
If you've used the Moose manpage's native attribute traits, or the MooX::HandlesVia manpage
before, you should have a fairly good idea what this does.

Why re-invent the wheel? Well, this is an implementation that should work
okay with Moo, Moose, Mouse, and any other OO toolkit you throw at it.
One ring to rule them all, so to speak.

Also, unlike the MooX::HandlesVia manpage, it honours type constraints, plus it
doesn't have the limitation that it can't mutate non-reference values.

%prep
%setup -q -n %{module_name}-%{version}
if [ %version = 0.013 ]; then
  sed -i '/List::Util/s/1\.54/1.5/' Makefile.PL
fi

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CREDITS Changes COPYRIGHT README
%perl_vendor_privlib/S*

%changelog
* Mon Nov 28 2022 Igor Vlasenko <viy@altlinux.org> 0.045-alt1
- automated CPAN update

* Fri Oct 28 2022 Igor Vlasenko <viy@altlinux.org> 0.040-alt1
- automated CPAN update

* Sat Oct 22 2022 Igor Vlasenko <viy@altlinux.org> 0.038-alt1
- automated CPAN update

* Tue Sep 27 2022 Igor Vlasenko <viy@altlinux.org> 0.037-alt1
- automated CPAN update

* Mon Aug 29 2022 Igor Vlasenko <viy@altlinux.org> 0.036-alt1
- automated CPAN update

* Thu Aug 18 2022 Igor Vlasenko <viy@altlinux.org> 0.035-alt1
- automated CPAN update

* Thu Aug 11 2022 Igor Vlasenko <viy@altlinux.org> 0.034-alt1
- automated CPAN update

* Sun Aug 07 2022 Igor Vlasenko <viy@altlinux.org> 0.033-alt1
- automated CPAN update

* Sat Jul 16 2022 Igor Vlasenko <viy@altlinux.org> 0.032-alt1
- automated CPAN update

* Tue Jul 12 2022 Igor Vlasenko <viy@altlinux.org> 0.031-alt1
- automated CPAN update

* Sun Jul 03 2022 Igor Vlasenko <viy@altlinux.org> 0.028-alt1
- automated CPAN update

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0.027-alt1
- automated CPAN update

* Thu Jun 16 2022 Igor Vlasenko <viy@altlinux.org> 0.025-alt1
- automated CPAN update

* Wed Jun 15 2022 Igor Vlasenko <viy@altlinux.org> 0.023-alt1
- automated CPAN update

* Sun Jun 12 2022 Igor Vlasenko <viy@altlinux.org> 0.020-alt1
- automated CPAN update

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1
- automated CPAN update

* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1
- new version

