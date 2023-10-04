Name:     vml
Version:  0.1.9
Release:  alt2

Summary:  Tool for easily and transparently work with qemu virtual machines
License:  MIT
Group:    Emulators
Url:      https://github.com/Obirvalger/vml

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires: libssl-devel
BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

Requires: rsync socat openssh-clients /usr/bin/kvm cloud-utils-cloud-localds

ExclusiveArch: aarch64 x86_64

%description
VML is a tool for easily and transparently work with qemu virtual machines.
Virtual machines present as directories with vml.toml files in it. VML is able
to initialize images with cloud-init. Virtual machines with ALT, Centos,
Debian, Fedora, openSUSE and Ubuntu could be created with just one command.

%prep
%setup

%build
export RUSTFLAGS="${RUSTFLAGS} -g"
%ifarch ppc64le
cargo build --no-default-features --features=native-tls --release %{?_smp_mflags} --offline
%else
cargo build --release %{?_smp_mflags} --offline
%endif

%install
%rust_install
install -Dm 644 files/configs/config.toml %buildroot%_sysconfdir/%name/config.toml
install -Dm 644 files/configs/images.toml %buildroot%_sysconfdir/%name/images.toml

mkdir -p %buildroot%_datadir/zsh/site-functions
%buildroot%_bindir/%name completion zsh > %buildroot%_datadir/zsh/site-functions/_%name
mkdir -p %buildroot%_datadir/bash-completion/completions
%buildroot%_bindir/%name completion bash > %buildroot%_datadir/bash-completion/completions/%name
mkdir -p %buildroot%_datadir/fish/vendor_completions.d
%buildroot%_bindir/%name completion fish > %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%files
%_bindir/%name
%_sysconfdir/%name
%config(noreplace) %attr(0644,root,root) %_sysconfdir/%name/config.toml
%config(noreplace) %attr(0644,root,root) %_sysconfdir/%name/images.toml
%_datadir/zsh/site-functions/_%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%doc doc *.md

%changelog
* Wed Oct 04 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.9-alt2
- Reduce transitive requires
- Set ExclusiveArch

* Tue Jun 06 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.9-alt1
- Fix updating images config
- Fix creating ~ with rsync-to
- Add clean command to prepare vm be used as image
- Add check to rsync commands
- Setup sudo for gui user
- Update ubuntu and fedora images
- Remove outdated images

* Tue Oct 04 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.8-alt1
- Fix vml show --all wrong state output
- Fix version show
- Add option to set ssh user on creation of a vm
- Add properties flag to pass vm properties on creation
- Add Rocky Linux image
- Add centos-9-stream
- Add AlmaLinux

* Mon Jun 27 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.7-alt1
- Improve work with gui images

* Mon Jun 20 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.6-alt1
- Add support of multiple arches

* Thu Dec 30 2021 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.5-alt1
- Fix finding running vms after qemu update
- Create openssh config for vms

* Mon Nov 15 2021 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.4-alt1
- Add more readable json output to show command
- Add ansible dynamic inventory - files/scripts/inventory.py
- Use anyhow and thiserror to get more readable error messages

* Mon Sep 06 2021 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.3-alt1
- Update images

* Wed Jun 23 2021 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.2-alt1
- 0.1.2

* Mon Apr 12 2021 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.1-alt1
- 0.1.1

* Mon Mar 29 2021 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
