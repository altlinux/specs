%define dist Net-XMPP
Name: perl-%dist
Version: 1.02
Release: alt1

Summary: XMPP Perl library
License: LGPL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch: perl-Net-XMPP-1.02-alt-syntax.patch

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 28 2010
BuildRequires: perl-Digest-SHA1 perl-Module-Build perl-XML-Stream

%description
Net::XMPP is a collection of Perl modules that provide a Perl Developer
access to the XMPP protocol.  Using OOP modules we provide a clean
interface to writing anything from a full client to a simple protocol
tester.

%prep
%setup -q -n %dist-%version
%patch -p1
rm -rv t/lib/Test/

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README 
%perl_vendor_privlib/Net*

%changelog
* Wed Apr 28 2010 Alexey Tourbin <at@altlinux.ru> 1.02-alt1
- 1.0 -> 1.02

* Wed Dec 15 2004 Andrey Brindeew <abr@altlinux.org> 1.0-alt2
- Packager tag added
- Added %name-1.0-alt-test-roster.patch (thanks Alexey Tourbin)

* Wed Dec 15 2004 Alexey Tourbin <at@altlinux.ru> 1.0-alt1.1
- build against system Test::More (removed t/lib/Test)
- fixed a bug in t/roster.t discovered with new Test::More (cpan #8888)

* Sun Nov 28 2004 Andrey Brindeew <abr@altlinux.org> 1.0-alt1
- First build for ALT Linux.
