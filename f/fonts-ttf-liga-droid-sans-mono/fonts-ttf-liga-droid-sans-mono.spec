%define _unpackaged_files_terminate_build 1
%define oname LigaDroidSansMono 
%define fname liga-droid-sans-mono

Name: fonts-ttf-%fname
Version: 20180801.8ace00c
Release: alt1
Summary: Droid Sans Mono font with programming ligatures
License: GPLv3
Group: System/Fonts/True type
Url: https://github.com/abogoyavlensky/DroidCode
Source: %name-%version.tar
Packager: Alexander Makeenkov <amakeenk@altlinux.org>

BuildArch: noarch
BuildRequires: rpm-build-fonts
BuildRequires: mkfontscale

%description
DroidCode font based on Droid Sans Mono with programming ligatures
inspired by FiraCode and build using Ligaturizer.

%prep
%setup

%install
mkdir -p %buildroot%_ttffontsdir/%fname
install -m 0644 %oname.ttf %buildroot%_ttffontsdir/%fname
mkfontscale %buildroot%_ttffontsdir/%fname
ln %buildroot%_ttffontsdir/%fname/fonts.scale %buildroot%_ttffontsdir/%fname/fonts.dir

%files
%_ttffontsdir/%fname
%doc LICENSE

%changelog
* Sun Oct 13 2019 Alexander Makeenkov <amakeenk@altlinux.org> 20180801.8ace00c-alt1
- Fixed version

* Sun Oct 13 2019 Alexander Makeenkov <amakeenk@altlinux.org> 1.0-alt1
- Initial build for ALT
