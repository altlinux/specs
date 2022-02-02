# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		fcitx-cloudpinyin
Version:	0.3.7
Release:	alt1
Summary:	Cloudpinyin module for fcitx
Group:		System/Libraries
License:	GPLv2+
URL:		https://fcitx-im.org/wiki/Cloudpinyin
Source0:	http://download.fcitx-im.org/fcitx-cloudpinyin/%{name}-%{version}.tar.xz

BuildRequires:	ctest cmake, fcitx-devel gettext gettext-tools, intltool, libcurl-devel
Requires:	fcitx, fcitx-pinyin
Source44: import.info

%description
Cloudpinyin is Fcitx addon that will add one candidate word to your pinyin
list. It current support four provider, Sogou, QQ, Baidu, Google.


%prep
%setup -q -n %{name}-%{version}


%build
mkdir -pv build
pushd build
%{fedora_cmake} ..
%make_build VERBOSE=1
popd

%install
pushd build
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
popd

%find_lang %{name}

%files -f %{name}.lang
%doc README COPYING 
%{_datadir}/fcitx/configdesc/*.desc
%{_datadir}/fcitx/addon/*.conf
%{_libdir}/fcitx/*.so


%changelog
* Wed Feb 02 2022 Ilya Mashkin <oddity@altlinux.ru> 0.3.7-alt1
- 0.3.7

* Mon Oct 30 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.5-alt1_1
- update to new version by fcimport

* Fri Sep 05 2014 Ilya Mashkin <oddity@altlinux.ru> 0.3.0-alt2
- build for Sisyphus

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_4
- update to new release by fcimport

* Fri May 31 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_3
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_2
- update to new release by fcimport

* Thu Dec 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_1
- initial fc import

