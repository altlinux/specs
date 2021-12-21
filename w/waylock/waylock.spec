Name: waylock
Version: 0.3.3
Release: alt1
Summary: simple screenlocker for wayland compositors
License: MIT
Group: Graphical desktop/Other
Url: https://github.com/ifreund/waylock
Source: %name-%version.tar
Source1: vendor.tar
Source44: %name.watch
#ExcludeArch: i586 armh

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: libpam-devel

%description
Waylock is a simple screenlocker for wayland compositors. It takes inspiration
from [slock](https://tools.suckless.org/slock/) with its minimalistic feature
set, but is implemented in [rust](https://www.rust-lang.org/) for first class
safety and security.

Waylock will work with any wayland compositor implementing the `wlr-layer-shell`
`wlr-input-inhibitor` protocols. In general, this means
[wlroots](https://github.com/swaywm/wlroots)-based compositors such as
[river](https://github.com/ifreund/river) or
[sway](https://github.com/swaywm/sway).

%prep
%setup
tar xf %SOURCE1
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

EOF

cat > console_lock <<EOF
#%PAM-1.0
auth		include		system-auth
account		required	pam_permit.so
password	required	pam_permit.so
EOF
subst 's/with_password("system-auth")/with_password("console_lock")/' src/lock/auth.rs

%build
export NPROCS=4
%rust_build

%install
%rust_install
mkdir -p %buildroot/etc/pam.d
install -m644 -D -t %buildroot/etc/pam.d/ console_lock
%find_lang --with-gnome %name

%check
%rust_test

%files -f %name.lang
%doc *.md
/etc/pam.d/*
%attr(102711,root,chkpwd) %_bindir/%name

%changelog
* Tue Dec 21 2021 Ildar Mulyukov <ildar@altlinux.ru> 0.3.3-alt1
- Initial build for Sisyphus
