%define _unpackaged_files_terminate_build 1
%define _localstatedir %_var

%def_disable check
%def_without test_keys
%def_without selinux

%global provider        github
%global provider_tld    com
%global project         snapcore
%global repo            snapd
# https://github.com/snapcore/snapd
%global provider_prefix %provider.%provider_tld/%project/%repo
%global import_path     %provider_prefix

%global snappy_svcs      snapd.service snapd.socket snapd.autoimport.service snapd.seeded.service snapd.mounts.target snapd.mounts-pre.target
%global snappy_user_svcs snapd.session-agent.service snapd.session-agent.socket

# Until we have a way to add more extldflags to gobuild macro...
%define gobuild_static(o:) go build -buildmode pie -compiler gc -tags="rpm_crashtraceback ${BUILDTAGS:-}" -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') -linkmode external -extldflags '${LDFLAGS:-} -static'" -a -v -x %{?**};

%define gobuild(o:) go build -buildmode pie -compiler gc -tags="rpm_crashtraceback ${BUILDTAGS:-}" -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') -linkmode external -extldflags '${LDFLAGS:-}'" -a -v -x %{?**};

# Compat path macros
%{!?_environmentdir: %global _environmentdir /lib/environment.d}
%{!?_systemdgeneratordir: %global _systemdgeneratordir /lib/systemd/system-generators}
%{!?_systemd_system_env_generator_dir: %global _systemd_system_env_generator_dir /lib/systemd/system-environment-generators}
%{!?_tmpfilesdir: %global _tmpfilesdir /lib/tmpfiles.d}
#%%define _libexecdir %%_prefix/libexec

Name: snapd
Version: 2.58.3
Release: alt1
Summary: A transactional software package manager
License: GPLv3
Group: System/Configuration/Other
Url: https://%provider_prefix
Source0: https://%provider_prefix/releases/download/%version/%{name}_%version.no-vendor.tar.xz
Source1: https://%provider_prefix/releases/download/%version/%{name}_%version.only-vendor.tar.xz

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang rpm-build-systemd
BuildRequires: libsystemd-devel
# for generate manpages
BuildRequires: /proc
Requires: snap-confine = %EVR
Requires: squashfs-tools

#Requires: squashfuse fuse

%if_with selinux
# Force the SELinux module to be installed
Requires: %name-selinux = %version-%release
%endif

%description
Snappy is a modern, cross-distribution, transactional package manager
designed for working with self-contained, immutable packages.

%package -n snap-confine
Summary: Confinement system for snap applications
Group: System/Configuration/Other
License: GPLv3
BuildRequires: gettext
BuildRequires: gnupg
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libcap)
BuildRequires: pkgconfig(libseccomp)
%if_with selinux
BuildRequires: pkgconfig(libselinux)
%endif
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(udev)
BuildRequires: libxfs-devel
BuildRequires: glibc-devel-static
BuildRequires: %_bindir/rst2man
BuildRequires: %_bindir/shellcheck

%description -n snap-confine
This package is used internally by snapd to apply confinement to
the started snap applications.

%if_with selinux
%package selinux
Summary: SELinux module for snapd
License: GPLv2+
Group: System/Configuration/Other
BuildArch: noarch
BuildRequires: selinux-policy, selinux-policy-devel
Requires(post): selinux-policy-base
Requires(post): policycoreutils
Requires:  libselinux-utils

%description selinux
This package provides the SELinux policy module to ensure snapd
runs properly under an environment with SELinux enabled.
%endif

%prep
%setup -D -b 1

# We don't want/need squashfuse in the rpm
sed -e 's:_ "github.com/snapcore/squashfuse"::g' -i systemd/systemd.go
# We don't need the snapcore fork for bolt - it is just a fix on ppc
#sed -e "s:github.com/snapcore/bolt:github.com/boltdb/bolt:g" -i advisor/*.go errtracker/*.go

sed -e "s:/usr/lib/environment.d/:/lib/environment.d/:g" -i data/systemd-env/Makefile
sed -e 's:${prefix}/lib/systemd/system-environment-generators:/lib/systemd/system-environment-generators:g' -i cmd/configure.ac

%build
# Build snapd
mkdir -p src/github.com/snapcore
ln -s ../../../ src/github.com/snapcore/snapd

