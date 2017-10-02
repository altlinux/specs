Name: sipsak
Version: 0.9.6
Release: alt2
Summary: CLI tool for SIP developers and administrators
License: GPL
Group: Communications

URL: http://sipsak.org/
Source: %name-%version.tar.bz2

# Automatically added by buildreq on Thu Oct 08 2009 (-bi)
BuildRequires: libssl-devel

%description
sipsak is a small command line tool for developers and administrators of
Session Initiation Protocol (SIP) applications. It can be used for some
simple tests on SIP applications and devices.

%prep
%setup

%build
%add_optflags -fgnu89-inline
%configure
%make

%install
%makeinstall

%files
%_bindir/*
%_man1dir/*
%doc AUTHORS INSTALL COPYING README NEWS TODO

%changelog
* Mon Oct 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.6-alt2
- Fixed build with gcc-6.

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.9.6-alt1.1.qa1
- NMU: rebuilt for debuginfo.

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 0.9.6-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Thu Oct 08 2009 Michael Bochkaryov <misha@altlinux.ru> 0.9.6-alt1
- Initial build for ALT Linux

