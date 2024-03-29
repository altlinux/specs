Name:           fbneo
Version:        1.0.0.2
Release:        alt1
Summary:        Multi-System emulator
License:        Custom
Group:          Emulators
URL:            https://neo-source.com
Source:         FBNeo-%version.tar.gz

%ifarch aarch64
BuildRequires:  pkgconfig(SDL_image)
%endif
BuildRequires:  build-essential
BuildRequires:  pkgconfig(SDL2_gfx)
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  nasm


ExcludeArch: ppc64le

%description
This is FinalBurn Neo, an Emulator for Arcade Games & Select Consoles.
It is based on the emulators FinalBurn and old versions of MAME.

%prep
%setup -q -n FBNeo-%version


%build

%make_build sdl2

%install
install -Dm0755 %name %buildroot%_bindir/%name

%files
%doc *.md fba.chm
%_bindir/%name

%changelog
* Sun Mar 24 2024 2024 Artyom Bystrov <arbars@altlinux.org> 1.0.0.2-alt1
- Initial commit for Sisyphus