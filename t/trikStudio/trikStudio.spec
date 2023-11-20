%define _unpackaged_files_terminate_build 1
%set_verify_elf_method unresolved=relaxed

%def_without separate_trikruntime
%def_without sanitize
%def_without debug
%define appname trik-studio

Name: trikStudio
Version: 2022.2
Release: alt2.1
Summary: Intuitive programming environment robots
Summary(ru_RU.UTF-8): Интуитивно-понятная среда программирования роботов
License: Apache-2.0
Group: Education
Url: https://github.com/trikset/trik-studio

Source: %name-%version.tar
Patch: %name-%version-alt.patch
Patch1: gamepad.patch
Patch2: alt-ftbfs.patch
Patch3: fix-build-with-qt5-quazip1.patch
Patch4: trikRuntime.patch
Patch5: support-python3.11.patch

BuildRequires: gcc-c++ qt5-base-devel qt5-svg-devel qt5-script-devel qt5-multimedia-devel libusb-devel libudev-devel libgmock-devel
BuildRequires: libqscintilla2-qt5-devel zlib-devel python3-dev libhidapi-devel quazip-qt5-devel qt5-serialport-devel p7zip-standalone
# Workaround due project build with -fsanitize=undefined natively
# https://bugzilla.altlinux.org/show_bug.cgi?id=38106
#if_with sanitize
%ifnarch %e2k
BuildRequires: libubsan-devel-static
%endif
#endif
BuildRequires: rsync qt5-tools

Requires: libhidapi lego-mindstorms-udev-rules
Requires: %name-data = %version-%release
Conflicts: lib%name

%description
Intuitive programming environment allows you to program robots using a sequence
of pictures. With TRIK Studio programming is easy and fun.

TRIK Studio perfectly as universal for teaching programming, provided the
transition from the chart to the textual programming language that is planned to
implement the language of block diagrams. The environment is also implemented
programming robots Lego Mindsorms NXT 2.0 and EV3, but the possibility of such
robots are very limited in comparison with the TRIK.

%description -l ru_RU.UTF-8
Интуитивно-понятная среда программирования позволяет программировать роботов с
помощью последовательности картинок. С TRIK Studio программирование становится
простым и увлекательным.

TRIK Studio прекрасно подходит как универсальное ПО преподавания основ
программирования, предусмотрен переход от диаграмм к текстовым языкам
программирования, планируется реализация языка блок-схем. В среде также
реализовано программирование роботов Lego Mindsorms NXT 2.0 и EV3, но
возможности таких роботов сильно ограничены в сравнении с ТРИК.

%package data
Summary: Data files for %name
Group: Education
BuildArch: noarch

%description data
Data files for %name

%package -n trikRuntime
Summary: Trik runtime libraries for %name
Group: Education
BuildArch: noarch

%description -n trikRuntime
Trik runtime libraries for %name

%package -n trikRuntime-devel
Summary: Trik runtime development files for %name
Group: Education
BuildArch: noarch

%description -n trikRuntime-devel
Trik runtime development files for %name

%prep
%setup
%patch -p1
%ifarch %e2k
# workaround of SIGILL in ecf_opt64 from LCC 1.25.23
sed -i "s/QOverload<QObject\*>::of/(void(*)(QObject*))/" qrkernel/settingsListener.h
%endif
sed -e '2 a export LD_LIBRARY_PATH=%_libdir\/%name\/' -i installer/platform/trikStudio.sh
sed -e 's|^trik-studio|%_libdir/%name/trik-studio|' -i installer/platform/trikStudio.sh

tar -xf ./.gear/Box2D.tar.bz2
tar -xf ./.gear/trikRuntime.tar.bz2
tar -xf ./.gear/gamepad.tar.bz2
tar -xf ./.gear/qt-solutions.tar.bz2
tar -xf ./.gear/qslog.tar.bz2
tar -xf ./.gear/checkapp.tar.bz2
rm -rf qscintilla quazip

pushd thirdparty/gamepad
%patch1
popd

pushd plugins/robots/thirdparty/trikRuntime/trikRuntime
%patch4
popd

# Quick hack for python3.11 but think about using system pythonqt library.
%patch5 -p1

%ifarch loongarch64 riscv64
# gold does not work on these architectures
sed -e '/use_gold_linker/d' -i \
    global.pri \
    plugins/robots/thirdparty/trikRuntime/trikRuntime/global.pri
%endif

