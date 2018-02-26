Name: perl-HTML-Table
Version: 2.08a
Release: alt1.1
Summary: Create HTML tables using simple interface
License: GPL+ or Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/HTML-Table/
Packager: Boris Savelev <boris@altlinux.org>

Source: http://www.cpan.org/modules/by-module/HTML/HTML-Table-%version.tar.gz
BuildArch: noarch

# Automatically added by buildreq on Mon Dec 01 2008
BuildRequires: perl-devel

%description
HTML::Table is used to generate HTML tables for CGI scripts.  By using the
methods provided fairly complex tables can be created, manipulated, then
 printed from Perl scripts.  The module also greatly simplifies creating
tables within tables from Perl.  It is possible to create an entire table
using the methods provided and never use an HTML tag.

HTML::Table also allows for creating dynamically sized tables via its addRow
and addCol methods.  These methods automatically resize the table if passed
more cell values than will fit in the current table grid.

Methods are provided for nearly all valid table, row, and cell tags specified
for HTML 3.0.

%prep
%setup -q -n HTML-Table-%version
for f in Changes lib/HTML/Table.pm
do
   iconv -f ISO-8859-1 -t UTF-8 -o ${f}.UTF-8 $f
   mv ${f}.UTF-8 $f
done

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install PERL_INSTALL_ROOT=%buildroot

find %buildroot -type f -name .packlist -exec rm -f {} ';'
find %buildroot -depth -type d -exec rmdir {} 2>/dev/null ';'

%files
%doc Changes README
%perl_vendor_privlib/*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 2.08a-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Dec 01 2008 Boris Savelev <boris@altlinux.org> 2.08a-alt1
- initial build

