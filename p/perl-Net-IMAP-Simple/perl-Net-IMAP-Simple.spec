## SPEC file for Perl module Net::IMAP::Simple

Name: perl-Net-IMAP-Simple
Version: 1.2034
Release: alt1

Summary: Perl extension for simple IMAP account handling

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Net-IMAP-Simple/
#URL: https://github.com/jettero/net--imap--simple

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Net-IMAP-Simple
Source: %real_name-%{version}.tar
Patch0: %real_name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Thu Oct 18 2012
# optimized out: perl-Class-Load perl-Class-Singleton perl-Data-OptList perl-DateTime perl-DateTime-Locale perl-DateTime-TimeZone perl-Email-Address perl-Email-MIME-ContentType perl-Email-MIME-Encodings perl-Email-MessageID perl-Email-Simple perl-Encode perl-List-MoreUtils perl-Math-Round perl-Module-Implementation perl-Module-Runtime perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-Validate perl-Sub-Install perl-Sub-Name perl-Try-Tiny perl-parent
BuildRequires: perl-Class-Accessor perl-DateTime-Format-Mail perl-DateTime-Format-Strptime perl-Email-MIME perl-Parse-RecDescent perl-Regexp-Common perl-devel


%description
Perl module Net::IMAP::Simple provides a simple way for accessing
IMAP accounts.

%prep
%setup  -n %real_name-%version
%patch0 -p1


%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes TODO
%perl_vendor_privlib/Net/IMAP/Simple*

%changelog
* Thu Oct 18 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.2034-alt1
- New version

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 1.2025-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Mar 25 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.17-alt1
- New version 1.17
  - Added debugging
  - Upgraded imap.pl example script
  - Updated documentation
  - Several small patches

* Thu Sep 28 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.16-alt1
- Initial build for ALT Linux Sisyphus

* Thu Sep 28 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.16-alt0
- Initial build

