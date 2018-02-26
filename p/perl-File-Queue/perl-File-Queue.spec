%define m_distro File-Queue

Name: perl-File-Queue
Version: 1.01a
Release: alt1.1

Summary: Persistent FIFO queue implemented in pure perl
License: Perl
Group: Development/Perl

Url: %CPAN %m_distro
Source: http://search.cpan.org/CPAN/authors/id/J/JL/JLAVOLD/%m_distro-%version.tar.gz

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch

# Automatically added by buildreq on Mon Oct 11 2010
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description
This module allows for the creation of persistent FIFO queue objects.

File::Queue only handles scalars as queue elements. If you want to work with
references, serialize them first!

The module was written with speed in mind, and it is very fast, but it should
be used with care. Please refer to the CAVEATS section.

%prep
%setup -n %m_distro

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/File*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.01a-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Oct 11 2010 Victor Forsiuk <force@altlinux.org> 1.01a-alt1
- 1.01a

* Sat Sep 13 2008 Michael Bochkaryov <misha@altlinux.ru> 1.00-alt2
- fix directory ownership violation

* Sat Jul 12 2008 Michael Bochkaryov <misha@altlinux.ru> 1.00-alt1
- first build for ALT Linux Sisyphus

