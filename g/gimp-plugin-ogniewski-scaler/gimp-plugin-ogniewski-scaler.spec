%define        _gimppluginsdir %(gimptool-3.0 --gimpplugindir)/plug-ins/

Name:          gimp-plugin-ogniewski-scaler
Version:       20250212
Release:       alt1.1
Summary:       Image scaling plugin for the GIMP
License:       GPL-3.0-only
Group:         Graphics
Url:           https://github.com/pannacotta98/ogniewski-scaler
Vcs:           https://github.com/pannacotta98/ogniewski-scaler.git

Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires: gcc-c++
BuildRequires: libgimp-devel >= 3.0
BuildRequires: intltool
BuildRequires: glib2-devel
#BuildRequires: libopenlibm-devel

%description
Image scaling plugin for the GIMP

%prep
%setup
touch NEWS README AUTHORS

%build
# This project uses floor(3), so should link with libm.
# Required at least on riscv64, should not hurt anywhere.
export LIBS=-lm

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
* Thu Feb 13 2025 Ivan A. Melnikov <iv@altlinux.org> 20250212-alt1.1
- NMU: explicitly link with libm (fixes build on riscv64).

* Wed Feb 12 2025 Pavel Skrylev <majioa@altlinux.org> 20250212-alt1
- 20220826 -> 20250212

* Tue Jan 03 2023 Pavel Skrylev <majioa@altlinux.org> 20220826-alt1
- initial build for Sisyphus
