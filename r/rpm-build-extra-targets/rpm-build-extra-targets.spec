
%define _unpackaged_files_terminate_build 1

Name: rpm-build-extra-targets
Version: 0.3
Release: alt1

Summary: Build packages for other platforms
License: GPLv2+
Group: Development/Other

Source: %name-%version-%release.tar

Requires: rpm-build

%description
This package adds a few files required to build RPM packages
for targets that current platform does not support.

This may be useful for OS bootstrap, re-packaging binaries,
checking architecture-specific patches with 'rpmbuild -bp',
or for testing Linux kernels and hardware-specific packages
(like u-boot) in pair with cross-compilation.

%prep
%setup -n %name-%version-%release

%build
mkdir build
DESTDIR=./build ./installplatform

%install
# Only install files that are not part of rpm-build already.
find build -name macros |
  while read filename; do
    # we should put this file here:
    dst=/"${filename#*build/}"
    # if it's already present in rpm-build, ignore it
    [ -f "$dst" ] && continue ||:
    # otherwise, install it
    install -Dm644 "$filename" "%buildroot$dst"
  done

find %buildroot%_rpmlibdir -type d -name '*-alt-linux' |
  while read dirname; do
    ln -sr "$dirname" "${dirname/-alt-/-}"
  done


%check
# If rpm-build for this platform has a file for the given
# platform, we should compare it with what we generated.
find build -name macros |
  while read filename; do
    # the local file to compare to:
    dst=/"${filename#*build/}"
    # if it doesn't exist, ignore this file
    [ -f "$dst" ] || continue
    # otherwise, compare our file with the REAL one
    diff -u "$dst" "$filename"
  done

%files
%_rpmlibdir/*
%doc README.md

%changelog
* Sat Jun 22 2024 Ivan A. Melnikov <iv@altlinux.org> 0.3-alt1
- Sync platform.in with rpmbuild 4.0.4.201-alt1

* Wed Feb 28 2024 Ivan A. Melnikov <iv@altlinux.org> 0.2-alt1
- Fix %%optflags definition for loongarch64.

* Tue Jul 25 2023 Ivan A. Melnikov <iv@altlinux.org> 0.1-alt1
- Initial build as a separate package (ALT #44453).
