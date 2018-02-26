%define dist Locale-Maketext-Gettext
Name: perl-%dist
Version: 1.28
Release: alt1.1

Summary: Joins the gettext and Maketext frameworks
License: %perl_license
Group: Development/Perl
Packager: Artem Zolochevskiy <azol@altlinux.ru>

URL: %CPAN %dist
# http://search.cpan.org/CPAN/authors/id/I/IM/IMACAT/Locale-Maketext-Gettext-1.28.tar.gz
Source: %dist-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue Jan 19 2010
BuildRequires: perl-Module-Build

BuildRequires: perl-Locale-Maketext perl-Encode-TW perl-Encode-CN

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators

%description
Locale::Maketext::Gettext joins the GNU gettext and Maketext
frameworks.  It is a subclass of Locale::Maketext that follows the
way GNU gettext works.  It works seamlessly, both in the sense of
GNU gettext and Maketext.  As a result, you enjoy both their
advantages, and get rid of both their problems, too.

You start as an usual GNU gettext localization project:  Work on
PO files with the help of translators, reviewers and Emacs.  Turn
them into MO files with msgfmt.  Copy them into the appropriate
locale directory, such as
/usr/share/locale/de/LC_MESSAGES/myapp.mo.

Then, build your Maketext localization class, with your base class
changed from Locale::Maketext to Locale::Maketext::Gettext.  That's
all.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build --install_path bindoc=%_man1dir

%install
%perl_vendor_install

%files
%doc BUGS Changes README THANKS TODO
%_bindir/*
%perl_vendor_privlib/Locale/
%_man1dir/*

%changelog
* Fri Nov 26 2010 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jan 19 2010 Artem Zolochevskiy <azol@altlinux.ru> 1.28-alt1
- initial build for Sisyphus
