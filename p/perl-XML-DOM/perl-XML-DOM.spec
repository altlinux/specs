%define dist XML-DOM
Name: perl-%dist
Version: 1.44
Release: alt3

Summary: A module for building DOM Level 1 compliant document structures
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 14 2011
BuildRequires: perl-XML-RegExp perl-devel perl-libxml-perl

%description
This is a Perl extension to XML::Parser. It adds a new 'Style' to XML::Parser,
called 'Dom', that allows XML::Parser to build an Object Oriented datastructure
with a DOM Level 1 compliant interface.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/XML

%changelog
* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 1.44-alt3
- rebuilt as plain src.rpm

* Wed Sep 30 2009 Alexey Tourbin <at@altlinux.ru> 1.44-alt2
- re-enabled japanese tests

* Sat Aug 27 2005 Andrey Brindeew <abr@altlinux.org> 1.44-alt1
- 1.44

* Sun May 16 2004 Andrey Brindeew <abr@altlinux.ru> 1.43-alt5
- Removed tests (due incompatibility with perl 5.8.4):
  + t/dom_jp_attr.t
  + t/dom_jp_cdata.t
  + t/dom_jp_minus.t
  + t/dom_jp_modify.t

* Tue Nov 25 2003 Andrey Brindeew <abr@altlinux.ru> 1.43-alt4
- Summary tag was fixed.

* Fri Sep 05 2003 Andrey Brindeew <abr@altlinux.ru> 1.43-alt3
- Sources patched (this makes `perl -c' happy).
- URL was fixed.

* Thu Aug 07 2003 Andrey Brindeew <abr@altlinux.ru> 1.43-alt2
- Rebuild.

* Tue Jul 29 2003 Andrey Brindeew <abr@altlinux.ru> 1.43-alt1
- 1.43
- BuildArch was changed to `noarch'.

* Fri Jul 18 2003 Andrey Brindeew <abr@altlinux.ru> 1.42-alt3
- Requires fixed.

* Fri Jul 18 2003 Andrey Brindeew <abr@altlinux.ru> 1.42-alt2
- Added patch (removed stupid selftest).

* Fri Jul 18 2003 Andrey Brindeew <abr@altlinux.ru> 1.42-alt1
- First build for ALTLinux.
