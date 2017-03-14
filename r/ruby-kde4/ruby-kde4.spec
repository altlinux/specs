
%add_findreq_skiplist %ruby_sitelibdir/soprano/soprano.rb

%define major 4
%define minor 14
%define bugfix 0
Name: ruby-kde4
Version: %major.%minor.%bugfix
Release: alt4

Group: Development/Ruby
Summary: Korundum Ruby-KDE library
License: LGPLv2.1+

Requires: ruby-qt4 >= %major.%minor

Provides: ruby-korundum = %EVR ruby-korundum4 = %EVR

Source: korundum-%version.tar
Url: https://projects.kde.org/projects/kde/kdebindings/ruby/korundum
Patch1: alt-no-examples.patch

# Automatically added by buildreq on Thu Aug 21 2014 (-bi)
# optimized out: automoc boost-devel-headers cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs kde4libs-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libakonadi4-calendar libakonadi4-contact libakonadi4-kabc libakonadi4-kcal libakonadi4-kde libakonadi4-kmime libakonadi4-notes libakonadi4-socialutils libakonadi4-xml libcloog-isl4 libdbus-devel libdbusmenu-qt2 libfreetype-devel libgpgmexx4-pthread libgst-plugins libpng-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-script libqt4-sql libqt4-svg libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libsoprano-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base rpm-build-ruby ruby ruby-qt4 ruby-stdlibs shared-desktop-ontologies-devel smokegen-devel smokeqt-devel soprano-backend-redland soprano-backend-virtuoso xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: akonadi-devel gcc-c++ glib2-devel kde4-kate-devel kde4-okular-devel kde4-smoke-devel kde4pimlibs-devel libXxf86misc-devel libqt3-devel libruby-devel python-module-protobuf qt4-designer ruby-qt4-devel soprano zlib-devel-static
BuildRequires: akonadi-devel gcc-c++ kde4-kate-devel kde4-okular-devel kde4-smoke-devel kde4pimlibs-devel
BuildRequires: libruby-devel ruby-qt4-devel
BuildRequires: kde-common-devel

%filter_from_requires /^ruby(\(analog_clock_config\|calendar\|clockapplet\|digital_clock_config\|timezones_config\))/d

%description
Ruby bindings for libraries created by the KDE community.

%prep
%setup -n korundum-%version
%patch1 -p1

%build
%K4build \
    #
#  -DCUSTOM_RUBY_SITE_ARCH_DIR:PATH=%{ruby_archdir} \
#  -DCUSTOM_RUBY_SITE_LIB_DIR:PATH=%{ruby_libdir} \

%install
%K4install
chmod a+x %buildroot/%ruby_sitelibdir/kio/kio.rb
chmod a+x %buildroot/%ruby_sitelibdir/khtml/khtml.rb

%files
%ruby_sitearchdir/*.so
%ruby_sitelibdir/KDE/
#%ruby_sitelibdir/soprano/
%ruby_sitelibdir/akonadi/
%ruby_sitelibdir/kio/
%ruby_sitelibdir/khtml/
%ruby_sitelibdir/ktexteditor/
%ruby_sitelibdir/solid/
#%ruby_sitelibdir/nepomuk/
#%ruby_sitelibdir/okular/
%_K4lib/krubypluginfactory.so
%_K4bindir/krubyapplication
%_K4bindir/rbkconfig_compiler4
%_K4srv/plasma-applet-ruby-analogclock.desktop
%_K4srv/plasma-ruby-digital-clock-default.desktop
%_K4apps/plasma_applet_ruby_clock/
%_K4apps/plasma_ruby_digital_clock/

%changelog
* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 4.14.0-alt4
- Rebuild with new %%ruby_sitearchdir location

* Mon Oct 03 2016 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt3
- rebuild with new libruby

* Fri Oct 16 2015 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt2
- rebuild with gcc5

* Thu Aug 21 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt1
- initial build
