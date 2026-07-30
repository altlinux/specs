%define _unpackaged_files_terminate_build 1

Name: fuseiso
Version: 20260614
Release: alt1

Summary: Mount ISO filesystem images as a non-root user
License: GPL-2.0-or-later
Group: File tools
URL: https://git.sr.ht/~whynothugo/fuseiso
VCS: https://git.sr.ht/~whynothugo/fuseiso

Source0: %name-%version.tar
Patch1: 0001-ALT-add-ISO9660-level-3-images-support.patch

BuildRequires: meson
BuildRequires: glib2-devel
BuildRequires: libfuse3-devel
BuildRequires: zlib-devel

%description
Mount ISO filesystem images as a non-root user. Currently supports
plain ISO9660 Level 1, 2 and 3, Rock Ridge, Joliet, zisofs.
Supported image types: ISO, BIN (single track only), NRG, MDF, IMG (CCD).

%prep
%setup
%autopatch -p2

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/fuseiso
%_datadir/doc/%name/

%changelog
* Thu Jul 30 2026 Anton Farygin <rider@altlinux.org> 20260614-alt1
- 20070708 -> 20260614.
- Switch build system to meson (fuse3).
- Drop patches merged upstream (4GB isos, typo, CVE fixes).
- Rebase ISO9660 level 3 images support patch.

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
