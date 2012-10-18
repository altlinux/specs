# Spec file for Perl module Net::IDN::Nameprep

Name: perl-Net-IDN-Nameprep
Version: 1.101
Release: alt1

Summary: Perl module implements IDN nameprep specification

%define real_name Net-IDN-Nameprep

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Net-IDN-Nameprep/

Packager: Nikolay Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Thu Oct 18 2012
# optimized out: perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Devel-StackTrace perl-Encode perl-JSON-PP perl-Module-Metadata perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Escapes perl-Pod-Simple perl-Unicode-Normalize perl-devel perl-podlators
BuildRequires: perl-HTML-Parser perl-Module-Build perl-Test-NoWarnings perl-Unicode-Stringprep perl-unicore

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
* Thu Oct 18 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.101-alt1
- New version

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.100-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> 1.100-alt1
- automated CPAN update

* Tue Mar 23 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.000-alt1
- Initial build for ALT Linux Sisyphus
