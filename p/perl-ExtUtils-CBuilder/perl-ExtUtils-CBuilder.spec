%define dist ExtUtils-CBuilder
Name: perl-%dist
Version: 0.280202
Release: alt1

Summary: Compile and link C code for Perl modules
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

Patch0: ExtUtils-CBuilder-0.280202-alt-unix.patch
Patch1: ExtUtils-CBuilder-0.280202-alt-link.patch

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 15 2011
BuildRequires: gcc-c++ perl-IPC-Cmd

%description
This module can build the C portions of Perl modules by invoking the
appropriate compilers and linkers in a cross-platform manner.  It was
motivated by the CModule::Build project, but may be useful for other
purposes as well.  However, it is not intended as a general
cross-platform interface to all your C building needs.  That would have
been a much more ambitious goal!

%prep
%setup -q -n %dist-%version
%patch0 -p1
%patch1 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	Changes README
%dir	%perl_vendor_privlib/ExtUtils
	%perl_vendor_privlib/ExtUtils/CBuilder.pm
%dir	%perl_vendor_privlib/ExtUtils/CBuilder
	%perl_vendor_privlib/ExtUtils/CBuilder/Base.pm
%dir	%perl_vendor_privlib/ExtUtils/CBuilder/Platform
	%perl_vendor_privlib/ExtUtils/CBuilder/Platform/Unix.pm

%changelog
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
