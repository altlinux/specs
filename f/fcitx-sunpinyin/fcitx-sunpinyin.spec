# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:			fcitx-sunpinyin
Version:		0.4.1
Release:		alt2
Summary:		Sunpinyin Wrapper for Fcitx
Packager: Ilya Mashkin <oddity@altlinux.ru>
Group:			System/Libraries
License:		GPLv2+
URL:			http://fcitx-im.org/wiki/Fcitx
Source0:		http://download.fcitx-im.org/%{name}/%{name}-%{version}.tar.xz

BuildRequires: ctest cmake
BuildRequires:	fcitx-devel
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	sunpinyin-devel
BuildRequires:	libdbus-devel
BuildRequires:	libtool
BuildRequires:	sunpinyin
BuildRequires:	fcitx
Requires:		fcitx
Requires:		fcitx-data
Source44: import.info

%description
Fcitx-sunpinyin is a Sunpinyin Wrapper for Fcitx.

SunPinyin is an SLM (Statistical Language Model) based input method
engine. To model the Chinese language, it use a backoff bigram and
trigram language model. 

%prep
%setup -q -n %{name}-%{version}


%build
mkdir -pv build
pushd build
%{fedora_cmake} ..
make %{?_smp_mflags}
popd

%install
pushd build
make install DESTDIR=$RPM_BUILD_ROOT
popd

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README COPYING 
%{_libdir}/fcitx/%{name}.so
%{_datadir}/fcitx/addon/%{name}.conf
%{_datadir}/fcitx/inputmethod/sunpinyin.conf
%{_datadir}/fcitx/configdesc/%{name}.desc
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/fcitx/skin/classic/sunpinyin.png
%{_datadir}/fcitx/skin/dark/sunpinyin.png
%{_datadir}/fcitx/skin/default/sunpinyin.png
%{_datadir}/fcitx/imicon/sunpinyin.png


%changelog
* Fri Sep 05 2014 Ilya Mashkin <oddity@altlinux.ru> 0.4.1-alt2
- build for Sisyphus

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_3
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_2
- update to new release by fcimport

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_1
- update to new release by fcimport

* Wed May 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1_1
- initial fc import

