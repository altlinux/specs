%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Contextual/Return.pm) perl(ExtUtils/MakeMaker.pm) perl(Scalar/Util.pm) perl(Symbol.pm) perl(Test/More.pm) perl(diagnostics.pm)
# END SourceDeps(oneline)
%define module_version 0.004012
%define module_name IO-Prompter
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.004012
Release: alt1
Summary: Prompt for input, read it, clean it, return it.
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/D/DC/DCONWAY/IO-Prompter-%{version}.tar.gz
BuildArch: noarch

%description
IO::Prompter exports a single subroutine, `prompt', that prints a.prompt (but only if the program's selected input and output streams are
connected to a terminal), then reads some input, then chomps it, and
finally returns an object representing that text.

The `prompt()' subroutine expects zero-or-more arguments.

Any argument that starts with a hyphen (`-') is treated as a named
option (many of which require an associated value, that may be passed as
the next argument). See the section on "Summary of options" and the section on "Options reference" for details of the available options.

Any other argument that is a string is treated as (part of) the prompt
to be displayed. All such arguments are concatenated together before the
prompt is issued. If no prompt string is provided, the string
`'> '' is used instead.

Normally, when `prompt()' is called in either list or scalar context,
it returns an opaque object that autoconverts to a string. In scalar
boolean contexts this return object evaluates true if the input
operation succeeded. In list contexts, if the input operation fails
`prompt()' returns an empty list instead of a return object. This
allows failures in list context to behave correctly (i.e. be false).

If you particularly need a list-context call to `prompt()' to always
return a value (i.e. even on failure), prefix the call with `scalar':

    # Only produces as many elements
    # as there were successful inputs...
    my @data = (
        prompt('Name:'),
        prompt(' Age:'),
        prompt(' Sex:'),
    );

    # Always produces exactly three elements
    # (some of which may be failure objects)...
    my @data = (
        scalar prompt('Name:'),
        scalar prompt(' Age:'),
        scalar prompt(' Sex:'),
    );

In void contexts, `prompt()' still requests input, but also issues a
warning about the general uselessness of performing an I/O operation
whose results are then immediately thrown away.
See the section on "Useful useless uses of `prompt()'" for an exception to this.

The `prompt()' function also sets `$_' if it is called in a boolean
context but its return value is not assigned to a variable. Hence, it is
designed to be a drop-in replacement for `readline' or `<>'.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/I*

%changelog
* Wed Feb 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.004012-alt1
- automated CPAN update

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.004011-alt1
- automated CPAN update

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.004010-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.004010-alt1
- regenerated from template by package builder

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.004007-alt1
- initial import by package builder

