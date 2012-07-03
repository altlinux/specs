BuildRequires: perl(Module/Build.pm)
%define dist HTML-TableExtract
Name: perl-%dist
Version: 2.11
Release: alt1

Summary: %dist module for perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/M/MS/MSISK/HTML-TableExtract-%{version}.tar.gz
Patch: %name-2.10-alt1.patch

BuildArch: noarch

# Automatically added by buildreq on Tue Aug 12 2008
BuildRequires: perl-HTML-Tree perl-Test-Pod

%description
HTML::TableExtract is a module that simplifies the extraction
of information contained in tables within HTML documents.

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%dir %perl_vendor_privlib/HTML
%perl_vendor_privlib/HTML/TableExtract.pm

%changelog
* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 2.11-alt1
- automated CPAN update

* Tue Aug 12 2008 Alexey Tourbin <at@altlinux.ru> 2.10-alt1
- 2.09 -> 2.10
- HTML/TableExtract.pm (new): fixed $Dpat param match (cpan #38410)

* Mon Jun 26 2006 Alexey Tourbin <at@altlinux.ru> 2.09-alt1
- 2.02 -> 2.09

* Thu Jun 30 2005 Alexey Tourbin <at@altlinux.ru> 2.02-alt1
- 1.08 -> 2.02
- specfile cleanup
- manual pages not packaged (use perldoc)

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.08-alt3.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Nov 01 2002 Stanislav Ievlev <inger@altlinux.ru> 1.08-alt3
- rebuild with new perl

* Sat May 18 2002 Stanislav Ievlev <inger@altlinux.ru> 1.08-alt2
- 1.08

* Mon Jun 25 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.06-alt2
- Rebuilt with perl-5.6.1
- Some spec cleanup

* Tue May 29 2001 AEN <aen@logic.ru> 1.06-alt1
- first build for Sisyphus
