%def_disable snapshot
%define ver_major 1.1
%define beta %nil
%define rdn_name com.system76.CosmicGreeter

%def_disable bootstrap
%def_enable check

Name: cosmic-greeter
Version: %ver_major.0
Release: alt1%beta

Summary: COSMIC Greeter
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-greeter

Vcs: https://github.com/pop-os/cosmic-greeter.git

%define git_ver epoch-%version%(echo %beta|sed 's/^\./-/')
%if_disabled snapshot
Source: %url/archive/%git_ver/%name-%version%beta.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: %name-%version%beta-cargo.tar

Requires: greetd
Requires: cosmic-comp
Requires: cosmic-randr
Requires: icon-theme-cosmic

Provides: greetd-greeter

BuildRequires(pre): rpm-build-rust rpm-macros-pam0 rpm-macros-alternatives rpm-macros-systemd
BuildRequires: just clang-devel
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(pam)

# no cosmic-comp for ppc64le
ExcludeArch: %ix86 armh ppc64le

%description
COSMIC greeter for greetd, which can be run inside cosmic-comp.

%prep
%setup -n %name-%{?_enable_snapshot:%version%beta}%{?_disable_snapshot:%git_ver} %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version%beta-cargo.tar .cargo/ vendor/}

%build
export VERGEN_GIT_SHA=%version
export VERGEN_GIT_COMMIT_DATE=%(date --iso-8601)
export RUSTFLAGS="${RUSTFLAGS} -g"
just build-release

%install
export VERGEN_GIT_SHA=%version
export VERGEN_GIT_COMMIT_DATE=%(date --iso-8601)
just rootdir=%buildroot install
install -Dm 644 %name.toml -t %buildroot/%_sysconfdir/greetd/greeters/

# greetd config
mkdir -p %buildroot/%_altdir
echo "%_sysconfdir/greetd/config.toml %_sysconfdir/greetd/greeters/%name.toml 30" \
    > %buildroot%_altdir/greetd-%name

# services
sed -i 's/cosmic-greeter.toml/config.toml/' debian/%name.service
install -Dm 644 debian/%name{.service,-daemon.service} -t %buildroot%_unitdir/

# PAM config
install -d %buildroot%_sysconfdir/pam.d
  ln -s greetd %buildroot%_sysconfdir/pam.d/%name

%check
export VERGEN_GIT_SHA=%version
export VERGEN_GIT_COMMIT_DATE=%(date --iso-8601)
%rust_test

%files
%_sysconfdir/greetd/greeters/%name.toml
%_sysconfdir/pam.d/%name
%_bindir/%name
%_bindir/%name-start
%_bindir/%name-daemon
%_altdir/greetd-%name
%_unitdir/%name.service
%_unitdir/%name-daemon.service
%_sysusersdir/%name.conf
%_tmpfilesdir/%name.conf
%_datadir/dbus-1/system.d/%rdn_name.conf
%doc README*

%changelog
* Wed Jun 24 2026 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Thu Jun 11 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.16-alt1
- 1.0.16

* Thu Jun 04 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.15-alt1
- 1.0.15

* Wed May 27 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.14-alt1
- 1.0.14

* Wed May 13 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.13-alt1
- 1.0.13

* Thu May 07 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.12-alt1
- 1.0.12

* Wed Apr 22 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.11-alt1
- 1.0.11

* Wed Apr 15 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.10-alt1
- 1.0.10

* Wed Apr 08 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.9-alt1
- 1.0.9

* Tue Feb 24 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.8-alt1
- 1.0.8

* Wed Feb 18 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.7-alt1
- 1.0.7

* Wed Feb 11 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.6-alt1
- 1.0.6

* Tue Feb 03 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.5-alt1
- 1.0.5

* Wed Jan 28 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.4-alt1
- 1.0.4

* Wed Jan 21 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Wed Jan 14 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Mon Jan 05 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1.2
- switched /etc/pam.d/cosmic-greeter to greetd PAM config (ALT #57427)

* Fri Jan 02 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1.1
- installed /etc/pam.d/cosmic-greeter
  as a symlink to /etc/pam.d/login (ALT #57416)

* Wed Dec 31 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Sat Dec 20 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1.1
- installed cosmic-greeter{.service,-daemon.service},
  and /etc/greetd/greeters/cosmic-greeter.toml as alternative of
  /etc/greetd/greeters/config.toml (ALT #57295)

* Thu Dec 11 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Thu Dec 04 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.82.beta.9
- 1.0.0-beta.9

* Thu Nov 13 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.81.beta.6
- 1.0.0-beta.6

* Sun Sep 21 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.80.beta.1
- 1.0.0-beta.1

* Thu Apr 24 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.70.alpha.7
- 1.0.0-alpha.7

* Sat Feb 22 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.60.alpha.6
- 1.0.0-alpha.6

* Wed Jan 15 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.51.alpha.5.1
- 1.0.0-alpha.5.1

* Fri Jan 10 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.5.alpha.5
- 1.0.0-alpha.5

* Sat Dec 07 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.4.alpha.4
- 1.0.0-alpha.4

* Thu Sep 26 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.2.alpha.2
- 1.0.0-alpha.2

* Sun Aug 18 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.1.alpha.1
- first build for Sisyphus (epoch-1.0.0-alpha.1-5-g3679ee5)


