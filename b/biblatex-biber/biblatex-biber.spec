Name: biblatex-biber
Version: 0.9.7
Release: alt1

Summary: A BibTeX replacement for users of biblatex

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Kirill Maslinsky <kirill@altlinux.org>

BuildArch: noarch

Source: biblatex-biber-v%version.tar

BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-unicore perl-IPC-Cmd perl-Readonly-XS perl-List-AllUtils perl-Log-Log4perl perl-File-Slurp perl-XML-LibXML-Simple perl-Config-General perl-Data-Dump perl-Unicode-Normalize perl-Test-Pod perl-Test-Pod-Coverage 
BuildRequires: perl-Regexp-Common perl-Text-BibTeX perl-Parse-RecDescent 
BuildRequires: perl-Module-Build perl-Readonly perl-Data-Compare perl-File-Slurp perl-IPC-Run3 perl-Unicode-Collate perl-XML-LibXSLT perl-Config-AutoConf perl-ExtUtils-LibBuilder perl-File-Find-Rule perl-Date-Simple perl-File-Slurp-Unicode 
# added for 0.9.7
BuildRequires: perl-Capture-Tiny perl-File-Which

Requires: perl-unicore perl-File-Find-Rule

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators

%description
The biblatex package by Philipp Lehman is likely to become the definitive
citation management tool for LaTeX users. Biblatex relies on the venerable
BibTeX program only for sorting and generating a very generic bbl file without
any formatting instruction. Everything else is taken care of by biblatex, which
provides a powerful and flexible macro interface for authors of citation
styles.

With Biber it is no longer necessary to rely on BibTeX. For maximal
portability, the current version includes a Pure Perl BibTeX parser with a
Parse::RecDescent grammar, but if available it will use the much faster
Text::BibTeX module which relies on the btparse C library. The objective of the
first development phase is to have a robust and reliable emulation of the
BibTeX processor with the biblatex.bst style file. In other words, given the
same .aux file as input, biber should output a functionally identical .bbl file
as BibTeX.

%prep
%setup -q -n %name-v%version
# disable test requiring network access
rm -fv t/remote-files.t

%build
%perl_vendor_build --install_path bindoc=%_man1dir

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Biber*
%perl_vendor_privlib/Unicode
%_bindir/*
%_man1dir/*

%changelog
* Mon Dec 05 2011 Kirill Maslinsky <kirill@altlinux.org> 0.9.7-alt1
- 0.9.7 (for use with biblatex 1.7)

* Thu Nov 03 2011 Kirill Maslinsky <kirill@altlinux.org> 0.9.5-alt1.2
- disable test requiring network access

* Thu Nov 03 2011 Kirill Maslinsky <kirill@altlinux.org> 0.9.5-alt1.1
- fix missing patch

* Tue Nov 01 2011 Kirill Maslinsky <kirill@altlinux.org> 0.9.5-alt1
- 0.9.5 (for use with biblatex 1.6)

* Fri Nov 26 2010 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Mar 31 2010 Kirill Maslinsky <kirill@altlinux.org> 0.5.3-alt1
- 0.5.3

* Mon Mar 22 2010 Kirill Maslinsky <kirill@altlinux.org> 0.5.3-alt0.1
- 0.5.3 (pre)

* Fri Mar 12 2010 Kirill Maslinsky <kirill@altlinux.org> 0.5.2-alt1
- initial build for ALT Linux Sisyphus


