Name:           libretro-overlays
Version:        1.17.0
Release:        alt1
Summary:        Collection of overlays for libretro
License:        CC-BY-4.0
Group:          Emulators
URL:            https://github.com/libretro/%{name}

Source:         https://github.com/libretro/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar

BuildRequires:  make
BuildArch:      noarch

%description
%summary

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_datadir}/libretro/overlays

for OL in borders configure ctr effects gamepads ipad keyboards misc wii; do
cp -r $OL %{buildroot}%{_datadir}/libretro/overlays
done

%files
%doc COPYING
%dir %{_datadir}/libretro/overlays
%{_datadir}/libretro/overlays/*

%changelog
* Thu Mar 21 2024 Artyom Bystrov  <arbars@altlinux.org> 1.17.0-alt1
- Initial commit for Sisyphus