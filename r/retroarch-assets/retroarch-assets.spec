Name:           retroarch-assets
Version:        git20220113
Release:        alt1
Summary:        RetroArch Assets
License:        CC-BY-4.0
Group:          Emulators
URL:            https://github.com/libretro/retroarch-assets

Source:         %{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  fonts-ttf-google-droid-sans
BuildRequires:  make
BuildArch: noarch

%description
Assets needed for RetroArch - e.g. menu drivers, etc. Also contains the official branding.

%prep
%setup -q

%build

%install
%makeinstall_std

%files
%doc COPYING
%dir %{_datadir}/libretro
%{_datadir}/libretro/assets

%changelog
* Mon Mar 18 2024 Artyom Bystrov <arbars@altlinux.org> git20220113-alt1
- Initial commit for Sisyphus