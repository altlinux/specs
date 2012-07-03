%define version    0.08
%define release    alt1

Name: perl-PodToHTML
Version: %version
Release: alt1.1

Summary: convert POD documentation to HTML 
Summary(ru_RU.UTF-8): преобразует документацию POD в HTML

License: %perl_license
Group: Development/Perl

%define real_name PodToHTML
URL: http://search.cpan.org/~ni-s/PodToHTML/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source: http://search.cpan.org/CPAN/authors/id/N/NI/NI-S/%real_name-%version.tar.gz

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Dec 14 2008
BuildRequires: perl-Font-AFM perl-HTML-Tree perl-Test-Pod perl-Test-Pod-Coverage
BuildRequires: perl-podlators

%description
PodToHTML is a several Perl modules and command line utility
podtohtml that generates  HTML from  one or (more typically) 
several files containing POD documentation. 


%description -l ru_RU.UTF-8
PodToHTML - несколько модулей Perl и утилита командной строки
podtohtml  для  создания документов HTML  из одного или  (что 
более типично)  нескольких  файлов,  содержащих  документацию
в формате POD.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_privlib/Pod/HTML_Elements*
%perl_vendor_privlib/Pod/Links*

%_bindir/podtohtml
#%%_bindir/findpods
%_mandir/man1/podtohtml*

%exclude /.perl.req

%changelog
* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.08-alt1.1
- rebuilt with perl 5.12

* Sun Dec 14 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.08-alt1
- New version 0.08

* Thu Feb 28 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.07-alt1
- New version 0.07

* Thu Aug 09 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.06-alt2
- Fix typo in package description

* Tue Mar 27 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.06-alt1
- New version 0.06
  - Updated dist to get rid of internal Pod::Find that conflicts
    with the one from Pod::Parser

* Thu Aug 31 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.05-alt2
- Small spec file fixes

* Sun Apr 23 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.05-alt1
- Initial build for ALT Linux

* Tue May 24 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.05-alt0.1
- Build for new perl-5.8.7

* Sat Mar 05 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.05-alt0
- Initial build for ALT Linux
