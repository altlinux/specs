%define dist IO-String
Name: perl-%dist
Version: 1.08
Release: alt2
Summary: IO::File interface emulation for in-core Perl strings
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Nov 19 2011
BuildRequires: perl-devel

%description
The "IO::String" module provide the "IO::File" interface for in-core
strings.  An "IO::String" object can be attached to a string, and will
make it possible to use the normal file operations for reading or
writing data, as well as seeking to various locations of the string.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/IO

%changelog
* Sat Nov 19 2011 Alexey Tourbin <at@altlinux.ru> 1.08-alt2
- rebuilt

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Jul 06 2006 Alexey Tourbin <at@altlinux.ru> 1.08-alt1
- 1.06 -> 1.08

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.06-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Mon Nov 08 2004 Alexey Tourbin <at@altlinux.ru> 1.06-alt1
- 1.05 -> 1.06

* Sat Apr 17 2004 Alexey Tourbin <at@altlinux.ru> 1.05-alt1
- 1.02 -> 1.05
- descriptions updated

* Tue Aug 19 2003 Michael Shigorin <mike@altlinux.ru> 1.02-alt1
- built for ALT Linux
