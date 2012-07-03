%define module Parse-PlainConfig
%define intmodule Parse-PlainConfig
%define m_name Parse::PlainConfig

Name: perl-%module
Version: 2.06
Release: alt1.1

Summary: Plain Config parser
License: GPLv2+
Group: Development/Perl
BuildArch: noarch
Url: %CPAN %module
Packager: Sergei Epiphanov <serpiph@altlinux.ru>

Source: http://search.cpan.org/CPAN/authors/id/C/CO/CORLISS/%intmodule/%intmodule-%version.tar.gz

# Automatically added by buildreq on Mon Oct 06 2003
BuildRequires: perl-devel perl(Paranoid.pm) perl(Text/ParseWords.pm) perl(Text/Tabs.pm)

%description
Parse::PlainConfig provides OO objects which can parse and generate human-readable configuration files.

%prep
%setup -q -n %intmodule-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_privlib/Parse*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 2.06-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Dec 18 2008 Sergei Epiphanov <serpiph@altlinux.ru> 2.06-alt1
- New version

* Thu Dec 21 2006 Sergei Epiphanov <serpiph@altlinux.ru> 1.7a-alt1
- Built for Sisyphus
