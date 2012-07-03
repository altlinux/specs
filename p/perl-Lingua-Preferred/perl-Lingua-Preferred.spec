%define	module_name	Lingua-Preferred

Name: perl-%module_name
Version: 0.2.4
Release: alt1.qa1.1

Summary: Perl extension to choose a language
Summary(ru_RU.UTF8): Расширение Perl для выбора языка веб-страниц
License: GPL/Artistic
Group: Development/Perl
URL: http://backpan.cpan.org/authors/id/E/ED/EDAVIS
Source: ftp://backpan.cpan.org/authors/id/E/ED/EDAVIS/%module_name-%version.tar.gz
BuildArch: noarch
AutoReqProv: yes, perl
BuildRequires: perl-devel

%description
Often human-readable information is available in more than one language. Which
should you use? This module provides a way for the user to specify possible
languages in order of preference, and then to pick the best language of those
available. Different 'dialects' given by the 'territory' part of the language
specifier (such as en, en_GB, and en_US) are also supported.

%description -l ru_RU.UTF8
Часто информация доступна более чем на одном языке. Какой из них выбрать? 
Этот модуль предоставляет возможность пользователю создать список предпочитаемых 
языков и затем выбирать наиболее подходящий. Также поддерживаются различные 
"диалекты", указываемые модификатором "территории" (например en_GB, и en_US).

%prep
%setup -q -n %module_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendorlib/Lingua/Preferred.pm
%perl_vendorlib/auto/Lingua/Preferred

%changelog
* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 0.2.4-alt1.qa1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Feb 06 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.2.4-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * altlinux-policy-perl-noarch-pkg-has-dirs-in-arch for perl-Lingua-Preferred
  * postclean-05-filetriggers for spec file

* Sat Mar 26 2005 Vyacheslav Dikonov <slava@altlinux.ru> 0.2.4-alt1
- ALTLinux build
