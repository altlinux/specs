%define themename altemu
	
%define set_theme %{_sbindir}/plymouth-set-default-theme

Name: plymouth-theme-%themename
Version: 1.0
Release: alt1

Summary: Graphical Boot Animation theme for ALTEMU
License: GPLv2+
Group: System/Base

Requires: plymouth plymouth-plugin-script plymouth-plugin-two-step
BuildArch: noarch

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

%description
This package contains ALTEMU boot splash theme for Plymouth.

%prep
%setup

%install
mkdir -p %buildroot%_datadir
cp -a plymouth %buildroot%_datadir

%post
# on initial install, set this as the new theme
if [ $1 -eq 1 ]; then
    %{set_theme} %{themename}
fi
	
%postun
# if uninstalling, reset to boring meatless default theme
	
if [ $1 -eq 0 ]; then
    if [ "$(%{set_theme})" == "%{themename}" ]; then
        %{set_theme} --reset
    fi	
fi

%files
%_datadir/plymouth/themes/%themename/*.png
%_datadir/plymouth/themes/%themename/%themename.plymouth


%changelog
* Sun Aug 17 2025 Artyom Bystrov <arbars@altlinux.org> 1.0-alt1
- initial build for ALT Sisyphus
