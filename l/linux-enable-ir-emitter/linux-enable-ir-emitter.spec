Name: linux-enable-ir-emitter
Version: 7.0.0
Release: alt1.beta2

Summary: Enables infrared cameras that are not directly enabled out-of-the box
License: MIT
Group: System/Configuration/Hardware

Url: https://github.com/EmixamPP/linux-enable-ir-emitter
Vcs: https://github.com/EmixamPP/linux-enable-ir-emitter.git
Source0: %name-%version.tar
Source1: vendor-%version.tar
Source2: linux-enable-ir-emitter.service.in
Source3: linux-enable-ir-emitter.sh.in
SOurce4: linux-enable-ir-emitter.rules.in
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo rustc
BuildRequires: clang-devel

%define _unpackaged_files_terminate_build 1

%define username e-ir-emitter
%define sysuser_dir %_localstatedir/%name/
%define bin_install_path %_usr/libexec

%description
This package contains linux-enable-ir-emitter utility that provides support
for infrared cameras that are not directly enabled out-of-the box on Linux
(at the very least, the kernel must recognize your infrared camera).
The purpose of this repository is to enable the emitter when the infrared camera
is invoked.
linux-enable-ir-emitter can automatically configure almost any UVC infrared
camera.

%prep
%setup
tar xf %SOURCE1
%patch -p1

sed -i 's;@SYS_USER_DIR@;%sysuser_dir;' .cargo/config.toml

mkdir -p .cargo
cat >> .cargo/config.toml <<EOF

[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[install]
root = "%buildroot%_prefix"

[profile.release]
strip = false

[source."git+https://github.com/EmixamPP/ansipix.git?rev=4e29437ea3fc23ea451a50b90cafdf7c519ffacb"]
git = "https://github.com/EmixamPP/ansipix.git"
rev = "4e29437ea3fc23ea451a50b90cafdf7c519ffacb"
replace-with = "vendored-sources"
EOF

%build
%rust_build
sed -e 's;@USERNAME@;%username;' -e 's;@E_IR_EMITTER_PATH@;%bin_install_path;' >%name.service  < %SOURCE2
sed -e 's;@USERNAME@;%username;' -e 's;@E_IR_EMITTER_PATH@;%bin_install_path;' >%name.sh  < %SOURCE3
sed 's;@E_IR_EMITTER_PATH@;%bin_install_path;' >%name.rules  < %SOURCE4

%install
%rust_install
# Move binary to %bin_install_path
mkdir -p %buildroot%bin_install_path/
mv %buildroot%_bindir/%name %buildroot%bin_install_path/

install -pD -m755 %name.sh %buildroot%_bindir/%name

install -pD -m644 %name.service %buildroot%_unitdir/%name.service
mkdir -p %buildroot%sysuser_dir/log

install -pD -m644 %name.rules %buildroot%_datadir/polkit-1/rules.d/%name.rules

%pre
getent passwd %username >/dev/null || \
	useradd -r -U -d %sysuser_dir -s /dev/null -c 'User for %name' %username >/dev/null 2>&1 ||:
id -Gn %username | grep -qsw video || usermod -a -G video %username >/dev/null 2>&1 ||:

%files
%doc CHANGELOG.md README.md LICENSE CONTRIBUTING.md
%_bindir/*
%bin_install_path/*
%_unitdir/%name.service
%_datadir/polkit-1/rules.d/%name.rules
%attr(755,%username,%username) %sysuser_dir

%changelog
* Mon Jul 06 2026 Mikhail Efremov <sem@altlinux.org> 7.0.0-alt1.beta2
- Initial build.
