Name:     tarts
Version:  0.1.25
Release:  alt1

Summary:  Screen savers and visual effects for terminal
License:  MIT
Group:    Terminals
Url:      https://github.com/oiwn/tarts

Source0:  %name-%version.tar
Source1:  vendor.tar

BuildRequires(pre): rpm-macros-rust

BuildRequires: rpm-build-rust

%description
tarts (Terminal Arts) is a collection of terminal-based screen savers
and visual effects written in Rust. It includes effects such as Matrix
digital rain, Conway's Game of Life, maze generation, boids flocking
simulation, rotating 3D cube, fire, plasma, pipes, donut and more.

All effects are rendered directly in the terminal using ANSI escape codes.

%prep
%setup -a 1

mkdir -p .cargo
cat >> .cargo/config.toml << 'EOF'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build --all-features

%install
%rust_install 

%files
%doc README.md CHANGELOG.md
%doc LICENSE
%_bindir/%name

%changelog
* Thu Jun 30 2026 Dina Tagantseva <dinchik@altlinux.org> 0.1.25-alt1
- Initial build for Sisyphus.
