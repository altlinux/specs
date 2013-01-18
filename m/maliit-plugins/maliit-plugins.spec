
Name: maliit-plugins
Version: 0.94.0
Release: alt1
Summary: Maliit Input Method Plugins

Group: System/Libraries
License: BSD
Url: http://www.maliit.org

Source: %name-%version.tar
# FC
Patch1: olpc_xo_layout_modifications.patch

BuildRequires: libmaliit-devel libqt4-devel
BuildRequires: libxkbfile-devel libhunspell-devel
BuildRequires: gcc-c++ doxygen

%description
Maliit Plugins provide reference input method plugins for use with Maliit Framework.
Currently it provides a single QML based keyboard plugin.

%prep
%setup -qn %name-%version
%patch1 -p1
find -type f -name \*.pro | \
while read f
do
    echo "QMAKE_CFLAGS+=%optflags" >>$f
    echo "QMAKE_CXXFLAGS+=%optflags" >>$f
done

%build
qmake-qt4 -r \
    CONFIG+=notests \
    CONFIG+=disable-preedit \
    MALIIT_DEFAULT_PROFILE=olpc-xo \
    LIBDIR=%_libdir
#    CONFIG+=enable-hunspell \
%make_build

%install
%make install INSTALL="install -p" INSTALL_ROOT=%buildroot

mkdir -p %buildroot%_datadir/maliit/plugins/org/

# clean docs
rm -rf %buildroot/%_defaultdocdir/maliit-plugins/html


%files
%doc LICENSE NEWS README
%_libdir/maliit/plugins/*
%_bindir/maliit-keyboard*
%dir %_datadir/maliit/
%_datadir/maliit/plugins/

%changelog
* Thu Jan 17 2013 Sergey V Turchin <zerg@altlinux.org> 0.94.0-alt1
- new version

* Thu Oct 18 2012 Sergey V Turchin <zerg@altlinux.org> 0.92.5-alt1
- initial build

