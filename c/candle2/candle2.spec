%define _unpackaged_files_terminate_build 1
%define candle2_prefix %_libdir/%name
%global appname Candle2

Name: candle2
Version: 2.4
Release: alt4

Summary: GRBL control interface in Qt
License: GPL-3.0-only
Group: Engineering
Url: https://github.com/Schildkroet/Candle2
VCS: https://github.com/Schildkroet/Candle2

# Source-url: https://github.com/Schildkroet/%appname/archive/refs/tags/V%version.tar.gz
Source: %name-%version.tar
Patch0: alt-fix-app-startup-errors.patch
Patch1: alt-fix-incorrect-window-scaling.patch
Patch2: alt-add-external-qmake-vars.patch
Patch3: alt-use-correct-file-extension-on-save.patch

BuildRequires: qt5-serialport-devel

%description
GRBL and GRBL-Advanced controller application with G-Code visualizer
written in Qt. Forked from denvi/Candle.

Supported functions:
    * Controlling GRBL-based CNC-Machine via console commands, buttons
    on form and numpad.
    * Monitoring cnc-machine state.
    * Loading, editing, saving and sending of G-code files to
    CNC-Machine.
    * Visualizing G-code files.

%prep
%setup
%autopatch -p1

%build
%qmake_qt5 \
    APP_VERSION=%version \
    APP_DATADIR=%_datadir/%name \
    APP_DOCDIR=%_defaultdocdir/%name-%version \
    -o Makefile src/candle2.pro \
    #
%make_build

%install
%__mkdir_p %buildroot{%_bindir,%_desktopdir}
%__mv Candle2 %name
%__install -Dpm 755 %name %buildroot%candle2_prefix/%{name}-bin

cat>%buildroot%_bindir/%name<<-EOF
#!/bin/sh

export QT_QPA_PLATFORM=xcb
%candle2_prefix/%{name}-bin \${1:+"\$@"}
EOF
%__chmod +x %buildroot%_bindir/%name

pushd src/images >/dev/null
for i in candle_*.png ; do
    sz=`echo $i | sed 's;candle_\([[:digit:]]\+\)\.png;\1;'`
    %__install -Dpm 644 $i %buildroot%_iconsdir/hicolor/${sz}x${sz}/apps/%name.png
done
popd

%__cat > %name.desktop <<EOF
[Desktop Entry]
Name=%appname
TryExec=%name
Exec=%name
Type=Application
Icon=%name
Categories=Graphics;Engineering;
MimeType=text/plain;
EOF
%__install -Dpm 644 %name.desktop %buildroot%_desktopdir/

%files
%doc Readme.md LICENSE
%_bindir/%name
%candle2_prefix
%_desktopdir/%name.desktop
%_iconsdir/hicolor/**/apps/%name.png

%changelog
* Fri May 15 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 2.4-alt4
- added filename checking on save (closes: 57211)
- fixed fullscreen window opening at 800x600 resolution (closes: 56511)

* Thu Nov 27 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 2.4-alt3
- renamed the application window title from "candle2-bin" to "Candle2"
- fixed missing license text in the application help
- fixed the version displayed in the application help (closes: 57038)
- fixed application window scaling on 1024x768 displays

* Mon Nov 24 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 2.4-alt2
- fixed errors on launch and the transparent window
  that appeared in place of the model (closes: 56510)
- fixed scaling for 4:3 displays (closes: 56511)

* Wed Jun 18 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 2.4-alt1
- Initial build for ALT Linux (closes: 54722)
