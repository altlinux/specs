%define module_name CLI-Osprey
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Capture/Tiny.pm) perl(Getopt/Long/Descriptive.pm) perl(Module/Build/Tiny.pm) perl(Module/Runtime.pm) perl(Moo.pm) perl(Moo/Role.pm) perl(Path/Tiny.pm) perl(Pod/Usage.pm) perl(Scalar/Util.pm) perl(Test/Lib.pm) perl(Test/More.pm) perl(overload.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.08
Release: alt2
Summary: MooX::Options + MooX::Cmd + Sanity
Group: Development/Perl
License: perl
URL: http://metacpan.org/release/CLI-Osprey

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/A/AR/ARODLAND/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
CLI::Osprey is a module to assist in writing commandline applications with M*
OO modules (Moose, Moo, Mo). With it, you structure your app as one or more
modules, which get instantiated with the commandline arguments as attributes.
Arguments are parsed using the Getopt::Long::Descriptive manpage, and both long and
short help messages as well as complete manual pages are automatically
generated. An app can be a single command with options, or have sub-commands
(like `git'). Sub-commands can be defined as modules (with options of their
own) or as simple coderefs.


%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README
%perl_vendor_privlib/C*

%changelog
* Wed Apr 28 2021 Igor Vlasenko <viy@altlinux.org> 0.08-alt2
- to Sisyphus as Dancer2 dep

* Wed Jul 15 2020 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- updated by package builder

* Fri Jul 03 2020 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- updated by package builder

* Wed Jul 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- updated by package builder

* Sun Mar 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- updated by package builder

* Wed Jul 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- regenerated from template by package builder

* Wed Dec 20 2017 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- regenerated from template by package builder

* Sun Oct 08 2017 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- regenerated from template by package builder

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

