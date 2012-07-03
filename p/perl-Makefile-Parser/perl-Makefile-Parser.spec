%define dist Makefile-Parser
Name: perl-%dist
Version: 0.215
Release: alt1

Summary: Simple parser for Makefiles
License: %perl_license
Group: Development/Perl
Packager: Artem Zolochevskiy <azol@altlinux.ru>

URL: %CPAN %dist
# http://search.cpan.org/CPAN/authors/id/A/AG/AGENT/Makefile-Parser-0.215.tar.gz
Source: %dist-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue Jan 12 2010
BuildRequires: perl-Class-Accessor perl-Class-Trigger perl-File-Slurp perl-Filter perl-IPC-Run3 perl-Makefile-DOM perl-PerlIO perl-devel

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators

%description
This is a simple parser for Makefiles. At this very early stage, the
parser only supports a limited set of features, so it may not recognize
most of the advanced features provided by certain make tools like GNU
make. Its initial purpose is to provide basic support for another module
named Makefile::GraphViz, which is aimed to render the building process
specified by a Makefile using the amazing GraphViz library. The Make
module is not satisfactory for this purpose, so I decided to build one
of my own.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc Changes README
%_bindir/*
%perl_vendor_privlib/Makefile/
%_man1dir/*

%changelog
* Mon Apr 16 2012 Vladimir Lettiev <crux@altlinux.ru> 0.215-alt1
- 0.211 -> 0.215 (Closes: #27223)

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.211-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jan 12 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.211-alt1
- initial build for Sisyphus
