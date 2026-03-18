%define _unpackaged_files_terminate_build 1
%define oname Myna
%define fname myna

Name: fonts-ttf-%fname
Version: 2.0.0.0.beta
Release: alt1

Summary: monospace typeface designed for symbol-rich programming (ttf)
License: OFL-1.1
Group: System/Fonts/True type
Url: https://github.com/sayyadirfanali/Myna
Vcs: https://github.com/sayyadirfanali/Myna

BuildArch: noarch

Source: %name-%version.tar

Requires(pre): fontconfig
BuildRequires(pre): rpm-build-fonts

%description
%summary.

%package -n fonts-otf-%fname
Summary: %summary (otf)
Group: System/Fonts/True type

%description -n fonts-otf-%fname
%summary.

%prep
%setup

%install
cd fonts
%ttf_fonts_install %fname
mv %fname.files ttf-%fname.files

%otf_fonts_install %fname
mv %fname.files otf-%fname.files

%files -n fonts-ttf-%fname -f fonts/ttf-%fname.files
%files -n fonts-otf-%fname -f fonts/otf-%fname.files

%changelog
* Wed Mar 18 2026 Anton Zhukharev <ancieg@altlinux.org> 2.0.0.0.beta-alt1
- Packaged for ALT Sisyphus.
