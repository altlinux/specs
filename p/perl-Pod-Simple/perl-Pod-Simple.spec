%define dist Pod-Simple
Name: perl-%dist
Version: 3.19
Release: alt2

Summary: Framework for parsing Pod
Group: Development/Perl
License: GPL or Artistic

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 15 2011
BuildRequires: perl-Encode-JP perl-Encode-TW perl-HTML-Parser perl-Pod-Escapes perl-devel

%description
Pod::Simple is a Perl library for parsing text in the Pod ("plain old
documentation") markup language that is typically used for writing
documentation for Perl and for Perl modules. The Pod format is explained
in the perlpod man page; the most common formatter is called "perldoc".

%prep
%setup -q -n %dist-%version

%ifdef __buildreqs
# avoid scanning the whole @INC
rm t/search50.t
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	ChangeLog README
%dir	%perl_vendor_privlib/Pod
%dir	%perl_vendor_privlib/Pod/Simple
	%perl_vendor_privlib/Pod/Simple.pm
%doc	%perl_vendor_privlib/Pod/Simple.pod
	%perl_vendor_privlib/Pod/Simple/*.pm
%doc	%perl_vendor_privlib/Pod/Simple/*.pod

%changelog
* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 3.19-alt2
- rebuilt as plain src.rpm

* Wed Sep 14 2011 Alexey Tourbin <at@altlinux.ru> 3.19-alt1
- 3.18 -> 3.19

* Sat Aug 06 2011 Alexey Tourbin <at@altlinux.ru> 3.18-alt1
- 3.16 -> 3.18

* Wed Mar 23 2011 Alexey Tourbin <at@altlinux.ru> 3.16-alt1
- 3.15 -> 3.16

* Sat Dec 25 2010 Alexey Tourbin <at@altlinux.ru> 3.15-alt1
- 3.14 -> 3.15

* Wed May 26 2010 Alexey Tourbin <at@altlinux.ru> 3.14-alt1
- 3.13 -> 3.14

* Fri Feb 19 2010 Alexey Tourbin <at@altlinux.ru> 3.13-alt1
- 3.07 -> 3.13

* Fri Sep 12 2008 Alexey Tourbin <at@altlinux.ru> 3.07-alt1
- 3.05 -> 3.07

* Wed Apr 18 2007 Alexey Tourbin <at@altlinux.ru> 3.05-alt1
- 3.04 -> 3.05

* Sun Apr 16 2006 Alexey Tourbin <at@altlinux.ru> 3.04-alt1
- 3.02 -> 3.04

* Tue Dec 28 2004 Alexey Tourbin <at@altlinux.ru> 3.02-alt1
- 2.06 -> 3.02
- manual pages not packaged (use perldoc)

* Sat May 08 2004 Alexey Tourbin <at@altlinux.ru> 2.06-alt1
- 2.05 -> 2.06

* Fri Nov 21 2003 Alexey Tourbin <at@altlinux.ru> 2.05-alt1
- 2.05

* Fri Oct 31 2003 Alexey Tourbin <at@altlinux.ru> 2.04-alt1
- 2.04

* Tue Oct 07 2003 Alexey Tourbin <at@altlinux.ru> 2.03-alt1
- initial revision
