%define dist Perl-Tags

Name: perl-Perl-Tags
Version: 0.28
Release: alt2

Summary: Generate (possibly exuberant) Ctags style tags for Perl sourcecode

License: Artistic
Group: Development/Perl
Url: %CPAN %dist

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Wed Jun 25 2008
BuildRequires: perl-Module-Locate perl-Test-Pod perl-Test-Pod-Coverage perl-PPI

%description
use Perl::Tags;
my $naive_tagger = Perl::Tags::Naive->new( max_level=>2 );
$naive_tagger->process(
    files => ['Foo.pm', 'bar.pl'],
    refresh=>1
);

Recursively follows "use" and "require" statements, up to a maximum
of "max_level".

The implemented tagger, "Perl::Tags::Naive" is a more-or-less straight
ripoff, slightly updated, of the original pltags code, and is rather
naive.  It should be possible to subclass using something like "PPI"
or "Text::Balanced", though be aware that this is alpha software and
the internals are subject to change (so get in touch to let me know
what you want to do and I'll try to help).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%_bindir/perl-tags
%perl_vendor_privlib/Perl/Tags*
%doc README Changes

%changelog
* Mon Feb 18 2013 Vladimir Lettiev <crux@altlinux.ru> 0.28-alt2
- add perl-tags script
- spec cleanup

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Jul 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1.1
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Wed Jun 25 2008 Michael Bochkaryov <misha@altlinux.ru> 0.23-alt1
- first build for ALT Linux Sisyphus

