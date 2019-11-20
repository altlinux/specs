Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(DBD/Pg.pm) perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl(Sub/Identify.pm)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Devel-REPL
Version:        1.003028
Release:        alt2_12
Summary:        Modern perl interactive shell
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Devel-REPL
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Devel-REPL-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl
BuildRequires:  perl(CPAN/Meta/Requirements.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Module/Metadata.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Runtime
BuildRequires:  perl(App/Nopaste.pm)
BuildRequires:  perl(B/Concise.pm)
BuildRequires:  perl(B/Keywords.pm)
BuildRequires:  perl(Data/Dump/Streamer.pm)
BuildRequires:  perl(Data/Dumper/Concise.pm)
BuildRequires:  perl(Devel/Peek.pm)
BuildRequires:  perl(File/HomeDir.pm)
BuildRequires:  perl(File/Next.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(Lexical/Persistence.pm)
BuildRequires:  perl(Module/Refresh.pm)
BuildRequires:  perl(Module/Runtime.pm)
BuildRequires:  perl(Moose.pm)
BuildRequires:  perl(Moose/Meta/Role.pm)
BuildRequires:  perl(Moose/Role.pm)
BuildRequires:  perl(Moose/Util/TypeConstraints.pm)
BuildRequires:  perl(MooseX/Getopt.pm)
BuildRequires:  perl(MooseX/Object/Pluggable.pm)
BuildRequires:  perl(namespace/autoclean.pm)
BuildRequires:  perl(PPI.pm)
BuildRequires:  perl(PPI/Dumper.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Sys/SigAction.pm)
BuildRequires:  perl(Term/ANSIColor.pm)
BuildRequires:  perl(Term/ReadLine.pm)
BuildRequires:  perl(Time/HiRes.pm)
# Tests only
BuildRequires:  perl(blib.pm)
BuildRequires:  perl(if.pm)
BuildRequires:  perl(Test/Fatal.pm)
BuildRequires:  perl(Test/More.pm)
Requires:       perl(Moose.pm) >= 0.930
Requires:       perl(Moose/Meta/Role.pm)
Requires:       perl(MooseX/Getopt.pm) >= 0.180
Requires:       perl(MooseX/Object/Pluggable.pm) >= 0.000.900
# Require plugins used by default, see Devel::REPL::Profile::Minimal
Requires:       perl(Devel/REPL/Plugin/Commands.pm)
Requires:       perl(Devel/REPL/Plugin/DDS.pm)
Requires:       perl(Devel/REPL/Plugin/History.pm)
Requires:       perl(Devel/REPL/Plugin/LexEnv.pm)
Requires:       perl(Devel/REPL/Plugin/MultiLine/PPI.pm)
Requires:       perl(Devel/REPL/Plugin/Packages.pm)



# Remove under-specified dependencies

Source44: import.info
%filter_from_requires /^perl(\(Data.Dump.Streamer\|Moose\).pm)/d

%description
This is an interactive shell for Perl, commonly known as a REPL - Read,
Evaluate, Print, Loop. The shell provides for rapid development or testing
of code without the need to create a temporary source code file.

Through a plugin system, many features are available on demand. These plugins
are available:

    Completion
    CompletionDriver::INC
    CompletionDriver::Keywords
    DDC
    DDS
    Interrupt
    LexEnv
    MultiLine::PPI
    Nopaste
    PPI
    Refresh

The plugins are available in standalone RPM packages. For example the
MultiLine::PPI plugin is delivered within %{name}-MultiLine-PPI package.

%package Plugin-Completion
Group: Development/Perl
Summary:        Devel-REPL plugin for tab completion
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Plugin-Completion
This Perl interactive shell plugin provides extensible tab completion. By
default, the Completion plugin explicitly does not use the GNU Readline or
Term::ReadLine::Perl fallback file name completion.

%package Plugin-CompletionDriver-INC
Group: Development/Perl
Summary:        Devel-REPL plugin for completing module names
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Plugin-CompletionDriver-INC
This Perl interactive shell plugin provides module names completion.

%package Plugin-CompletionDriver-Keywords
Group: Development/Perl
Summary:        Devel-REPL plugin for completing keywords and operators
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Plugin-CompletionDriver-Keywords
This Perl interactive shell plugin provides keyword and operator names
completion.

%package Plugin-DDC
Group: Development/Perl
Summary:        Devel-REPL plugin for formatting results with Data::Dumper::Concise
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Plugin-DDC
This Perl interactive shell plugin formats results with Data::Dumper::Concise.

%package Plugin-DDS
Group: Development/Perl
Summary:        Devel-REPL plugin for formatting results with Data::Dump::Streamer
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(Data/Dump/Streamer.pm) >= 2.390

%description Plugin-DDS
This Perl interactive shell plugin formats results with Data::Dump::Streamer.

%package Plugin-Interrupt
Group: Development/Perl
Summary:        Devel-REPL plugin for trapping INT signal
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Plugin-Interrupt
By default Devel::REPL exits on SIGINT (usually Ctrl-C). If you load this
module, SIGINT will be trapped and used to kill long-running commands
(statements) and also to kill the line being edited (like e.g. BASH do).
(You can still use Ctrl-D to exit.)

%package Plugin-LexEnv
Group: Development/Perl
Summary:        Devel-REPL plugin for lexical environments
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Plugin-LexEnv
This Perl interactive shell plugin provides environments for lexical variables.

%package Plugin-MultiLine-PPI
Group: Development/Perl
Summary:        Devel-REPL plugin for multi-line blocks
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Plugin-MultiLine-PPI
This Perl interactive shell plugin will collect lines until you have no
unfinished structures.  This lets you write subroutines, "if" statements,
loops, etc. more naturally.

%package Plugin-Nopaste
Group: Development/Perl
Summary:        Devel-REPL plugin for uploading data to a nopaste site
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(App/Nopaste.pm)

%description Plugin-Nopaste
This Perl interactive shell plugin allows you to upload session's input and
output to a nopaste site.

%package Plugin-PPI
Group: Development/Perl
Summary:        Devel-REPL plugin for dumping Perl code
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Plugin-PPI
This Perl interactive shell plugin provides a "ppi" command that uses
PPI::Dumper to dump PPI-parsed Perl documents.

%package Plugin-Refresh
Group: Development/Perl
Summary:        Devel-REPL plugin for reloading libraries
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Plugin-Refresh
This Perl interactive shell plugin allows you to reload Perl libraries with
Module::Refresh module.

%prep
%setup -q -n Devel-REPL-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=%{buildroot}
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc --no-dereference LICENCE
%doc Changes CONTRIBUTING README examples
%{_bindir}/*
%{perl_vendor_privlib}/*

# Plugin-Completion
%exclude %{perl_vendor_privlib}/Devel/REPL/Plugin/Completion.pm

# Plugin-CompletionDriver-INC
%exclude %{perl_vendor_privlib}/Devel/REPL/Plugin/CompletionDriver/INC.pm

# Plugin-CompletionDriver-Keywords
%exclude %{perl_vendor_privlib}/Devel/REPL/Plugin/CompletionDriver/Keywords.pm

# Plugin-DDC
%exclude %{perl_vendor_privlib}/Devel/REPL/Plugin/DDC.pm

# Plugin-DDS
%exclude %{perl_vendor_privlib}/Devel/REPL/Plugin/DDS.pm

# Plugin-Interrupt
%exclude %{perl_vendor_privlib}/Devel/REPL/Plugin/Interrupt.pm

# Plugin-LexEnv
%exclude %{perl_vendor_privlib}/Devel/REPL/Plugin/LexEnv.pm

# Plugin-MultiLine-PPI
%exclude %{perl_vendor_privlib}/Devel/REPL/Plugin/MultiLine

# Plugin-Nopaste
%exclude %{perl_vendor_privlib}/Devel/REPL/Plugin/Nopaste.pm

# Plugin-PPI
%exclude %{perl_vendor_privlib}/Devel/REPL/Plugin/PPI.pm

# Plugin-Refresh
%exclude %{perl_vendor_privlib}/Devel/REPL/Plugin/Refresh.pm

%files Plugin-Completion
%{perl_vendor_privlib}/Devel/REPL/Plugin/Completion.pm

%files Plugin-CompletionDriver-INC
%{perl_vendor_privlib}/Devel/REPL/Plugin/CompletionDriver/INC.pm

%files Plugin-CompletionDriver-Keywords
%{perl_vendor_privlib}/Devel/REPL/Plugin/CompletionDriver/Keywords.pm

%files Plugin-DDC
%{perl_vendor_privlib}/Devel/REPL/Plugin/DDC.pm

%files Plugin-DDS
%{perl_vendor_privlib}/Devel/REPL/Plugin/DDS.pm

%files Plugin-Interrupt
%{perl_vendor_privlib}/Devel/REPL/Plugin/Interrupt.pm

%files Plugin-LexEnv
%{perl_vendor_privlib}/Devel/REPL/Plugin/LexEnv.pm

%files Plugin-MultiLine-PPI
%{perl_vendor_privlib}/Devel/REPL/Plugin/MultiLine

%files Plugin-Nopaste
%{perl_vendor_privlib}/Devel/REPL/Plugin/Nopaste.pm

%files Plugin-PPI
%{perl_vendor_privlib}/Devel/REPL/Plugin/PPI.pm

%files Plugin-Refresh
%{perl_vendor_privlib}/Devel/REPL/Plugin/Refresh.pm


%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1.003028-alt2_12
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.003028-alt2_8
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.003028-alt2_7
- update to new release by fcimport

* Sun Nov 05 2017 Igor Vlasenko <viy@altlinux.ru> 1.003028-alt2_3
- to Sisyphus as perl-PDL dep

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.003028-alt1_3
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.003028-alt1_2
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.003028-alt1_1
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 1.003027-alt1_1
- update to new release by fcimport

* Tue Dec 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.003026-alt1_1
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.003015-alt1_5
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.003015-alt1_4
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.003015-alt1_3
- update to new release by fcimport

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.003015-alt1_1
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.003014-alt1_2
- update to new release by fcimport

* Wed Jan 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.003014-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.003013-alt1_3
- update to new release by fcimport

* Wed Jun 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.003013-alt1_1
- fc import

