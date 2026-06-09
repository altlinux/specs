%global _unpackaged_files_terminate_build 1
%def_with check
ExcludeArch: %ix86
Name: zoryn
Version: 0.40.0
Release: alt1
Summary: Maintainer assistant for ALT Linux package maintenance
Group: System/Configuration/Packaging
License: GPL-2.0-or-later
Url: https://rider.altlinux.team/zoryn/
VCS: https://altlinux.space/rider/zoryn
Source0: %name-%version.tar
Patch0: %name-%version-dev.patch

BuildRequires: ocaml >= 4.08.0
BuildRequires: libcurl-devel
BuildRequires: dune >= 3.0
BuildRequires: ocaml-cmdliner-devel >= 2.1.0
BuildRequires: ocaml-re-devel >= 1.10.0
BuildRequires: ocaml-yaml-devel >= 3.0.0
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
BuildRequires: ocaml-uucp-devel
BuildRequires: ocaml-pcre2-devel
BuildRequires: ocaml-markup-devel
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
%_man1dir/zoryn*.1*
%_datadir/bash-completion/completions/zoryn
%_datadir/zsh/site-functions/_zoryn
%_datadir/fish/vendor_completions.d/zoryn.fish

%files -n ocaml-%name -f ocaml-files.runtime

%files -n ocaml-%name-devel -f ocaml-files.devel

%changelog
* Tue Jun 09 2026 Anton Farygin <rider@altlinux.org> 0.40.0-alt1
- added sandbox [sandbox] specbr to skip BuildRequires with a bare chroot init
- added submit kernel-module template autodetect with per-flavour specsubst tags
- added submit universal multi-tag --replace for flavour and batch submits
- added task gitclone to clone every subtask repo at its built commit
- added task mkrepo (experimental) merged apt repo overlaying a task on its branch
- added up --reset-to-gear to hard-reset a package to its published state
- fixed up: expand the RPM builtin %nil macro to the empty string in versions
- fixed up: set the upstream remote from any reachable forge, not an allowlist
- fixed up scheme detection for merges of prefixed and non-semver upstream tags
- fixed build --section to expand @var@ specsubst placeholders before rpmbuild
- fixed gen environment GPG key generation hangs on legacy and classic keyrings
- fixed several submit and task test-rebuild edge cases

