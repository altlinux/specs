%define _unpackaged_files_terminate_build 1

%define module Po4a
%define m_distro po4a
%define m_name %module
%define m_author_id unknown
%define _disable_test 0

Name: po4a
Version: 0.65
Release: alt2

Summary: Tools for helping translation of documentation

License: GPLv2+
Group: Text tools

Url: http://po4a.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

# Note! change this magic number before upgrade
Source: %name-%version.tar

# Automatically added by buildreq on Sat Sep 07 2013
# optimized out: docbook-dtds libgpg-error perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Encode perl-JSON-PP perl-Module-Metadata perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-Text-CharWidth perl-devel perl-podlators python3-base xml-common
BuildRequires: docbook-style-xsl perl-HTML-Parser perl-Locale-gettext perl-Module-Build perl-SGMLSpm perl-Term-ReadKey perl-Text-WrapI18N xsltproc

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators

BuildRequires:  perl-Module-Build >= 0.42
BuildRequires:  perl-SGMLSpm
BuildRequires:  perl-Pod-Parser
# for Unicode::GCString
BuildRequires:  perl-Unicode-LineBreak 
BuildRequires:  perl-YAML-Tiny

Requires: gettext-tools

%description
The po4a (po for anything) project goal is to ease translations (and
more interestingly, the maintenance of translations) using gettext
tools on areas where they were not expected like documentation.

This package contains the main libraries of po4a, and the following
sub-modules:
 - KernelHelp: Help messages of each kernel compilation option.
 - Man: Good old manual page format.
 - Pod: Perl documentation format.
 - Sgml: either debiandoc or docbook DTD.
 - Dia: uncompressed Dia diagrams.
 - LaTeX: generic TeX or LaTeX format

%prep
%setup

%build
export LC_ALL=en_US.UTF-8
perl Build.PL
%perl_vendor_build --install_path bindoc=%_man1dir --install_path libdoc=%_man3dir

%check
# requires texlive, which is too heavy for the package
rm t/24-tex.t
./Build test

%install
%perl_vendor_install
# remove localized man pages
rm -rf %buildroot%_mandir/??{,_*}
rm -rf %buildroot%_datadir/locale/??_???? # TBD: why is this not packaged?
%find_lang %name

%files -f %name.lang
%_bindir/*
# Locale already created in perl-Locale-gettext
%perl_vendor_privlib/Locale/Po4a/
%_man1dir/*
%_man3dir/*
%_man7dir/*

%changelog
* Thu Feb 09 2023 Anton Midyukov <antohami@altlinux.org> 0.65-alt2
- Requires: gettext-tools (Closes: 43546)

* Thu Dec  9 2021 Aleksey Cheusov <cheusov@altlinux.org> 0.65-alt1
- 0.65

* Tue Dec  7 2021 Aleksey Cheusov <cheusov@altlinux.org> 0.47-alt1.2
- Keep remote "upstream" here .gear/upstream/remotes.
  Minor updates and clean-ups in .spec file.

* Thu Jul 15 2021 Igor Vlasenko <viy@altlinux.org> 0.47-alt1.1
- NMU: drop 1.03ii from requires on perl-SGMLSpm

* Fri Oct 16 2015 Andrey Cherepanov <cas@altlinux.org> 0.47-alt1
- New version from https://alioth.debian.org/anonscm/git/po4a/po4a.git
- Package man pages

* Sat Sep 07 2013 Vitaly Lipatov <lav@altlinux.ru> 0.45-alt1
- new version 0.45 (with rpmrb script)

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.44-alt1
- new version 0.44 (with rpmrb script)

* Fri Nov 26 2010 Igor Vlasenko <viy@altlinux.ru> 0.33.3-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Nov 15 2008 Vitaly Lipatov <lav@altlinux.ru> 0.33.3-alt2
- fix build

* Sat Apr 12 2008 Vitaly Lipatov <lav@altlinux.ru> 0.33.3-alt1
- new version 0.33.3 (with rpmrb script)
- update buildreqs

* Sun Jan 13 2008 Vitaly Lipatov <lav@altlinux.ru> 0.32-alt1
- new version 0.32 (with rpmrb script)
- disable test
- update buildreqs

* Thu Apr 12 2007 Vitaly Lipatov <lav@altlinux.ru> 0.28-alt1
- new version 0.28 (with rpmrb script)

* Fri Feb 17 2006 Vitaly Lipatov <lav@altlinux.ru> 0.23-alt0.1
-  initial build for ALT Linux Sisyphus
