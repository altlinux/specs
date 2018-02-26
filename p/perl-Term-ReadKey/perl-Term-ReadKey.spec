%define dist TermReadKey
Name: perl-Term-ReadKey
Version: 2.30
Release: alt2.2

Summary: A perl module for simple terminal control
License: distributable
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Sat Oct 15 2011
BuildRequires: perl-devel

%description
Term::ReadKey is a compiled perl module dedicated to providing simple
control over terminal driver modes (cbreak, raw, cooked, etc.,)
support for non-blocking reads and some generalized handy functions
for working with terminals.

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%if "%([ -c /dev/tty ] || echo no)" == "no"
%def_without test
%endif

%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	README
%dir	%perl_vendor_archlib/Term
	%perl_vendor_archlib/Term/ReadKey.pm
%dir	%perl_vendor_autolib/Term
%dir	%perl_vendor_autolib/Term/ReadKey
	%perl_vendor_autolib/Term/ReadKey/ReadKey.so

%changelog
* Sat Oct 15 2011 Alexey Tourbin <at@altlinux.ru> 2.30-alt2.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 2.30-alt2.1
- rebuilt with perl 5.12

* Tue Apr 10 2007 Alexey Tourbin <at@altlinux.ru> 2.30-alt2
- fixed SetTerminalSize() return value (rt.cpan.org #26235)
- removed AutoLoader, replaced DynaLoader with XSLoader
- made internal C functions static

* Fri Jan 14 2005 Alexey Tourbin <at@altlinux.ru> 2.30-alt1
- 2.21 -> 2.30
- manual pages not packaged (use perldoc)

* Fri Jul 02 2004 Alexey Tourbin <at@altlinux.ru> 2.21-alt3
- specfile cleanup

* Thu Sep 11 2003 Alexey Tourbin <at@altlinux.ru> 2.21-alt2
- skip test when /dev/tty does not exist

* Thu Oct 31 2002 Stanislav Ievlev <inger@altlinux.ru> 2.21-alt1
- Initial Build
