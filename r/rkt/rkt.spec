%def_disable tpm

%global provider github.com
%global project coreos
%global repo rkt

%global provider_prefix %provider/%project/%repo
%global import_path %provider_prefix
%global commit 6de500a70706403c8c611d80491aea64019141b0
%global shortcommit %(c=%commit; echo ${c:0:7})

# valid values: src coreos host kvm fly
%global stage1_flavors host,fly
%global images_dir %_sharedstatedir/rkt/stage1-images

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/*

Name: rkt
Version: 1.29.0
Release: alt1.git.%shortcommit
Summary: A pod-native container engine for Linux
Group: Development/Other
License: ASL 2.0
Url: https://%provider_prefix
ExclusiveArch: %go_arches aarch64
Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: bc
BuildRequires: glibc-devel-static
BuildRequires: golang >= 1.6
BuildRequires: gperf
BuildRequires: gnupg
BuildRequires: libacl-devel
BuildRequires: libcap-devel
BuildRequires: libgcrypt-devel
BuildRequires: libseccomp-devel
BuildRequires: libmount-devel
BuildRequires: libxkbcommon-devel
%{?_enable_tpm:BuildRequires: libtrousers-devel}
BuildRequires: perl-Config-Tiny
BuildRequires: squashfs-tools
BuildRequires: systemd-devel >= 219
BuildRequires: systemd-container
BuildRequires: systemd-stateless
BuildRequires: /proc

Requires: iptables
Requires: systemd-container
Requires: systemd-stateless
Requires: systemd-utils
Requires: systemd
Requires: /sbin/sysctl

%description
%{summary}.  It is composable, secure, & built
on standards.  Some of rkt's key features and goals include:

* Pod-native: rkt's basic unit of execution is a pod, linking together
resources and user applications in a self-contained environment.

* Security: rkt is developed with a principle of "secure-by-default", and
includes a number of important security features like support for SELinux, TPM
measurement, and running app containers in hardware-isolated VMs.

* Composability: rkt is designed for first-class integration with init systems
(like systemd, upstart) and cluster orchestration tools (like Kubernetes and
Nomad), and supports swappable execution engines.

* Open standards and compatibility: rkt implements the appc specification,
supports the Container Networking Interface specification, and can run Docker
images and OCI images. Broader native support for OCI images and runtimes is
in development.

%prep
%setup -q

%build
%autoreconf

# ./configure flags: https://github.com/coreos/rkt/blob/master/Documentation/build-configure.md
%configure \
	%{subst_enable tpm} \
	--with-stage1-flavors=%stage1_flavors \
	--with-stage1-flavors-version-override=%version-%release \
	--with-stage1-default-images-directory=%images_dir \
	--with-stage1-default-location=%images_dir/stage1-host.aci

GOPATH="$GOPATH:%go_path:$(pwd)/Godeps/_workspace" %make all bash-completion manpages

%install
# install binaries
install -dp %buildroot{%_bindir,%images_dir,%_unitdir}
install -dp %buildroot%_sharedstatedir/%name

install -dp %buildroot{%_sysconfdir,/usr/lib}/%name/trustedkeys/prefix.d
install -dp %buildroot%_man1dir
install -p -m 644 dist/manpages/*.1 %buildroot%_man1dir

install -p -m 755 build-%name-%version/target/bin/%name %buildroot%_bindir
install -p -m 644 build-%name-%version/target/bin/stage1-*.aci %buildroot%images_dir

# install bash completion
install -dp %buildroot%_datadir/bash-completion/completions
install -p -m 644 dist/bash_completion/%name.bash %buildroot%_datadir/bash-completion/completions/%name

# install metadata unitfiles
install -p -m 644 dist/init/systemd/%name-gc.timer %buildroot%_unitdir
install -p -m 644 dist/init/systemd/%name-gc.service %buildroot%_unitdir
install -p -m 644 dist/init/systemd/%name-api.service %buildroot%_unitdir
install -p -m 644 dist/init/systemd/%name-api-tcp.socket %buildroot%_unitdir
install -p -m 644 dist/init/systemd/%name-metadata.socket %buildroot%_unitdir
install -p -m 644 dist/init/systemd/%name-metadata.service %buildroot%_unitdir

# setup of data directories
install -dp %buildroot%_sharedstatedir/%name/tmp
install -dp %buildroot%_sharedstatedir/%name/cas/{db,imagelocks,imageManifest,blob,tmp,tree,treestorelocks}
install -dp %buildroot%_sharedstatedir/%name/locks
install -dp %buildroot%_sharedstatedir/%name/pods/{embryo,prepare,prepared,run,garbage,exited-garbage}

touch %buildroot%_sharedstatedir/%name/cas/db/ql.db
touch %buildroot%_sharedstatedir/%name/cas/db/.34a8b4c1ad933745146fdbfef3073706ee571625

%pre
%_sbindir/groupadd -r -f %name 2>/dev/null ||:
%_sbindir/groupadd -r -f %name-admin 2>/dev/null ||:

%post
%post_service %name-metadata

%preun
%preun_service %name-metadata

%files
%doc CONTRIBUTING.md DCO LICENSE README.md Documentation/*
%_man1dir/*
%_bindir/%name
%dir %images_dir
%images_dir/stage1-*.aci
%_unitdir/%name-*
%_datadir/bash-completion/completions/%name
%dir /usr/lib/%name
%dir /usr/lib/%name/trustedkeys
%dir /usr/lib/%name/trustedkeys/prefix.d

%dir %attr(2750,root,rkt) %_sharedstatedir/%name
%dir %attr(2750,root,rkt) %_sharedstatedir/%name/tmp
%dir %attr(2770,root,rkt) %_sharedstatedir/%name/cas
%dir %attr(2770,root,rkt) %_sharedstatedir/%name/cas/db
%dir %attr(2770,root,rkt) %_sharedstatedir/%name/cas/imagelocks
%dir %attr(2770,root,rkt) %_sharedstatedir/%name/cas/imageManifest
%dir %attr(2770,root,rkt) %_sharedstatedir/%name/cas/blob
%dir %attr(2770,root,rkt) %_sharedstatedir/%name/cas/tmp
%dir %attr(0700,root,rkt) %_sharedstatedir/%name/cas/tree
%dir %attr(0700,root,rkt) %_sharedstatedir/%name/cas/treestorelocks
%dir %attr(2750,root,rkt) %_sharedstatedir/%name/locks
%dir %attr(2750,root,rkt) %_sharedstatedir/%name/pods
%dir %attr(2750,root,rkt) %_sharedstatedir/%name/pods/embryo
%dir %attr(2750,root,rkt) %_sharedstatedir/%name/pods/prepare
%dir %attr(2750,root,rkt) %_sharedstatedir/%name/pods/prepared
%dir %attr(2750,root,rkt) %_sharedstatedir/%name/pods/run
%dir %attr(2750,root,rkt) %_sharedstatedir/%name/pods/exited-garbage
%dir %attr(2750,root,rkt) %_sharedstatedir/%name/pods/garbage
%dir %config %attr(0775,root,rkt-admin) %_sysconfdir/%name
%dir %config %attr(0775,root,rkt-admin) %_sysconfdir/%name/trustedkeys
%dir %config %attr(0775,root,rkt-admin) %_sysconfdir/%name/trustedkeys/prefix.d

%attr(0660,root,rkt) %_sharedstatedir/%name/cas/db/ql.db
%attr(0660,root,rkt) %_sharedstatedir/%name/cas/db/.34a8b4c1ad933745146fdbfef3073706ee571625

%changelog
* Tue Feb 06 2018 Alexey Shabalin <shaba@altlinux.ru> 1.29.0-alt1.git.6de500a
- Initial package
