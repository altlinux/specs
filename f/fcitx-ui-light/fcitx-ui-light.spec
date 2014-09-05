# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name: fcitx-ui-light
Version: 0.1.3
Release: alt2
Summary: Light UI for fcitx
Packager: Ilya Mashkin <oddity@altlinux.ru>
Group: System/Libraries
License: GPLv2+
Url: http://code.google.com/p/fcitx/
Source0: http://fcitx.googlecode.com/files/%name-%version.tar.bz2

BuildRequires: ctest cmake fcitx-devel gettext intltool libcurl-devel
BuildRequires: fontconfig fontconfig-devel libXpm-devel libXft-devel
BuildRequires: desktop-file-utils
Requires: fcitx
Source44: import.info

%description
Light UI is a light-weight user interface for fcitx.

%prep
%setup -n %name-%version

%build
mkdir -pv build
pushd build
%fedora_cmake ..
make %{?_smp_mflags} VERBOSE=1

%install
pushd build
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
popd

desktop-file-install --delete-original \
  --dir $RPM_BUILD_ROOT%_datadir/applications \
  $RPM_BUILD_ROOT%_datadir/applications/fcitx-light.desktop

cat << EOF > %name.lang
%lang(zh) /usr/share/locale/zh_TW/LC_MESSAGES/fcitx-light-ui.mo
%lang(zh) /usr/share/locale/zh_CN/LC_MESSAGES/fcitx-light-ui.mo
EOF

%files -f %name.lang
%doc README COPYING AUTHORS
%_datadir/fcitx/configdesc/*.desc
%_datadir/fcitx/addon/*.conf
%_libdir/fcitx/*.so
%_datadir/applications/fcitx-light.desktop

%changelog
* Fri Sep 05 2014 Ilya Mashkin <oddity@altlinux.ru> 0.1.3-alt2
- build for Sisyphus

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1_6
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1_5
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1_4
- update to new release by fcimport

* Thu Dec 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1_3
- initial fc import

