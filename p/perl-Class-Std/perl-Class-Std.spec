# SPEC file for building Perl module Class-Std

%define real_name Class-Std

Name: perl-Class-Std
Version: 0.013
Release: alt1

Summary: Perl module for creating standard "inside-out" classes 
Group: Development/Perl
License: %perl_license

URL: %CPAN %real_name
Source: %real_name-%version.tar
Patch: %name-0.011-alt-pod.patch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sat May 30 2015
# optimized out: perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Encode perl-JSON-PP perl-Module-Metadata perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Escapes perl-Pod-Simple perl-devel perl-parent perl-podlators
BuildRequires: perl-HTML-Parser perl-Module-Build

BuildArch: noarch

%description
Perl module Class::Std provides the standard infrastructure
required to create "inside-out" classes, as described in
Chapters 15 and 16 of "Perl Best Practices" (O'Reilly, 2005).

%prep
%setup -q -n %real_name-%version
%patch -p2

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Class/Std*
%doc README Changes

%changelog
* Sat May 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.013-alt1
- New version

* Tue Oct 09 2012 Vladimir Lettiev <crux@altlinux.ru> 0.011-alt2
- corrected version
- fixed POD

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Mar 08 2010 Nikolay A. Fetisov <naf@altlinux.ru> 0.11-alt1
- New version

* Sat May 24 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.0.9-alt1
- New version

* Thu Aug 09 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.0.8-alt1
- Initial build for ALT Linux Sisyphus

