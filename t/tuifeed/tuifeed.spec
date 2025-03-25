Name: tuifeed
Version: 0.4.1
Release: alt1

Summary: A terminal feed reader with a fancy ui
License: MIT
Group: Networking/News
Url: https://github.com/veeso/tuifeed
VCS: https://github.com/veeso/tuifeed

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

%description
tuifeed is a news feed reader with a fancy terminal user interface. 
It allows you read news from your favourite RSS and Atom sources, 
which can be easily configured in a TOML file.

%prep
%setup -a1
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build 

%install
%rust_install 

install -Dm 0644 docs/images/%name-128.png %buildroot%_iconsdir/hicolor/128x128/apps/%name.png
install -Dm 0644 docs/images/%name-256.png %buildroot%_iconsdir/hicolor/256x256/apps/%name.png
install -Dm 0644 docs/images/%name-512.png %buildroot%_iconsdir/hicolor/512x512/apps/%name.png

cat >> %name.desktop <<EOF
[Desktop Entry]
Categories=Network;
Name=tuifeed
GenericName=A terminal feed reader with a fancy ui
Type=Application
Exec=%name
Icon=%name
Terminal=true
EOF

install -Dm 644 %name.desktop %buildroot%_datadir/applications/%name.desktop


%files
%doc *.md LICENSE
%_bindir/%name
%_iconsdir/hicolor/*/*/*.png
%_datadir/applications/%name.desktop

%changelog
* Tue Mar 25 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.4.1-alt1
- 0.3.2 -> 0.4.1

* Mon Feb 24 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.3.2-alt1
- Initial build for ALT Linux.
