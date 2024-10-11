%define _unpackaged_files_terminate_build 1

Name: gpui
Version: 0.2.55
Release: alt1

Summary: Group policy editor
License: GPLv2+
Group: Other
Url: https://github.com/august-alt/gpui

BuildRequires: cmake
BuildRequires: rpm-macros-cmake
BuildRequires: cmake-modules
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-declarative-devel
BuildRequires: qt5-tools-devel
BuildRequires: libsmbclient-devel libsmbclient

BuildRequires: samba-devel
BuildRequires: libldap-devel
BuildRequires: libsasl2-devel
BuildRequires: libsmbclient-devel
BuildRequires: libuuid-devel
BuildRequires: glib2-devel
BuildRequires: libpcre-devel
BuildRequires: libkrb5-devel
BuildRequires: libgtest-devel

BuildRequires: qt5-base-common
BuildRequires: doxygen
BuildRequires: libxerces-c-devel
BuildRequires: xsd
BuildRequires: boost-devel-headers

BuildRequires: desktop-file-utils ImageMagick-tools

BuildRequires: libqt-mvvm-devel

BuildRequires: xorg-xvfb xvfb-run

Requires: admx-basealt

Source0: %name-%version.tar

%description
Group policy editor

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

cd %_cmake__builddir
desktop-file-install --dir=%buildroot%_desktopdir \
                     --set-key Exec --set-value %_bindir/gpui-main \
                     ../setup/gpui.desktop

for size in 48 64 128 256 512; do
    mkdir -p %buildroot%_datadir/icons/hicolor/''${size}x''${size}/apps/
    convert ../setup/logo_1024_1024.png -resize ''${size}x''${size} \
    %buildroot%_datadir/icons/hicolor/''${size}x''${size}/apps/gpui.png
done

install -v -p -m 644 -D ../setup/man/en/gpui.1 %buildroot%_man1dir/gpui.1
install -v -p -m 644 -D ../setup/man/ru/gpui.1 %buildroot%_mandir/ru/man1/gpui.1

export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:%_libdir/gpui/plugins/

LD_PRELOAD=%buildroot%_libdir/gpui/plugins/libadministrative-templates-plugin.so

%files
%doc README.md
%doc INSTALL.md
%_bindir/gpui-main

%_libdir/libgpui-core.so
%_libdir/libgpui-gui.so
%_libdir/libgpui-io.so
%_libdir/libgpui-ldap.so

%_libdir/gpui/plugins/libadministrative-templates-plugin.so
%_libdir/gpui/plugins/libpreferences-plugin.so

%_libdir/gpui/plugins/libadml-plugin.so
%_libdir/gpui/plugins/libadmx-plugin.so
%_libdir/gpui/plugins/libcmtl-plugin.so
%_libdir/gpui/plugins/libcmtx-plugin.so
%_libdir/gpui/plugins/libinifile-plugin.so
%_libdir/gpui/plugins/libinifile-ascii-plugin.so
%_libdir/gpui/plugins/libreg-plugin.so
%_libdir/gpui/plugins/libspol-plugin.so
%_libdir/gpui/plugins/libpol-plugin.so
%_libdir/gpui/plugins/libscripts-plugin.so

%_libdir/gpui/plugins/libsmb-storage-plugin.so

%_datadir/icons/hicolor/48x48/apps/gpui.png
%_datadir/icons/hicolor/64x64/apps/gpui.png
%_datadir/icons/hicolor/128x128/apps/gpui.png
%_datadir/icons/hicolor/256x256/apps/gpui.png
%_datadir/icons/hicolor/512x512/apps/gpui.png

%_desktopdir/gpui.desktop

%_man1dir/gpui.*
%_mandir/ru/man1/gpui.*

%changelog
* Fri Oct 11 2024 Vladimir Rubanov <august@altlinux.org> 0.2.55-alt1
- 0.2.54-alt1
- Fixes:
  + Fix list values dialog (Closes: 51681).

* Mon Oct 4 2024 Vladimir Rubanov <august@altlinux.org> 0.2.54-alt1
- 0.2.54-alt1
- Fixes:
  + Fix list values saving in administrative templates (Closes: 51587).

* Mon Sep 16 2024 Vladimir Rubanov <august@altlinux.org> 0.2.53-alt1
- 0.2.53-alt1
- Fixes:
  + Fix add ascii ini file plugin (Closes: 51451, 51466, 47576).

* Fri Sep 13 2024 Vladimir Rubanov <august@altlinux.org> 0.2.52-alt1
- 0.2.52-alt1
- Fixes:
  + Fix comment path on smb share.
  + Fix group policy template name.

