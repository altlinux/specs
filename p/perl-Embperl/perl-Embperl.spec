%define _unpackaged_files_terminate_build 1
%define dist Embperl
Name: perl-%dist
Version: 2.5.0
Release: alt2.1

Summary: Building dynamic Websites with Perl
License: GPL
Group: System/Libraries

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/G/GR/GRICHTER/Embperl-%{version}.tar.gz

# Automatically added by buildreq on Tue Oct 18 2011 (-bi)
BuildRequires: apache2-httpd-prefork apache2-mod_perl-devel libxslt-devel perl-CGI perl-Date-Calc perl-Filter-Simple perl-libwww perl(Data/Clone.pm)

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
export NPROCS=1
%perl_vendor_build LIBS='-lxslt -lxml2 -lm -lapr-1 -laprutil-1'

%check
make test TESTARGS='-o'

%install
%perl_vendor_install 

# TODO: killme: this file is not created with perl >= 5.20.1
# XXX brp-cleanup fails on this file
rm -f %buildroot%perl_vendor_autolib/Embperl/Embperl.bs

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
* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt2.1
- rebuild with new perl 5.20.1

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt2
- preparation for perl 5.20.1

* Tue Apr 22 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1
- automated CPAN update

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 2.4.0-alt4
- built for perl 5.18

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 2.4.0-alt3
- rebuilt for perl-5.16

* Tue Oct 18 2011 Alexey Tourbin <at@altlinux.ru> 2.4.0-alt2
- rebuilt for perl-5.14

* Tue Feb 01 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.4.0-alt1
- First build for ALTLinux.
