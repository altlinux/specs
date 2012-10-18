## SPEC file for Perl module CGI::SSI
## Used in ikiwiki

Name: perl-CGI-SSI
Version: 0.92
Release: alt1

Summary: Perl module for using SSI from CGI scripts

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/CGI-SSI/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name CGI-SSI
Source: %real_name-%version.tar
Patch0: %real_name-0.92-alt-drop_network_tests.patch

BuildRequires(pre): rpm-build-licenses


# Automatically added by buildreq on Thu Oct 18 2012
# optimized out: perl-HTTP-Cookies perl-HTTP-Date perl-HTTP-Message perl-URI
BuildRequires: perl-HTML-SimpleParse perl-TimeDate perl-devel perl-libwww

%description
Perl module CGI::SSI is meant to be used as an easy way to filter
shtml through CGI scripts in a loose imitation of Apache's
mod_include. If you're using  Apache, you may want to use either
mod_include or the Apache::SSI module instead of CGI::SSI.
Limitations in a CGI script's knowledge of how the server behaves
make some SSI directives impossible to imitate from a CGI script.

%prep
%setup  -n %real_name-%version
%patch0

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%exclude /.perl.req
%perl_vendor_privlib/CGI

%changelog
* Thu Oct 18 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.92-alt1
- Initial build for ALT Linux Sisyphus