* Fri Sep 13 2024 Vladimir Rubanov <august@altlinux.org> 0.2.51-alt1
- 0.2.51-alt1
- Fixes:
  + Fix group policy template name in scripts dialog.

* Mon Sep 2 2024 Vladimir Rubanov <august@altlinux.org> 0.2.50-alt1
- 0.2.50-alt1
- Fixes:
  + Fix group policy template version update.

* Wed Aug 28 2024 Vladimir Rubanov <august@altlinux.org> 0.2.49-alt1
- 0.2.49-alt1
- Fixes:
  + Add support for smb located comments.

* Tue Aug 20 2024 Vladimir Rubanov <august@altlinux.org> 0.2.48-alt1
- 0.2.48-alt1
- Fixes:
  + Fix order of pol instructions in internal storage.
  + Fix list based policies (Closes: 50123).
  + Fix comment values (Closes: 47576).
  + Fix script settings description (Closes: 49099).

* Tue Aug 6 2024 Vladimir Rubanov <august@altlinux.org> 0.2.47-alt1
- 0.2.47-alt1
- Fixes:
  + Fix pol parser validation.

* Tue Aug 6 2024 Vladimir Rubanov <august@altlinux.org> 0.2.46-alt1
- 0.2.46-alt1
- Fixes:
  + Fix saving of square brakets in pol file (Closes: 50706).
  + Fix checkbox based policies (Closes: 48970, 47742).

* Fri Jun 6 2024 Vladimir Rubanov <august@altlinux.org> 0.2.45-alt1
- 0.2.45-alt1
- Fixes:
  + Fix creation of gpt.ini while saving.

* Fri Apr 1 2024 Vladimir Rubanov <august@altlinux.org> 0.2.44-alt1
- 0.2.44-alt1
- Fixes:
  + Fix admx-firefox elements order (Closes: 47727).
  + Fix memory leak in ini plugin.
  + Fix file widget in preferences plugin.

* Fri Mar 15 2024 Vladimir Rubanov <august@altlinux.org> 0.2.43-alt1
- 0.2.43-alt1
- Fixes:
  + Fix build with samba 4.20.rc4.

* Wed Mar 6 2024 Vladimir Rubanov <august@altlinux.org> 0.2.42-alt1
- 0.2.42-alt1
- Features:
  + Add environment variables dialog to preferences.

* Tue Feb 29 2024 Vladimir Rubanov <august@altlinux.org> 0.2.41-alt1
- 0.2.41-alt1
- Features:
  + Add edit entry to preferences context menu (Closes: 49098).
- Fixes:
  + Fix admx-firefox elements order (Closes: 44507).
  + Fix text elements order (Closes: 49053).

* Tue Dec 26 2023 Vladimir Rubanov <august@altlinux.org> 0.2.40-alt1
- 0.2.40-alt1
- Fixes:
  + Fix replace path with name in script dialog.

* Mon Dec 25 2023 Vladimir Rubanov <august@altlinux.org> 0.2.39-alt1
- 0.2.39-alt1
- Fixes:
  + Fix add script dialog.
  + Fix script's folder creation.

* Fri Oct 13 2023 Vladimir Rubanov <august@altlinux.org> 0.2.38-alt1
- 0.2.38-alt1
- Fixes:
  + Fix ldap guid path.

* Fri Oct 13 2023 Vladimir Rubanov <august@altlinux.org> 0.2.37-alt1
- 0.2.37-alt1
- Fixes:
  + Fix "both" policy type.
  + Fix extensions guid in gpc.

* Mon Oct 09 2023 Vladimir Rubanov <august@altlinux.org> 0.2.36-alt1
- 0.2.36-alt1
- Fixes:
  + Emergency fix for invalid pol files.

* Thu Oct 05 2023 Vladimir Rubanov <august@altlinux.org> 0.2.35-alt1
- 0.2.35-alt1
- Fixes:
  + Fix subsequent deletion of multiple elements in scripts dialog (Closes: 47553).
  + Fix desktop file entry.
  + Fix add folder name to script path.

* Mon Sep 04 2023 Vladimir Rubanov <august@altlinux.org> 0.2.34-alt1
- 0.2.34-alt1
- Fixes:
  + Fix translations language list (Closes: 47437).
  + Fix translations for comment in administrative templates plugin (Fixes: 109650).
  + Fix scripts encoding to UTF-16LE.
  + Remove browse button from add script widget.

