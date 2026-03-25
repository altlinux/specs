%define        _gimppluginsdir %(gimptool-3 --gimpplugindir)/plug-ins/

Name:          gimp-plugin-ogniewski-scaler
Version:       20250212
Release:       alt2.1
Summary:       Image scaling plugin for the GIMP
License:       GPL-3.0-only
Group:         Graphics
Url:           https://github.com/pannacotta98/ogniewski-scaler
Vcs:           https://github.com/pannacotta98/ogniewski-scaler.git

Source:        %name-%version.tar
BuildRequires: gcc-c++
BuildRequires: libgimp-devel >= 3.0
BuildRequires: intltool
BuildRequires: glibc-devel

%description
Image scaling plugin for the GIMP

%prep
%setup
touch NEWS README AUTHORS

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
%find_lang gimp30-plugin-template

%files         -f gimp30-plugin-template.lang
%_gimppluginsdir/*
%_datadir/ogniewski-scaler


%changelog
* Wed Mar 25 2026 Pavel Skrylev <majioa@altlinux.org> 20250212-alt2.1
- ! fixed call to gimptool-3

* Thu Feb 13 2025 Pavel Skrylev <majioa@altlinux.org> 20250212-alt2
- fixed the plugin

* Thu Feb 13 2025 Ivan A. Melnikov <iv@altlinux.org> 20250212-alt1.1
- NMU: explicitly link with libm (fixes build on riscv64).

* Wed Feb 12 2025 Pavel Skrylev <majioa@altlinux.org> 20250212-alt1
- 20220826 -> 20250212

* Tue Jan 03 2023 Pavel Skrylev <majioa@altlinux.org> 20220826-alt1
- initial build for Sisyphus
