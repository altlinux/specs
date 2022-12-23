%def_without benchmark

Name:     b3sum
Version:  1.3.3
Release:  alt1

Summary:  A command line utility for calculating BLAKE3 hashes
License:  Apache-2.0
Group:    Development/Tools
Url:      https://github.com/BLAKE3-team/BLAKE3

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
%if_with benchmark
BuildRequires: hyperfine
%endif

%description
A command line utility for calculating BLAKE3 hashes, similar to Coreutils
tools like b2sum or md5sum.

%prep
%setup
%patch -p1

%build
cd b3sum
export RUSTFLAGS="${RUSTFLAGS} -g"
%ifarch %arm
cargo build --release %{?_smp_mflags} --offline --features neon
%else
cargo build --release %{?_smp_mflags} --offline
%endif

%install
cd b3sum
install -Dm 755 target/release/%name %buildroot%_bindir/%name

%check
cd b3sum
cargo test --release --no-fail-fast
%if_with benchmark
SIZE="$(numfmt --from=iec 10G)"
head -"$SIZE"c /dev/zero > /tmp/zero
hyperfine --style basic --warmup 3 \
    "sh -c 'head -c $SIZE /dev/zero | %buildroot%_bindir/b3sum'" \
    "sh -c 'head -c $SIZE /dev/zero | b2sum'" \
    "sh -c 'head -c $SIZE /dev/zero | md5sum'" \
    "sh -c 'head -c $SIZE /dev/zero | sha256sum'" \
    #
%endif

%files
%_bindir/*
%doc *.md

%changelog
* Thu Dec 22 2022 Mikhail Gordeev <obirvalger@altlinux.org> 1.3.3-alt1
- new version 1.3.3

* Fri Aug 26 2022 Mikhail Gordeev <obirvalger@altlinux.org> 1.3.1-alt1
- new version 1.3.1

* Mon Nov 08 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.0-alt1
- new version 1.2.0

* Wed Oct 27 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.0-alt1
- new version 1.1.0

* Tue Aug 03 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.0-alt2
- Remove ExclusiveArch

* Mon Aug 02 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
