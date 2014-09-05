# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name: fcitx-libpinyin
Version: 0.2.92
Release: alt2
Summary: Libpinyin Wrapper for Fcitx
Packager: Ilya Mashkin <oddity@altlinux.ru>
Group: System/Libraries
License: GPLv2+
Url: http://code.google.com/p/fcitx/
Source0: http://fcitx.googlecode.com/files/%name-%{version}_dict.tar.xz

BuildRequires: libpinyin-devel >= 0.9.91
BuildRequires: ctest cmake fcitx-devel gettext intltool libpinyin-devel
BuildRequires: libpinyin-tools glib2-devel fcitx
Requires: fcitx
Source44: import.info

%description
Fcitx-libpinyin is a libpinyin Wrapper for Fcitx.

Libpinyin is a Frontend of the Intelligent Pinyin IME Backend.

%prep
%setup -n %name-%version

%build
mkdir -pv build
pushd build
%fedora_cmake ..
make VERBOSE=1 %{?_smp_mflags}
popd

%install
pushd build
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
popd

%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING README
%_libdir/fcitx/%name.so
%_datadir/fcitx/addon/%name.conf
%_datadir/fcitx/configdesc/%name.desc
%_datadir/fcitx/inputmethod/*-libpinyin.conf
%_datadir/fcitx/libpinyin/
%_datadir/icons/hicolor/48x48/status/fcitx-bopomofo.png

%changelog
* Fri Sep 05 2014 Ilya Mashkin <oddity@altlinux.ru> 0.2.92-alt2
- build for Sisyphus

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.92-alt1_2
- update to new release by fcimport

* Mon May 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.92-alt1_1
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.90-alt1_1
- initial fc import

