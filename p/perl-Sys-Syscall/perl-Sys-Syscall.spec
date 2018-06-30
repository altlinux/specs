%define _unpackaged_files_terminate_build 1
%define m_distro Sys-Syscall
Name: perl-%m_distro
Version: 0.25
Release: alt2
Summary: access system calls that Perl doesn't normally provide access to

Group: Development/Perl
License: Artistic
Url: http://search.cpan.org/~bradfitz/%m_distro/
Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildArch: noarch
Source: %m_distro-%version.tar
# ghpr#6, rhbz#1288335
Patch0:         Sys-Syscall-0.25-Add-ppc64le-support.patch
Patch1:         Sys-Syscall-0.25-Add-s390-x-support.patch
Patch2:         Sys-Syscall-0.25-Add-aarch64-support.patch

BuildRequires: perl-devel

%description
Use epoll, sendfile, from Perl. Mostly Linux-only support now, but more
syscalls/OSes planned for future.

%prep
%setup -q -n %m_distro-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

# possible fs conflicts
rm -f %buildroot%perl_vendor_privlib/Sys/README.pod

%files
%perl_vendor_privlib/Sys/Syscall*
%doc CHANGES README.pod

%changelog
* Fri Jun 29 2018 Igor Vlasenko <viy@altlinux.ru> 0.25-alt2
- fixed unpackaged files
- aarch64 support

* Tue Oct 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated CPAN update

* Mon Apr 26 2010 Vladimir Lettiev <crux@altlinux.ru> 0.23-alt1
- New version 0.23

* Mon Oct 26 2009 Vladimir Lettiev <crux@altlinux.ru> 0.22-alt1
- initial build