* Fri Sep 01 2023 Vladimir Rubanov <august@altlinux.org> 0.2.33-alt1
- 0.2.33-alt1
- Fixes:
  + Fix translations for path and parameters in scripts plugin (Closes: 47133).
  + Fix show files button in scripts plugin (Closes: 47136).
  + Fix list parameters in administrative templates plugin (Closes: 47137).
- Features:
  + New logging system.

* Fri Jul 21 2023 Vladimir Rubanov <august@altlinux.org> 0.2.32-alt1
- 0.2.32-alt1
- Features:
  + Implement support of platforms in filter dialog.

* Wed Jul 19 2023 Vladimir Rubanov <august@altlinux.org> 0.2.31-alt1
- 0.2.31-alt1
- Fixes:
  + Fix scripts plugin.

* Fri Jul 14 2023 Vladimir Rubanov <august@altlinux.org> 0.2.30-alt1
- 0.2.30-alt1
- Fixes:
  + Fix comments plugin.

* Thu Jul 13 2023 Vladimir Rubanov <august@altlinux.org> 0.2.29-alt1
- 0.2.29-alt1
- Fixes:
  + Add comments support.

* Wed Jun 21 2023 Vladimir Rubanov <august@altlinux.org> 0.2.28-alt1
- 0.2.28-alt1
- Fixes:
  + Fix update of administrative templates filter dialog.

* Tue Jun 20 2023 Vladimir Rubanov <august@altlinux.org> 0.2.27-alt1
- 0.2.27-alt1
- Features:
  + Implement administrative templates filter dialog.

* Wed Jun 07 2023 Vladimir Rubanov <august@altlinux.org> 0.2.26-alt1
- 0.2.26-alt1
- Fixes:
  + Fix policies with value name only. (Closes: 46082).
  + Fix namespaces. (Closes: 46282).

* Fri May 19 2023 Vladimir Rubanov <august@altlinux.org> 0.2.25-alt1
- 0.2.25-alt1
- Fixes:
  + Fix application launch without arguments (Closes: 46189).

* Tue Apr 11 2023 Vladimir Rubanov <august@altlinux.org> 0.2.24-alt1
- 0.2.24-alt1
- Fixes:
  + Fix laguage loading in plugins.
  + Fix tests.

* Wed Apr 05 2023 Vladimir Rubanov <august@altlinux.org> 0.2.23-alt1
- 0.2.23-alt1
- Fixes:
  + Fix support for files without extensions in files preference.

* Wed Mar 29 2023 Vladimir Rubanov <august@altlinux.org> 0.2.22-alt1
- 0.2.22-alt1
- Fixes:
  + Fix policy path in scripts plugin.

* Mon Mar 27 2023 Vladimir Rubanov <august@altlinux.org> 0.2.21-alt1
- 0.2.21-alt1
- Fixes:
  + Add button to clear key sequence in shortcuts widget.
  + Fix typos in folder preferences.
  + Fix writing script to smb shares.

* Sun Mar 05 2023 Vladimir Rubanov <august@altlinux.org> 0.2.20-alt1
- 0.2.20-alt1
- Fixes:
  + Fix policy's key search for lists in administrative templates.

* Sun Mar 05 2023 Vladimir Rubanov <august@altlinux.org> 0.2.19-alt1
- 0.2.19-alt1
- Fixes:
  + Replace std::regex with QRegularExpression in scripts module.

* Thu Jan 19 2023 Vladimir Rubanov <august@altlinux.org> 0.2.18-alt1
- 0.2.18-alt1
- Features:
  + Implement scripts module.

* Thu Jan 19 2023 Vladimir Rubanov <august@altlinux.org> 0.2.17-alt18
- 0.2.17-alt18
- Fixes:
  + Fix input in section field in ini widget on delete action.
  + Fix set default setting to true for user context in user policies.

* Thu Jan 12 2023 Vladimir Rubanov <august@altlinux.org> 0.2.17-alt17
- 0.2.17-alt17
- Fixes:
  + #91098 Fix translations for shortcuts widget on KDE systems.

* Tue Jan 10 2023 Vladimir Rubanov <august@altlinux.org> 0.2.17-alt16
- 0.2.17-alt16
- Fixes:
  + #91098 Fix translations for shortcuts widget.
  + #88126 Implement shortcuts key sequence encoding.

* Wed Dec 28 2022 Vladimir Rubanov <august@altlinux.org> 0.2.17-alt15
- 0.2.17-alt15
- Fixes:
  + #91635 Fix e2k preferences build.
  + #91629 Fix translations on e2kv4.
  + #75874 Change spinbox behaviour to mimic windows behaviour.
  + #89621 Fix typo in ini widget.
  + #91060 Fix OK and Cancel buttons to work in a message box.

