%define module		Exporter-Lite
%define m_distro	Exporter-Lite
%define m_name		Exporter::Lite
%define m_author_id	MSCHWERN
Name: perl-%module
Version: 0.02
Release: alt1

Summary: Exporter::Lite - Lightweight exporting of variables

Group: Development/Perl
License: Unknown

Packager: Vitaly Lipatov <lav@altlinux.ru>

Url: http://search.cpan.org/dist/%m_distro/
Source: http://www.cpan.org/authors/id/M/MS/MSCHWERN/Exporter-Lite-0.02.tar.gz

BuildArch: noarch

# manually removed: perl-Exporter-Lite
# Automatically added by buildreq on Sun Feb 27 2005
BuildRequires: perl-devel

%description
This is an alternative to Exporter intended to provide a lightweight
subset of its functionality.  It supports C<import()>, C<@EXPORT> and
C<@EXPORT_OK> and not a whole lot else.

Unlike Exporter, it is not necessary to inherit from Exporter::Lite
(ie. no C<@ISA = qw(Exporter::Lite)> mantra).  Exporter::Lite simply
exports its import() function.  This might be called a "mix-in".

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf %buildroot%perl_vendor_man3dir/

%files
%perl_vendor_privlib/Exporter/

%changelog
* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.01-alt2
- fix directory ownership violation
- disable man packing

* Sun Feb 27 2005 Vitaly Lipatov <lav@altlinux.ru> 0.01-alt1
- first build for ALT Linux Sisyphus
