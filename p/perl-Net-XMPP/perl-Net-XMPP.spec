%define _unpackaged_files_terminate_build 1
%define dist Net-XMPP
Name: perl-%dist
Version: 1.05
Release: alt1

Summary: XMPP Perl library
License: LGPL
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DA/DAPATRICK/Net-XMPP-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 28 2010
BuildRequires: perl-Digest-SHA1 perl-Module-Build perl-XML-Stream perl(YAML/Tiny.pm) perl(LWP/Online.pm) /proc

%description
Net::XMPP is a collection of Perl modules that provide a Perl Developer
access to the XMPP protocol.  Using OOP modules we provide a clean
interface to writing anything from a full client to a simple protocol
tester.

%prep
%setup -q -n %dist-%version
# TODO
[ %version == 1.05 ] && rm t/gtalk.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README 
%perl_vendor_privlib/Net*

%changelog
* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- automated CPAN update

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
