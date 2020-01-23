%def_with cppunit

Name: xournalpp
Version: 1.0.16
Release: alt1
Summary: Handwriting note-taking software with PDF annotation support
Group: Office

License: GPLv2+
Url: https://github.com/%name/%name
Source: %name-%version.tar.gz

# Automatically added by buildreq on Thu Jan 23 2020
# optimized out: at-spi2-atk cmake cmake-modules cppunit fontconfig glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libalsa-devel libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libharfbuzz-devel libpango-devel libpoppler8-glib libsasl2-3 libstdc++-devel libwayland-client libwayland-cursor libwayland-egl pkg-config python-modules python2-base python3 python3-base sh4 shared-mime-info xorg-proto-devel zlib-devel
BuildRequires: cppunit-devel ctest fonts-bitmap-misc gcc-c++ git-core libXi-devel libgtk+3-devel libpoppler-glib-devel libportaudio2-devel libsndfile-devel libssl-devel libxml2-devel libzip-devel

%description
Xournal++ is a handwriting note-taking software with PDF annotation support.
Supports Pen input like Wacom Tablets

%package plugins
Summary: Default plugin for %name
BuildArch: noarch
Group: Office

%description plugins
The %name-plugins package contains sample plugins for  %name.

%package ui
Summary: User interface for %name
BuildArch: noarch
Group: Office

%description ui
The %name-ui package contains a graphical user interface for  %name.

%prep
%setup

#Fix tlh aka klingon language
mv po/tlh_AA.po po/tlh.po
sed -i 's|tlh-AA|tlh|g' po/tlh.po

%build
%if_with cppunit
%cmake -DENABLE_CPPUNIT=ON
%else
%cmake
%endif

%cmake_build

make -C BUILD test

%install
%cmakeinstall_std

%find_lang %name

#Remove scripts from icons interface
rm -r %buildroot%_datadir/%name/ui/icons/hicolor/update-icon-cache.sh
rm -r %buildroot%_datadir/%name/ui/iconsDark/hicolor/update-icon-cache.sh

%check
make -C BUILD test

%files -f %name.lang
%doc README.md AUTHORS
%_bindir/xournal-thumbnailer
%_bindir/%name
%_datadir/applications/com.github.%name.%name.desktop
%_datadir/icons/hicolor/scalable/apps/com.github.%name.%name.svg
%_datadir/icons/hicolor/scalable/mimetypes/*
%_datadir/mime/packages/com.github.%name.%name.xml
%exclude %_datadir/mimelnk/application/*
%_datadir/thumbnailers/com.github.%name.%name.thumbnailer
%dir %_datadir/%name
%_datadir/metainfo/com.github.%name.%name.appdata.xml

%files plugins
%_datadir/%name/plugins

%files ui
%_datadir/%name/ui

%changelog
* Thu Jan 23 2020 Fr. Br. George <george@altlinux.ru> 1.0.16-alt1
- Autobuild version bump to 1.0.16

* Thu Jan 23 2020 Fr. Br. George <george@altlinux.ru> 1.0.15-alt1
- Initial build from Fedora

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 1.0.16-9
- Rebuild for poppler-0.84.0

* Sun Jan 12 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 1.0.16-8
- Remove depreciate key in desktop file

* Mon Dec 16 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 1.0.16-7
- Remove architecture requirement for plugins and ui

* Mon Dec 16 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 1.0.16-6
- Fix typos

* Mon Dec 16 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 1.0.16-5
- Fix architecture requirement for ui

* Wed Dec 11 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 1.0.16-4
- Review fixes

* Wed Dec 11 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 1.0.16-3
- Add hicolor-icon-theme to requirement
- Use desktop file validation
- Split xournal data share into subpackages
- Review fixes

* Sun Nov 17 2019 Luya Tshimbalanga <luya@fedoraproject.org> 1.0.16-2
- Remove scripts from ui icons directory
- Relocate tlh locale directory

* Sun Nov 17 2019 Luya Tshimbalanga <luya@fedoraproject.org> 1.0.16-1
- Release 1.0.16
- Enable cppunit

* Sun Nov 10 2019 Luya Tshimbalanga <luya@fedoraproject.org> 1.0.15-2
- Update spec file based on review
- Include appstream data

* Sun Nov 10 2019 Luya Tshimbalanga <luya@fedoraproject.org> 1.0.15-1
- Release 1.0.15

* Tue Aug 13 2019 dfas <d.dfas@moens.cc> - 1.0.13-2.git7349762
- Release 1.0.13-current

* Tue Jun 25 2019 dfas <d.dfas@moens.cc> - 1.0.13-1.gita7f0275
- Release 1.0.13-current

* Fri May 3 2019 Francisco Gonzalez <gzmorell@gmail.com> - 1.0.10-1
- First attempt at packaging xournalpp.
