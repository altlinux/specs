# Spec file for Perl module ParseLex

Name: perl-ParseLex
Version: 2.20
Release: alt1

Summary: generator of lexical analyzers
Summary(ru_RU.UTF-8): генератор лексических анализаторов

%define real_name ParseLex

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/~pscust/%real_name/


Packager: Nikolay Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Mon Nov 29 2010
BuildRequires: perl-Parse-Template

%description
The Parse::Lex.pm module for perl5 is an object-oriented
generator of lexical analyzers.

%description -l ru_RU.UTF-8
Модуль Perl Parse::Lex - объектно-ориентированный генератор
лексических анализаторов.


%prep
%setup -q -n %real_name-%version

# Origin tarball contains old version of Parse::Template, which now packaged separatly.
rm -f lib/Parse/Template.pm

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%doc examples/*
%perl_vendor_privlib/Parse/*

%changelog
* Mon Nov 29 2010 Nikolay A. Fetisov <naf@altlinux.ru> 2.20-alt1
- New version

* Wed Jun 28 2006 Nikolay A. Fetisov <naf@altlinux.ru> 2.15-alt2
- Removes from package old version of Parse::Template, 
  which now packaged separately

* Sun Apr 23 2006 Nikolay A. Fetisov <naf@altlinux.ru> 2.15-alt1
- Initial build for ALT Linux

* Wed Mar 16 2005 Nikolay A. Fetisov <naf@altlinux.ru> 2.15-alt0
- Spec cleanup
- Preparing for ALT Linux

* Sat Oct 2 2004 Nikolay A. Fetisov <naf@naf.net.ru> 2.15-naf1
- First build

