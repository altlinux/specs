
Name: mame
Version: 0.250
Release: alt1
Group: Games/Arcade
Summary: Multiple Arcade Machine Emulator
Summary(ru_RU.UTF-8): Эмулятор множества аркадных (и не только) машин
#LGPLv2+:
#src/mame/audio/snes_snd.cpp: LGPL (v2 or later)
#src/devices/sound/tiasound.cpp: LGPL (v2) (with incorrect FSF address)
#src/devices/sound/tiasound.h: LGPL (v2) (with incorrect FSF address)
#
#ASL 2.0
#3rdparty/bgfx

License: GPLv2+
Url: http://mamedev.org/
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
Patch0: system_lua.patch
BuildRequires: libexpat-devel rapidjson libsqlite3-devel libutf8proc-devel zlib-devel libjpeg-devel liblinenoise-devel
BuildRequires: libflac-devel libglm-devel libportaudio2-devel libportmidi-devel fontconfig-devel
BuildRequires: git-core libxcb libSDL2_ttf-devel libXi-devel libXinerama-devel libalsa-devel python-modules-compiler
BuildRequires: python-modules-encodings python-modules-logging python-modules-xml qt5-base-devel libpulseaudio-devel
BuildRequires: libuv-devel asio-devel gettext-tools

Provides: bundled(lua) = 5.3.4
Provides: bundled(luafilesystem)
Provides: bundled(lua-linenoise)
Provides: bundled(lua-zlib)

ExclusiveArch: x86_64

%description
MAME stands for Multiple Arcade Machine Emulator.  When used in conjunction
with an arcade game's data files (ROMs), MAME will more or less faithfully
reproduce that game on a PC.

The ROM images that MAME utilizes are "dumped" from arcade games' original
circuit-board ROM chips.  MAME becomes the "hardware" for the games, taking
the place of their original CPUs and support chips.  Therefore, these games
are NOT simulations, but the actual, original games that appeared in arcades.

MAME's purpose is to preserve these decades of video-game history.  As gaming
technology continues to rush forward, MAME prevents these important "vintage"
games from being lost and forgotten.  This is achieved by documenting the
hardware and how it functions, thanks to the talent of programmers from the
MAME team and from other contributors.  Being able to play the games is just
a nice side-effect, which doesn't happen all the time.  MAME strives for
emulating the games faithfully.

