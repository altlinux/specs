%define dist Class-Accessor
Name: perl-%dist
Version: 0.51
Release: alt1

Summary: Automated accessor generation
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/K/KA/KASEI/%{dist}-%{version}.tar.gz

BuildArch: noarch

# always loaded when available
Requires: perl-Sub-Name

# Automatically added by buildreq on Tue Oct 04 2011
BuildRequires: perl-Sub-Name perl-devel

%description
This module automagically generates accessor/mutators for your class.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README examples
%perl_vendor_privlib/Class

%changelog
* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1
- automated CPAN update

* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 0.34-alt3
- rebuilt as plain src.rpm

* Tue Apr 20 2010 Alexey Tourbin <at@altlinux.ru> 0.34-alt2
- enabled dependency on Sub::Name

* Tue Oct 20 2009 Alexey Tourbin <at@altlinux.ru> 0.34-alt1
- 0.33 -> 0.34

* Mon May 18 2009 Alexey Tourbin <at@altlinux.ru> 0.33-alt1
- 0.31 -> 0.33

* Sun Aug 05 2007 Alexey Tourbin <at@altlinux.ru> 0.31-alt1
- 0.27 -> 0.31

* Sun Oct 22 2006 Alexey Tourbin <at@altlinux.ru> 0.27-alt1
- 0.25 -> 0.27
- imported sources into git and built with gear

* Thu Jul 06 2006 Alexey Tourbin <at@altlinux.ru> 0.25-alt1
- 0.22 -> 0.25

* Fri Sep 23 2005 Alexey Tourbin <at@altlinux.ru> 0.22-alt1
- 0.19 -> 0.22

* Wed Jul 06 2005 Alexey Tourbin <at@altlinux.ru> 0.19-alt1
- initial revision
