# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name: fcitx-table-other
Version: 0.2.2
Release: alt2
Summary: Other tables for Fcitx
Packager: Ilya Mashkin <oddity@altlinux.ru>
Group: System/Libraries
License: GPLv3+
Url: https://fcitx-im.org/wiki/Fcitx
Source0: http://download.fcitx-im.org/fcitx-table-other/%name-%version.tar.xz

BuildRequires: ctest cmake fcitx-devel gettext intltool libtool fcitx
BuildArch: noarch
Requires: fcitx
Source44: import.info

%description
Fcitx-table-other is a fork of ibus-table-others for Fcitx,
provides additional tables.

%prep
%setup -n %name-%version

%build
mkdir -pv build
pushd build
%fedora_cmake ..
make VERBOSE=1

%install
pushd build
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
popd

%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING README
%_datadir/fcitx/table/*.mb
%_datadir/fcitx/table/*.conf
%_datadir/fcitx/imicon/*.png
%_datadir/icons/hicolor/64x64/apps/*.png
%_datadir/icons/hicolor/48x48/apps/*.png
%_datadir/icons/hicolor/32x32/apps/*.png

%changelog
* Fri Sep 05 2014 Ilya Mashkin <oddity@altlinux.ru> 0.2.2-alt2
- build for Sisyphus

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt1_2
- update to new release by fcimport

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt1_1
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_3
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_2
- update to new release by fcimport

* Thu Dec 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_1
- initial fc import

