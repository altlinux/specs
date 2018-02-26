%define module HTML-Template-Expr

Name: perl-%module
Version: 0.07
Release: alt2.1

Summary: Perl module to use expressions in HTML Template
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/HTML/%module-%version.tar.gz
Patch: perl-%module-alt-regexp.patch
BuildArch: noarch
Packager: Stanislav Yadykin <tosick@altlinux.ru>

# Automatically added by buildreq on Thu Dec 11 2008
BuildRequires: perl-HTML-Template perl-Parse-RecDescent perl-devel

%description
This module provides an extension to HTML::Template which allows
expressions in the template syntax.  This is purely an addition - all
the normal HTML::Template options, syntax and behaviors will still
work.

Expression support includes comparisons, math operations, string
operations and a mechanism to allow you add your own functions at
runtime.

%prep
%setup -q -n %module-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes ANNOUNCE
%perl_vendor_privlib/HTML/Template/*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.07-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Dec 11 2008 Stanislav Yadykin <tosick@altlinux.org> 0.07-alt2
- Packager: tag has been added

* Fri Sep 15 2006 Stanislav Yadykin <tosick@altlinux.ru> 0.07-alt1
- 0.07

* Wed Mar 23 2005 Stanislav Yadykin <tosick@altlinux.ru> 0.04-alt2
- added regexp support
- removed man pages

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.ru> 0.04-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Nov 05 2004 Stanislav Yadykin <tosick@altlinux.ru> 0.04-alt1
Build for Sisyphus

