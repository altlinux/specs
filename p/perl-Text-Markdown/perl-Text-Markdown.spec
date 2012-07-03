## SPEC file for Perl module Text::Markdown
## Used in ikiwiki

Name: perl-Text-Markdown
Version: 1.0.31
Release: alt1

Summary: a text-to-HTML filter

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/~bobtfish/Text-Markdown/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Text-Markdown
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Sun Nov 28 2010
BuildRequires: perl-HTML-Tidy perl-List-MoreUtils perl-Module-Install perl-Test-Differences perl-Test-Exception perl-Test-Pod perl-Test-Pod-Coverage perl-Text-Balanced

%description
Perl module Text::Markdown is a text-to-HTML filter; it translates
an easy-to-read / easy-to-write structured text format into HTML.
Markdown's text format is most similar to that of plain text email,
and supports features such as headers, *emphasis*, code blocks,
blockquotes, and links.

%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Readme.text Changes
%exclude /.perl.req
%perl_vendor_privlib/Text/Markdown*
%_bindir/Markdown.pl

%changelog
* Sun Nov 28 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.31-alt1
- New version

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.26-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Oct 17 2009 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.26-alt1
- New version 1.0.26

* Sun Dec 14 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.24-alt1
- New version 1.0.24

* Sat Feb 23 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.5-alt1
- Initial build for ALT Linux Sisyphus

* Mon Feb 18 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.5-alt0.1
- Initial build