#export BUILDDIR="$PWD/.gopath"
#export GOPATH="$BUILDDIR:%go_path"

export IMPORT_PATH="%import_path"
export GOPATH=$(pwd):%go_path
export GO111MODULE=off

# Generate version files
./mkversion.sh "%version-%release"

BUILDTAGS="nosecboot"

# We have to build snapd first to prevent the build from
# building various things from the tree without additional
# set tags.
%gobuild -o bin/snapd $GOFLAGS %import_path/cmd/snapd
BUILDTAGS="${BUILDTAGS} nomanagers"
%gobuild -o bin/snap $GOFLAGS %import_path/cmd/snap
%gobuild -o bin/snap-failure $GOFLAGS %import_path/cmd/snap-failure

# To ensure things work correctly with base snaps,
# snap-exec, snap-update-ns, and snapctl need to be built statically
%gobuild_static -o bin/snap-exec $GOFLAGS %import_path/cmd/snap-exec
%gobuild_static -o bin/snap-update-ns $GOFLAGS %import_path/cmd/snap-update-ns
%gobuild_static -o bin/snapctl $GOFLAGS %import_path/cmd/snapctl

%ifarch %ix86
export CGO_CFLAGS="$CGO_CFLAGS -fno-stack-protector"
%endif
%gobuild -o bin/snap-seccomp $GOFLAGS %import_path/cmd/snap-seccomp

%if_with selinux
    # Build SELinux module
    cd ./data/selinux
    # pass M4PARAM in env instead of as an override, so that make can still
    # manipulate it freely, for more details see:
    # https://www.gnu.org/software/make/manual/html_node/Override-Directive.html
    M4PARAM="$M4PARAM" make SHARE="%_datadir" TARGETS="snappy"
%endif

# Build snap-confine
pushd ./cmd
%autoreconf
# FIXME: add --enable-caps-over-setuid as soon as possible (setuid discouraged!)
%configure \
    --disable-apparmor \
%if_with selinux
    --enable-selinux \
%endif
    --libexecdir=%_libexecdir/snapd/ \
    --enable-nvidia-biarch \
    %if %_lib == lib64
    --with-32bit-libdir=%prefix/lib \
    %endif
    --with-snap-mount-dir=%_sharedstatedir/snapd/snap

%make_build
popd

# Build systemd units, dbus services, and env files
pushd ./data
make BINDIR="%_bindir" LIBEXECDIR="%_libexecdir" DATADIR="%_datadir" \
     SYSTEMDSYSTEMUNITDIR="%_unitdir" SYSTEMDUSERUNITDIR="%_userunitdir" \
     TMPFILESDIR="%_tmpfilesdir" \
     SNAP_MOUNT_DIR="%_sharedstatedir/snapd/snap" \
     SNAPD_ENVIRONMENT_FILE="%_sysconfdir/sysconfig/snapd"
popd

%install
install -d -p %buildroot%_bindir
install -d -p %buildroot%_libexecdir/snapd
install -d -p %buildroot%_man8dir
install -d -p %buildroot%_environmentdir
install -d -p %buildroot%_systemdgeneratordir
install -d -p %buildroot%_systemd_system_env_generator_dir
install -d -p %buildroot%_tmpfilesdir
install -d -p %buildroot%_unitdir
install -d -p %buildroot%_userunitdir
install -d -p %buildroot%_sysconfdir/profile.d
install -d -p %buildroot%_sysconfdir/sysconfig
install -d -p %buildroot%_sharedstatedir/snapd/assertions
install -d -p %buildroot%_sharedstatedir/snapd/cookie
install -d -p %buildroot%_sharedstatedir/snapd/dbus-1/services
install -d -p %buildroot%_sharedstatedir/snapd/dbus-1/system-services
install -d -p %buildroot%_sharedstatedir/snapd/desktop/applications
install -d -p %buildroot%_sharedstatedir/snapd/device
install -d -p %buildroot%_sharedstatedir/snapd/hostfs
install -d -p %buildroot%_sharedstatedir/snapd/inhibit
install -d -p %buildroot%_sharedstatedir/snapd/lib/gl
install -d -p %buildroot%_sharedstatedir/snapd/lib/gl32
install -d -p %buildroot%_sharedstatedir/snapd/lib/glvnd
install -d -p %buildroot%_sharedstatedir/snapd/lib/vulkan
install -d -p %buildroot%_sharedstatedir/snapd/mount
install -d -p %buildroot%_sharedstatedir/snapd/seccomp/bpf
install -d -p %buildroot%_sharedstatedir/snapd/snaps
install -d -p %buildroot%_sharedstatedir/snapd/snap/bin
install -d -p %buildroot%_cachedir
install -d -p %buildroot%_cachedir/snapd
install -d -p %buildroot%_datadir/polkit-1/actions
%if_with selinux
install -d -p %buildroot%_datadir/selinux/devel/include/contrib
install -d -p %buildroot%_datadir/selinux/packages
%endif

