%define dist YAML
Name: perl-%dist
Version: 0.77
Release: alt1

Summary: YAML Ain't Markup Language
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch: YAML-0.77-alt-fixes.patch

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 14 2011
BuildRequires: perl-Filter perl-Pod-Escapes perl-URI perl-devel

%description
The YAML.pm module implements a YAML Loader and Dumper based on the
YAML 1.0 specification.  YAML is a generic data serialization language
that is optimized for human readability.  It can be used to express the
data structures of most modern programming languages (including Perl).

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

# avoid dependency on perl-devel
%add_findreq_skiplist */Test/YAML*

%files
%doc Changes README
%perl_vendor_privlib/Test
%perl_vendor_privlib/YAML*

%changelog
* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 0.77-alt1
- 0.71 -> 0.77

* Mon Mar 29 2010 Alexey Tourbin <at@altlinux.ru> 0.71-alt1
- 0.66 -> 0.71

* Sat May 17 2008 Alexey Tourbin <at@altlinux.ru> 0.66-alt1
- 0.65 -> 0.66

* Sat Aug 18 2007 Alexey Tourbin <at@altlinux.ru> 0.65-alt1
- 0.62 -> 0.65

* Wed Dec 20 2006 Alexey Tourbin <at@altlinux.ru> 0.62-alt1
- 0.60 -> 0.62
- fixed dependency on B::Deparse (cpan #24018)

* Sun Jul 02 2006 Alexey Tourbin <at@altlinux.ru> 0.60-alt1
- 0.58 -> 0.60
- fixed t/bugs-rt.t so that it works with recent CGI.pm

* Thu Apr 20 2006 Alexey Tourbin <at@altlinux.ru> 0.58-alt1
- 0.39 -> 0.58

* Thu Jun 23 2005 Alexey Tourbin <at@altlinux.ru> 0.39-alt1
- 0.36 -> 0.39

* Fri Mar 11 2005 Alexey Tourbin <at@altlinux.ru> 0.36-alt1
- 0.35 -> 0.36
- manual pages not packaged (use perldoc)

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.35-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Apr 27 2004 Alexey Tourbin <at@altlinux.ru> 0.35-alt1
- initial revision
