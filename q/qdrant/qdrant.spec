ExcludeArch: %ix86
Name: qdrant
Version: 1.18.2
Release: alt1

Summary: Qdrant Vector Search Engine
License: Apache-2.0
Group: Databases
Url: https://qdrant.tech/
VCS: https://github.com/qdrant/qdrant

Source: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: config.toml
Source3: qdrant.service
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rust >= 1.89
BuildRequires: rust-cargo
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: clang
BuildRequires: lld
BuildRequires: protobuf-compiler
BuildRequires: libprotobuf-devel
BuildRequires: pkg-config

%description
Qdrant is a high-performance vector search engine and vector database.
It is designed to index and search large collections of high-dimensional
vectors with a convenient API.

%prep
%setup -a1
%patch0 -p1
install -pD %SOURCE2 .cargo/config.toml


%build
export CARGO_HOME="$PWD/.cargo_home"
export PROTOC=/usr/bin/protoc
cargo build --release --locked

%install
install -Dpm 0755 target/release/qdrant %buildroot%_bindir/qdrant
install -Dpm 0640 config/deb.yaml %buildroot%_sysconfdir/qdrant/config.yaml
install -Dpm 0644 %SOURCE3 %buildroot%_unitdir/qdrant.service
install -dm 0750 %buildroot%_localstatedir/qdrant/storage
install -dm 0750 %buildroot%_localstatedir/qdrant/snapshots

%pre
groupadd -r -f qdrant
useradd -r -g qdrant -d %_localstatedir/qdrant -s /dev/null -c "Qdrant daemon" qdrant >/dev/null 2>&1 ||:

%post
# Generate unique API key on first install
if [ $1 -eq 1 ]; then
    if [ -c /dev/urandom ]; then
        API_KEY=$(tr -dc 'a-zA-Z0-9' < /dev/urandom | head -c 48)
        sed -i "s/__GENERATED_API_KEY__/$API_KEY/" %_sysconfdir/qdrant/config.yaml
    else
        sed -i "s/  api_key: __GENERATED_API_KEY__/  # api_key: <set manually>/" %_sysconfdir/qdrant/config.yaml
    fi
fi
%post_service qdrant

%preun
%preun_service qdrant

%files
%doc README.md LICENSE
%_bindir/qdrant
%dir %attr(0750,qdrant,qdrant) %_localstatedir/qdrant
%dir %attr(0750,qdrant,qdrant) %_localstatedir/qdrant/storage
%dir %attr(0750,qdrant,qdrant) %_localstatedir/qdrant/snapshots
%dir %_sysconfdir/qdrant
%config(noreplace) %attr(0640,root,qdrant) %_sysconfdir/qdrant/config.yaml
%_unitdir/qdrant.service

%changelog
* Mon Jun 08 2026 Anton Farygin <rider@altlinux.org> 1.18.2-alt1
- 1.17.1 -> 1.18.2

* Fri Apr 24 2026 Anton Farygin <rider@altlinux.org> 1.17.1-alt1
- 1.17.0 -> 1.17.1

* Wed Mar 04 2026 Anton Farygin <rider@altlinux.org> 1.17.0-alt1
- 1.16.3 -> 1.17.0

* Sat Feb 14 2026 Anton Farygin <rider@altlinux.org> 1.16.3-alt1
- initial build for ALT Linux
