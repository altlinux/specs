%define dist Digest-Haval256
Name: perl-%dist
Version: 1.0.5
Release: alt1.3

Summary: A 5-round, 256-bit one-way hash function
License: GPL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# patch from rt #24682
Patch: Digest-Haval256-1.0.5-word-64bit.patch

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-devel

%description
Haval is a variable-length, variable-round one-way hash function
designed by Yuliang Zheng, Josef Pieprzyk, and Jennifer Seberry.
The number of rounds can be 3, 4, or 5, while the hash length can be
128, 160, 192, 224, or 256 bits. Thus, there are a total of 15
different outputs. For better security, however, this module
implements the 5-round, 256-bit output.

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README LICENSE Changes examples
%perl_vendor_archlib/Digest
%perl_vendor_autolib/Digest

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.0.5-alt1.3
- rebuilt for perl-5.14

* Sat Nov 13 2010 Vladimir Lettiev <crux@altlinux.ru> 1.0.5-alt1.2
- rebuilt with perl 5.12
- fixed build on x86_64 (patch from rt #24682)

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1.1
- NMU for unknown reason

* Mon Jun 30 2008 Michael Bochkaryov <misha@altlinux.ru> 1.0.5-alt1
- first build for ALT Linux Sisyphus
