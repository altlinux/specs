%define module HTML-Template-JIT

Name: perl-%module
Version: 0.05
Release: alt2.1

Summary: A just-in-time compiler for HTML::Template
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/HTML/%module-%version.tar.gz
BuildArch: noarch
Packager: Stanislav Yadykin <tosick@altlinux.ru>
Requires: perl-HTML-Template >= 2.8

# Automatically added by buildreq on Thu Dec 11 2008
BuildRequires: perl-HTML-Template perl-Inline perl-Parse-RecDescent

%description
This module provides a just-in-time compiler for HTML::Template.  See
the module docs for more information.

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes ANNOUNCE
%perl_vendor_privlib/HTML/Template/*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Dec 11 2008 Stanislav Yadykin <tosick@altlinux.ru> 0.05-alt2
- Packager: tag has been added

* Fri Sep 15 2006 Stanislav Yadykin <tosick@altlinux.ru> 0.05-alt1
- 0.05

* Wed Jan 26 2005 Stanislav Yadykin <tosick@altlinux.ru> 0.04-alt1
- build for Sisyphus

