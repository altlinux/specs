%define        gimpscriptsdir %(gimptool-2.0 --gimpdatadir)/scripts/
%define        gimppluginsdir %(gimptool-2.0 --gimpplugindir)/plug-ins/
%define        gimphelpdir %(gimptool-2.0 --gimpdatadir)/help

Name:          gimp-plugin-elsamuko
Version:       20220103
Release:       alt1
Summary:       Elsamuko Gimp scripts
License:       GPL-3.0-only
Group:         Graphics
Url:           https://elsamuko.github.io/gimp-elsamuko/scripts
Vcs:           git@github.com:elsamuko/gimp-elsamuko.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
Patch:         patch.patch
BuildRequires: gcc-c++
BuildRequires: libgimp-devel
BuildRequires: libopencv-devel
BuildRequires: qt5-base-devel

%description
Set of elsamuko GIMP FU-scripts.


%package       help
Summary:       Elsamuko Gimp scripts documentation files
Group:         Documentation
BuildArch:     noarch

Requires:      %name = %EVR

%description   help
Elsamuko Gimp scripts documentation files


%package       devel
Summary:       Elsamuko Gimp scripts development package
Group:         Development/KDE and QT
BuildArch:     noarch

Requires:      %name = %EVR
Requires:      gcc-c++
Requires:      libgimp-devel
Requires:      libopencv-devel
Requires:      qt5-base-devel

%description   devel
Elsamuko Gimp scripts development package


%prep
%setup
%autopatch

%build
find plugins/ -name "*.pro" | while read f; do pushd "$(dirname "$f")"; %_qt5_qmake "$(basename "$f")"; make; popd; done

%install
mkdir -p %buildroot/%gimphelpdir/en/
install -D -t %buildroot/%gimppluginsdir -m644 $(find $(find $HOME/.config/gimp -name plug-ins)/* -type f)
install -D -t %buildroot/%gimpscriptsdir -m644 scripts/*
cp -pr docs/* %buildroot/%gimphelpdir/en/


%files
%gimpscriptsdir/*
%gimppluginsdir/*
%doc README.md

%files help
%gimphelpdir/en/*

%files devel


%changelog
* Mon Jan 02 2023 Pavel Skrylev <majioa@altlinux.org> 20220103-alt1
- initial build for Sisyphus