* Mon Dec 26 2022 Vladimir Rubanov <august@altlinux.org> 0.2.17-alt14
- 0.2.17-alt14
- Fixes:
  + #91097 Fix names of hidden and archive fields in folder widget.
  + #91237 Remove sorting in table header.
  + #90987 Fix status bar message.
  + #91312 Add translation to '-n' command line option.
  + #91047 Fix segmentation fault in the absence of kerberos tickets.

* Thu Dec 15 2022 Vladimir Rubanov <august@altlinux.org> 0.2.17-alt13
- 0.2.17-alt13
- Fixes:
  + Fix presentation builder to allow build on e2k.

* Thu Dec 15 2022 Vladimir Rubanov <august@altlinux.org> 0.2.17-alt12
- 0.2.17-alt12
- Fixes:
  + Fix e2k build.

* Fri Dec 09 2022 Vladimir Rubanov <august@altlinux.org> 0.2.17-alt11
- 0.2.17-alt11
- Fixes:
  + #89597 Fix message box.
  + #88897 Ask to save changes.
  + #75885 Add sort to drop down list elements.
  +        Fix set correct resource for non existent registry.pol files.
  +        Fix copy policy to copied item.
  + #76835 Fix policy names.
  + #88907 Fix google chrome policies handling.

* Tue Dec 06 2022 Vladimir Rubanov <august@altlinux.org> 0.2.17-alt10
- 0.2.17-alt10
- Fixes:
  + #89553 Switch search to be case insensitive.
  + #89558 Fix translations of shortcuts widget.
  + #89561 Fix russian translations in properties widget.
  + #89621 Fix ini file's widget translations.
  + #89692 Fix translation of shortcuts widget.
  + #89648 Fix russian translation of shares widget.
  + #89648 Fix russian translation of common widget.

* Wed Nov 30 2022 Vladimir Rubanov <august@altlinux.org> 0.2.17-alt9
- 0.2.17-alt9
- Fixes:
  + Fix null pointer in ldap library.
  + Fix invalid drive name.

* Tue Nov 29 2022 Vladimir Rubanov <august@altlinux.org> 0.2.17-alt8
- 0.2.17-alt8
- Fixes:
  + #88602 Fix creation of network share's attributes.
  + #88794 Fix drive map's xml structure.
  + #44378 Allow empty section name in ini widget.
  + #74009 Remove labels in empty widget.
  + #88711 Modify model builder of network shares to write only required fields.
  + #88844 Fix save of admx path setting.

* Wed Nov 16 2022 Vladimir Rubanov <august@altlinux.org> 0.2.17-alt7
- 0.2.17-alt7
- Fixes:
  + #88813 Fix restore dependency on admx-basealt.
  + #88495 Fix translations in environment variable widget.
  + #88226 Fix folder creation.
  + #88143 Fix folder attributes during deletion of folders.
  + #88586 Fix russian translation of mapped drive context menu.

* Wed Nov 16 2022 Vladimir Rubanov <august@altlinux.org> 0.2.17-alt6
- 0.2.17-alt6
  Features:
  + Add mapped drives for computers and network shares for user.

* Wed Nov 16 2022 Vladimir Rubanov <august@altlinux.org> 0.2.17-alt5
- 0.2.17-alt5
- Fixes:
  + #88226 Fix inability to create folders.
  + #88226 Fix inability to create files.
  + Restore n option.

* Fri Nov 11 2022 Vladimir Rubanov <august@altlinux.org> 0.2.17-alt4
- 0.2.17-alt4
- Features:
  + Add custom tree view for preferences.

* Fri Nov 11 2022 Vladimir Rubanov <august@altlinux.org> 0.2.17-alt3
- 0.2.17-alt3
- Fixes:
  + #74208 Fix group policy name.
  + Fix translations in administrative templates plugin.

* Thu Nov 10 2022 Vladimir Rubanov <august@altlinux.org> 0.2.17-alt2
- 0.2.17-alt2

* Thu Nov 03 2022 Vladimir Rubanov <august@altlinux.org> 0.2.17-alt1
- 0.2.17

* Thu Sep 29 2022 Vladimir Rubanov <august@altlinux.org> 0.2.16-alt1
- Fixes:
  + #84127 Fix invalid types for list enums.
  + #76835 Fix message on policy state change.

* Thu Aug 04 2022 Vladimir Rubanov <august@altlinux.org> 0.2.15-alt1
- Fixes:
  + #81760 Fix disabled and enabled list in policies.

