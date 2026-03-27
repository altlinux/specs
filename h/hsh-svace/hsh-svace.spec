%define _unpackaged_files_terminate_build 1

Name: hsh-svace
Version: 1.8
Release: alt1

Summary: Run SVACE in hasher
License: GPL-3.0
Group: Development/Other
Url: https://github.com/Blarse/hsh-svace

BuildArch: noarch

Source0: %name-%version.tar

# These scripts are run in hasher
%add_findreq_skiplist %_libexecdir/hsh-svace/hsh-svace-build.sh
%add_findreq_skiplist %_libexecdir/hsh-svace/hsh-svace-analyze.sh

%description
%summary.

This package requires special hasher configuration, please refer to README.md.

%prep
%setup
sed -i 's/@VERSION@/%version/' hsh-svace

%install
mkdir -pv %buildroot%_libexecdir/hsh-svace/
mkdir -pv %buildroot%_bindir
ln -svf %_libexecdir/hsh-svace/hsh-svace %buildroot%_bindir/hsh-svace
install -Dm755 ./hsh-svace -t %buildroot%_libexecdir/hsh-svace/
install -Dm644 ./hsh-svace-build.sh -t %buildroot%_libexecdir/hsh-svace/
install -Dm644 ./hsh-svace-analyze.sh -t %buildroot%_libexecdir/hsh-svace/
install -Dm755 ./hsh-svace-svacer-import -t %buildroot%_bindir
install -Dm644 ./bash_completion.d/hsh-svace -t %buildroot%_datadir/bash-completion/completions/

%files
%doc README.md LICENSE
%_bindir/hsh-svace
%_bindir/hsh-svace-svacer-import
%dir %_libexecdir/hsh-svace
%_libexecdir/hsh-svace/*
%_datadir/bash-completion/completions/hsh-svace

%changelog
* Thu Mar 26 2026 Egor Ignatov <egori@altlinux.org> 1.8-alt1
- Add --svace-config and --svace-config-file options for custom svace config
- Add --svace-warning, --svace-warning-all and --svace-warning-file options
  for custom warning settings
- Add bash completion

* Thu Mar 26 2026 Egor Ignatov <egori@altlinux.org> 1.7-alt1
- Refactor hsh-svace to standard hasher utility style
- Use hsh-sh-functions and hsh-sh-rebuild-functions
- Replace high-level wrappers with low-level hasher primitives
- Add standard hasher options (--number, --hasher-priv-dir, --target, etc.)
- Add --analyze-only mode for running svace analyze from existing results
- Add --install-svace and --bind-svace options for svace installation method

* Mon Aug 04 2025 Egor Ignatov <egori@altlinux.org> 1.6-alt1
- Replace HASP license server bind mount with proper config file setup.

* Thu Nov 28 2024 Egor Ignatov <egori@altlinux.org> 1.5-alt1
- hsh-svace-svacer-import: fix argument parsing

* Fri Oct 18 2024 Egor Ignatov <egori@altlinux.org> 1.4-alt1
- Fix error code propagation.

* Tue Oct 15 2024 Egor Ignatov <egori@altlinux.org> 1.3-alt1
- Add --apt-config option.

* Tue Oct 15 2024 Egor Ignatov <egori@altlinux.org> 1.2-alt1
- Add hsh-svace-svacer-import script.

* Tue Oct 15 2024 Egor Ignatov <egori@altlinux.org> 1.1-alt1
- Output the results as a tar archive.
- Use required mountpoints for build and analysis.

* Wed Oct 09 2024 Egor Ignatov <egori@altlinux.org> 1.0-alt1
- First build for ALT.
