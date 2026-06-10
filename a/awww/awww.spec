%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define binname awww
%define bash_completions_dir %_datadir/bash-completion/completions
%define zsh_completions_dir %_datadir/zsh/site-functions/
%define fish_completions_dir %_datadir/fish/vendor_completions.d/
%define elv_completions_dir %_datadir/elvish/lib/

Name: awww
Version: 0.12.1
Release: alt1

Summary: An Answer to your Wayland Wallpaper Woes
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://codeberg.org/LGFae/awww
Vcs: https://codeberg.org/LGFae/awww

Source0: %name-%version.tar
Source1: vendor.tar
Source2: config.toml
Patch: %name-%version-alt.patch

BuildRequires: rust-cargo
BuildRequires: /proc
BuildRequires: scdoc
BuildRequires: liblz4-devel
BuildRequires: wayland-protocols
BuildRequires: wayland-devel

%description
%summary.
Efficient animated wallpaper daemon for wayland, controlled at runtime.

%prep
%setup -a1
%autopatch -p1
install -vDt .cargo %SOURCE2

%build
cargo build %_smp_mflags --offline --release
./doc/gen.sh

%install
sourcedir="$(pwd)"
cd "$sourcedir/target/release"
install -Dpvt %buildroot%_bindir %binname %binname-daemon
cd "$sourcedir/completions"
datadir="%buildroot%_datadir"
install -Dpvt %buildroot%zsh_completions_dir _%binname
install -Dpvt %buildroot%bash_completions_dir %binname.bash
install -Dpvt %buildroot%fish_completions_dir %binname.fish
install -Dpvt %buildroot%elv_completions_dir %binname.elv
cd "$sourcedir/doc/generated"
find -type f -exec install -m644 -Dpvt %buildroot%_man1dir/ {} \;

%files
%_bindir/%{binname}*
%zsh_completions_dir/_%binname
%bash_completions_dir/%binname.bash
%fish_completions_dir/%binname.fish
%elv_completions_dir/%binname.elv
%_man1dir/%{binname}*.1*
%doc README.md LICENSE example_scripts

%changelog
* Wed Jun 10 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.12.1-alt1
- Updated to 0.12.1.

* Mon Mar 30 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.12.0-alt1
- Updated to 0.12.0.

* Thu Nov 20 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.11.2-alt1.61.gad93339
- Initial build for ALT Sisyphus.
