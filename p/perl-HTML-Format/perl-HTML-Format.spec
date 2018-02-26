BuildRequires: perl(Module/Build.pm)
%define dist HTML-Format
Name: perl-%dist
Version: 2.10
Release: alt1

Summary: Perl HTML formatters
Group: Development/Perl
License: GPL

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/N/NI/NIGELM/HTML-Format-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Apr 05 2011
BuildRequires: perl-File-Slurp perl-Font-AFM perl-HTML-Tree perl-devel

%description
This is a collection of perl modules that are able to format a HTML
syntax tree into various printable formats (plaintext, PostScript or RTF).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%dir %perl_vendor_privlib/HTML
%perl_vendor_privlib/HTML/Format*.pm

%changelog
* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1
- automated CPAN update

* Tue Apr 05 2011 Alexey Tourbin <at@altlinux.ru> 2.05-alt1
- 2.04 -> 2.05

* Sat Jun 25 2005 Alexey Tourbin <at@altlinux.ru> 2.04-alt1
- 2.03 -> 2.04
- manual pages not packaged (use perldoc)

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.03-alt2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Oct 17 2003 Alexey Tourbin <at@altlinux.ru> 2.03-alt2
- BuildRequires updated; various fixes

* Tue Mar 18 2003 Stanislav Ievlev <inger@altlinux.ru> 2.03-alt1
- Initial release for Sisyphus