%description -l ru_RU.UTF-8
MAME создавался как эмулятор множества аркадных машин.  При использовании
оригинальных данных из чипов ПЗУ автоматов (ROM'ов), MAME может более-менее
точно воспроизводить эти игры на ПК.

Образы ПЗУ, которые использует MAME, "дампятся" (снимаются) с оригинальных чипов
системных плат аркадных автоматов.  MAME становится "железом" для этих игр, заменяя
собой оригинальные процессоры и чипсеты машин.  Тем не менее, игры НЕ симулируются,
а выполняются так же, как и на реальных аркадных автоматах.

Задача MAME - сберечь десятилетия видеоигровой истории. Пока игровые технологии
продолжают стремиться вперёд, MAME сберегает эти важные "винтажные" игры от
безвозвратной утери и забытья.  Это вознаграждается документированием железа,
его функционала, благодаря талантливым программистов из команды разработки
MAME и других людей, вносящих вклад.  возможность запука игры - лишь приятный
побочный эффект, что происходит не часто.  MAME старается добиться максимально
точной эмуляции.

%package tools
Group: Games/Arcade
Summary: Additional tools for MAME
Requires: %name%{?_isa} = %version-%release

%description tools
%summary.

%package data
Group: Games/Arcade
Summary: Data files used by MAME

BuildArch: noarch

%description data
Group: Games/Arcade
%summary.

%package data-software-lists
Group: Games/Arcade
Summary: Software lists used by MAME
Requires: %name-data >= %version-%release
BuildArch: noarch

%description data-software-lists
%summary. These are split from the main -data
subpackage due to relatively large size.

%package doc
Group: Games/Arcade
Summary: Documentation for MAME
BuildArch: noarch

%description doc
HTML documentation for MAME.

%prep
%setup -n %name-%version

%patch0 -p1

rm -rf 3rdparty/compat \
    3rdparty/asio \
    3rdparty/dxsdk \
    3rdparty/expat \
    3rdparty/glm \
    3rdparty/libflac \
    3rdparty/libjpeg \
    3rdparty/portaudio \
    3rdparty/portmidi \
    3rdparty/rapidjson \
    3rdparty/SDL2 \
    3rdparty/SDL2-override \
    3rdparty/sqlite3 \
    3rdparty/tap-windows6 \
    3rdparty/utf8proc \
    3rdparty/zlib \
    docs/themes

# Create ini files
cat > %name.ini << EOF
# Define multi-user paths
artpath            %_datadir/%name/artwork;%_datadir/%name/effects
bgfx_path          %_datadir/%name/bgfx
cheatpath          %_datadir/%name/cheat
crosshairpath      %_datadir/%name/crosshair
ctrlrpath          %_datadir/%name/ctrlr
fontpath           %_datadir/%name/fonts
hashpath           %_datadir/%name/hash
languagepath       %_datadir/%name/language
pluginspath        %_datadir/%name/plugins
rompath            %_datadir/%name/roms;%_datadir/%name/chds
samplepath         %_datadir/%name/samples

# Allow user to override ini settings
inipath            \$HOME/.%name/ini;%_sysconfdir/%name

# Set paths for local storage
cfg_directory      \$HOME/.%name/cfg
comment_directory  \$HOME/.%name/comments
diff_directory     \$HOME/.%name/diff
input_directory    \$HOME/.%name/inp
nvram_directory    \$HOME/.%name/nvram
snapshot_directory \$HOME/.%name/snap
state_directory    \$HOME/.%name/sta

# %vendor custom defaults
video              opengl
autosave           1
EOF

%build
# sorry guys, but race of streams is pain:
# https://github.com/mamedev/mame/issues/5741

make -j8 OPTIMISE="%optflags" \
    $MAME_FLAGS \
    TOOLS=1 \
    NOWERROR=1 \
    ARCHOPTS=-U_FORTIFY_SOURCE \
    USE_SYSTEM_LIB_ASIO=1 \
    USE_SYSTEM_LIB_EXPAT=1 \
    USE_SYSTEM_LIB_FLAC=1 \
    USE_SYSTEM_LIB_GLM=1 \
    USE_SYSTEM_LIB_JPEG=1 \
    USE_SYSTEM_LIB_PORTAUDIO=1 \
    USE_SYSTEM_LIB_PORTMIDI=1 \
    USE_SYSTEM_LIB_RAPIDJSON=1 \
    USE_SYSTEM_LIB_SQLITE3=1 \
    USE_SYSTEM_LIB_UTF8PROC=1 \
    USE_SYSTEM_LIB_ZLIB=1

#pushd docs
#    %%make_build html
#popd

%install
# create directories
install -d %buildroot%_sysconfdir/%name
for folder in cfg comments diff ini inp memcard nvram snap sta
do
    install -d %buildroot%_sysconfdir/skel/.%name/$folder
done
install -d %buildroot%_bindir
for folder in artwork bgfx chds cheats ctrlr effects fonts hash language \
    plugins hlsl keymaps roms samples shader
do
    install -d %buildroot%_datadir/%name/$folder
done
install -d %buildroot%_man1dir
install -d %buildroot%_man6dir

# install files
install -pm 644 %name.ini %buildroot%_sysconfdir/%name
%if_with debug
install -pm 755 %{name}d %buildroot%_bindir/%{name}d || \
install -pm 755 %{name}64d %buildroot%_bindir/%{name}d
%else
install -pm 755 %name %buildroot%_bindir/%name || \
install -pm 755 %{name}64 %buildroot%_bindir/%name
%endif
install -pm 755 castool chdman floptool imgtool jedutil ldresample ldverify \
     nltool nlwav pngcmp romcmp unidasm %buildroot%_bindir
for tool in regrep split srcclean
do
    install -pm 755 $tool %buildroot%_bindir/%name-$tool
done
pushd artwork
    find -type d -exec install -d %buildroot%_datadir/%name/artwork/{} \;
    find -type f -exec install -pm 644 {} %buildroot%_datadir/%name/artwork/{} \;
popd
pushd bgfx
    find -type d -exec install -d %buildroot%_datadir/%name/bgfx/{} \;
    find -type f -exec install -pm 644 {} %buildroot%_datadir/%name/bgfx/{} \;
popd
install -pm 644 hash/* %buildroot%_datadir/%name/hash
install -pm 644 hlsl/*.fx %buildroot%_datadir/%name/hlsl
install -pm 644 keymaps/* %buildroot%_datadir/%name/keymaps
pushd language
    find -type d -exec install -d %buildroot%_datadir/%name/language/{} \;
    find -type f -name \*.mo -exec install -pm 644 {} %buildroot%_datadir/%name/language/{} \;
popd
pushd plugins
    find -type d -exec install -d %buildroot%_datadir/%name/plugins/{} \;
    find -type f -exec install -pm 644 {} %buildroot%_datadir/%name/plugins/{} \;
popd
pushd src/osd/modules/opengl
    install -pm 644 shader/*.?sh %buildroot%_datadir/%name/shader
popd
pushd docs/man
install -pm 644 castool.1 chdman.1 imgtool.1 floptool.1 jedutil.1 ldresample.1 \
    ldverify.1 romcmp.1 %buildroot%_man1dir
install -pm 644 mame.6 %buildroot%_man6dir
popd
find %buildroot%_datadir/%name -name LICENSE -exec rm {} \;

%find_lang %name

%files
%config(noreplace) %_sysconfdir/%name/%name.ini
%dir %_sysconfdir/%name
%_sysconfdir/skel/.%name
%if_with debug
%_bindir/%named
%else
%_bindir/%name
%endif
%_man6dir/mame.6*

%files tools
%_bindir/castool
%_bindir/chdman
%_bindir/floptool
%_bindir/imgtool
%_bindir/jedutil
%_bindir/ldresample
%_bindir/ldverify
%_bindir/nltool
%_bindir/nlwav
%_bindir/pngcmp
%_bindir/%name-regrep
%_bindir/romcmp
%_bindir/%name-split
%_bindir/%name-srcclean
%_bindir/unidasm
%_man1dir/castool.1*
%_man1dir/chdman.1*
%_man1dir/floptool.1*
%_man1dir/imgtool.1*
%_man1dir/jedutil.1*
%_man1dir/ldresample.1*
%_man1dir/ldverify.1*
%_man1dir/romcmp.1*

%files data
%doc README.md COPYING
%_datadir/%name
%exclude %_datadir/%name/hash/*

%files data-software-lists
%_datadir/%name/hash/*

%changelog
* Sat Dec 03 2022 Artyom Bystrov <arbars@altlinux.org> 0.250-alt1
- Update to new version

* Mon Oct 18 2022 Artyom Bystrov <arbars@altlinux.org> 0.248-alt1
- Update to new version

* Thu Aug 04 2022 Artyom Bystrov <arbars@altlinux.org> 0.246-alt1
- Update to new version

* Thu Jul 22 2022 Artyom Bystrov <arbars@altlinux.org> 0.245-alt1.1
- experimenting with multi-thread building

* Thu Jul 15 2022 Artyom Bystrov <arbars@altlinux.org> 0.245-alt1
- initial build for ALT Sisyphus
