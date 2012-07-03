%define dist XML-XPath
Name: perl-%dist
Version: 1.13
Release: alt5

Summary: A set of modules for parsing and evaluating XPath statements
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch: perl-XML-XPath-1.13-alt-fixes.patch

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 05 2011
BuildRequires: perl-XML-Parser perl-devel

%description
This module aims to comply exactly to the XPath specification at
http://www.w3.org/TR/xpath and yet allow extensions to be added
in the form of functions. Modules such as XSLT and XPointer may
need to do this as they support functionality beyond XPath.

%prep
%setup -q -n %dist-%version
%patch0 -p1

# examples should not be installed into /usr/bin
sed -i- '/EXE_FILES/d' Makefile.PL

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README examples
%perl_vendor_privlib/XML

%changelog
* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 1.13-alt5
- specfile cleanup

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.13-alt4.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.13-alt4.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Nov 25 2003 Andrey Brindeew <abr@altlinux.ru> 1.13-alt4
- Summary tag was fixed.

* Tue Sep 30 2003 Andrey Brindeew <abr@altlinux.ru> 1.13-alt3
- Rebuild with new rpm scripts. Patched again.

* Thu Sep 04 2003 Andrey Brindeew <abr@altlinux.ru> 1.13-alt2
- Patched. Now 'perl -c' will be happy.
- URL was fixed.

* Wed Jul 30 2003 Andrey Brindeew <abr@altlinux.ru> 1.13-alt1
- First build for ALTLinux.

