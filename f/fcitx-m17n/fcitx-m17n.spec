# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name: fcitx-m17n
Version: 0.1.3
Release: alt2
Summary: M17n Engine for Fcitx
Group: System/Libraries
Packager: Ilya Mashkin <oddity@altlinux.ru>
License: LGPLv2+
Url: http://code.google.com/p/fcitx/
Source0: http://fcitx.googlecode.com/files/%name-%version.tar.xz

BuildRequires: ctest cmake fcitx-devel gettext intltool libm17n-devel
Requires: fcitx
Source44: import.info

%description
Fcitx-m17n is a M17n engine wrapper for Fcitx.
It allows input of many languages using the
input table maps from m17n-db.

%prep
%setup -n %name-%version

%build
mkdir -pv build
pushd build
%fedora_cmake ..
make %{?_smp_mflags} VERBOSE=1
popd

%install
pushd build
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
popd

%find_lang %name

%files -f %name.lang
%doc COPYING
%_libdir/fcitx/%name.so
%_datadir/fcitx/addon/%name.conf
%_datadir/fcitx/configdesc/%name.desc
%_datadir/fcitx/m17n/default

%changelog
* Fri Sep 05 2014 Ilya Mashkin <oddity@altlinux.ru> 0.1.3-alt2
- build for Sisyphus

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1_3
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1_2
- update to new release by fcimport

* Thu Dec 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1_1
- initial fc import