* Mon Apr 18 2022 Vladimir Rubanov <august@altlinux.org> 0.2.14-alt1
- Fixes:
  + Vesioning improved.
  + Fixed build on e2k platform.

* Fri Apr 04 2022 Vladimir Rubanov <august@altlinux.org> 0.2.0-alt13
- Fixes:
  + #75065 Add workaround for bug #75065.

* Fri Mar 31 2022 Vladimir Rubanov <august@altlinux.org> 0.2.0-alt12
- Fixes:
  + Fix -n command line option.

* Fri Mar 30 2022 Vladimir Rubanov <august@altlinux.org> 0.2.0-alt11
- Fixes:
  + #74198 Improve ability to detect policy changes and notify user about them.
  + #74149 Fix install/removal of packages through list element.
  + #74217 Add switch between elements through keyboard.
  + #75076 Fix -b option.
  + #75070 Add decimal text box minimum and maximum.
  + #75065 Add message boxes for access errors.
  + Fix several build issues on e2k platform.

* Fri Mar 25 2022 Vladimir Rubanov <august@altlinux.org> 0.2.0-alt10
- Fixes:
  + #74754 Fix ability to generate pol setting for "both" policy type.
  + #74151 Fix generate Chromium/Firefox start page in pol file.
  + #75062 Prevent doubling of items in drop list.
  + #75058 Fix command name in manual.
  + #75062 Remove icons from OK/Cancel buttons.
  + #75035 Set fixed container height for label.

* Fri Mar 18 2022 Vladimir Rubanov <august@altlinux.org> 0.2.0-alt9
- Fixes:
  + Fix segmentation fault on selecting new policy item.
  + Fix translation of message box window.

* Wed Mar 16 2022 Vladimir Rubanov <august@altlinux.org> 0.2.0-alt8
- Fixes:
  + #74163 Fix segmentation fault on selecting item in "security category".
  + #74704 Fix window resize on label resize.
  + #74050 Fix cancel buttons translation.
  + #74050 Man was added.

* Mon Mar 14 2022 Vladimir Rubanov <august@altlinux.org> 0.2.0-alt7
- Fixes:
  + #74215 Add message for the change of policy's state.
  + #74217 Add ability to select policies with keyboard.
  + #74208 Add policy name label.
  + #74172 Make list dialog modal.
  + #74005 Remove empty folders from tree view.
  + #74015 Add ability to resize right frame.
  + #74028 Remove --help-all command argument.
  + #74046 Improve sort order of tree view.
  + #74054 Fix ability to save integer values.

* Tue Mar 01 2022 Vladimir Rubanov <august@altlinux.org> 0.2.0-alt6
- Fixes:
  + #74114 Fix ability to load ADMX bundle.

* Mon Feb 28 2022 Vladimir Rubanov <august@altlinux.org> 0.2.0-alt5
- Fixes:
  + #73976 Correct dialog flags to provide ability to select folders.
  + #73977 Switch to Qt based dialog to add application icon to dialog.
  + #73617 Fix bug with caption in about window.
  + #74027 Fix version command.
  + #74048 Fix English translation of help menu.
  + #74052 Fix remove empty strings from multi-string.
  + #74051 Fix saving of language settings.
  + #74002 Fix saving of admx settings.

* Mon Feb 21 2022 Vladimir Rubanov <august@altlinux.org> 0.2.0-alt4
- Fixes:
  + #73754 Fix translations in open admx dialog.
  + #73747 Fix translation of command line options.
  + #73625 Fix add application icon.
  + #73788 Fix add admx-basealt to spec.
  + #73738 Fix add manual.

* Fri Feb 18 2022 Vladimir Rubanov <august@altlinux.org> 0.2.0-alt3
- Fixes:
  + #73617 Fix difference of about window from that of ADMC.
  + #73627 Fix invalid header of the main window.
  + #73629 Fix absent translation of program icon in start menu.
  + Fix disabling and non configuring policies.

* Wed Feb 17 2022 Vladimir Rubanov <august@altlinux.org> 0.2.0-alt2
- Fixes:
  + Fix string saving to pol file.

* Wed Feb 16 2022 Vladimir Rubanov <august@altlinux.org> 0.2.0-alt1
- 0.2.0
- Features:
  + Implement signal based save system.
  + Introduce policy element types into policy elements.
- Fixes:
  + Fix combo box indices and values.

* Tue Feb 01 2022 Vladimir Rubanov <august@altlinux.org> 0.1.0-alt2
- A first implementation of smb routines.

* Mon Jul 05 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0-alt1
- Initial build
