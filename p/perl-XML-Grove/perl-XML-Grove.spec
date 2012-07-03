%define dist XML-Grove
Name: perl-%dist
Version: 0.46
Release: alt4

Summary: Simple access to infoset of parsed XML, HTML, or SGML instances
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-0.46alpha.tar.gz
Patch: perl-XML-Grove-test.patch

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 15 2011
BuildRequires: perl-devel perl-libxml-perl

%description
XML::Grove is a tree-based object model for accessing the information
set of parsed or stored XML, HTML, or SGML instances.

%prep
%setup -q -n %dist-0.46alpha
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README DOM examples
%perl_vendor_privlib/XML

%changelog
* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 0.46-alt4
- rebuilt as plain src.rpm

* Wed Sep 30 2009 Alexey Tourbin <at@altlinux.ru> 0.46-alt3
- applied perl-XML-Grove-test.patch from Fedora, enabled tests

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.46-alt2.alpha.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Sep 05 2003 Andrey Brindeew <abr@altlinux.ru> 0.46-alt2.alpha
- BuildRequires updated.
- URL fixed.

* Wed Jul 30 2003 Andrey Brindeew <abr@altlinux.ru> 0.46-alt1.alpha
- BuildArch was changed to `noarch'.
- Minor specfile fixes.

* Fri Jul 18 2003 Andrey Brindeew <abr@altlinux.ru> 0.46-alt0.2alpha
- BuildRequires fixed using buildreq.
- Added `build_without_tests' switch into specfile.

* Fri Jul 18 2003 Andrey Brindeew <abr@altlinux.ru> 0.46-alt0.1alpha
- First build for ALTLinux.
