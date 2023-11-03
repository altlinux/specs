Name:     stacer
Version:  1.1.0
Release:  alt1.4

Summary:  Linux System Optimizer and Monitoring - https://oguzhaninan.github.io/Stacer-Web
License:  GPL-3.0
Group:    System/Configuration/Hardware
Url:      https://github.com/oguzhaninan/Stacer

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source:   %name-%version.tar
Patch1:  stacer-1.1.0-translation.patch
Patch2:  stacer-1.0.0-apt-rpm.patch
Patch3:  stacer-1.0.0-fixlscpu.patch
Patch4:  stacer-1.0.0-fix_warnings.patch

BuildRequires(pre): rpm-macros-cmake  rpm-macros-qt5
BuildRequires: cmake gcc-c++
BuildRequires: qt5-base-devel qt5-svg-devel qt5-charts-devel qt5-tools-devel 
Requires: util-linux

%description
%summary



%prep
%setup
%patch1 -p1
%patch2 -p2
%patch3 -p2
%patch4 -p1

%build
export PATH=$PATH:%_qt5_bindir
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

#-DCMAKE_BUILD_TYPE=Release
# translations
lupdate-qt5 stacer/stacer.pro -no-obsolete
lrelease-qt5 stacer/stacer.pro
install -d  stacer/translations
mv translations/*.qm stacer/translations



%install
export PATH=$PATH:%_qt5_bindir
%cmake_install

mkdir -p %buildroot%_datadir/%name/translations
cp stacer/translations/%{name}*.qm %buildroot%_datadir/%name/translations


%find_lang %name


%files
%_bindir/*
%doc *.md
%_iconsdir/*
%_desktopdir/*
%exclude %_target_libdir_noarch
%dir %_datadir/%name/
%_datadir/%name/*


%changelog
* Thu Nov 02 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.1.0-alt1.4
- NMU: trimmed build dependencies according to CMakeLists.txt.
  As a side effect package can be built for LoongArch.

* Fri Jun 03 2022 Hihin Ruslan <ruslandh@altlinux.ru> 1.1.0-alt1.3
- Add apt-rpm

* Thu Jun 02 2022 Hihin Ruslan <ruslandh@altlinux.ru> 1.1.0-alt1.2
- Correct Translations

* Wed Jun 01 2022 Hihin Ruslan <ruslandh@altlinux.ru> 1.1.0-alt1.1
- Correct BuildRequires

* Tue May 31 2022 Hihin Ruslan <ruslandh@altlinux.ru> 1.1.0-alt1
- Initial build for Sisyphus


