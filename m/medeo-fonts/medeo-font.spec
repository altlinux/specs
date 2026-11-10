%define _unpackaged_files_terminate_build 1

Name: medeo-fonts
Version: 1.1.0
Release: alt1

Summary: An open type family for Latin and Cyrillic by DNF
License: OFL-1.1
Group: System/Fonts/True type
Url: https://github.com/DNFDEVS/medeo-font
Vcs: https://github.com/DNFDEVS/medeo-font

BuildArch: noarch

Source: %name-%version.tar

Requires(pre): fontconfig
BuildRequires(pre): rpm-build-fonts

%description
Medeo is a free font family for Latin and Cyrillic by DNF Studio.

%package -n fonts-ttf-medeo-serif
Summary: Medeo Serif font
Group: System/Fonts/True type
%description -n fonts-ttf-medeo-serif
Medeo Serif for text and headings. One style: Regular.

%package -n fonts-ttf-medeo-sans
Summary: Medeo Sans font
Group: System/Fonts/True type
%description -n fonts-ttf-medeo-sans
Medeo Sans for interfaces and text. Weight 100-900, optical size 14-32, upright
and italic. Includes Medeo Sans Display for headings.

%package -n fonts-ttf-medeo-mono
Summary: Medeo Mono font
Group: System/Fonts/True type
%description -n fonts-ttf-medeo-mono
Medeo Mono for code and aligned columns. Weight 100-900, upright and italic.

%package -n fonts-ttf-medeo-pixel
Summary: Medeo Pixel font
Group: System/Fonts/True type
%description -n fonts-ttf-medeo-pixel
Medeo Pixel for display text. Five pixel shapes: Square, Circle, Grid,
Triangle, and Line.

%package -n fonts-ttf-medeo-mono-nerd-font
Summary: Medeo Mono Nerd Font
Group: System/Fonts/True type
%description -n fonts-ttf-medeo-mono-nerd-font
Medeo Mono with the Nerd Fonts icons, for terminals, editors and shell themes.

%prep
%setup

%install
cd fonts/MedeoSerif/ttf
%ttf_fonts_install medeo-serif
cd ../../MedeoSans/ttf
%ttf_fonts_install medeo-sans
cd ../../MedeoMono/ttf
%ttf_fonts_install medeo-mono
cd ../../MedeoPixel/ttf
%ttf_fonts_install medeo-pixel
cd ../../MedeoMonoNerdFont/ttf
%ttf_fonts_install medeo-mono-nerd-font

%files -n fonts-ttf-medeo-serif -f fonts/MedeoSerif/ttf/medeo-serif.files
%files -n fonts-ttf-medeo-sans -f fonts/MedeoSans/ttf/medeo-sans.files
%files -n fonts-ttf-medeo-mono -f fonts/MedeoMono/ttf/medeo-mono.files
%files -n fonts-ttf-medeo-pixel -f fonts/MedeoPixel/ttf/medeo-pixel.files
%files -n fonts-ttf-medeo-mono-nerd-font -f fonts/MedeoMonoNerdFont/ttf/medeo-mono-nerd-font.files

%changelog
* Tue Nov 10 2026 Anton Zhukharev <ancieg@altlinux.org> 1.1.0-alt1
- Updated to 1.1.0.

* Tue Nov 10 2026 Anton Zhukharev <ancieg@altlinux.org> 1.0.0-alt1
- Packaged for ALT Sisyphus.
