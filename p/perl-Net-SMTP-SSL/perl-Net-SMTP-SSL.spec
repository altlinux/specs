%define dist Net-SMTP-SSL
Name: perl-%dist
Version: 1.01
Release: alt1

Summary: SSL support for Net::SMTP
License: GPL or Artistic
Group: Development/Perl
URL: %CPAN %dist
Packager: Dmitry V. Levin <ldv@altlinux.org>
BuildArch: noarch

Source: %dist-%version.tar

# Automatically added by buildreq on Wed Mar 12 2008 (-bi)
BuildRequires: perl-IO-Socket-SSL perl-devel perl-libnet

%description
Implements the same API as Net::SMTP, but uses IO::Socket::SSL for its
network operations. Due to the nature of "Net::SMTP"'s "new" method, it
is not overridden to make use of a default port for the SMTPS service.
Perhaps future versions will be smart like that. Port 465 is usually
what you want, and it's not a pain to specify that.

For interface documentation, please see Net::SMTP.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Net/SMTP/

%changelog
* Wed Mar 12 2008 Dmitry V. Levin <ldv@altlinux.org> 1.01-alt1
- Initial build, to satisfy git-email package requirements.
