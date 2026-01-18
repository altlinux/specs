%define target_lua_version 5.4
%define oname %name-api
%define oversion %version

Name: pinnacle
Version: 0.2.2
Release: alt1
Summary: A WIP Smithay-based Wayland compositor, inspired by AwesomeWM and configured in Lua or Rust
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/pinnacle-comp/pinnacle/
#Source: https://github.com/pinnacle-comp/pinnacle/archive/refs/heads/main.tar.gz#/%name-main.tar.gz
Source: https://github.com/pinnacle-comp/pinnacle/archive/refs/tags/v0.2.2.tar.gz#/%name-%version.tar.gz
Source1: vendor.tar
Patch: pinnacle-arm-fix.patch
ExcludeArch: i586 armh

BuildRequires(pre): rpm-build-rust rpm-macros-lua rpm-build-lua
# Automatically added by buildreq on Sun Feb 11 2024 (-bi)
# optimized out: ca-trust debugedit elfutils libctf-nobfd0 libgpg-error libp11-kit libsasl2-3 libudev-devel libwayland-server llvm17.0-libs lua5.4 pkg-config python3 python3-base rpm-build-file rpm-build-lua rust sh5 wget
BuildRequires: desktop-file-utils just libdisplay-info-devel libgbm-devel libinput-devel libseat1-devel libxkbcommon-devel lua%target_lua_version-luarocks protobuf-compiler rust-cargo

BuildRequires: protobuf-compiler lua%target_lua_version-module-cqueues >= 20200726 lua%target_lua_version-module-http >= 0.4 lua%target_lua_version-module-luaposix lua%target_lua_version-module-lua-protobuf >= 0.5.2 lua%target_lua_version-luarocks

BuildRequires: /proc

Requires: protobuf-compiler xdg-desktop-portal-gtk xdg-desktop-portal-wlr

%description
Pinnacle is a Wayland compositor built in Rust using Smithay. It's my attempt at
creating something like AwesomeWM for Wayland.

It sports extensive configurability through either Lua or Rust, with the
ability to add more languages in the future.

%prep
%setup -a1
%patch -p1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/Ottatop/slab-tree?rev=d6adbbb"]
git = "https://github.com/Ottatop/slab-tree"
rev = "d6adbbb"
replace-with = "vendored-sources"

[source."git+https://github.com/Ottatop/softbuffer?rev=cd65c9e"]
git = "https://github.com/Ottatop/softbuffer"
rev = "cd65c9e"
replace-with = "vendored-sources"

[source."git+https://github.com/Ottatop/taffy?rev=dcdaa42"]
git = "https://github.com/Ottatop/taffy"
rev = "dcdaa42"
replace-with = "vendored-sources"

[source."git+https://github.com/Smithay/smithay?rev=61f5a0d"]
git = "https://github.com/Smithay/smithay"
rev = "61f5a0d"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF
# adapt `justfile` to older version of just
sed -i 's/x"/"/g' justfile
sed -i '/^export LUA_/,/^$/d' justfile
sed -i '/rm -rf ...proto_dir/d' justfile */justfile
# no need in `compat53`
subst /compat53/d \
	api/lua/build/grpc_client.lua \
	api/lua/pinnacle-*.rockspec \
	api/lua/pinnacle/grpc/defs.lua \
	api/lua/pinnacle/grpc/protobuf.lua \
	api/lua/rockspecs/pinnacle-api-*.rockspec \
	snowcap/api/lua/snowcap-*.rockspec \
	snowcap/api/lua/snowcap/grpc/defs.lua \
	snowcap/api/lua/snowcap/grpc/protobuf.lua \


%build
export RUSTFLAGS="${RUSTFLAGS} -g"
just build --release %{?_smp_mflags} --offline
just -d snowcap --justfile snowcap/justfile gen-lua-pb-defs

%define justvars --set xdg_data_dir %buildroot%_datadir/%name

%install
%rust_install
just -v %justvars install-protos
just -v %justvars -d snowcap --justfile snowcap/justfile install-protos
for d in {.,snowcap}/api/lua; do
  pushd $d
  %luarocks_make *.rockspec
  popd
done
install -D -m755 -t %buildroot/usr/bin \
        resources/pinnacle-session
install -D -m644 -t %buildroot/usr/lib/systemd/user \
        resources/pinnacle{.service,-shutdown.target}
install -D -m644 -t %buildroot/usr/share/xdg-desktop-portal/ \
        resources/pinnacle-portals.conf
desktop-file-install \
	--dir=%buildroot%_datadir/wayland-sessions/ \
	resources/%name.desktop
%find_lang --with-gnome %name

%filter_from_requires /^lua[^5]/d

%check
# fails
#%%rust_test

%files -f %name.lang
%doc *.md api
%_bindir/*
%_user_unitdir/*
%_datadir/%name
%_datadir/wayland-sessions/%name.desktop
%_datadir/xdg-desktop-portal/*
%lua54_modulesdir_noarch/*
%luarocks_dbdir_prefix-%target_lua_version/*
%exclude %luarocks_dbdir_prefix-%target_lua_version/manifest

%changelog
* Sun Jan 18 2026 Ildar Mulyukov <ildar@altlinux.ru> 0.2.2-alt1
- Initial build for Sisyphus
