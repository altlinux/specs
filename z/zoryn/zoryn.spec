%global _unpackaged_files_terminate_build 1
%def_with check
ExcludeArch: %ix86
Name: zoryn
Version: 0.18.0
Release: alt1
Summary: Maintainer assistant for ALT Linux package maintenance
Group: System/Configuration/Packaging
License: GPL-2.0-or-later
Url: https://altlinux.space/rider/zoryn
VCS: https://altlinux.space/rider/zoryn
Source0: %name-%version.tar
Patch0: %name-%version-dev.patch

BuildRequires: ocaml >= 4.08.0
BuildRequires: libcurl-devel
BuildRequires: dune >= 3.0
BuildRequires: ocaml-cmdliner-devel >= 2.1.0
BuildRequires: ocaml-re-devel >= 1.10.0
BuildRequires: ocaml-yojson-devel >= 1.7.0
BuildRequires: ocaml-curl-devel >= 0.9.0
BuildRequires: ocaml-toml-devel
BuildRequires: ocaml-opam-file-format-devel >= 2.1.0
BuildRequires: ocaml-parsexp-devel
BuildRequires: ocaml-ppxlib-devel >= 0.28.0
BuildRequires: ocaml-alt-releases-matrix-devel >= 0.2.0
BuildRequires: ocaml-lambda-term-devel >= 3.0.0
BuildRequires: ocaml-lwt-devel >= 5.0.0
BuildRequires: ocaml-linenoise-devel
BuildRequires: libev-devel

%if_with check
BuildRequires: ocaml-alcotest-devel >= 1.7.0
BuildRequires: ocaml-crowbar-devel >= 0.2.2
BuildRequires: ocaml-bisect_ppx-devel
BuildRequires: git-core
BuildRequires: git-subtree
BuildRequires: gear
BuildRequires: /dev/pts
BuildRequires: /proc
%endif

Requires: gear
Requires: hasher
Requires: bubblewrap
Requires: git-core
Requires: openssh-clients
Requires: rsync
Requires: alt-releases-matrix
Requires: sisyphus_check

%description
Zoryn is a maintainer assistant that simplifies routine ALT Linux package
maintenance tasks. It provides a unified interface for version updates from
upstream, local and remote hasher builds with multi-arch support, spec file
operations, task management on gitery/gyle, and cross-branch submissions.
Includes batch builds, automatic dependency detection, and CVE detection
in changelogs.

%package -n ocaml-%name
Summary: OCaml libraries for %name
Group: Development/ML

%description -n ocaml-%name
OCaml runtime libraries for %name.

%package -n ocaml-%name-devel
Summary: Development files for %name
Requires: ocaml-%name = %EVR
Group: Development/ML

%description -n ocaml-%name-devel
The ocaml-%name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
%dune_build -p zoryn

%install
%dune_install --docdir=%_docdir/%name-%version zoryn

%check
%dune_check -p zoryn

%files
%_docdir/%name-%version/
%_bindir/zoryn
%_bindir/zoryn_config_fix
%_man1dir/zoryn*.1*
%_datadir/bash-completion/completions/zoryn
%_datadir/zsh/site-functions/_zoryn
%_datadir/fish/vendor_completions.d/zoryn.fish

%files -n ocaml-%name -f ocaml-files.runtime

%files -n ocaml-%name-devel -f ocaml-files.devel

%changelog
* Mon Feb 16 2026 Anton Farygin <rider@altlinux.org> 0.18.0-alt1
- added --repo flag to builder add for apt config generation
- added interactive repo input with TAB completion in builder add
- added repo URL and apt config status to builder list
- added beehive FTBFS status to task test-rebuild
- fixed builder add apt-config generation for sources.list with [label] syntax
- fixed builder add hasher satellite user detection
- fixed builder add hasher_number validation for hasher-useradd

