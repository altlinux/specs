%define dist Params-Validate
Name: perl-%dist
Version: 1.00
Release: alt1

Summary: Validate method/function parameters
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-Attribute-Handlers perl-Module-Build

%description
The Params::Validate module allows you to validate method or function
call parameters to an arbitrary level of specificity.  At the simplest
level, it is capable of validating the required parameters were given
and that no unspecified additional parameters were passed in.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build --xs

%install
%perl_vendor_install

# workaround ValidatePP.pm and ValidateXS.pm syntax check failure
%define __spec_autodep_custom_pre export PERL5OPT='-I%buildroot%perl_vendor_archlib -MParams::Validate'

%files
%doc Changes README
%perl_vendor_archlib/Params
%perl_vendor_autolib/Params
%perl_vendor_archlib/Attribute

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.00-alt1
- 0.95 -> 1.00
- built for perl-5.14
- rebuilt as plain src.rpm

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 0.95-alt1
- 0.94 -> 0.95
- built for perl-5.12

* Tue Feb 16 2010 Alexey Tourbin <at@altlinux.ru> 0.94-alt1
- 0.92 -> 0.94

* Sun Sep 27 2009 Alexey Tourbin <at@altlinux.ru> 0.92-alt1
- 0.91 -> 0.92

* Tue May 06 2008 Alexey Tourbin <at@altlinux.ru> 0.91-alt1
- 0.89 -> 0.91

* Fri Feb 22 2008 Alexey Tourbin <at@altlinux.ru> 0.89-alt1
- 0.88 -> 0.89

* Sun Aug 05 2007 Alexey Tourbin <at@altlinux.ru> 0.88-alt1
- 0.87 -> 0.88

* Tue Feb 27 2007 Alexey Tourbin <at@altlinux.ru> 0.87-alt1
- 0.86 -> 0.87

* Thu Oct 26 2006 Alexey Tourbin <at@altlinux.ru> 0.86-alt2
- imported sources into git and built with gear
- adjusted ValidatePP.pm and ValidateXS.pm to pass syntax check

* Tue Sep 05 2006 Alexey Tourbin <at@altlinux.ru> 0.86-alt1
- 0.85 -> 0.86

* Thu Jul 06 2006 Alexey Tourbin <at@altlinux.ru> 0.85-alt1
- 0.81 -> 0.85

* Mon Apr 17 2006 Alexey Tourbin <at@altlinux.ru> 0.81-alt1
- 0.78 -> 0.81

* Sat Sep 24 2005 Alexey Tourbin <at@altlinux.ru> 0.78-alt1
- 0.76 -> 0.78

* Thu Dec 16 2004 Alexey Tourbin <at@altlinux.ru> 0.76-alt1
- 0.74 -> 0.76
- manual pages not packaged (use perldoc)

* Thu Jul 01 2004 Alexey Tourbin <at@altlinux.ru> 0.74-alt1
- initial revision
