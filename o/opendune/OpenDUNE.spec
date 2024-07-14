Summary:        A faithful re-creation of the popular game Dune II
License:        GPL-2.0-only
Group:          Games/Strategy
Name:           opendune
Version:        0.9
Release:        alt1
Source:         %{name}-%{version}.tar
URL:            http://www.opendune.org/

BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libmt32emu-devel
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(sdl2)

%description
OpenDUNE is an open source re-creation of the popular game "Dune II",
originally made by Westwood Studios, and released by Virgin Entertainment.
It attempts to re-create the original game and apply modern technology to it
to allow it to be run natively on most operating systems.

%prep
%setup

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install INSTALL_DIR=%{buildroot}
mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{_prefix}/games/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/doc/%{name}
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

%changelog
* Sun Jul 14 2024 Artyom Bystrov <arbars@altlinux.org> 0.9-alt1
- Initial build for Sisyphus
