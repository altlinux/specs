Name: variety
Version: 0.8.0
Release: alt1
Summary: Wallpaper changer that automatically downloads wallpapers
License: GPLv3
Url: https://github.com/varietywalls/variety
Group: Graphical desktop/Other

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires: python3-dev
BuildRequires: rpm-build-python3
BuildRequires: python3-module-configobj
BuildRequires: python3-module-lxml
BuildRequires: python3-module-gexiv2
BuildRequires: python3-module-pycurl
BuildRequires: python3-module-requests
BuildRequires: python3-module-Pillow-devel
BuildRequires: python3-module-distutils-extra
BuildRequires: intltool
BuildRequires: libyelp-devel
BuildRequires: python3-module-dbus
BuildRequires: python3-module-pycairo-devel
BuildRequires: pkgconfig(libnotify)
BuildRequires: gettext
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
Requires: ImageMagick /usr/bin/gsettings

AutoReq: noshell

%filter_from_requires /AyatanaAppIndicator3/d
%filter_from_requires /libappindicator/d
%filter_from_requires /data.plugins.downloaders/d

%description
Variety changes the desktop wallpaper on a regular basis,
using user-specified or automatically downloaded images.

Variety sits conveniently as an indicator in the panel
and can be easily paused and resumed. The mouse wheel
can be used to scroll wallpapers back and forth until
you find the perfect one for your current mood.

Apart from displaying images from local folders, several
different online sources can be used to fetch wallpapers
according to user-specified criteria.

Variety can also automatically apply various fancy
filters to the displayed images - charcoal painting,
oil painting, heavy blurring, etc. - so that your
desktop is always fresh and unique.

%prep
%setup -n %name-%version

%add_python3_path %_datadir/%name/plugins/downloaders/

%build
python3 setup.py build

%install
python3 setup.py install --root=%buildroot

%find_lang %name

%check
desktop-file-validate %buildroot%_datadir/applications/*.desktop
appstream-util validate-relax --nonet %buildroot/%_datadir/metainfo/%name.appdata.xml

%files -f %name.lang
%doc README.md LICENSE
%_bindir/%name
%_datadir/applications/%name.desktop
%_datadir/metainfo/%name.appdata.xml
%_datadir/%name/
#%exclude %_datadir/%name/plugins/downloders/RedditDownloader.py
#%exclude %_datadir/%name/plugins/downloders/RedditDownloader.py
%python3_sitelibdir/jumble/
%python3_sitelibdir/%name-*-py*.egg-info
%python3_sitelibdir/%name/
%python3_sitelibdir/%{name}_lib/
%_datadir/icons/hicolor/22x22/apps/%name-indicator-dark.png
%_datadir/icons/hicolor/22x22/apps/%name-indicator.png
%_datadir/icons/hicolor/scalable/apps/%name.svg

%changelog
* Thu Nov 14 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.8.0-alt1
- first build based on Fedora package

