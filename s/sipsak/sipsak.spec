Name: sipsak
Version: 0.9.6
Release: alt1.1
Summary: CLI tool for SIP developers and administrators
License: GPL
Group: Communications

URL: http://sipsak.org/
Source: %name-%version.tar.bz2

Packager: Michael Bochkaryov <misha@altlinux.ru>

# Automatically added by buildreq on Thu Oct 08 2009 (-bi)
BuildRequires: libssl-devel

%description
sipsak is a small command line tool for developers and administrators of
Session Initiation Protocol (SIP) applications. It can be used for some
simple tests on SIP applications and devices.

%prep
%setup -n %name-%version

%build
%configure
%make

%install
%makeinstall

%files
%_bindir/*
%_man1dir/*
%doc AUTHORS INSTALL COPYING README NEWS TODO

%changelog
* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 0.9.6-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Thu Oct 08 2009 Michael Bochkaryov <misha@altlinux.ru> 0.9.6-alt1
- Initial build for ALT Linux

