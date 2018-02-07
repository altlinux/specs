Name: gnupg-pkcs11-scd
Version: 0.9.0
Release: alt2

Summary: A GnuPG PKCS#11 token daemon
Group: System/Configuration/Hardware
License: BSD
Url: https://github.com/alonbl/gnupg-pkcs11-scd

Source: %name-%version.tar

BuildRequires: libssl-devel
BuildRequires: libgnutls-devel
BuildRequires: libassuan-devel
BuildRequires: libgcrypt-devel
BuildRequires: libgpg-error-devel
BuildRequires: libpkcs11-helper-devel

%description
gnupg-pkcs11 is a project to implement a BSD-licensed smart-card daemon to
enable the use of PKCS#11 tokens with GnuPG.

PKCS#11 is the de-facto standard for accessing cryptographic tokens, and thus
we strongly disagree with WK\'s attitude towards it.

%prep
%setup

%build
%autoreconf
%configure --enable-proxy --localstatedir=%_var
%make_build

%install
%makeinstall_std

%check
#%make check

%files
%_bindir/*
%exclude %_docdir/%name/COPYING
%_docdir/%name/README
%_docdir/%name/*.conf.example
%_man1dir/*.1.*

%changelog
* Wed Feb 07 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.0-alt2
- Fixed localstatedir location.

* Fri Sep 15 2017 Paul Wolneykien <manowar@altlinux.org> 0.9.0-alt1
- Version 0.9.0: Initial build.
