Name: neovim
Version: 0.12.3
Release: alt1

Summary: heavily refactored vim fork

License: Apache-2.0 and Vim
Group: Editors
Url: https://neovim.io/

# git://git.altlinux.org/gears/n/neovim.git
Source: %name-%version-%release.tar
Source1: %name.watch
Source2: sysinit.vim
# Neovim doesn't have fallback to Vim grammar for a few
# languages (e.g. lua, vimdoc). So we require system parsers
# in this case. It is expected that the rest of the parsers
# will be installed by user using one of the Neovim package managers.
%define neovim_ts_parsers_dir %_libdir/neovim/ts-parsers

BuildRequires(pre): rpm-macros-cmake cmake

BuildRequires: /proc
BuildRequires: gcc-c++
BuildRequires: gperf
BuildRequires: libjemalloc-devel
BuildRequires: libmsgpack-c-devel
BuildRequires: libtermkey-devel
BuildRequires: libuv-devel
BuildRequires: libvterm-devel
BuildRequires: luajit libluajit-devel
BuildRequires: lua5.1-module-lpeg lua5.1-mpack
BuildRequires: libluv-devel
BuildRequires: unibilium-devel
BuildRequires: libtree-sitter-devel >= 0.26.0
BuildRequires: libutf8proc-devel

ExcludeArch: armh

Provides: nvim = %EVR
Requires: %name-runtime = %EVR
Requires: lua5.1(lpeg)

%package runtime
Summary: heavily refactored vim fork - runtime files
Group: Editors
Requires: %name-ts-parsers

%define common_descr \
Neovim is a refactor, and sometimes redactor, in the tradition of Vim (which\
itself derives from Stevie). It is not a rewrite but a continuation and\
extension of Vim. Many clones and derivatives exist; some are very clever, but\
none are Vim. Neovim strives to be a superset of Vim except for some\
intentionally-removed misfeatures. It is built for users who want the good parts\
of Vim, and more.

%description
%common_descr

%description runtime
%common_descr

This package contains runtime files.

%package ts-parsers
Summary: TS parsers for Neovim
Group: Editors
License: Apache-2.0 and MIT
Requires: tree-sitter-lua
Requires: tree-sitter-vimdoc
Requires: tree-sitter-markdown

%description ts-parsers
Minimum set of TS parsers for Neovim for languages that don't have corresponding
languagename.vim syntax files.

%prep
%setup

%build
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DNVIM_VERSION_RELEASE=%release \
	-D USE_BUNDLED=OFF \
	#
%cmake_build

%install
%cmake_install
%find_lang nvim

install -pm0644 runtime/nvim.desktop -Dt %buildroot%_desktopdir
install -pm0644 runtime/nvim.png -Dt %buildroot%_pixmapsdir

install -pm0644 %SOURCE2 %buildroot%_datadir/nvim

# make symlinks to system tree-sitter grammars
install -d %buildroot%neovim_ts_parsers_dir
ln -s %neovim_ts_parsers_dir %buildroot%_datadir/nvim/runtime/parser

ln -s %_libdir/libtree-sitter-lua.so %buildroot/%neovim_ts_parsers_dir/lua.so
ln -s %_libdir/libtree-sitter-vimdoc.so %buildroot/%neovim_ts_parsers_dir/vimdoc.so
ln -s %_libdir/libtree-sitter-markdown.so %buildroot/%neovim_ts_parsers_dir/markdown.so
ln -s %_libdir/libtree-sitter-markdown_inline.so %buildroot/%neovim_ts_parsers_dir/markdown_inline.so

# dependency is handled manually since the lua5.1-module-lpeg doesn't provide "Provides: lpeg.so"
%filter_from_requires /lpeg.so/d

%files -f nvim.lang
%doc LICENSE.txt
%_bindir/nvim
%_man1dir/nvim*

