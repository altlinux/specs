%define _unpackaged_files_terminate_build 1
%define dist ExtUtils-CBuilder
Name: perl-%dist
Version: 0.280230
Release: alt1

Summary: Compile and link C code for Perl modules
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/A/AM/AMBS/%{dist}-%{version}.tar.gz

Patch0: ExtUtils-CBuilder-0.280202-alt-unix.patch
Patch1: ExtUtils-CBuilder-0.280202-alt-link.patch

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 15 2011
BuildRequires: gcc-c++ perl-IPC-Cmd perl(Perl/OSType.pm)

%description
This module can build the C portions of Perl modules by invoking the
appropriate compilers and linkers in a cross-platform manner.  It was
motivated by the CModule::Build project, but may be useful for other
purposes as well.  However, it is not intended as a general
cross-platform interface to all your C building needs.  That would have
been a much more ambitious goal!

%prep
%setup -q -n %{dist}-%{version}
%patch0 -p1
%patch1 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	Changes README README.mkdn README.patching README.release
%dir	%perl_vendor_privlib/ExtUtils
	%perl_vendor_privlib/ExtUtils/CBuilder.pm
%dir	%perl_vendor_privlib/ExtUtils/CBuilder
	%perl_vendor_privlib/ExtUtils/CBuilder/Base.pm
%dir	%perl_vendor_privlib/ExtUtils/CBuilder/Platform
	%perl_vendor_privlib/ExtUtils/CBuilder/Platform/Unix.pm
%exclude %perl_vendor_privlib/ExtUtils/CBuilder/Platform/VMS.pm
%exclude %perl_vendor_privlib/ExtUtils/CBuilder/Platform/Windows.pm
%exclude %perl_vendor_privlib/ExtUtils/CBuilder/Platform/Windows/BCC.pm
%exclude %perl_vendor_privlib/ExtUtils/CBuilder/Platform/Windows/GCC.pm
%exclude %perl_vendor_privlib/ExtUtils/CBuilder/Platform/Windows/MSVC.pm
%exclude %perl_vendor_privlib/ExtUtils/CBuilder/Platform/aix.pm
%exclude %perl_vendor_privlib/ExtUtils/CBuilder/Platform/android.pm
%exclude %perl_vendor_privlib/ExtUtils/CBuilder/Platform/cygwin.pm
%exclude %perl_vendor_privlib/ExtUtils/CBuilder/Platform/darwin.pm
%exclude %perl_vendor_privlib/ExtUtils/CBuilder/Platform/dec_osf.pm
%exclude %perl_vendor_privlib/ExtUtils/CBuilder/Platform/os2.pm

%changelog
* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.280230-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.280226-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.280224-alt1
- automated CPAN update

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.280220-alt1
- automated CPAN update

* Tue Sep 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.280219-alt1
- automated CPAN update

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.280217-alt1
- automated CPAN update

* Mon Mar 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.280216-alt1
- automated CPAN update

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.280212-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.280205-alt1
- automated CPAN update

* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 0.280202-alt1
- 0.2701 -> 0.280202

* Wed Feb 17 2010 Alexey Tourbin <at@altlinux.ru> 0.27-alt1
- 0.24 -> 0.2701

* Tue May 12 2009 Alexey Tourbin <at@altlinux.ru> 0.24-alt2
- reverted -Wl,-z,defs,--warn-unresolved-symbols in 0.19-alt1

* Sat Sep 27 2008 Alexey Tourbin <at@altlinux.ru> 0.24-alt1
- 0.21 -> 0.24

* Thu Nov 01 2007 Alexey Tourbin <at@altlinux.ru> 0.21-alt1
- 0.19 -> 0.21

* Mon Aug 13 2007 Alexey Tourbin <at@altlinux.ru> 0.19-alt1
- 0.18 -> 0.19
- adjusted linkage code to link with -lperl -lpthread

* Mon May 22 2006 Alexey Tourbin <at@altlinux.ru> 0.18-alt1
- initial revision
