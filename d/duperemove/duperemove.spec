# SPEC file for duperemove package

Name:    duperemove
Version: 0.13
Release: alt1

Summary: tool for deduping file system extents

License: %gpl2only
Group:   File tools
URL:     http://markfasheh.github.io/duperemove/
#URL:    https://github.com/markfasheh/duperemove

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue Oct 15 2019
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 pkg-config python-base python-modules python3 python3-base python3-dev ruby ruby-stdlibs sh4
BuildRequires: glib2-devel libsqlite3-devel

%description
Duperemove  is a simple tool for finding duplicated extents
and submitting them for deduplication. When given a list of
files it will hash their contents on a block by block basis
and compare those hashes to each other, finding and
categorizing extents that match each other. When given
the -d option, duperemove will submit those extents for
deduplication using the Linux kernel extent-same ioctl.

Duperemove can store the hashes it computes in a 'hashfile'.
If given an existing hashfile, duperemove will only compute
hashes for those files which have changed since the last
run. Thus you can run duperemove repeatedly on your data
as it changes, without having to re-checksum unchanged data.

Duperemove can also take input from the fdupes program.


%prep
%setup -q
%patch0 -p1

mv -f -- LICENSE LICENSE.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/LICENSE) LICENSE

%build
%make_build

%install
%make_install \
    DESTDIR=%buildroot \
    PREFIX=%_usr \
    install

%files
%doc README.md LICENSE.xxhash
%doc --no-dereference LICENSE

%_bindir/%name
%_bindir/btrfs-extent-same
%_bindir/show-shared-extents
%_bindir/hashstats

%_man8dir/%{name}.*
%_man8dir/btrfs-extent-same.*
%_man8dir/show-shared-extents.*
%_man8dir/hashstats.*

%changelog
* Sat Oct 21 2023 Nikolay A. Fetisov <naf@altlinux.org> 0.13-alt1
- New version

* Mon Sep 11 2023 Nikolay A. Fetisov <naf@altlinux.org> 0.12-alt1
- New version
  - duplication lookup is now based on extents
  - new hashfile format
  - batching has been implemented to use on large dataset
  - all hash algorithm has been removed and replaced by xxh128

* Sat Nov 06 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.11.3-alt1
- New version

* Thu Mar 18 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.11.1-alt2.git0df677ea
- Update to the current development state, commit v0.11.beta4-117-g0df677e
  - Fix build with GCC 10.2
  - Impove hashing performance
  - Update documentation

* Tue Oct 15 2019 Nikolay A. Fetisov <naf@altlinux.org> 0.11.1-alt1
- Initial build for ALT Linux Sisyphus