* Sun Feb 15 2026 Anton Farygin <rider@altlinux.org> 0.17.1-alt1
- added HTTP response size limits (64 MB) and download size limits (50 GB)
- added DNS rebinding SSRF protection via CURLOPT_PREREQFUNCTION
- changed gen environment to enable parallel builds by default
- changed builder add to create hasher users by default
- fixed gen environment hasher workdir to use local $USER
- fixed builder add to not include obsolete download command
- fixed lock files to use restrictive permissions (0o600)

* Thu Feb 12 2026 Anton Farygin <rider@altlinux.org> 0.17.0-alt1
- added check packages command for post-build quality checks
- added builder add --create-hasher-users flag
- added fish shell completion
- added builder name validation (alphanumeric only)
- fixed gen environment SSH config Port and username docs
- fixed hsh-rebuild template expansion for remote SSH builds
- fixed check spec changelog_bugs position-based comparison
- fixed build and builder help text examples

* Sun Feb 08 2026 Anton Farygin <rider@altlinux.org> 0.16.0-alt1
- added apt config auto-generation in builder add for easy multi-branch setup
- added builder run command for running commands inside hasher chroot
- added task rebuild --skip and --skip-gyle-done options
- added coverage-guided fuzzing for 9 libraries (73 targets)
- changed task rebuild --all-subtasks to track build results with skip/retry
- changed submit -b option to -B/--branch
- changed task copy to not auto-start task (use --run)
- fixed version normalize to strip all leading v/V prefixes
- fixed check spec url_reachable to expand RPM macros
- fixed up for spec files with composite macros
- fixed up watch file parsing with trailing backslash in comments
- fixed up to support watch files with regex patterns in URL directories

* Tue Feb 04 2026 Anton Farygin <rider@altlinux.org> 0.15.1-alt1
- changed clone to not automatically add gitery remote (use --init-gitery)
- fixed submit to create gitery repo and run init-db for new packages
- fixed submit to use actual package Name instead of spec filename
- fixed up to show correct next step hint (zoryn submit)
- fixed check spec VCS URL validation for git-only servers

* Mon Feb 03 2026 Anton Farygin <rider@altlinux.org> 0.15.0-alt1
- added configurable shell commands via [commands] section in ~/.zoryn
- added readline support in gen environment interactive prompts
- fixed zoryn up to change to git root directory before running

* Thu Jan 30 2026 Anton Farygin <rider@altlinux.org> 0.14.0-alt1
- added terminal title display during long-running commands
- added changelog bug closure syntax validation in check spec
- fixed build to use [builders] default list for multi-builder mode
- fixed build to create .gear/ directory for build logs
- fixed task batch EINTR crash when resizing terminal window

* Mon Jan 27 2026 Anton Farygin <rider@altlinux.org> 0.13.1-alt1
- fixed submit to reuse existing tag on HEAD
- fixed flaky check_host_available test

* Mon Jan 27 2026 Anton Farygin <rider@altlinux.org> 0.13.0-alt1
- added 'check spec' command for RPM spec validation before submit
- added 'gen version-up --filter' for version prefix filtering
- added 'task batch --test' local test build mode
- added 'task batch --skip' and '-b' builder selection
- added '--run' and '--commit' options for submit
- added submit config section in ~/.zoryn
- changed submit to unified task run behavior across all modes
- fixed gen version-up tag prefix and pattern handling
- integrated check spec validation into submit workflow

* Sat Jan 24 2026 Anton Farygin <rider@altlinux.ru> 0.12.0-alt2
- excluded 32-bit architectures (unstable, no real-world usage)

* Fri Jan 24 2026 Anton Farygin <rider@altlinux.org> 0.12.0-alt1
- added 'zoryn builder copy' for copying files into/from hasher chroot
- added 'submit --replace' to replace subtask in existing task
- added 'submit --dry-run' to preview actions without executing
- added '--no-edit-commit' option to submit, task rebuild, task batch
- changed 'submit --with' to auto-replace subtask if same tag exists
- removed 'task replace' command (use 'submit --replace' instead)
- fixed build with ppxlib 0.37.0
- fixed error messages for common exceptions
- fixed task download to auto-create destination directory
- fixed task rebuild topological sorting with cycle handling

