%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(FindBin.pm) perl(Test/CPAN/Changes.pm) perl(Test/EOL.pm) perl(Test/Kwalitee.pm) perl(Test/NoTabs.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:       perl-MooseX-App-Cmd
Version:    0.32
Release:    alt1.1
# see lib/MooseX/App/Cmd.pm
License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    Mashes up MooseX::Getopt and App::Cmd
Source:     http://www.cpan.org/authors/id/E/ET/ETHER/MooseX-App-Cmd-%{version}.tar.gz
Url:        http://search.cpan.org/dist/MooseX-App-Cmd
BuildArch:  noarch

BuildRequires: perl
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm) perl(MooseX/NonMoose.pm)

# Run-time:
BuildRequires: perl(Any/Moose.pm)
BuildRequires: perl(App/Cmd.pm)
BuildRequires: perl(App/Cmd/Command.pm)
BuildRequires: perl(English.pm)
BuildRequires: perl(File/Basename.pm)
BuildRequires: perl(Getopt/Long/Descriptive.pm)
# any_moose('::Object')
BuildRequires: perl(Moose/Object.pm)
# any_moose('X::Getopt')
BuildRequires: perl(MooseX/Getopt.pm)
BuildRequires: perl(Mouse.pm)
BuildRequires: perl(namespace/clean.pm)

# Tests:
BuildRequires: perl(base.pm)
BuildRequires: perl(Carp.pm)
BuildRequires: perl(Data/Dumper.pm)
# File::Copy not used
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(IPC/Open3.pm)
BuildRequires: perl(IO/Handle.pm)
# File::Temp not used
# FindBin not used
BuildRequires: perl(lib.pm)
BuildRequires: perl(Moose.pm)
# Both any_moose('X::Getopt') exercised by t/00-compile.t
BuildRequires: perl(MouseX/Getopt.pm)
# Pod::Coverage::TrustPod not used
# Test::EOL not used
# Test::Kwalitee 1.12 not used
# Test::CPAN::Changes 0.19 not used
# Test::CPAN::Meta not used
BuildRequires: perl(Test/More.pm)
# Test::NoTabs not used
# Test::Pod 1.41 not used
# Test::Pod::Coverage 1.08 not used
# Test::use::ok not used
BuildRequires: perl(YAML.pm)

# Optional tests:
# MouseX::ConfigFromFile not yet packaged
## any_moose('X::ConfigFromFile')
#BuildRequires: perl(MouseX::ConfigFromFile) >= 0.08
BuildRequires: perl(Scalar/Util.pm)
BuildRequires: perl(Test/Output.pm)

# we don't pick up Moose keywords automagically yet
Requires:   perl(App/Cmd.pm) >= 0.321
Requires:   perl(App/Cmd/Command.pm)
Requires:   perl(Getopt/Long/Descriptive.pm) >= 0.091
# any_moose('::Object')
Requires:   perl(Moose/Object.pm)
# any_moose('X::Getopt')
Requires:   perl(MooseX/Getopt.pm) >= 0.18



Source44: import.info
%filter_from_requires /^perl\\(Getopt.Long.Descriptive.pm\\)$/d


%description
This package marries App::Cmd with MooseX::Getopt.

Use it like the App::Cmd manpage advises (especially see the
App::Cmd::Tutorial manpage), swapping App::Cmd::Command for
MooseX::App::Cmd::Command.

Then you can write your commands as Moose classes, with the
MooseX::Getopt defining the options for you instead of 'opt_spec'
returning a Getopt::Long::Descriptive spec.


%package -n perl-MouseX-App-Cmd
Group: Development/Perl
Summary:    Mashes up MouseX::Getopt and App::Cmd
# we don't pick up Moose keywords automagically yet
Requires:   perl(MooseX/App/Cmd.pm)
Requires:   perl(MooseX/App/Cmd/Command.pm)
# any_moose('::Object')
Requires:   perl(Mouse/Object.pm)
# any_moose('X::Getopt')
Requires:   perl(MouseX/Getopt.pm)

%description -n perl-MouseX-App-Cmd
This package marries App::Cmd with MouseX::Getopt.

It extends MooseX::App::Cmd which uses Any::Moose to work with either
Moose or Mouse.


%prep
%setup -q -n MooseX-App-Cmd-%{version}
# Test::use::ok is useless,
# <https://github.com/mjgardner/moosex-app-cmd/issues/11>
sed -i -e '/Test::use::ok/d' Makefile.PL META.*

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes LICENSE README
%{perl_vendor_privlib}/MooseX

%changelog
* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1.1
- rebuild to restore role requires

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1_4
- update to new release by fcimport

* Mon Jun 30 2014 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1_3
- moved to Sisyphus as dependency

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_7
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_5
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_4
- update to new release by fcimport

* Wed May 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_2
- fc import

