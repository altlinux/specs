%define module Po4a
%define m_distro po4a
%define m_name %module
%define m_author_id unknown
%define _disable_test 1

Name: po4a
Version: 0.33.3
Release: alt2.1

Summary: Tools for helping translation of documentation

License: GPL
Group: Text tools

Url: http://po4a.alioth.debian.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: http://alioth.debian.org/frs/download.php/2379/%m_distro-%version.tar.bz2

# manually removed: po4a
# Automatically added by buildreq on Sat Apr 12 2008 (-bi)
BuildRequires: man perl-Locale-gettext perl-Module-Build perl-SGMLSpm perl-Term-ReadKey perl-Text-WrapI18N

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators

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
%setup -q -n %m_distro-%version

%build
%perl_vendor_build --install_path bindoc=%_man1dir

%install
%perl_vendor_install
%find_lang %name
# remove localized man pages
rm -rf %buildroot%_mandir/??
rm -rf %buildroot%perl_vendor_privlib/i386-linux/

%files -f %name.lang
%_bindir/*
# Locale already created in perl-Locale-gettext
%perl_vendor_privlib/Locale/Po4a/
%_man1dir/*
#%_man7dir/*

%changelog
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
