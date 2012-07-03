%define dist Mail-Sender

Name: perl-%dist
Version: 0.8.16
Release: alt1.1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Perl module for sending mails with attachments through an SMTP server
License: Perl
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/modules/by-module/Mail/%dist-%version.tar.gz
Source1: Mail-Sender.config

BuildArch: noarch

# Set this manually. Due to dumb config engine this module isn't
# compatible w/ ALT perl build machinery.
%add_findreq_skiplist */Mail/Sender.pm

Requires: perl(Carp.pm), perl(File/Basename.pm), perl(FileHandle.pm), perl(MIME/Base64.pm), perl(MIME/QuotedPrint.pm), perl(Socket.pm), perl(open.pm), perl(warnings.pm)

# Automatically added by buildreq on Fri Aug 01 2008
BuildRequires: perl-devel

%description
Mail::Sender provides an object oriented interface to sending mails. It
doesn't need any outer program. It connects to a mail server directly from
Perl, using Socket.

%prep
%setup -n %dist-%version

%build
# We can not just use %%perl_vendor_build
perl Makefile.PL INSTALLDIRS=vendor
make </dev/null
make test
install -m 0644 %SOURCE1 blib/lib/Mail/Sender.config

%install
%perl_vendor_install
# Remove the Win32 module in order to avoid requiring perl(Win32API::Registry).
# Well, to be honest our build machinery smart enough to not generate such
# requirement, but we nuke this junk just in case... ;)
rm -f %buildroot%perl_vendor_privlib/Mail/Sender/CType/Win32.pm

%files
%doc README
%perl_vendor_privlib/Mail

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.8.16-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Aug 01 2008 Victor Forsyuk <force@altlinux.org> 0.8.16-alt1
- 0.8.16

* Wed Jul 11 2007 Victor Forsyuk <force@altlinux.org> 0.8.13-alt1
- 0.8.13

* Wed Aug 24 2005 Alexey Morozov <morozov@altlinux.org> 0.8.10-alt1
- Initial build for ALT Linux
