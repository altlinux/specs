%define module Net-SSH-Expect
%define _enable_test 1

Name: perl-Net-SSH-Expect
Version: 1.09
Release: alt2

Summary: SSH wrapper to execute remote commands

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Alexey Shabalin <shaba@altlinux.ru>

BuildArch: noarch
Source: %module-%version.tar.gz

# Automatically added by buildreq on Fri Oct 08 2010
BuildRequires: perl-Expect perl-devel

%description
This module is a wrapper to the *ssh* executable that is available in your system's *$PATH*.
Use this module to execute commands on the remote SSH server.
It authenticates with the user and password you passed in the constructor's attributes
"user" and "password".

Once an ssh connection was started using the "connect()" method it will remain open
until you call the "close()" method. This allows you execute as many commands as you want
with the "exec()" method using only one connection. This is a better approach over other
ssh wrapper implementations, i.e: Net::SCP, Net::SSH and Net::SCP::Expect, that start a new
ssh connection each time a remote command is issued or a file is transfered.

It uses *Expect.pm* module to interact with the SSH server. A "get_expect()" method is
provided so you can obtain the internal "Expect" object connected to the SSH server. Use
this only if you have some special need that you can't do with the "exec()" method.

This module was inspired by Net::SCP::Expect <http://search.cpan.org/~djberg/Net-SCP-Expect-0.12/Expect.pm>
and by Net::Telnet and some of its methods work the same as these two modules.

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Net/*

%changelog
* Mon Nov 15 2010 Alexey Shabalin <shaba@altlinux.ru> 1.09-alt2
- drop %%perl_vendor_man3dir

* Fri Oct 08 2010 Alexey Shabalin <shaba@altlinux.ru> 1.09-alt1
- initial build for ALT Linux Sisyphus

