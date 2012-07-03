# Spec file for Perl module Net::IDN::Nameprep

Name: perl-Net-IDN-Nameprep
Version: 1.100
Release: alt1.1

Summary: Perl module implements IDN nameprep specification

%define real_name Net-IDN-Nameprep

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/~miyagawa/Net-IDN-Nameprep/

Packager: Nikolay Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Wed Mar 24 2010
BuildRequires: perl-Module-Build perl-Test-NoWarnings perl-Unicode-Stringprep

%description
Perl module Net::IDN::Nameprep implements IDN (Internationalized
Domain Names) nameprep specification (RFC 3491).


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Net/IDN/Nameprep*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.100-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> 1.100-alt1
- automated CPAN update

* Tue Mar 23 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.000-alt1
- Initial build for ALT Linux Sisyphus
