
Name: rhythmbox-plugins-gmusic
Version: 2.0
Release: alt1

Summary: Rhythmbox Google Play Music Plugin
Group: Sound
License: BSD
Url: https://github.com/nvbn/rhythmbox-gmusic/

Source: %name-%version.tar

BuildRequires: python-module-setuptools
Requires: rhythmbox

%description
Plugin for playing music from Google Play Music in Rhythmbox.

%prep
%setup -q

sed -i -e 's|/usr/lib/rhythmbox/plugins/googleplaymusic|%_libdir/rhythmbox/plugins/googleplaymusic|' setup.py
sed -i -e 's|rhythmboxgmusic|googleplaymusic|' googleplaymusic.plugin

%build
%python_build

%install
mkdir -p %buildroot%_libdir/rhythmbox/plugins/googleplaymusic
install -m 0644 rhythmboxgmusic/__init__.py %buildroot%_libdir/rhythmbox/plugins/googleplaymusic/googleplaymusic.py
install -m 0644 googleplaymusic.plugin %buildroot%_libdir/rhythmbox/plugins/googleplaymusic/googleplaymusic.plugin
mkdir -p %buildroot%_datadir/locale/ru/LC_MESSAGES
install -m 0644 po/ru/rhythmbox-gmusic.mo %buildroot%_datadir/locale/ru/LC_MESSAGES/

%find_lang rhythmbox-gmusic

%files -f rhythmbox-gmusic.lang
%_libdir/rhythmbox/plugins/googleplaymusic

%changelog
* Mon Aug 06 2012 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt1
- first build for Sisyphus
