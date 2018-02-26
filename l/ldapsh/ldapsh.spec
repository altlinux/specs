# SPEC file for ldapsh
#

Name: ldapsh
Version: 2.00
Release: alt2

Summary: a console tool for searching/managing data in LDAP
Summary(ru_RU.UTF-8): консольная утилита для поиска/управления данными в LDAP

License: %gpl2plus
Group: Databases
Packager: Nikolay Fetisov <naf@altlinux.ru>

URL: http://reductivelabs.com/projects/ldapsh
# http://search.cpan.org/~loosifer/ldapsh/

Source: http://search.cpan.org/CPAN/authors/id/L/LO/LOOSIFER/%name-%version.tar.gz
Source1: %name-2.00-alt-test_config.conf
Patch0: %name-2.00-alt-docs_fix.patch
Patch1: %name-2.00-alt-use_vars.patch
Patch2: %name-2.00-alt-help_msg_fix.patch
Patch3: %name-2.00-alt-help_msg_align.patch
Patch4: %name-2.00-alt-config_msg.patch
Patch5: %name-2.00-alt-fix_undef_print.patch
Patch6: %name-2.00-alt-fix_parse.patch

BuildArch: noarch

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Mon Nov 29 2010
BuildRequires: perl-Date-Manip perl-ParseLex perl-Term-ReadKey perl-devel perl-ldap perl-podlators

BuildRequires: perl-podlators
BuildRequires: perl-Parse-RecDescent perl-Term-ReadLine-Gnu

%description
ldapsh is an interactive LDAP shell, written entirely in Perl and
using Net::LDAP. It's extensible in that it is relatively easy to
add  new commands to it.  It is  largely modeled  after the  Unix
shell, but does not at this point allow multiple tokens through a
mechanism like pipes.

%description -l ru_RU.UTF-8
ldapsh - интерактивная оболочка для LDAP, написанная целиком на Perl
и использующая модуль Net::LDAP.  ldapsh позволяет  перемещаться  по
дереву LDAP,  просматривать, изменять  и создавать новые записи. Она 
расширяема, в неё сравнительно легко добавить новые команды.  Работа
с ldapsh похожа на работу с обычным командным  интерпретатором UNIX, 
хотя на данный момент в ней нет возможности объединения команд через 
механизмы перенаправления ввода/вывода.


%prep
%setup -q -n %name-%version
%patch0
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6

subst 's@##DOCDIR##@%_docdir/%name-%version@' lib/Net/LDAP/Config.pm

# In 2.00 tarball sample ldapsh_config named as ldapsh_profile and 
# does not matched test suit. Fix this.
subst 's@examples/ldapsh_profile@examples/ldapsh_config@' t/00source-tests.t
cp -- %SOURCE1 examples/ldapsh_config
rm -f -- examples/ldapsh_profile

# Create link to GPL v2. license file
mv -f -- LICENSE LICENSE.GPL.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/LICENSE) LICENSE

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir


%install
%perl_vendor_install

%files
%doc README TODO CHANGES COMMANDS
%doc --no-dereference LICENSE
%doc examples*

%_bindir/%name
%_man1dir/*
%perl_vendor_privlib/Net/LDAP/*
%exclude /.perl.req

%changelog
* Sun Nov 28 2010 Nikolay A. Fetisov <naf@altlinux.ru> 2.00-alt2
- Fix build with Perl 5.12

* Wed Jun 28 2006 Nikolay A. Fetisov <naf@altlinux.ru> 2.00-alt1
- First build for ALT Linux Sisyphus

* Thu Jun 15 2006 Nikolay A. Fetisov <naf@altlinux.ru> 2.00-alt0.7
- Fix parse error with empty input line
- Adding patches for sample config file message and printing undefined dn() value
- Make help message more condensed
- Fix russian description.
- Fix mistake in command list help message
- Fix AutoReqProv clause.
- Fix scope problems with external commands

* Sun May 07 2006 Nikolay A. Fetisov <naf@altlinux.ru> 2.00-alt0
- Updating for current ALT Linux Sisyphus

* Tue Oct 5 2004 Nikolay A. Fetisov <naf@naf.net.ru> 2.0b1-naf1
- First build

