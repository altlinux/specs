%define _unpackaged_files_terminate_build 1

%global fname font-logos
Name: fonts-%fname
Summary: Icon font for Distributions and FOSS
Version: 4.6.1
Release: alt1
License: GPL-3.0-or-later
Group: System/Fonts/True type
Url: https://www.proxmox.com
Vcs: git://git.proxmox.com/git/fonts-font-logos.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-macros-fonts

%description
Font-logos is an icon font containing logos of popular linux distributions and
other open source software. All brand icons are trademarks of their respective
owners and should only be used to represent the company or product to which
they refer..

%prep
%setup

%build
%install
install -Dm0644 src/font-logos/assets/* -t %buildroot%_datadir/%name/fonts/
install -Dm0644 src/font-logos.css -t %buildroot%_datadir/%name/css/
install -Dm0644 src/font-logos/vectors/* -t %buildroot%_datadir/%name/vectors/

# Move .ttf to Policy-based directory 
mkdir -p %buildroot%_ttffontsdir/%fname/
mv %buildroot%_datadir/%name/fonts/font-logos.ttf %buildroot%_ttffontsdir/%fname/
# Make symlink to it for Proxmox-compatibility
ln -s %_ttffontsdir/%fname/font-logos.ttf %buildroot%_datadir/%name/fonts/font-logos.ttf


%files
%doc debian/copyright
%_datadir/%name
%_ttffontsdir/%fname

%changelog
* Mon Feb 10 2025 Sergey Konev <darisishe@altlinux.org> 4.6.1-alt1
- Initial package
