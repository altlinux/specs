%define _unpackaged_files_terminate_build 1

Name: gitoskop
Version: 1.5.0
Release: alt1

Summary: Read-only HTTP API for browsing trees of bare git repositories
License: AGPL-3.0-or-later
Group: System/Servers
Url: https://altlinux.space/rider/gitoskop
Vcs: https://altlinux.space/rider/gitoskop.git
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-systemd
BuildRequires: rust rust-cargo gcc make
# test fixtures shell out to git
BuildRequires: git-core

%description
gitoskop serves trees of bare git repositories (gear/gitery mirrors) over a
read-only HTTP API: browsing, log with ref decorations, commit details,
tree/blob/raw access, unified diffs and byte-exact patches that apply with
git am, plus substring search over the repository index. Everything is
bounded (blob/patch size caps, tree entry caps, request concurrency and
timeouts) so it can face untrusted clients.

%package webui
Summary: Static web interface for the gitoskop API
Group: Networking/WWW
BuildArch: noarch

%description webui
A static (HTML/CSS/vanilla JS, no build step) browser interface for a
gitoskop API instance: repository tree, file view with syntax highlighting
and blame, content grep, commit log, side-by-side diffs and shareable line
links.

The files are installed unconfigured under %_datadir/%name/web: no web
server configuration is shipped. Serve that directory with any web server;
the API base URL is set in the interface itself, so the API may live on
another host and this package does not require gitoskop locally.

%prep
%setup
# The vendored crates are committed to the packaging branch by
# .gear/merge-up.d/01-vendor.sh; wire cargo to them and stay offline.
mkdir -p .cargo
cat > .cargo/config.toml <<'EOF'
[source.crates-io]
replace-with = "vendored-sources"
[source.vendored-sources]
directory = "vendor"
[net]
offline = true
EOF

%build
cargo build --release --locked --offline

%install
install -Dm755 target/release/%name %buildroot%_bindir/%name
install -Dm644 dist/%name.service %buildroot%_unitdir/%name.service
install -Dm644 dist/%name.conf.example %buildroot%_sysconfdir/%name/%name.conf
# Static web UI, without the JS test suite.
mkdir -p %buildroot%_datadir/%name
cp -a web %buildroot%_datadir/%name/web
rm -rf %buildroot%_datadir/%name/web/test

%pre
/usr/sbin/groupadd -r -f %name 2>/dev/null ||:
/usr/sbin/useradd -r -g %name -d /var/lib/%name -s /dev/null \
	-c 'gitoskop git browsing API' %name 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%check
cargo test --release --locked --offline

%files
%doc README.md CHANGELOG.md AUTHORS
%_bindir/%name
%_unitdir/%name.service
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/%name.conf

%files webui
%doc LICENSE
%dir %_datadir/%name
%_datadir/%name/web

%changelog
* Sat Aug 29 2026 Anton Farygin <rider@altlinux.org> 1.5.0-alt1
- 1.4.1 -> 1.5.0

* Thu Aug 20 2026 Anton Farygin <rider@altlinux.org> 1.4.1-alt1
- 1.4.0 -> 1.4.1
- webui: spec section jump strip now scrolls to the section on click and
  lists only sections (dropped the %%define clutter)
- fixed a flaky change-signal test that broke %%check on fast build hosts

* Thu Aug 20 2026 Anton Farygin <rider@altlinux.org> 1.4.0-alt1
- 1.3.0 -> 1.4.0
- new "ui" config key: the server serves its own web UI from the binary,
  no separate web server needed
- new "gitweb_compat" config key: answers old gitweb.cgi URLs
- webui: RPM spec syntax highlighting, section/macro jump strip, autolinks
- webui accessibility: screen readers get row kinds and controls as
  text, not decorative glyphs
- webui: content centered on wide screens, aligned toolbar controls,
  narrow-screen and mobile layout fixes
- zip and tar.bz2 archives; commit/<rev>.patch and .diff URLs
- faster first listing after a restart, faster large directories
- hardening against unauthenticated resource exhaustion

* Sat Aug 15 2026 Anton Farygin <rider@altlinux.org> 1.3.0-alt1
- 1.2.0 -> 1.3.0
- new gitoskop-webui subpackage: static web interface, installed
  unconfigured under %_datadir/%name/web (repository tree, syntax
  highlighting, blame, content grep, log, side-by-side diffs, shareable
  line links with notes, RU/EN)
- MCP endpoint at POST /_/mcp for AI agents: eight read-only tools with
  bounded, pageable results (mcp_enabled, mcp_max_bytes)
- new endpoints: blame, content grep, streamed tar.gz archives,
  annotated tag bodies, Atom feeds for history, tags and directories
- HTTP caching: immutable for OID-addressed content, ETag elsewhere
- path-filtered log follows git's history simplification; tags listed
  newest-first by commit time
- per-root upstream merge_status; new object_cache_bytes config key
- security: Content-Disposition filename sanitization, .gitmodules URL
  scheme filtering, XML Char filtering in Atom feeds, hardening against
  unauthenticated resource exhaustion
- default max_blob_bytes lowered 50 MiB -> 10 MiB

* Thu Jul 23 2026 Anton Farygin <rider@altlinux.org> 1.2.0-alt1
- 1.1.0 -> 1.2.0

* Tue Jul 21 2026 Anton Farygin <rider@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus (v1.1.0).
