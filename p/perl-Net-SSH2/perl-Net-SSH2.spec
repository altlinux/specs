Name: perl-Net-SSH2
Version: 0.39
Release: alt2

Summary: Support for the SSH 2 protocol via libssh2
License: Perl
Group: Development/Perl

URL: http://search.cpan.org/dist/Net-SSH2/
Source: Net-SSH2-%version.tar.gz

# Automatically added by buildreq on Tue Oct 11 2011
BuildRequires: libssh2-devel libssl-devel perl-Module-Install-CheckLib zlib-devel

%description
Net::SSH2 is a perl interface to the libssh2 (http://www.libssh2.org)
library.  It supports the SSH2 protocol (there is no support for SSH1)
with all of the key exchanges, ciphers, and compression of libssh2.

%prep
%setup -q -n Net-SSH2-%version
rm -rv inc/

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README 
%perl_vendor_archlib/Net
%perl_vendor_autolib/Net

%changelog
* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 0.39-alt2
- rebilt for perl-5.14

* Tue Aug 23 2011 Vladimir Lettiev <crux@altlinux.ru> 0.39-alt1
- initial build
