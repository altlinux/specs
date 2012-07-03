%define dist File-HomeDir
Name: perl-%dist
Version: 0.98
Release: alt2

Summary: Get the home directory for yourself or other users
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-File-Which perl-Pod-Escapes perl-devel perl-prefork

%description
File::HomeDir is a module for dealing with issues relating to the
location of directories for various purposes that are "owned" by a user,
and to solve these problems consistently across a wide variety of
platforms.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/File

%changelog
* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 0.98-alt2
- disabled build dependency on perl-Module-Install

* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 0.98-alt1
- 0.93 -> 0.98
- rebuild as plain src.rpm

* Sun Nov 21 2010 Vladimir Lettiev <crux@altlinux.ru> 0.93-alt1
- 0.80 -> 0.93 (Closes: #24065)
- build with bundled Module::Install (requires version >= 1.0.0)
- new build dep: perl-File-Which

* Sun Aug 10 2008 Alexey Tourbin <at@altlinux.ru> 0.80-alt1
- 0.65 -> 0.80

* Sun Jun 17 2007 Alexey Tourbin <at@altlinux.ru> 0.65-alt1
- 0.63 -> 0.65

* Thu Feb 01 2007 Alexey Tourbin <at@altlinux.ru> 0.63-alt1
- 0.60_03 -> 0.63

* Thu Oct 26 2006 Alexey Tourbin <at@altlinux.ru> 0.60-alt1
- 0.58 -> 0.60_03
- imported sources into git and built with gear

* Thu Aug 10 2006 Alexey Tourbin <at@altlinux.ru> 0.58-alt1
- initial revision, for AppConfig 1.63
