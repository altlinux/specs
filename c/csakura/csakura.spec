%define _unpackaged_files_terminate_build 1

Name: csakura
Version: 2.0.0
Release: alt1

Summary: A sakura tree with falling petals for your terminal (cmatrix-style)
License: MIT
Group: Toys
Url: https://github.com/realstrawhat/csakura
Vcs: https://github.com/realstrawhat/csakura

Source: %name-%version.tar

BuildRequires: libncursesw-devel

%description
Csakura draws a procedurally grown cherry-blossom tree in your terminal, in
the spirit of cmatrix and cava. No two crowns share a silhouette: two octaves
of value noise break the canopy into clusters, directional light gives it
volume, and limbs show through where the blossom thins. Petals drift down on
a wandering wind, settle on the ground, and fade.

%prep
%setup

%build
%make_build CFLAGS="%optflags" LDFLAGS="%optflags"

%install
%make_install install DESTDIR=%buildroot PREFIX=%prefix

%files
%doc README.md LICENSE
%_bindir/%name

%changelog
* Tue Sep 01 2026 Bogdan Boguslavskij <bogdanb@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus.

