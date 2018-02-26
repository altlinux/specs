## SPEC file for Perl module URI-Encode

Name: perl-URI-Encode
Version: 0.06
Release: alt1

Summary: Perl module for simple percent Encoding/Decoding

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/URI-Encode/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name URI-Encode
Source: %real_name-%version.tar
Patch0: %real_name-%version-%release.patch

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Sat Jan 28 2012
# optimized out: perl-CPAN-Meta perl-CPAN-Meta-YAML perl-Encode perl-JSON-PP perl-Module-Metadata perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Escapes perl-Pod-Simple perl-devel perl-podlators
BuildRequires: perl-Module-Build

%description
provides simple URI (Percent) encoding/decoding.

The main purpose of this module is to provide an easy method to
encode strings (mainly URLs) into a format which can be pasted
into a plain text emails, and that those links are 'click-able'
by the person reading that email. This can be accomplished by
NOT encoding the reserved characters.

If you are looking for speed and want to encode reserved
characters, use URI::Escape::XS .

%prep
%setup  -n %real_name-%version
%patch0 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/URI/Encode*

%changelog
* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.06-alt1
- Initial build for ALT Linux Sisyphus