* Wed Jan 22 2026 Anton Farygin <rider@altlinux.org> 0.11.0-alt1
- added 'zoryn task test-rebuild' for testing rebuilds with dependencies
- added 'zoryn builder remove' for deleting builder configs
- added sandbox execution for .gear/up.d and .gear/merge-up.d hooks
- added --dptype/--depth options to task rebuild for RDB queries
- added smart download for remote builds (only new packages)
- added interactive input with linenoise in 'zoryn builder add'
- added 'gen environment --update-config' option
- fixed build commands to respect [builders] default config
- fixed hasher_number to apply to all build commands
- fixed various TUI and rebuild workflow issues

* Sun Jan 19 2026 Anton Farygin <rider@altlinux.org> 0.10.0-alt1
- security: multiple fixes for shell injection, SSRF, path traversal
- security: enabled TLS verification, use HTTPS for git/SRPM downloads
- added 'zoryn task batch' for batch package submission
- added 'zoryn task refresh' to update stale rebuild subtasks
- added 'zoryn builder clean' for hasher chroot cleanup
- added concatenated digits support in gen version-up (e.g. camlidl113)
- added PyPI support in gen watch for Gentoo ebuilds
- migrated config files to TOML with legacy INI fallback
- fixed version leading zeros preservation in zoryn up
- fixed remote builder directory handling and exit code detection
- fixed task dependency logic for multi-repo builds

* Wed Jan 15 2026 Anton Farygin <rider@altlinux.org> 0.9.0-alt1
- added interactive TUI mode (--top) for monitoring multi-builder builds
- added parallel builder status checks with fork
- added 'zoryn builder config' and 'zoryn builder list --simple' commands
- added 'zoryn task rebuild --all-subtasks' for rebuilding all packages from task
- added default builder, default_arch and parallel options in config
- added --sequential flag for build commands
- added comma-separated --builder option for multiple builders
- added per-project changelog template in .gear/version-up
- changed build command from gear-hsh to hsh (unified tarball workflow)
- fixed TUI cancel killing all builders instead of selected one
- fixed remote build output garbling with ssh -tt (now uses script wrapper)
- fixed task replace to preserve subtask position
- fixed --builder option being ignored when default_arch configured
- fixed builder selection to prefer free builders over busy ones

* Mon Jan 13 2026 Anton Farygin <rider@altlinux.org> 0.8.0-alt1
- added 'zoryn builder' command for managing remote/local builders
- added builder support to 'zoryn build', 'zoryn up', 'zoryn task rebuild'
- added parallel and multi-architecture builds

* Mon Jan 13 2026 Anton Farygin <rider@altlinux.org> 0.7.5-alt1
- added 'zoryn build' command for local hasher builds
- added 'zoryn gen environment' command for dev environment setup
- added task rebuild --build-deps and --up options
- added zsh completion

* Sun Jan 12 2026 Anton Farygin <rider@altlinux.org> 0.7.4-alt1
- renamed 'zoryn build' command to 'zoryn submit'

* Sun Jan 12 2026 Anton Farygin <rider@altlinux.org> 0.7.3-alt1
- gen watch: added Gentoo/Arch fallback when Debian watch not found
- task rebuild: added --from-log option with smart log search
- task download: added -o/--output option and task ID argument
- up: added gear-update-opts config option
- build: added batch specsubst support
- watch: fixed uversionmangle/pagemangle/downloadurlmangle handling
- added man pages for all commands
- fixed bash-completion install path

* Sun Jan 11 2026 Anton Farygin <rider@altlinux.org> 0.7.2-alt1
- Initial build for ALT Linux.
