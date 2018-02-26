%define dist X11-Protocol
Name: perl-%dist
Version: 0.56
Release: alt1.1

Summary: Raw interface to X Window System servers
License: GPL or Artistic
Group: Development/Perl
Packager: Sergey Vlasov <vsu@altlinux.ru>

URL: %CPAN %dist
Source: %dist-%version.tar.bz2

BuildArch: noarch

# Automatically added by buildreq on Sat Jan 28 2006 (-bi)
BuildRequires: perl-devel

%description
X11::Protocol is a client-side interface to the X11 Protocol, allowing
perl programs to display windows and graphics on X11 servers.

%prep
%setup -q -n %dist-%version

%build
# test tries to display a window
%def_without test
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes Todo
%perl_vendor_privlib/X11*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.56-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Oct 23 2006 Sergey Vlasov <vsu@altlinux.ru> 0.56-alt1
- Version 0.56 (fixes infinite loop on X error).
- Added Packager: tag.

* Sat Jan 28 2006 Sergey Vlasov <vsu@altlinux.ru> 0.55-alt1
- Initial revision
