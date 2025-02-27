%define _unpackaged_files_terminate_build 1

Name: fuseiso
Version: 20070708
Release: alt4

Summary: Mount ISO filesystem images as a non-root user
License: GPL-2.0-or-later
Group: File tools
URL: http://sourceforge.net/projects/fuseiso/

Source0: %name-%version.tar
Patch1: 0001-ALT-add-multithreading-and-libraries-flags-for-ld.patch
Patch2: 0002-REDHAT-handle-larger-than-4GB-isos.patch
Patch3: 0003-Fix-typo.patch
Patch4: 0004-DEBIAN-CVE-2015-8837.patch
Patch5: 0005-DEBIAN-prevent-integer-overflow-in-ZISO-code.patch
Patch6: 0006-ALT-add-ISO9660-level-3-images-support.patch

BuildRequires: gcc-c++
BuildRequires: glib2-devel
BuildRequires: libfuse-devel
BuildRequires: zlib-devel

%description
Mount ISO filesystem images as a non-root user. Currently supports
plain ISO9660 Level 1, 2 and 3, Rock Ridge, Joliet, zisofs.
Supported image types: ISO, BIN (single track only), NRG, MDF, IMG (CCD).

%prep
%setup
%autopatch -p2

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog NEWS README
%_bindir/fuseiso

%changelog
* Thu Feb 27 2025 Ajrat Makhmutov <rauty@altlinux.org> 20070708-alt4
- Add ISO9660 level 3 images support (thanks proskur@).
- Fix License tag according to SPDX.

* Thu Oct 29 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 20070708-alt3
- Applied patches from Gentoo (Fixes: CVE-2015-8836, CVE-2015-8837).

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 20070708-alt2.qa1
- NMU: rebuilt for debuginfo.

* Sun Nov 16 2008 Igor Zubkov <icesik@altlinux.org> 20070708-alt2
- update Url

* Sun Jun 29 2008 Igor Zubkov <icesik@altlinux.org> 20070708-alt1
- build for Sisyphus
