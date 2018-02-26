%define dist Tk-TableMatrix
Name: perl-%dist
Version: 1.23
Release: alt2

Summary: The Tk::TableMatrix Widget
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-Tk-devel

%description
Tk::TableMatrix is a table/matrix widget extension to perl/tk
for displaying data in a table (or spreadsheet) format.

%package devel
Summary: The Tk::TableMatrix Widget
Group: Development/Perl
Requires: %name = %version-%release

%description devel
Tk::TableMatrix is a table/matrix widget extension to perl/tk
for displaying data in a table (or spreadsheet) format.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%dir %perl_vendor_archlib/Tk
%perl_vendor_archlib/Tk/TableMatrix*
%perl_vendor_autolib/Tk

%files devel
%dir %perl_vendor_archlib/Tk
%perl_vendor_archlib/Tk/pTk

%changelog
* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 1.23-alt2
- rebuilt for perl-5.14

* Wed Sep 21 2011 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1
- automated CPAN update

* Mon Nov 08 2010 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt2.1
- rebuilt with perl 5.12

* Sat Sep 09 2006 Vyacheslav Dikonov <slava@altlinux.ru> 1.1-alt2
- Buildreq fixes

* Sat Mar 26 2005 Vyacheslav Dikonov <slava@altlinux.ru> 1.1-alt1
- ALTLinux build
