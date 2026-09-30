%define _unpackaged_files_terminate_build 1

%def_without check

Name: ibus-typing-booster
Version: 2.31.1
Release: alt1

Summary: Intelligent typing completion input method for IBus
License: GPL-3.0-or-later AND Apache-2.0
Group: System/Internationalization
URL: https://github.com/mike-fabian/ibus-typing-booster
VCS: https://github.com/mike-fabian/ibus-typing-booster.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gettext-tools
BuildRequires: libibus-devel
BuildRequires: python3-devel

%if_with check
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
%endif

Requires: ibus
Requires: libm17n
Requires: libm17n-db

%description
IBus Typing Booster is a predictive input method for the IBus input
framework.

It provides context-sensitive word completion, spell checking,
dictionary support, emoji input, Unicode character input and support
for many input methods using m17n.

The input method learns from user input and can suggest words based
on previously typed text.

%package -n emoji-picker
Summary: Unicode emoji picker from IBus Typing Booster
Group: System/Internationalization

Requires: %name = %EVR
Requires: python3-module-pygobject3

%description -n emoji-picker
Emoji Picker is a graphical Unicode emoji selection utility shipped
with IBus Typing Booster.

It allows searching and selecting emoji and other Unicode characters.

%prep
%setup

%build
autoreconf -fiv

%configure \
    --libexecdir=%_libexecdir/ibus

%make_build

%install
%makeinstall_std

# Remove libtool files if upstream installs any.
find %buildroot -name '*.la' -delete

%find_lang %name

%check
# Keep the initial ALT package checks reasonably small.
# The complete upstream test suite requires a running DBus/dconf
# session, additional m17n data and several Hunspell dictionaries.

if command -v appstream-util >/dev/null 2>&1; then
    find %buildroot%_datadir/metainfo \
        -type f -name '*.xml' \
        -exec appstream-util validate-relax --nonet '{}' \;
fi

if command -v desktop-file-validate >/dev/null 2>&1; then
    find %buildroot%_datadir/applications \
        -type f -name '*.desktop' \
        -exec desktop-file-validate '{}' \;
fi

%files -f %name.lang
%doc README LICENSE
%_datadir/ibus-typing-booster/
%_datadir/ibus/component/typing-booster.xml
%_datadir/metainfo/org.freedesktop.ibus.engine.typing_booster.metainfo.xml
%_libexecdir/ibus/ibus-engine-typing-booster
%_libexecdir/ibus/ibus-setup-typing-booster
%_datadir/applications/ibus-setup-tb.desktop
%_datadir/applications/ibus-setup-typing-booster.desktop
%_datadir/glib-2.0/schemas/org.freedesktop.ibus.engine.typing-booster.gschema.xml
%_datadir/icons/hicolor/16x16/apps/ibus-typing-booster.png
%_datadir/icons/hicolor/22x22/apps/ibus-typing-booster.png
%_datadir/icons/hicolor/32x32/apps/ibus-typing-booster.png
%_datadir/icons/hicolor/48x48/apps/ibus-typing-booster.png
%_datadir/icons/hicolor/64x64/apps/ibus-typing-booster.png
%_datadir/icons/hicolor/128x128/apps/ibus-typing-booster.png
%_datadir/icons/hicolor/256x256/apps/ibus-typing-booster.png
%_datadir/icons/hicolor/scalable/apps/ibus-typing-booster.svg

%files -n emoji-picker
%doc README LICENSE
%_bindir/emoji-picker
%_datadir/metainfo/org.freedesktop.ibus.engine.typing_booster.emoji_picker.metainfo.xml
%_datadir/applications/emoji-picker.desktop

%changelog
* Wed Sep 30 2026 Timofei Fedotov <sovtouch@altlinux.org> 2.31.1-alt1
- Initial build for ALT Sisyphus. (Closes: #51876)
