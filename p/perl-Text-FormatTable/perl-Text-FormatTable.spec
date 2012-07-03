%define dist Text-FormatTable
Name: perl-%dist
Version: 1.03
Release: alt1

Summary: Format text tables
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Apr 30 2010
BuildRequires: perl-devel

%description
Text::FormatTable renders simple tables as text. You pass to the constructor
a table format specification similar to LaTeX (e.g. "r|l|l") and you call
methods to fill the table data and insert rules. After the data is filled,
you render the table as text.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Text*

%changelog
* Fri Apr 30 2010 Alexey Tourbin <at@altlinux.ru> 1.03-alt1
- 1.01 -> 1.03

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.01-alt2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Sun Nov 28 2004 Andrey Brindeew <abr@altlinux.ru> 1.01-alt2
- Excluded example.pl from docs.

* Sun Nov 28 2004 Andrey Brindeew <abr@altlinux.ru> 1.01-alt1
- First build for ALT Linux.


