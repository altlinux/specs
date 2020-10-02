Name: perl-XML-LibXML-PrettyPrint
Version: 0.006
Release: alt1
Summary: Add pleasant white space to an XML tree
# CONTRIBUTING: GPL+ or Artistic or CC-BY-SA
# COPYRIGHT:    Public Domain
# LICENSE:      GPL1 and Artistic license text
# Other files:  GPL+ or Artistic
License: (GPL-1.0-or-later or Artistic-1.0) and (GPL-1.0-or-later or Artistic-1.0 or CC-BY-SA-2.0) and Public Domain
Group: Graphical desktop/Other
Url: https://metacpan.org/release/XML-LibXML-PrettyPrint
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/XML-LibXML-PrettyPrint-%version.tar.gz
# Do not use %%_bindir/env in scripts
Patch: XML-LibXML-PrettyPrint-0.006-Normalize-shell-bang.patch
BuildArch: noarch
BuildRequires: make
#BuildRequires: perl-generators
#BuildRequires: perl-interpreter
BuildRequires: perl-devel >= 0.96
# Run-time:
BuildRequires: perl-base >= 5.8.1
BuildRequires: perl-Exporter-Tiny
BuildRequires: perl-XML-LibXML >= 1.62
# Tests:
BuildRequires: perl-Test-Warnings
#Requires: perl(:MODULE_COMPAT_%%(eval "`perl -V:version`"; echo $version))

%description
XML::LibXML::PrettyPrint is a Perl module that can be applied to an
XML::LibXML DOM tree to reformat it into a more readable result.

%prep
%setup -n XML-LibXML-PrettyPrint-%version
%patch -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make

%install
make pure_install DESTDIR=%buildroot
%_fixperms %buildroot/*

%check
make test

%files
%doc LICENSE
%doc Changes CONTRIBUTING COPYRIGHT CREDITS README
%_bindir/*
%perl_vendor_privlib/*
#_man1dir/*
#_man3dir/*

%changelog
* Mon Mar 18 2019 Leontiy Volodin <lvol@altlinux.org> 0.006-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