%_desktopdir/nvim.desktop
%_pixmapsdir/nvim.png
%_iconsdir/hicolor/*/apps/nvim.png

%files runtime
%dir %_datadir/nvim
%dir %_datadir/nvim/runtime
%_datadir/nvim/runtime/*
%_datadir/nvim/sysinit.vim

%files ts-parsers
%dir %neovim_ts_parsers_dir
%neovim_ts_parsers_dir/*

%changelog
* Mon Jun 15 2026 Vladimir Didenko <cow@altlinux.org> 0.12.3-alt1
- new version

* Fri Apr 24 2026 Vladimir Didenko <cow@altlinux.org> 0.12.2-alt1
- new version

* Wed Apr 8 2026 Vladimir Didenko <cow@altlinux.org> 0.12.1-alt1
- new version

* Mon Mar 30 2026 Vladimir Didenko <cow@altlinux.org> 0.12.0-alt1
- new version

* Wed Jan 28 2026 Vladimir Didenko <cow@altlinux.org> 0.11.6-alt1
- new version

* Tue Nov 11 2025 Vladimir Didenko <cow@altlinux.org> 0.11.5-alt1
- new version
- vendor markdown TS parser (closes: #56721)

* Wed Sep 10 2025 Vladimir Didenko <cow@altlinux.org> 0.11.4-alt1
- new version

* Mon Jul 14 2025 Vladimir Didenko <cow@altlinux.org> 0.11.3-alt1
- new version

* Mon Jun 2 2025 Vladimir Didenko <cow@altlinux.org> 0.11.2-alt1
- new version

* Wed Apr 30 2025 Vladimir Didenko <cow@altlinux.org> 0.11.1-alt1
- new version

* Thu Mar 27 2025 Vladimir Didenko <cow@altlinux.org> 0.11.0-alt1
- new version

* Thu Jan 30 2025 Vladimir Didenko <cow@altlinux.org> 0.10.4-alt1
- new version

* Mon Dec 23 2024 Vladimir Didenko <cow@altlinux.org> 0.10.3-alt1
- new version

* Fri Nov 15 2024 Vladimir Didenko <cow@altlinux.org> 0.10.2-alt3
- use system TS parsers

* Fri Nov 15 2024 Vladimir Didenko <cow@altlinux.org> 0.10.2-alt2
- vendor vimdoc TS parser

* Mon Oct 07 2024 Vladimir Didenko <cow@altlinux.org> 0.10.2-alt1
- New version

* Mon Sep 30 2024 Vladimir Didenko <cow@altlinux.org> 0.10.1-alt3
- Vendor Lua TS parser

* Mon Aug 26 2024 Vladimir Didenko <cow@altlinux.org> 0.10.1-alt2
- Include system TS parsers
- Require lua TS parser (closes: #51257)

* Thu Jul 25 2024 Vladimir Didenko <cow@altlinux.org> 0.10.1-alt1
- New version

* Sun May 19 2024 Vladimir Didenko <cow@altlinux.org> 0.10.0-alt1
- New version

* Thu Jan 11 2024 Vladimir Didenko <cow@altlinux.org> 0.9.5-alt1
- New version

* Wed Oct 11 2023 Vladimir Didenko <cow@altlinux.org> 0.9.4-alt1
- New version

* Thu Sep 7 2023 Vladimir Didenko <cow@altlinux.org> 0.9.2-alt1
- New version

* Fri Jun 9 2023 Vladimir Didenko <cow@altlinux.org> 0.9.1-alt1
- New version

* Mon Apr 10 2023 Vladimir Didenko <cow@altlinux.org> 0.9.0-alt1
- New version
- Rebuild with libmsgpack-c

* Mon Feb 6 2023 Vladimir Didenko <cow@altlinux.org> 0.8.3-alt1
- New version

* Mon Jan 9 2023 Vladimir Didenko <cow@altlinux.org> 0.8.2-alt1
- New version

* Tue Nov 15 2022 Vladimir Didenko <cow@altlinux.org> 0.8.1-alt1
- New version

* Wed Oct 5 2022 Vladimir Didenko <cow@altlinux.org> 0.8.0-alt1
- New version

* Tue Jun 28 2022 Vladimir Didenko <cow@altlinux.org> 0.7.2-alt1
- New version

* Thu Apr 28 2022 Vladimir Didenko <cow@altlinux.org> 0.7.0-alt1
- New version

* Mon Jan 10 2022 Vladimir Didenko <cow@altlinux.org> 0.6.1-alt1
- New version

* Thu Dec 2 2021 Vladimir Didenko <cow@altlinux.org> 0.6.0-alt1
- New version

* Fri Oct 1 2021 Vladimir Didenko <cow@altlinux.org> 0.5.1-alt1
- New version

* Mon Aug 30 2021 Vladimir Didenko <cow@altlinux.org> 0.5.0-alt2
- Add /usr/share/vim/vimfiles into the runtimepath (closes: #40825)

* Tue Jul 6 2021 Vladimir Didenko <cow@altlinux.org> 0.5.0-alt1
- New version
- Enable package build on aarch64

* Mon May 31 2021 Vladimir Didenko <cow@altlinux.org> 0.4.4-alt2
- Fix build with a new cmake macros

* Thu Aug 6 2020 Vladimir Didenko <cow@altlinux.org> 0.4.4-alt1
- New version
- Fix license name
- Don't build on armh

* Fri Nov 8 2019 Vladimir Didenko <cow@altlinux.org> 0.4.3-alt1
- New version

* Fri Sep 20 2019 Vladimir Didenko <cow@altlinux.org> 0.4.2-alt2
- Don't build on aarch64

* Wed Sep 18 2019 Vladimir Didenko <cow@altlinux.org> 0.4.2-alt1
- New version

* Thu Jul 4 2019 Vladimir Didenko <cow@altlinux.org> 0.3.8-alt2
- fix build on ppc64le

* Thu Jul 4 2019 Vladimir Didenko <cow@altlinux.org> 0.3.8-alt1
- New version (fixes: #36883, CVE-2019-12735)

* Mon Jun 10 2019 Michael Shigorin <mike@altlinux.org> 0.3.7-alt2
- Moved to rpm-macros-luajit

* Mon Jun 10 2019 Vladimir Didenko <cow@altlinux.org> 0.3.7-alt1
- New version

* Tue Apr 30 2019 Vladimir Didenko <cow@altlinux.org> 0.3.5-alt1
- New version

* Wed Jan 16 2019 Vladimir Didenko <cow@altlinux.org> 0.3.4-alt1
- New version

* Wed Jan 9 2019 Vladimir Didenko <cow@altlinux.org> 0.3.3-alt1
- New version

* Wed Jul 25 2018 Vladimir Didenko <cow@altlinux.org> 0.3.1-alt1
- New version

* Thu Jun 28 2018 Vladimir Didenko <cow@altlinux.org> 0.3.0-alt1
- New version

* Mon Jun 04 2018 Vladimir Didenko <cow@altlinux.org> 0.2.2-alt1
- New version

* Wed May 03 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus.
