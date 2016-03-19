## SPEC file for Perl module AWS::Signature4

%define real_name AWS-Signature4

Name: perl-AWS-Signature4
Version: 1.02
Release: alt1

Summary: create a version4 signature for Amazon Web Services

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/AWS-Signature4/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sat Mar 19 2016
# optimized out: perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Encode perl-HTML-Parser perl-HTTP-Message perl-JSON-PP perl-Module-Metadata perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Escapes perl-Pod-Simple perl-URI perl-devel perl-parent perl-podlators python3 python3-base
BuildRequires: perl-Digest-SHA perl-Module-Build perl-TimeDate perl-libwww

%description
Perl module AWS::Signature4 implements Amazon Web Service's
Signature version 4. It can be used to add authentication
information to the headers of GET, POST, PUT and DELETE.

The module can be also used to generate "signed" URLs. These
are preauthorized URLs that contain all the authenticationand
header information in the URL query parameters. They can be
sent to another user to, for example, grant time-limited
access to a private S3 bucket.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changes
%perl_vendor_privlib/AWS/Signature4*

%changelog
* Sat Mar 19 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1.02-alt1
- Initial build for ALT Linux Sisyphus