* Tue May 26 2026 Anton Farygin <rider@altlinux.org> 0.39.0-alt1
- changed task rebuild default --dptype to binary.
- changed up merge-hooks: .gear/merge-up.d/* run only when this invocation
  produced a merge commit (or via explicit --stage merge-hooks).
- added up: sync local repo with public gears/srpms mirror before
  detection on known ALT branches.
- added task copy --into to append subtasks into an existing target task.
- added task copy --subtask to copy only selected subtasks.
- added task test-rebuild --without-task baseline mode.
- added task add --replace to replace an existing subtask in one command.
- added task add positional shorthands <task>^<sub> and <task>/<sub>.
- fixed submit / task batch tag-overwrite safety: recreate stale local tag
  only when ancestor of HEAD and not in gears; --allow-overwrite-tag
  bypasses checks; output distinguishes Created/Reusing/Recreated.
- fixed task copy on fresh source task without fetched artifacts.
- fixed builder clear_hasher_rpms to wipe SRPMS.hasher/ too.
- fixed test-rebuild fork_single_task to clean apt-tmpdir and per-task
  temp dirs on SIGINT/SIGTERM and normal exit.
- fixed up merge when target upstream tag already merged.
- fixed task manage retry on gyle reason-required rejection.
- fixed gear rules parser to recognise any tar.<comp>: directive
  (tar.zst was missed).
- fixed up merge-hooks $TAG resolution via find_all_matching_tags.
- fixed task batch main-package tag handling on second target repo.

* Tue May 05 2026 Anton Farygin <rider@altlinux.org> 0.38.0-alt1
- added task refresh --run/--commit/--test-only/-m to chain task run.
- added web_regex parser for upstream HTML release notes (Wireshark and similar).
- removed legacy INI config support (the migration utility, INI parser, auto-detection).
- fixed task delete/approve/disapprove/log: pkg.git=tag now picks the
  matching subtask instead of the first one sharing the git repo (closes #74).
- fixed bash completion: TAB after pkg.git=tag prefix no longer stalls or
  duplicates the prefix.
- fixed config: invalid TOML in any user config now fails loudly instead
  of silently falling back to defaults.
- fixed up: scheme detection falls back to tarball-watch when only a watch
  file is present.
- fixed up: tarball-watch + PyPI Url uses PyPI for the version and the watch
  file only for the tarball download URL.
- fixed test_cmd_gen_watch flakiness against live upstream endpoints.

* Wed Apr 22 2026 Anton Farygin <rider@altlinux.org> 0.37.0-alt1
- up: added unsandboxed hooks prompt with full script listing
- up: refused symlinks under .gear/{up,merge-up}.d/ (BREAKING)
- up: added [tarball] subdir config field and mozilla changelog parser
- task manage: added full mouse text selection with OSC 52 copy
- task manage: fixed ghost characters on subtask and deps headers
- task manage: fixed mouse selection leaks across screens and refreshes
- task approve/disapprove all: delegated to gyle in a single SSH call
- task refresh: fixed stale snapshot selection on girar
- added project website with bilingual MkDocs documentation

* Wed Apr 15 2026 Anton Farygin <rider@altlinux.org> 0.36.0-alt1
- task manage: added approval/disapproval status line on task list
- task manage: colored checkmark/cross symbols for subtask approvals
- added persistent search history in TUI search inputs (test-rebuild,
  up, task manage) with readline-style Ctrl+R reverse-i-search
- build: added --section bb/ba (pkgbinary/pkgall) for short-circuit
  repackage in existing chroot
- build (python auto-deps): auto-fix retry reuses existing chroot via
  hsh-rebuild
- task rebuild: fixed --skip to work in every mode (was silently
  ignored outside --all-subtasks)
- up: fixed upstream fetch aborting on local/upstream tag clash
- submit: fixed bogus --deps on tasks from a different build chain
- build --section install: fixed by dropping unsupported --nocheck
- build (python auto-deps): detect pyproject_deps.json drift on check
  dependencies source change

* Thu Apr 09 2026 Anton Farygin <rider@altlinux.org> 0.35.0-alt1
- added zoryn commit command (extended analogue of gear-commit)
- rebuild: anchored SRPM filename matcher, unified on
  Builder.find_srpm_in_path
- up: fixed state file path for git worktree support
- up: added auto-setup upstream remote and scheme detection via
  merge-base
- up: fixed scheme detection for non-standard merge messages
- up: fixed PyPI tag lookup with decorative prefix patterns
- check version-up: fixed spec lookup to respect .gear/rules spec:
  directive
- gen version-up: fixed .gear/version-up path in subdirectories
- builder add: fixed --hasher-dir in --multi-add mode with
  {hasher_number} template
- task add: TAB completion now searches across all branches via
  Repoteka API
- gen pypi2spec: fixed VCS tag from home_page, --url override,
  URL normalisation

* Mon Apr 06 2026 Anton Farygin <rider@altlinux.org> 0.34.0-alt1
- task refresh: added --from flag for cross-branch sync (detect stale
  subtasks and replace with copy from source branch)
- task refresh: added --types flag to control which subtask types are
  checked (copy, rebuild, build=gear+srpm, ALL)
- task test-rebuild: added FTBFS warning and --skip-ftbfs flag
- added TAB completion for package names via Repoteka API
- task ls/show: fixed missing package names for delete/copy/rebuild subtasks
- build: unified batch build logic for single and multi-builder modes

* Sun Apr 05 2026 Anton Farygin <rider@altlinux.org> 0.33.0-alt1
- task manage: added mouse text selection (click+drag, double/triple-click,
  auto-scroll, OSC 52 clipboard copy)
- task manage: added Space/b page navigation keys in log viewer
- task manage: added syntax highlighting for log output (sublime-syntax,
  PCRE2 JIT) with user-customizable .tmTheme color themes
- task manage: changed line wrapping to character-based instead of word-based
- task manage: fixed last character lost on line wrap
- task manage: fixed wrapped continuation lines not using full screen width
- task manage: fixed syntax highlighting caches not cleared between lines
- build: added --section flag for running specific rpmbuild section in
  existing chroot, --rpmbuild-args for extra arguments
- build: added configurable log filename template in [build] config
- build: added --skip-check rpmbuild value to skip %%check section
- build: fixed SKIP instead of FAIL for ExcludeArch/ExclusiveArch
- build: fixed batch value not passed in single-builder batch path
- gen pypi2spec: improved runtime deps, autoreq settings, spec naming,
  %%define pypi_name for correct dist-info path

* Tue Mar 31 2026 Anton Farygin <rider@altlinux.org> 0.32.0-alt1
- added submit automatic squash of duplicate release commits
- added PyPI version source for Python packages in up and check version
- added task test-rebuild --top full TUI rewrite using LTerm with log viewer
- added tui_logview shared library for log viewer logic
- added task abort command
- added task approve and task disapprove commands
- added task test-rebuild --package and --packages-file flags
- added CVE:YYYY-NNNNN format support in changelog parser
- fixed gen version-up v-prefix stripping for tag parts
- fixed task test-rebuild --top view mode and log viewer issues
- fixed package_spec is_alt_release for branch and arch releases
- fixed task test-rebuild --continue-no-refresh stats update
- fixed task manage approve/disapprove with message in TUI
- fixed task test-rebuild incorrect rebuild with same git repo tags
- fixed rdb parse_task_packages_json for gear subtasks with multiple packages

* Tue Mar 24 2026 Anton Farygin <rider@altlinux.org> 0.31.0-alt1
- added gen pypi2spec command for generating RPM specs from PyPI metadata
- added task log command for direct TUI log viewing
- added task manage SSE real-time updates, copy subtask support, commit/test-only actions
- added task ls clickable hyperlinks (OSC 8)
- added task batch --continue/--abort/--restart for interrupted batch recovery
- added per-branch default builders via TOML sub-tables ([builders.<branch>])
- fixed task test-rebuild ignoring [builders] default config setting
- fixed up merge abort when unresolved conflicts remain
- fixed up tarball-watch file parser and version detection with HTTP redirects
- fixed HTTP handling of non-standard Content-Encoding

* Wed Mar 18 2026 Anton Farygin <rider@altlinux.org> 0.30.0-alt1
- added zoryn up --continue/--abort/--restart/--stage/--from pipeline control
- added pipeline library for generic sequential pipeline with state persistence
- added task test-rebuild --verify-failures for distinguishing regressions
- added task manage interactive TUI with full-text search, log viewer, event log
- added task manage --no-color flag and NO_COLOR env variable support
- added task manage per-part coloring matching task ls color scheme
- added task manage subtask search in task detail view
- fixed sandbox env var names escaping in execute_direct and execute_hasher
- fixed pipeline lock file descriptor leak
- fixed up --from, --sandbox, --rebuild flag handling in pipeline stages
- fixed build post-build checks to only check current build RPMs
- fixed build log parsing with compression suffix

* Sun Mar 15 2026 Anton Farygin <rider@altlinux.org> 0.29.0-alt1
- suppressed noisy sandbox chroot preparation output with stage progress
- extracted build stage detection into build_log library
- fixed rebuild fallback checking wrong log filename
- fixed print_error and print_warning to write to stderr
- fixed IPv6 link-local SSRF check false positives
- fixed PTY fork safety and buffer cleanup
- fixed case-insensitive Version/Release tag matching in spec writes
- fixed spec detect_old_version to search only after %%changelog
- fixed RPM macro expansion in get_vcs_tag
- fixed crash on narrow terminals in TUI
- fixed remote name validation in girar
- fixed sandbox environment variable key escaping
- fixed version/release split on last dash in RDB
- fixed SSH multiplexing host registration on master start failure
- fixed spec-check to skip reachability checks for unexpanded RPM macros

* Thu Mar 12 2026 Anton Farygin <rider@altlinux.org> 0.28.0-alt1
- fixed task copy to use SRPM package names and Tasks API instead of SSH
- fixed task copy to use batch RDB query for EVR comparison
- fixed spec changelog CVE sub-item indentation and format detection
- fixed task ls to show warning when Tasks API is unavailable
- fixed up --switch-to-upstream-git to always run gear-update-tag
- added --copy-rebuilds, --rebuild-only and --dry-run flags to task copy
- added get_task function and EVR fields to task_api
- added --all flag to task ls

* Tue Mar 10 2026 Anton Farygin <rider@altlinux.org> 0.27.0-alt1
- added task_api library for Tasks API with automatic SSH fallback
- added task add command with repo/del/rebuild/copy actions
- added task run command to queue tasks for build
- added task delsub alias for task delete
- added --needs-approval filter to task ls (maint/tester)
- added swift, aborted_by, depends header fields to task show
- added new subtask fields from Taskoteka API to task show
- added TAB completion for task IDs, users, actions and branches
- fixed task rebuild and task test-rebuild branch derivation from task_repo

* Mon Mar 09 2026 Anton Farygin <rider@altlinux.org> 0.26.0-alt1
- added task rm command for removing tasks from gyle
- added task show command with colorized output, brief and JSON modes
- added task ls command with filters and streaming output
- added SSH multiplexing for girar and gau_git connections
- added --batch-pkgs flag to filter batch values in build/submit/up
- added subtask positioning in submit --with
- added Oracle CSAF JSON advisory parser for changelog
- added per-call max_body_size parameter for gau_http
- added compact_continuation CVE format for changelog entries
- added builders_to_rebuild recording in task test-rebuild stats
- added multiple osv-package names support (comma-separated or TOML array)
- added check version-up command for config validation
- added sandbox fallback confirmation prompt in up command
- fixed submit spec check to report wrong changelog dates as errors
- fixed up --tag version extraction for packages with dashes

* Tue Mar 03 2026 Anton Farygin <rider@altlinux.org> 0.25.0-alt1
- added --switch-to-upstream-git command for migrating to upstream git scheme
- added [merge] scheme override in .gear/version-up
- added Config.set_value_preserving for comment-preserving TOML editing
- fixed gen watch Debian area detection for non-main packages
- fixed gen watch cross-source fallbacks with override names
- fixed up searchmode=plain for watch files
- fixed changelog parsing of Valkey-style release-note headers
- fixed task rebuild to sync RPMs from task before rebuilding
- fixed ssh mux stale socket cleanup and ServerAlive settings
- fixed builder clean to use SSH multiplexing and filter mux errors

* Mon Mar 02 2026 Anton Farygin <rider@altlinux.org> 0.24.0-alt1
- added desktop notifications for long-running commands
- added SSH connection multiplexing via ControlMaster
- added duplicate version-release detection in add_changelog_entry
- fixed watch file parsing of opts= with regex patterns
- fixed watch macro expansion before version matching
- fixed watch Debian macro expansion during parsing
- fixed up to commit only source directory after gear-update
- fixed up to handle add_changelog_entry errors in batch update

* Sun Mar 01 2026 Anton Farygin <rider@altlinux.org> 0.23.0-alt1
- added mountpoint pre-flight validation in build command
- added automatic mountpoint fixes in builder add
- added pattern selectors for -b flag (@all, @host:, ranges, exclusions)
- removed --all-builders flag (use -b @all instead)
- fixed builder status SSH connection throttling per host
- fixed spec check VCS URL fallback to git ls-remote
- fixed HTTP response decompression for watch files
- fixed SRPM lookup on remote builders in task test-rebuild
- improved security

* Thu Feb 26 2026 Anton Farygin <rider@altlinux.org> 0.22.0-alt1
- added --multi-add flag for mass builder creation with interactive mode
- added OSV API integration for CVE extraction in version updates
- added CVE scanning from upstream changelog in tarball workflow
- added spec add changelog --auto CVE extraction
- fixed task copy to replicate subtask types instead of assuming builds
- fixed false git-merge scheme detection for nginx-like packages
- fixed RPM version comparison in changelog range queries
- fixed version-config template v prefix stripping
- improved stability and security

* Tue Feb 24 2026 Anton Farygin <rider@altlinux.org> 0.21.1-alt1
- fixed relative URL resolution in watch files (RFC 3986)
- added Content-Disposition filename support for watch downloads
- fixed uscan-compatible href matching in watch files

* Tue Feb 24 2026 Anton Farygin <rider@altlinux.org> 0.21.0-alt1
- added --packager support in build commands (no more ~/.hasher/config needed)
- added packager configuration to gen environment
- changed waiting for busy builders to default behavior
- fixed local builder status with ~ in hasher_dir path
- fixed test failures on riscv64 (closes: #57983)

* Mon Feb 23 2026 Anton Farygin <rider@altlinux.org> 0.20.0-alt1
- added optional groups (?:...)? support in version-up patterns
- added non-printable character detection in spec check
- added Unicode support for locale-tagged fields in spec check
- improved watch @ANY_VERSION@ expansion to match uscan behavior
- improved watch pattern matching with URL anchoring like uscan
- improved spec check to report exact line and column for non-printable bytes
- extended submit --replace syntax with TASK_ID:N, removed --subtask flag
- improved submit --replace to show package names in subtask list
- unified rpm_spec changelog header parsing, added non-ALT release support

* Tue Feb 17 2026 Anton Farygin <rider@altlinux.org> 0.19.0-alt1
- added changelog date validation to spec check
- added --host, --arch, --branch filter options to builder list
- fixed deadlock on remote builders in builder clean
- fixed batch builds to use parallel multi-builder mode
- fixed batch build log filenames to include batch value
- fixed builder add to include --target for cross-architecture builds
- fixed builder status to report unavailable remote builders

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

* Wed Feb 04 2026 Anton Farygin <rider@altlinux.org> 0.15.1-alt1
- changed clone to not automatically add gitery remote (use --init-gitery)
- fixed submit to create gitery repo and run init-db for new packages
- fixed submit to use actual package Name instead of spec filename
- fixed up to show correct next step hint (zoryn submit)
- fixed check spec VCS URL validation for git-only servers

* Tue Feb 03 2026 Anton Farygin <rider@altlinux.org> 0.15.0-alt1
- added configurable shell commands via [commands] section in ~/.zoryn
- added readline support in gen environment interactive prompts
- fixed zoryn up to change to git root directory before running

* Fri Jan 30 2026 Anton Farygin <rider@altlinux.org> 0.14.0-alt1
- added terminal title display during long-running commands
- added changelog bug closure syntax validation in check spec
- fixed build to use [builders] default list for multi-builder mode
- fixed build to create .gear/ directory for build logs
- fixed task batch EINTR crash when resizing terminal window

* Tue Jan 27 2026 Anton Farygin <rider@altlinux.org> 0.13.1-alt1
- fixed submit to reuse existing tag on HEAD
- fixed flaky check_host_available test

* Tue Jan 27 2026 Anton Farygin <rider@altlinux.org> 0.13.0-alt1
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

* Sat Jan 24 2026 Anton Farygin <rider@altlinux.org> 0.12.0-alt1
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

* Thu Jan 22 2026 Anton Farygin <rider@altlinux.org> 0.11.0-alt1
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

* Mon Jan 19 2026 Anton Farygin <rider@altlinux.org> 0.10.0-alt1
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

* Thu Jan 15 2026 Anton Farygin <rider@altlinux.org> 0.9.0-alt1
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

* Tue Jan 13 2026 Anton Farygin <rider@altlinux.org> 0.8.0-alt1
- added 'zoryn builder' command for managing remote/local builders
- added builder support to 'zoryn build', 'zoryn up', 'zoryn task rebuild'
- added parallel and multi-architecture builds

* Tue Jan 13 2026 Anton Farygin <rider@altlinux.org> 0.7.5-alt1
- added 'zoryn build' command for local hasher builds
- added 'zoryn gen environment' command for dev environment setup
- added task rebuild --build-deps and --up options
- added zsh completion

* Mon Jan 12 2026 Anton Farygin <rider@altlinux.org> 0.7.4-alt1
- renamed 'zoryn build' command to 'zoryn submit'

* Mon Jan 12 2026 Anton Farygin <rider@altlinux.org> 0.7.3-alt1
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
