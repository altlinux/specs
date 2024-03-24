Name:           libretro-core-info
Version:        1.17.0
Release:        alt1
Summary:        Provide libretro's core info files
License:        MIT
Group:          Emulators
URL:            https://github.com/libretro/%{name}

Source:         https://github.com/libretro/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar

BuildRequires:  make
BuildArch:      noarch

%description
Provide libretro's core info files

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_datadir}/libretro/info
cp *.info %{buildroot}%{_datadir}/libretro/info

%files
%doc COPYING
%dir %{_datadir}/libretro/info
%{_datadir}/libretro/info/*.info

%changelog
* Thu Mar 21 2024 Artyom Bystrov  <arbars@altlinux.org> 1.17.0-alt1
- Initial commit for Sisyphus