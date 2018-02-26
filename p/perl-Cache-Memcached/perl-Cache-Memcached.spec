%define module  Cache-Memcached

Name: perl-%module
Version: 1.29
Release: alt2

Summary: an object-oriented Perl module for memcached
License: %perl_license
Group: Development/Perl

Url: http://search.cpan.org/dist/%module/
BuildArch: noarch
Source: %module-%version.tar

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Mon Mar 08 2010
BuildRequires: perl-Compress-Zlib perl-Encode perl-Socket6 perl-Storable perl-String-CRC32 perl-devel

%description
This is the Perl API for memcached, a distributed memory cache daemon.
See the documentation within the module for details on its use.

###########################
# Building module in incoming's hasher environment
# causes an error due to disable network support.
# Disabling test for public releases.
%ifdef __BTE
    %def_without test
%endif

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README ChangeLog TODO
%perl_vendor_privlib/Cache*

%changelog
* Sat Aug 13 2011 Nikolay A. Fetisov <naf@altlinux.ru> 1.29-alt2
- Disabing tests in hasher environment

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Oct 10 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.29-alt1
- New version 1.29

* Mon Mar 08 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.28-alt1
- New version 1.28

* Sat Oct 17 2009 Nikolay A. Fetisov <naf@altlinux.ru> 1.27-alt1
- New version 1.27

* Sat Dec 20 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.24-alt1
- New version 1.24

* Mon Nov 14 2005 LAKostis <lakostis at altlinux.ru> 1.14-alt1
- first build for Sisyphus;
- don't package man pages - use perldoc.

