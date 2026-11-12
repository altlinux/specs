Name: mermaid-rs-renderer
Version: 0.3.1
Release: alt1

Summary: Native Mermaid diagram renderer to SVG and PNG

License: MIT
Group: Graphics
URL: https://github.com/1jehuang/mermaid-rs-renderer
# Source-url: https://github.com/1jehuang/mermaid-rs-renderer.git
Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust /proc

# resvg and text metrics load system fonts through fontdb at runtime.
Requires: fonts-ttf-dejavu

%description
mmdr renders Mermaid diagrams directly to SVG and PNG using native Rust
parsers and renderers. It supports flowcharts, state diagrams, Git graphs
and other diagram types without a browser or JavaScript runtime.

%prep
%setup -a1
install -vD %SOURCE2 .cargo/config.toml

%build
%rust_build

%install
%rust_install mmdr

%check
# Known layout assertions also skipped by Alpine (upstream issue #84).
%rust_test --lib -- \
    --skip cycle_fixture_subgraph_entry_aligns_with_spine \
    --skip dense_flowchart_avoids_crossing_between_middle_and_far_edges

%files
%_bindir/mmdr
%doc README.md LICENSE

%changelog
* Wed Nov 11 2026 Vitaly Lipatov <lav@altlinux.ru> 0.3.1-alt1
- initial build for ALT Linux.

