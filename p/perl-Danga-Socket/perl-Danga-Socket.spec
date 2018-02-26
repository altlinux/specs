%define m_distro Danga-Socket
Name: perl-%m_distro
Version: 1.61
Release: alt1
Summary: Event loop and event-driven async socket base class

Group: Development/Perl
License: Artistic
Url: http://search.cpan.org/~bradfitz/%m_distro/

BuildArch: noarch
Source: %m_distro-%version.tar
Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: perl-devel perl-Sys-Syscall

%description
This is an abstract base class for objects backed by a socket which
provides the basic framework for event-driven asynchronous IO, designed
to be fast. Danga::Socket is both a base class for objects, and an event
loop.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Danga/Socket*
%doc CHANGES

%changelog
* Mon Oct 26 2009 Vladimir Lettiev <crux@altlinux.ru> 1.61-alt1
- initial build

