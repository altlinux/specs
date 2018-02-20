Name: casync
Version: 2.0.101.git8595b4d
Release: alt1

Summary: Content Addressable Data Synchronizer

Group: Networking/File transfer
License: LGPLv2+
URL: https://github.com/systemd/casync

Source: %name-%version.tar
# git://git.altlinux.org/gears/c/casync.git
Patch: %name-%version-%release.patch

%def_enable fuse
%def_enable selinux
%def_enable udev
%def_enable man

%define meson_subst_bool() %{expand:%%{?_enable_%{1}:-D%{1}=true}%%{?_disable_%{1}:-D%{1}=false}}

BuildRequires: meson >= 0.42.0
BuildRequires: gcc
BuildRequires: pkgconfig(liblzma) >= 5.1.0
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libcurl) >= 7.32.0
BuildRequires: pkgconfig(libssl)
BuildRequires: libacl-devel
%{?_enable_fuse:BuildRequires: pkgconfig(fuse) >= 2.6}
%{?_enable_selinux:BuildRequires: pkgconfig(libselinux)}
%{?_enable_udev:BuildRequires: pkgconfig(libudev)}
%{?_enable_man:BuildRequires: python3-module-sphinx}
%{?_enable_man:BuildRequires: python3-module-sphinx-sphinx-build-symlink}
# for tests
%{?_enable_fuse:BuildRequires: fuse}
BuildRequires: rsync

%description
casync provides a way to efficiently transfer files which change over
time over the internet. It will split a given set into a git-inspired
content-addressable set of smaller compressed chunks, which can then
be conveniently transferred using HTTP. On the receiving side those
chunks will be uncompressed and merged together to recreate the
original data. When the original data is modified, only the new chunks
have to be transferred during an update.

%prep
%setup
%patch -p1

%build
%meson \
    --wrap-mode=nodownload \
    %{meson_subst_bool fuse} \
    %{meson_subst_bool selinux} \
    %{meson_subst_bool udev} \
    %{meson_subst_bool man} \
    #
%meson_build

%check
#export LC_ALL=en_US.UTF-8
export LC_CTYPE=en_US.UTF-8

# Meson-related macros in ALT are broken!
# (ok, they just make little sense for the purpose of packaging)

# Some of them are actually ninja-build macros and should belong to that package.
# Really. They already do.

# XXX: test 05 (nbd) fails in hasher (same reason?)
#meson_test \
meson test -C %_target_platform \
%ifndef __BTE
    test-script.sh \
    test-script-sha256.sh \
    test-script-gzip.sh \
    test-script-xz.sh \
    test-nbd.sh \
    test-fuse.sh \
%endif
    test-cachunk \
    test-cachunker \
    test-cachunker-histogram \
    test-cadigest \
    test-caencoder \
    test-camakebst \
    test-caorigin \
    test-casync \
    test-cautil \
    test-util \
#

%install
%meson_install

%files
%doc README.md TODO NEWS
%_bindir/casync
%dir %_libexecdir/casync
%dir %_libexecdir/casync/protocols
%_libexecdir/casync/protocols/casync-ftp
%_libexecdir/casync/protocols/casync-http
%_libexecdir/casync/protocols/casync-https
%_libexecdir/casync/protocols/casync-sftp
%_man1dir/casync.1*
%_udevrulesdir/75-casync.rules

%changelog
* Tue Feb 20 2018 Arseny Maslennikov <arseny@altlinux.org> 2.0.101.git8595b4d-alt1
- 2-25-git6daefa8 -> 2-101-git8595b4d.
- Built with libudev to leverage new functionality.
- Included upstream NEWS in the package.

* Sat Oct 07 2017 Arseny Maslennikov <arseny@altlinux.org> 2.0.25.git6daefa8-alt1
- Initial build for ALT Sisyphus.

