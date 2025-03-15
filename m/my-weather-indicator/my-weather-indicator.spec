%define _unpackaged_files_terminate_build 1

Name: my-weather-indicator
Version: 0.10.18
Release: alt1

Summary: Get weather information for your town with My-Weather-Indicator
License: MIT
Group: Graphical desktop/Other
URL: https://github.com/atareao/my-weather-indicator

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-fonts
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3(hatchling)

Requires: typelib(AyatanaAppIndicator3)
Requires: typelib(Notify)
Requires: typelib(WebKit2)
Requires: fonts-ttf-mplus-1c

BuildArch: noarch

Source: %name-%version.tar

Patch: %name-%version-%release.patch

%description
A Weather Indicator for Linux Desktop (Plasma, GNOME, MATE, XFCE,...).
My-Weather-Indicator is an an application especially designed for Ubuntu,
you will be informed of current weather and the weather forecast.
Integrated with the Ubuntu desktop via an indicator. With local maps,
showing the conditions in nearby towns. The weather forecast for the
next few days in your city. You can have up to two indicators for two
cities, and choose the best weather service information that you provide.
You select customizable widgets to make your desktop more personalized.

%prep
%setup -n %name-%version
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

# taken and adapted from
# https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=my-weather-indicator-git
#
pkgdir=%buildroot
# Don't install to /opt and install locales to correct directory
find . -type f -exec \
  sed -i -e 's:/opt/extras.ubuntu.com/my-weather-indicator:/usr:g' \
         -e 's:locale-langpack:locale:g' '{}' \;

# Install translations
while read lang; do
    mkdir -p "$pkgdir/usr/share/locale/$lang/LC_MESSAGES"
    msgfmt "po/$lang" -o "$pkgdir/usr/share/locale/$lang/LC_MESSAGES/my-weather-indicator.mo"
done < po/languages.txt

# Install the files, set correct permissions
while read _in _out ; do
    mkdir -p "${pkgdir}/${_out}/"
    cp -r ${_in} "${pkgdir}/${_out}/"
done < debian/install

chmod 755 "${pkgdir}"/usr/bin/my-weather-indicator

%find_lang %name

%files -f %name.lang
%doc AUTHORS LICENSE README.md
%_bindir/%name
%_desktopdir/%{name}.desktop
%_pixmapsdir/%{name}.*
%python3_sitelibdir/*-info/METADATA
%python3_sitelibdir/*.dist-info
%dir %_datadir/my-weather-indicator
%_datadir/my-weather-indicator/*
# Already packaged in fonts-ttf-mplus-1c
%exclude %_datadir/fonts/truetype/mplus-1c
# Exclude bundled fonts
%exclude %_datadir/fonts/truetype/existence
%exclude %_datadir/fonts/truetype/encode-sans

%changelog
* Sat Mar 15 2025 Nikolay Strelkov <snk@altlinux.org> 0.10.18-alt1
- Initial build for Sisyphus
