%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lfs=relaxed

%define _pseudouser_user     _greeter
%define _pseudouser_group    _greeter
%define _pseudouser_home     %_var/empty

Name: greetd
Version: 0.8.0
Release: alt2
Summary: Generic greeter daemon
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://git.sr.ht/~kennylevinsen/greetd

Source: %name-%version.tar
Source1: %name-%version-vendor.tar

# adapted pam file from Arch
Source2: %name.pam

Patch1: greetd-alt-compat.patch
Patch3500: 0001-updated-vendored-libc-crate-for-LoongArch-support.patch

BuildRequires: /proc
BuildRequires: rust
BuildRequires: rust-cargo
BuildRequires: libpam-devel
BuildRequires: scdoc

%description
greetd is a minimal and flexible login manager daemon
that makes no assumptions about what you want to launch.

%prep
%setup -a1
%patch1 -p1
%patch3500 -p1

mkdir -p .cargo
cat > .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
cargo build \
	--release \
	%{?_smp_mflags} \
	--offline \
	%nil

pushd man
for i in *.scd
do
	scdoc < "$i" > "$(basename "$i" .scd)".roff
done
popd

%install
install -Dm755 target/release/greetd %buildroot%_bindir/greetd
install -Dm755 target/release/agreety %buildroot%_bindir/agreety

pushd man
for s in 1 5 7
do
	install -d "%buildroot%_mandir/man$s"
	for i in *-$s.roff
	do
		install -m755 "$i" "%buildroot%_mandir/man$s/${i%-*}.$s"
	done
done
popd

install -Dm644 greetd.service %buildroot%_unitdir/greetd.service

echo 'u _greeter - "greetd greeter user" - /bin/bash' |
	install -Dm644 /dev/stdin %buildroot/lib/sysusers.d/greetd.conf

install -Dm644 %SOURCE2 %buildroot%_sysconfdir/pam.d/greetd
install -Dm644 config.toml %buildroot%_sysconfdir/greetd/config.toml

%pre
/usr/sbin/groupadd -r -f %_pseudouser_group ||:
/usr/sbin/useradd -g %_pseudouser_group -c 'greetd greeter user' \
	-d %_pseudouser_home -s /dev/null -r %_pseudouser_user >/dev/null 2>&1 ||:

%files
%doc LICENSE
%doc README.md
%dir %_sysconfdir/greetd
%config(noreplace) %_sysconfdir/greetd/config.toml
%config(noreplace) %_sysconfdir/pam.d/greetd
%_unitdir/greetd.service
/lib/sysusers.d/greetd.conf
%_bindir/*
%_man1dir/*.1*
%_man5dir/*.5*
%_man7dir/*.7*

%changelog
* Tue Oct 31 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.8.0-alt2
- NMU: support LoongArch architecture

* Tue Feb 15 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.0-alt1
- Updated to upstream version 0.8.0.

* Fri Mar 19 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.0-alt1
- Initial build for ALT.
