Name:    Ikemen_GO-Elecbyte-Screenpack
Version: 0.1
Release: alt1

Summary: Electbyte's Mugen screenpack and font files with some modifications for Ikemen GO
License: Creative Commons 3.0 Non-commercial
Group:   Games/Arcade
Url:     https://github.com/ikemen-engine/Ikemen_GO-Elecbyte-Screenpack

Source: %name-%version.tar

BuildArch: noarch

#BuildRequires:

%description
%summary

%prep
%setup

%build

#Empty section - nothing to build

%install
mkdir -p %buildroot%_datadir/%name
for res in chars data font sound stages; do
cp -r $res %buildroot%_datadir/%name/
done

%files
%_datadir/%name/*

%changelog
* Wed Sep 25 2024 Artyom Bystrov <arbars@altlinux.org> 0.1-alt1
- Initial build for Sisyphus
