%define m_distro Sys-Syscall
Name: perl-%m_distro
Version: 0.23
Release: alt1
Summary: access system calls that Perl doesn't normally provide access to

Group: Development/Perl
License: Artistic
Url: http://search.cpan.org/~bradfitz/%m_distro/

BuildArch: noarch
Source: %m_distro-%version.tar
Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: perl-devel

%description
Use epoll, sendfile, from Perl. Mostly Linux-only support now, but more
syscalls/OSes planned for future.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Sys/Syscall*
%doc CHANGES

%changelog
* Mon Apr 26 2010 Vladimir Lettiev <crux@altlinux.ru> 0.23-alt1
- New version 0.23

* Mon Oct 26 2009 Vladimir Lettiev <crux@altlinux.ru> 0.22-alt1
- initial build

