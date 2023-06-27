# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat rpm-macros-ninja-build
BuildRequires: /usr/bin/desktop-file-install libncurses-devel qt5-base-devel libreadline-devel pkgconfig(libusb-1.0)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		android-file-transfer
Version:	4.2
Release:	alt1_2
Summary:	Reliable Android MTP client with minimalist UI
Group:		Development/Tools
License:	LGPLv2+
URL:		https://github.com/whoozle/android-file-transfer-linux
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:		android-file-transfer-4.2-gcc13.patch

BuildRequires:	libappstream-glib
BuildRequires:	ccmake cmake ctest
BuildRequires:	desktop-file-utils
BuildRequires:	gcc-c++
BuildRequires:	ninja-build
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Help)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(fuse)
BuildRequires:	pkgconfig(openssl)
#BuildRequires:	pkgconfig(readline)
BuildRequires:	pkgconfig(taglib)
Source44: import.info

%description
Android File Transfer for Linux a.. reliable MTP client with minimalist UI
similar to Android File Transfer for Mac.
Features:
- Simple Qt UI with progress dialogs.
- FUSE wrapper (If you'd prefer mounting your device), supporting partial
  read/writes, allowing instant access to your files.
- No file size limits.
- Automatically renames album cover to make it visible from media player.
- USB 'Zerocopy' support found in recent Linux kernel
- No extra dependencies (e.g. libptp/libmtp).
- Command line tool (aft-mtp-cli)

%prep
%setup -q -n %{name}-linux-%{version}
%patch -p2

%build
%{mageia_cmake} -GNinja
%ninja_build -C %{_vpath_builddir}

%install
%ninja_install -C %{_vpath_builddir}

find %{buildroot} -name '*.a' -delete

desktop-file-install                                       \
    --remove-category="System"                             \
    --remove-category="Filesystem"                         \
    --delete-original                                      \
    --dir=%{buildroot}%{_datadir}/applications             \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%files
%doc README.md FAQ.md
%doc --no-dereference LICENSE
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.appdata.xml
%{_iconsdir}/hicolor/*/apps/%{name}.png


%changelog
* Tue Jun 27 2023 Anton Midyukov <antohami@altlinux.org> 4.2-alt1_2
- NMU: fix buildrequires
- NMU: fix build with gcc13

* Mon Jan 25 2021 Igor Vlasenko <viy@altlinux.ru> 4.2-alt1_1
- new version

* Mon Dec 28 2020 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_1
- new version

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 3.9-alt1_3
- fixed build

* Sun Jul 07 2019 Igor Vlasenko <viy@altlinux.ru> 3.9-alt1_1
- update by mgaimport

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 3.8-alt1_1
- update by mgaimport

* Thu Apr 25 2019 Igor Vlasenko <viy@altlinux.ru> 3.7-alt2_2
- update by mgaimport

* Thu Mar 14 2019 Igor Vlasenko <viy@altlinux.ru> 3.7-alt2_1
- fixed build

* Mon Jan 07 2019 Igor Vlasenko <viy@altlinux.ru> 3.7-alt1_1
- new version

