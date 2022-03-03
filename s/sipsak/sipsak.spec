%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: sipsak
Version: 0.9.8.1
Release: alt1
Summary: CLI tool for SIP developers and administrators
License: GPLv2+
Group: Communications
URL: https://github.com/nils-ohlmeier/sipsak

# https://github.com/nils-ohlmeier/sipsak.git
Source: %name-%version.tar

# Automatically added by buildreq on Thu Oct 08 2009 (-bi)
BuildRequires: libssl-devel

%description
sipsak is a small command line tool for developers and administrators of
Session Initiation Protocol (SIP) applications. It can be used for some
simple tests on SIP applications and devices.

%prep
%setup

%build
%add_optflags -D_FILE_OFFSET_BITS=64

%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/*
%_man1dir/*

%changelog
* Thu Mar 03 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.8.1-alt1
- Updated to upstream version 0.9.8.1.

* Fri Dec 04 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.7-alt1.git.02e5b5c
- Updated to latest upstream commit.

* Fri Jul 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.7-alt1
- Updated to upstream version 0.9.7.

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 0.9.6-alt2.1
- NMU: Rebuild with new openssl 1.1.0.

* Mon Oct 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.6-alt2
- Fixed build with gcc-6.

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.9.6-alt1.1.qa1
- NMU: rebuilt for debuginfo.

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 0.9.6-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Thu Oct 08 2009 Michael Bochkaryov <misha@altlinux.ru> 0.9.6-alt1
- Initial build for ALT Linux

