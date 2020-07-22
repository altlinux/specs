# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: ima-evm-utils
Version: 1.3
Release: alt1

Summary: IMA/EVM support utilities
License: GPL-2.0-only
Group: System/Configuration/Other

Url: http://linux-ima.sourceforge.net/
Vcs: https://git.code.sf.net/p/linux-ima/ima-evm-utils
# Docs: https://sourceforge.net/p/linux-ima/wiki/Home/
# Manual: https://en.opensuse.org/SDB:Ima_evm

# Repacked http://sourceforge.net/projects/linux-ima/files/ima-evm-utils/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires: asciidoc
BuildRequires: docbook-style-xsl
BuildRequires: libattr-devel
BuildRequires: libkeyutils-devel
BuildRequires: libssl-devel
BuildRequires: libtpm2-tss-devel
BuildRequires: xsltproc

# For tests
%{?!_without_check:%{?!_disable_check:BuildRequires: openssl attr e2fsprogs xxd rpm-build-vm >= 1.0-alt4}}

Requires: libimaevm = %EVR

%description
The Trusted Computing Group(TCG) run-time Integrity Measurement Architecture
(IMA) maintains a list of hash values of executables and other sensitive
system files, as they are read or executed. These are stored in the file
systems extended attributes. The Extended Verification Module (EVM) prevents
unauthorized changes to these extended attributes on the file system.
ima-evm-utils is used to prepare the file system for these extended attributes.

(This package contains IMA/EVM utilities.)

%package -n libimaevm
Summary: IMA/EVM libraries
Group: System/Libraries

%description -n libimaevm
The Trusted Computing Group(TCG) run-time Integrity Measurement Architecture
(IMA) maintains a list of hash values of executables and other sensitive
system files, as they are read or executed. These are stored in the file
systems extended attributes. The Extended Verification Module (EVM) prevents
unauthorized changes to these extended attributes on the file system.
ima-evm-utils is used to prepare the file system for these extended attributes.

(This package contains libimaevm library.)

%package -n libimaevm-devel
Summary: Development files for applications which use libimaevm
Group: Development/C

%description -n libimaevm-devel
The Trusted Computing Group(TCG) run-time Integrity Measurement Architecture
(IMA) maintains a list of hash values of executables and other sensitive
system files, as they are read or executed. These are stored in the file
systems extended attributes. The Extended Verification Module (EVM) prevents
unauthorized changes to these extended attributes on the file system.
ima-evm-utils is used to prepare the file system for these extended attributes.

(This package contains headers and development files.)

%prep
%setup

sed 's|MANPAGE_DOCBOOK_XSL="/.*|MANPAGE_DOCBOOK_XSL="%_datadir/xml/docbook/xsl-stylesheets/manpages/docbook.xsl"|' \
	-i m4/manpage-docbook-xsl.m4

%build
%autoreconf
%configure \
	--disable-static \
	--with-xml-catalog=/usr/share/xml/docbook/catalog
%make_build

%install
%makeinstall_std doc_DATA=

%check
# ext4 is required to run tests becasue of xattrs
vm-run --overlay=ext4 make check

%files
%doc ChangeLog README AUTHORS COPYING examples/*.sh
%_bindir/*
%_man1dir/*

%files -n libimaevm
%_libdir/libimaevm.so.*

%files -n libimaevm-devel
%_includedir/*
%_libdir/libimaevm.so

%changelog
* Wed Jul 22 2020 Vitaly Chikunov <vt@altlinux.org> 1.3-alt1
- Update to v1.3 (2020-07-21).

* Mon Aug 19 2019 Vitaly Chikunov <vt@altlinux.org> 1.2.1-alt5
- Enable Large File Support.

* Sun Aug 18 2019 Michael Shigorin <mike@altlinux.org> 1.2.1-alt4
- Rework rpm-build-vm use to avoid archdep BR:.

* Sun Aug 18 2019 Vitaly Chikunov <vt@altlinux.org> 1.2.1-alt3
- ifarch tests and rpm-build-vm to only working arches.

* Mon Aug 12 2019 Vitaly Chikunov <vt@altlinux.org> 1.2.1-alt2
- Run tests in rpm-build-vm

* Fri Aug 02 2019 Vitaly Chikunov <vt@altlinux.org> 1.2.1-alt1
- Updated to v1.2.1.

* Thu Nov 08 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.0.0.5.g8c8f29e-alt1
- Updated to v1.1-5-g8c8f29e.

* Tue Sep 04 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1-alt1
- Updated to 1.1.

* Wed Sep 06 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0-alt1
- Initial build.
