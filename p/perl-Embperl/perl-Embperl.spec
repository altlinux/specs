%define dist Embperl
Name: perl-%dist
Version: 2.4.0
Release: alt2

Summary: Building dynamic Websites with Perl
License: GPL
Group: System/Libraries

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Tue Oct 18 2011 (-bi)
BuildRequires: apache2-httpd-prefork apache2-mod_perl-devel libxslt-devel perl-CGI perl-Date-Calc perl-Filter-Simple perl-libwww

%description
Embperl gives you the power to embed Perl code in your HTML documents
and the ability to build your Web site out of small reusable objects in
an object-oriented style. You can also take advantage of all the
usual Perl modules, (including DBI for database access) use their
functionality and easily include their output in your web pages.
Additionaly Embperl support including XML, XSLT tranformations and
a lot of other sources formats.

%prep
%setup -q -n Embperl-%version

sed -i- 's|apr_includedir}|apr_includedir} -I/usr/include/apu-1|g' Makefile.PL

# XXX fails under LD_BIND_NOW=1
%def_without test

%build
%perl_vendor_build LIBS='-lxslt -lxml2 -lm -lapr-1 -laprutil-1'

%check
make test TESTARGS='-o'

%install
%perl_vendor_install 

# XXX brp-cleanup fails on this file
rm %buildroot%perl_vendor_autolib/Embperl/Embperl.bs

# used only with apache
%add_findreq_skiplist */Embperl/Session.pm

# disable conditional dependencies on apache
%filter_from_requires /^perl.Apache/d
%filter_from_requires /^perl.APR/d

%files
%doc README
%_bindir/embp*
%perl_vendor_archlib/Embperl*
%perl_vendor_autolib/Embperl

%changelog
* Tue Oct 18 2011 Alexey Tourbin <at@altlinux.ru> 2.4.0-alt2
- rebuilt for perl-5.14

* Tue Feb 01 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.4.0-alt1
- First build for ALTLinux.
