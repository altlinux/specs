%define _unpackaged_files_terminate_build 1
%define dist XML-XPath
Name: perl-%dist
Version: 1.40
Release: alt1

Summary: A set of modules for parsing and evaluating XPath statements
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/M/MA/MANWAR/XML-XPath-%{version}.tar.gz
# rewrite it if it is still needed
Patch: perl-XML-XPath-1.18-alt-fixes.patch

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 05 2011
BuildRequires: perl-XML-Parser perl-devel perl(Path/Tiny.pm)

%description
This module aims to comply exactly to the XPath specification at
http://www.w3.org/TR/xpath and yet allow extensions to be added
in the form of functions. Modules such as XSLT and XPointer may
need to do this as they support functionality beyond XPath.

%prep
%setup -q -n %dist-%version

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
* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.40-alt1
- automated CPAN update

* Sun Jun 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.37-alt1
- automated CPAN update

* Wed Apr 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.36-alt1
- automated CPAN update

* Thu Apr 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.35-alt1
- automated CPAN update

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.34-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.30-alt1
- automated CPAN update

* Mon Jan 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1
- automated CPAN update

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