# Install snap and snapd
install -p -m 0755 bin/snap %buildroot%_bindir
install -p -m 0755 bin/snap-exec %buildroot%_libexecdir/snapd
install -p -m 0755 bin/snap-failure %buildroot%_libexecdir/snapd
install -p -m 0755 bin/snapd %buildroot%_libexecdir/snapd
install -p -m 0755 bin/snap-update-ns %buildroot%_libexecdir/snapd
install -p -m 0755 bin/snap-seccomp %buildroot%_libexecdir/snapd
# Ensure /usr/bin/snapctl is a symlink to /usr/libexec/snapd/snapctl
install -p -m 0755 bin/snapctl %buildroot%_libexecdir/snapd/snapctl
ln -sfr %buildroot%_libexecdir/snapd/snapctl %buildroot%_bindir/snapctl

%if_with selinux
# Install SELinux module
install -p -m 0644 data/selinux/snappy.if %buildroot%_datadir/selinux/devel/include/contrib
install -p -m 0644 data/selinux/snappy.pp.bz2 %buildroot%_datadir/selinux/packages
%endif

# Install snap(8) man page
bin/snap help --man > %buildroot%_mandir/man8/snap.8

# Install the "info" data file with snapd version
install -m 644 -D data/info %buildroot%_libexecdir/snapd/info

# Install bash completion for "snap"
install -m 644 -D data/completion/bash/snap %buildroot%_datadir/bash-completion/completions/snap
install -m 644 -D data/completion/bash/complete.sh %buildroot%_libexecdir/snapd
install -m 644 -D data/completion/bash/etelpmoc.sh %buildroot%_libexecdir/snapd
# Install zsh completion for "snap"
install -d -p %buildroot%_datadir/zsh/site-functions
install -m 644 -D data/completion/zsh/_snap %buildroot%_datadir/zsh/site-functions/_snap

# Install snap-confine
pushd cmd
%makeinstall_std
# Undo the 0111 permissions, they are restored in the files section
chmod 0755 %buildroot%_sharedstatedir/snapd/void
# We don't use AppArmor
rm -rfv %buildroot%_sysconfdir/apparmor.d
# ubuntu-core-launcher is dead
rm -fv %buildroot%_bindir/ubuntu-core-launcher
popd

# Install all systemd and dbus units, and env files
pushd data
%makeinstall_std BINDIR="%_bindir" LIBEXECDIR="%_libexecdir" DATADIR="%_datadir" \
              SYSTEMDSYSTEMUNITDIR="%_unitdir" SYSTEMDUSERUNITDIR="%_userunitdir" \
              TMPFILESDIR="%_tmpfilesdir" \
              SNAP_MOUNT_DIR="%_sharedstatedir/snapd/snap" \
              SNAPD_ENVIRONMENT_FILE="%_sysconfdir/sysconfig/snapd"
popd

# Remove snappy core specific units
rm -fv %buildroot%_unitdir/snapd.system-shutdown.service
rm -fv %buildroot%_unitdir/snapd.snap-repair.*
rm -fv %buildroot%_unitdir/snapd.core-fixup.*
rm -fv %buildroot%_unitdir/snapd.recovery-chooser-trigger.service

# Remove snappy core specific scripts and binaries
rm -f %buildroot%_libexecdir/snapd/snapd.core-fixup.sh
rm -f %buildroot%_libexecdir/snapd/system-shutdown

# Remove snapd apparmor service
rm -f %buildroot%_unitdir/snapd.apparmor.service
rm -f %buildroot%_libexecdir/snapd/snapd-apparmor

# Remove prompt services
rm %buildroot%_unitdir/snapd.aa-prompt-listener.service
rm %buildroot%_userunitdir/snapd.aa-prompt-ui.service
rm %buildroot%_datadir/dbus-1/services/io.snapcraft.Prompt.service

