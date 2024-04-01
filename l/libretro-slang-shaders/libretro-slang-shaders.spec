Name:           libretro-slang-shaders
Version:        git1c0a4cc
Release:        alt1
Summary:        Collection of SLANG shaders for libretro
License:        CC-BY-4.0
Group:          Emulators
URL:            https://github.com/libretro/slang-shaders

Source:         %{name}-%{version}.tar

BuildRequires:  make
BuildArch:      noarch

%description
%summary

%prep
%setup -q

%build

%install
%makeinstall_std

%files
%doc README.md
%dir %{_datadir}/libretro/shaders/shaders_slang
%{_datadir}/libretro/shaders/shaders_slang

%changelog
* Thu Mar 21 2024 Artyom Bystrov  <arbars@altlinux.org> git1c0a4cc-alt1
- Initial commit for Sisyphus