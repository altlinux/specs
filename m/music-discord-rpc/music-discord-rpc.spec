Name: music-discord-rpc
Version: 0.7.0
Release: alt1

Summary: Cross-platform Discord rich presence for music with album cover and progress bar support
License: MIT
Group: Other

Url: https://github.com/patryk-ku/music-discord-rpc
VCS: https://github.com/patryk-ku/music-discord-rpc

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc pkgconfig(dbus-1)

%description
Cross-platform Discord rich presence for music with album cover and
progress bar support. You can customize additional buttons, such as
linking to your Last.fm profile or searching for the current song on
YouTube. There's also an option to display either the music player's
icon or your Last.fm avatar next to the album cover. Album covers are
fetched from Last.fm, with MusicBrainz used as a fallback.

%prep
%setup -a1

mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/vionya/discord-rich-presence?branch=main"]
git = "https://github.com/vionya/discord-rich-presence"
branch = "main"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build 

%install
%rust_install

%files
%doc *.md LICENSE
%_bindir/%name

%changelog
* Wed May 20 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.7.0-alt1
- Initial build for ALT Linux.