# Install Polkit configuration
install -m 644 -D data/polkit/io.snapcraft.snapd.policy %buildroot%_datadir/polkit-1/actions

# Disable re-exec by default
echo 'SNAP_REEXEC=0' > %buildroot%_sysconfdir/sysconfig/snapd

# Create state.json and the README file to be ghosted
touch %buildroot%_sharedstatedir/snapd/state.json
touch %buildroot%_sharedstatedir/snapd/snap/README

# When enabled, create a symlink for /snap to point to /var/lib/snapd/snap
%if_with snap_symlink
ln -sr %buildroot%_sharedstatedir/snapd/snap %buildroot/snap
%endif

%check
for binary in snap-exec snap-update-ns snapctl; do
    ldd bin/$binary 2>&1 | grep 'not a dynamic executable'
done

# snapd tests
export IMPORT_PATH="%import_path"
export GOPATH=$(pwd):%go_path
export GO111MODULE=off
%gotest %import_path/...

# snap-confine tests (these always run!)
pushd ./cmd
make check
popd

%post
%systemd_post %snappy_svcs
%systemd_user_post %snappy_user_svcs

# If install, test if snapd socket and timer are enabled.
# If enabled, then attempt to start them. This will silently fail
# in chroots or other environments where services aren't expected
# to be started.
if [ $1 -eq 1 ] ; then
   if systemctl -q is-enabled snapd.socket > /dev/null 2>&1 ; then
      systemctl start snapd.socket > /dev/null 2>&1 || :
   fi
fi

%preun
%systemd_preun %snappy_svcs
%systemd_user_preun %snappy_user_svcs

# Remove all Snappy content if snapd is being fully uninstalled
if [ $1 -eq 0 ]; then
   %_libexecdir/snapd/snap-mgmt --purge || :
fi

%postun
%systemd_postun_with_restart %snappy_svcs
%systemd_user_postun_with_restart %snappy_user_svcs

%if_with selinux
%pre selinux
%selinux_relabel_pre

%post selinux
%selinux_modules_install %_datadir/selinux/packages/snappy.pp.bz2
%selinux_relabel_post

%postun selinux
%selinux_modules_uninstall snappy
if [ $1 -eq 0 ]; then
    %selinux_relabel_post
fi
%endif