%build
%qmake_qt5 -r \
    LIBS+="`pkg-config --libs quazip1-qt5`" \
    INCLUDEPATH+="`pkg-config --cflags-only-I quazip1-qt5 |
      sed 's/-I//g'`" \
%if_with debug
    CONFIG+=debug CONFIG-=release \
%else
    CONFIG-=debug CONFIG+=release \
%endif
%ifarch %e2k
    CONFIG+=noPch CONFIG+=warn_off \
%endif
    QMAKE_LFLAGS+=-Wl,-rpath-link=%_builddir/%name-%version/bin/release \
    QMAKE_LFLAGS+=-Wl,-rpath=%_libdir/%name \
%if_with sanitize
    CONFIG+=!nosanitizers \
%endif
    CONFIG+=no_rpath \
    PREFIX=%_prefix LIBDIR=%_libdir TRIK_STUDIO_VERSION=%version studio.pro
%make_build

%install

for N in Kernel Network Hal Control ScriptRunner ; do
    [ -e bin/release/libtrik${N}.la ] || ln -sf libtrik${N}.so bin/release/libtrik${N}.la ||:
    [ -e bin/release/trik${N}.pc ] || echo > bin/release/trik${N}.pc ||:
done
%make_install INSTALL_ROOT=%buildroot install
mv %buildroot%_libdir/*.so* %buildroot%_libdir/%name
mv %buildroot%_bindir/trik-studio %buildroot%_libdir/%name/
ln -fs %name %buildroot%_bindir/trik-studio
%if_with separate_trikruntime
mv %buildroot%_prefix/lib/libqslog*.so* %buildroot%_libdir
mv %buildroot%_prefix/lib/libtrik*.so* %buildroot%_libdir
%else
rm -rf %buildroot%_sysconfdir/trik
rm -f %buildroot%_prefix/lib/libqslog*.so*
rm -f %buildroot%_prefix/lib/libtrik*.so*
rm -rf %buildroot%_datadir/trikRuntime
rm -rf %buildroot%_prefix/local/share/qslog/
rm -rf %buildroot%_includedir/trik*
rm -rf %buildroot%_includedir/qslog*
rm -rf %buildroot%_includedir/QsLog*
%endif
rm -f %buildroot%_prefix/lib/**.pc
rm -f %buildroot/lib/*PythonQt_QtAll* %buildroot/include/PythonQt_QtAll.h
rm -f %buildroot%_libdir/%name/plugins/tools/kitPlugins/librobots-null-interpreter.so

pushd bin/release
for d in examples help translations images; do
    cp -fr $d %buildroot%_datadir/%name/
done
#cp -fr trikSharp %buildroot%_libdir/%name/
cp -f gamepad %buildroot%_bindir/
mv -f %buildroot/opt/checkapp/bin/checkapp %buildroot%_bindir/
mkdir -p %buildroot%_datadir/%name/languages
cp -f ../../thirdparty/gamepad/gamepad/languages/*.qm %buildroot%_datadir/%name/languages/

popd

%files
%_bindir/*
%_libdir/%name
%_sysconfdir/%appname.config

%files data
%_datadir/%name
%_miconsdir/*
%_liconsdir/*
%_niconsdir/*
%_desktopdir/*
%doc LICENSE NOTICE README.md

%if_with separate_trikruntime
%files -n trikRuntime
%_sysconfdir/trik
%_libdir/libqslog*.so.*
%_libdir/libtrik*.so.*
%_datadir/trikRuntime

%files -n trikRuntime-devel
%_libdir/libqslog*.so
%_libdir/libtrik*.so
%_includedir/trik*
%_includedir/qslog*
%_includedir/QsLog*
%endif

%changelog
* Mon Nov 20 2023 Ivan A. Melnikov <iv@altlinux.org> 2022.2-alt2.1
- Don't use gold on loongarch64 and riscv64
- Allow building with multiple parallel processes

* Fri May 05 2023 Grigory Ustinov <grenka@altlinux.org> 2022.2-alt2
- Fixed build with python3.11.

* Tue Sep 27 2022 Valery Sinelnikov <greh@altlinux.org> 2022.2-alt1
- Update to 2022.2

* Mon Jul 25 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2022.1-alt3.1
- Fixed build for Elbrus

* Fri Jun 17 2022 Valery Sinelnikov <greh@altlinux.org> 2022.1-alt3
- Fixed building with gcc-12

* Thu Feb 10 2022 Valery Sinelnikov <greh@altlinux.org> 2022.1-alt2
- Removed build dependency libquazip-qt5-devel

* Wed Feb 09 2022 Valery Sinelnikov <greh@altlinux.org> 2022.1-alt1
- Update to 2022.1

* Mon Feb 07 2022 Valery Sinelnikov <greh@altlinux.org> 2021.2-alt3
- Rebuild with RPATH due upgraded lib.req which sets "library not found"
  warnings to errors.

* Tue Jan 25 2022 Grigory Ustinov <grenka@altlinux.org> 2021.2-alt2
- Fixed building with python3.10.

* Tue Jan 11 2022 Valery Sinelnikov <greh@altlinux.org> 2021.2-alt1
- Update to 2021.2

* Sun Jan 02 2022 Anton Midyukov <antohami@altlinux.org> 2021.1-alt4
- fix build with qt5-quazip1
- clean add_findreq_skiplist
- drop old Conflicts
- fix Requires

* Sat Oct 30 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2021.1-alt3
- Fixed build for Elbrus

* Thu Apr 29 2021 Evgeny Sinelnikov <sin@altlinux.org> 2021.1-alt2
- Set TRIK_STUDIO_VERSION to package version for cmake build.
- Add HomeLocation prefix in invariantPath() substitution for paths started with
  .config and .local substrings for backward compatibility.
- Remove user directories from system config options (set to default):
  + pathToGeneratorRoot to ~/.local/share/trik-studio/
  + pathToLogs to ~/.config/trik-studio/logs/

* Mon Apr 26 2021 Evgeny Sinelnikov <sin@altlinux.org> 2021.1-alt1
- Update to 2021.1

* Thu Feb 04 2021 Valery Sinelnikov <greh@altlinux.org> 2020.6-alt1
- Update to 2020.6

* Thu Oct 01 2020 Sergey V Turchin <zerg@altlinux.org> 2020.3-alt2
- build with Qt-5.15

* Fri Aug 21 2020 Valery Sinelnikov <greh@altlinux.org> 2020.4-alt1
- Update to 2020.4

* Tue Jun 09 2020 Valery Sinelnikov <greh@altlinux.org> 2020.3-alt1
- Update to 2020.3

* Thu Apr 30 2020 Valery Sinelnikov <greh@altlinux.org> 2020.1-alt3
- Changing the path of the language catalog with translation for the gamepad

* Thu Apr 23 2020 Valery Sinelnikov <greh@altlinux.org> 2020.1-alt2
- Build with latest gamepad sources
- Copy language directory with translation for gamepad (Closes: 38375)

* Fri Apr 17 2020 Valery Sinelnikov <greh@altlinux.org> 2020.1-alt1
- Update to 2020.1

* Thu Apr 09 2020 Valery Sinelnikov <greh@altlinux.org> 2019.8-alt8
- Fix gamepad segfault during close application

* Fri Mar 20 2020 Valery Sinelnikov <greh@altlinux.org> 2019.8-alt7
- Fix to load default platform config

* Wed Mar 18 2020 Valery Sinelnikov <greh@altlinux.org> 2019.8-alt6
- Replace /etc/trikStudio.config settings to global settingsDefaultValues

* Wed Mar 18 2020 Valery Sinelnikov <greh@altlinux.org> 2019.8-alt5
- Add requirement to libhidapi for ev3 robots plugin
- Fix null model removing

* Fri Mar 13 2020 Valery Sinelnikov <greh@altlinux.org> 2019.8-alt4
- Disable sanitize_undefined due it produces false positives with derived
  objects causing the runtime error member with call on address which does
  not point to an object of type.

* Tue Feb 18 2020 Valery Sinelnikov <greh@altlinux.org> 2019.8-alt3
- Build with workaround force requirement to libubsan-devel-static
- Add missed requirement to libquazip-qt5

* Sun Feb 16 2020 Valery Sinelnikov <greh@altlinux.org> 2019.8-alt2
- Build with explicitly enable gcc sanitize options needs
  libubsan-devel-static as build requirement

* Fri Feb 14 2020 Valery Sinelnikov <greh@altlinux.org> 2019.8-alt1
- Update to 2019.8
- Change license to Apache-2.0

* Thu Nov 21 2019 Valery Sinelnikov <greh@altlinux.org> 2019.6-alt1
- New version 2019.6

* Thu Jun 20 2019 Evgeny Sinelnikov <sin@altlinux.org> 3.2.0-alt3
- Fix program name in desktop file (Closes: 36823)

* Fri Feb 15 2019 Evgeny Sinelnikov <sin@altlinux.org> 3.2.0-alt2
- Fix installation on different 64-bit platforms via LIBDIR as qmake option

* Wed Feb 13 2019 Evgeny Sinelnikov <sin@altlinux.org> 3.2.0-alt1
- New version 3.2.0 with trikRuntime from trikset git submodule:
  https://github.com/trikset/trikRuntime

* Fri Jul 15 2016 Anton Midyukov <antohami@altlinux.org> 3.1.4-alt1
- New version 3.1.4
- Remove install.patch

* Tue Jun 21 2016 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt5.91af0cec.1
- New snapshot
- Replaced library
- Packages libtrikStudio, libtrikStudio-devel united into a package trikStudio.

* Sat Mar 26 2016 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt4.30210b3a.1
- Move config file from package trikStudio-data in package trikStudio
- Added conflict with libqscintilla2-qt4-devel.

* Wed Mar 23 2016 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt3.30210b3a.1
- fix install.patch

* Wed Mar 23 2016 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt2.30210b3a.1
- new package libtrikStudio
- rename package trikStudio-devel to libtrikStudio-devel

* Mon Mar 21 2016 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt1.30210b3a.1
- Fix altlinux-policy-shared-lib-contains-devel-so
- Exclude libqextserialport (it has in the repository)
- Diveded into 3 package

* Fri Mar 18 2016 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt0.1.30210b3a
- Initial build for ALT Linux Sisyphus (Closes: 31733).
