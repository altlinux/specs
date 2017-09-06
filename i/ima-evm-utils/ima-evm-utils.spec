%define _unpackaged_files_terminate_build 1

Name: ima-evm-utils
Version: 1.0
Release: alt1

Summary: IMA/EVM support utilities
Group: System/Configuration/Other
License: GPLv2
Url: http://linux-ima.sourceforge.net/

# Repacked http://sourceforge.net/projects/linux-ima/files/ima-evm-utils/%name-%version.tar.gz
Source: %name-%version.tar

# Automatically added by buildreq on Tue Feb 14 2017
# optimized out: docbook-dtds libgpg-error perl pkg-config python-base python-modules xml-common
BuildRequires: asciidoc docbook-style-xsl libattr-devel libkeyutils-devel libssl-devel python-modules-compiler python-modules-encodings time xsltproc

Requires: libimaevm0 = %EVR

%description
The Trusted Computing Group(TCG) run-time Integrity Measurement Architecture
(IMA) maintains a list of hash values of executables and other sensitive
system files, as they are read or executed. These are stored in the file
systems extended attributes. The Extended Verification Module (EVM) prevents
unauthorized changes to these extended attributes on the file system.
ima-evm-utils is used to prepare the file system for these extended attributes.

(This package contains IMA/EVM utilities.)

%package -n libimaevm0
Summary: IMA/EVM libraries
Group: System/Libraries

%description -n libimaevm0
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

sed 's|^MANPAGE_DOCBOOK_XSL *=.*|MANPAGE_DOCBOOK_XSL = %_datadir/xml/docbook/xsl-stylesheets/manpages/docbook.xsl|' \
	-i Makefile.am

%build
%autoreconf
%configure \
	--disable-static \
	#
%make_build

%install
%makeinstall_std doc_DATA=

%files
%doc ChangeLog README AUTHORS COPYING examples/*.sh
%_bindir/*
%_man1dir/*

%files -n libimaevm0
%_libdir/libimaevm.so.0*

%files -n libimaevm-devel
%_includedir/*
%_libdir/libimaevm.so

%changelog
* Wed Sep 06 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0-alt1
- Initial build.