%files
%doc README.md docs/*
%_bindir/snap
%_bindir/snapctl
%_environmentdir/990-snapd.conf
%dir %_libexecdir/snapd
%_libexecdir/snapd/snapctl
%_libexecdir/snapd/snapd
%_libexecdir/snapd/snap-exec
%_libexecdir/snapd/snap-failure
%_libexecdir/snapd/info
%_libexecdir/snapd/snap-mgmt
%if_with selinux
%_libexecdir/snapd/snap-mgmt-selinux
%endif
%_mandir/man8/snap.8*
%_datadir/applications/snap-handle-link.desktop
%_datadir/bash-completion/completions/snap
%_libexecdir/snapd/complete.sh
%_libexecdir/snapd/etelpmoc.sh
%_datadir/zsh/site-functions/_snap
%_libexecdir/snapd/snapd.run-from-snap
%attr(0755,root,root) %_sysconfdir/profile.d/snapd.sh
%_mandir/man8/snapd-env-generator.8*
%_systemd_system_env_generator_dir/snapd-env-generator
%_datadir/fish/vendor_conf.d/snapd.fish
%_datadir/snapd/snapcraft-logo-bird.svg
%_unitdir/snapd.socket
%_unitdir/snapd.service
%_unitdir/snapd.autoimport.service
%_unitdir/snapd.failure.service
%_unitdir/snapd.seeded.service
%_unitdir/snapd.mounts.target
%_unitdir/snapd.mounts-pre.target
%_userunitdir/snapd.session-agent.service
%_userunitdir/snapd.session-agent.socket
%_tmpfilesdir/snapd.conf
%_datadir/dbus-1/services/io.snapcraft.Launcher.service
%_datadir/dbus-1/services/io.snapcraft.SessionAgent.service
%_datadir/dbus-1/services/io.snapcraft.Settings.service
%_datadir/dbus-1/session.d/snapd.session-services.conf
%_datadir/dbus-1/system.d/snapd.system-services.conf
%_datadir/polkit-1/actions/io.snapcraft.snapd.policy
%_datadir/applications/io.snapcraft.SessionAgent.desktop
%_sysconfdir/xdg/autostart/snap-userd-autostart.desktop
%config(noreplace) %_sysconfdir/sysconfig/snapd
%dir %_sharedstatedir/snapd
%dir %_sharedstatedir/snapd/assertions
%dir %_sharedstatedir/snapd/cookie
%dir %_sharedstatedir/snapd/dbus-1
%dir %_sharedstatedir/snapd/dbus-1/services
%dir %_sharedstatedir/snapd/dbus-1/system-services
%dir %_sharedstatedir/snapd/desktop
%dir %_sharedstatedir/snapd/desktop/applications
%dir %_sharedstatedir/snapd/device
%dir %_sharedstatedir/snapd/hostfs
%dir %_sharedstatedir/snapd/inhibit
%dir %_sharedstatedir/snapd/lib
%dir %_sharedstatedir/snapd/lib/gl
%dir %_sharedstatedir/snapd/lib/gl32
%dir %_sharedstatedir/snapd/lib/glvnd
%dir %_sharedstatedir/snapd/lib/vulkan
%dir %_sharedstatedir/snapd/mount
%dir %_sharedstatedir/snapd/seccomp
%dir %_sharedstatedir/snapd/seccomp/bpf
%dir %_sharedstatedir/snapd/snaps
%dir %_sharedstatedir/snapd/snap
%ghost %dir %_sharedstatedir/snapd/snap/bin
%dir %_cachedir/snapd
%ghost %_sharedstatedir/snapd/state.json
%ghost %_sharedstatedir/snapd/snap/README
%if_with snap_symlink
/snap
%endif

%files -n snap-confine
%doc cmd/snap-confine/PORTING
%dir %_libexecdir/snapd
# For now, we can't use caps
# FIXME: Switch to "%%attr(0755,root,root) %%caps(cap_sys_admin=pe)" asap!
%attr(4711,root,root) %_libexecdir/snapd/snap-confine
%_libexecdir/snapd/snap-device-helper
%_libexecdir/snapd/snap-discard-ns
%_libexecdir/snapd/snap-gdb-shim
%_libexecdir/snapd/snap-gdbserver-shim
%_libexecdir/snapd/snap-seccomp
%_libexecdir/snapd/snap-update-ns
%_mandir/man8/snap-confine.8*
%_mandir/man8/snap-discard-ns.8*
%_systemdgeneratordir/snapd-generator
%attr(0711,root,root) %_sharedstatedir/snapd/void

%if_with selinux
%files selinux
%doc data/selinux/COPYING
%doc data/selinux/README.md
%_datadir/selinux/packages/snappy.pp.bz2
%_datadir/selinux/devel/include/contrib/snappy.if
%endif

%changelog
* Wed Mar 22 2023 Alexey Shabalin <shaba@altlinux.org> 2.58.3-alt1
- 2.58.3

* Wed Dec 21 2022 Alexey Shabalin <shaba@altlinux.org> 2.58-alt1
- 2.58 (Fixes: CVE 2022-3328)

* Mon Jun 06 2022 Alexey Shabalin <shaba@altlinux.org> 2.56-alt1
- 2.56

* Sun Feb 20 2022 Alexey Shabalin <shaba@altlinux.org> 2.54.3-alt1
- 2.54.3 (Fixes: CVE-2021-44730, CVE-2021-44731, CVE-2021-4120)

* Sat Dec 25 2021 Alexey Shabalin <shaba@altlinux.org> 2.54.1-alt1
- 2.54.1
- /etc/profile.d/snapd.sh: made executable (ALT #41625)

* Wed Dec 15 2021 Alexey Shabalin <shaba@altlinux.org> 2.53.4-alt1
- 2.53.4
- Add altlinux support (ALT #41518)

* Mon Nov 01 2021 Alexey Shabalin <shaba@altlinux.org> 2.53.1-alt1
- 2.53.1.

* Thu Sep 02 2021 Alexey Shabalin <shaba@altlinux.org> 2.51.7-alt1
- 2.51.7.

* Mon Aug 23 2021 Alexey Shabalin <shaba@altlinux.org> 2.51.6-alt1
- Initial build for ALT
