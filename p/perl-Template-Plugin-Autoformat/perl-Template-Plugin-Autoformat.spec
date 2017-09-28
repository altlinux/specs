%define module_version 2.77
%define module_name Template-Plugin-Autoformat
%define _without_test 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Template.pm) perl(Template/Plugin.pm) perl(Template/Test.pm) perl(Test/More.pm) perl(Text/Autoformat.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 2.77
Release: alt2
Summary: TT plugin for Text::Autoformat
Group: Development/Perl
License: perl
URL: https://github.com/karpet/template-plugin-autoformat

Source0: http://cpan.org.ua/authors/id/K/KA/KARMAN/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
This Template Toolkit plugin module is an interface to Damian
Conway's `Text::Autoformat' Perl module which provides advanced text wrapping
and formatting.

Configuration options may be passed to the plugin constructor via the 
`USE' directive.

    [%% USE autoformat(right => 30) %%]

The autoformat subroutine can then be called, passing in text items which 
will be wrapped and formatted according to the current configuration.

    [%% autoformat('The cat sat on the mat') %%]

Additional configuration items can be passed to the autoformat subroutine
and will be merged with any existing configuration specified via the 
constructor.

    [%% autoformat(text, left => 20) %%]

Configuration options are passed directly to the `Text::Autoformat' plugin.
At the time of writing, the basic configuration items are:

    left        left margin (default: 1)
    right       right margin (default 72)
    justify     justification as one of 'left', 'right', 'full'
                or 'centre' (default: left)
    case        case conversion as one of 'lower', 'upper',
                'sentence', 'title', or 'highlight' (default: none)
    squeeze     squeeze whitespace (default: enabled)

The plugin also accepts a `form' item which can be used to define a 
format string.  When a form is defined, the plugin will call the 
underlying `form()' subroutine in preference to `autoformat()'.

    [%% USE autoformat(form => '>>>>.<<') %%]
    [%% autoformat(123.45, 666, 3.14) %%]

Additional configuration items relevant to forms can also be specified.

    [%% USE autoformat(form => '>>>>.<<', numeric => 'AllPlaces') %%]
    [%% autoformat(123.45, 666, 3.14) %%]

These can also be passed directly to the autoformat subroutine.

    [%% USE autoformat %%]
    [%% autoformat( 123.45, 666, 3.14,
                   form    => '>>>>.<<', 
                   numeric => 'AllPlaces' )
    %%]

See the Text::Autoformat manpage for further details.


%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md
%perl_vendor_privlib/T*

%changelog
* Thu Sep 28 2017 Igor Vlasenko <viy@altlinux.ru> 2.77-alt2
- to Sisyphus

* Thu Apr 02 2015 Igor Vlasenko <viy@altlinux.ru> 2.77-alt1
- regenerated from template by package builder

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 2.76-alt1
- regenerated from template by package builder

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 2.75-alt1
- regenerated from template by package builder

* Mon Apr 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.71-alt1
- initial import by package builder

