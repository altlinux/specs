%def_with curtain
%def_with replays

Name: retris
Version: 1.20260409
Release: alt1

Summary: A tetromino game with graphics output to a Linux terminal or LED smart curtain. In this game you can rewind time. 
License: 0BSD
Group: Games/Arcade

Url: https://github.com/ilyakurdyukov/retris
Source: %name-%version.tar
Source1: replays.zip

%if_with curtain
BuildRequires: libbluez-devel
%endif
%if_with replays
BuildRequires: unzip
%endif

%description
A tetromino game with the following features:

- demo recording and playback
- time rewind
- automatic playback of recorded demos after a gameover
- gamepad support
- Linux terminal output
- Zengge/Surplife 20x20 LED smart curtain output

%prep
%setup

sed -i 's|"replays"|"%_gamesdatadir/%name/replays"|' %name.6

%build
%make_build \
%if_without curtain
	CURTAIN=0 \
%endif
	REPLAYS_DIR="%_gamesdatadir/%name/replays" \
	%nil

%install
install -pDm755 %name %buildroot%_gamesbindir/%name
%if_with replays
unzip %SOURCE1
mkdir -p %buildroot%_gamesdatadir/%name/replays
install -pDm644 replays/* %buildroot%_gamesdatadir/%name/replays/
%endif
install -pDm644 %name.6 %buildroot%_man6dir/%name.6

%files
%_gamesbindir/%name
%if_with replays
%_gamesdatadir/%name
%endif
%_man6dir/%name.6*

%changelog
* Thu Apr 09 2026 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.20260409-alt1
- first release in ALT Linux

