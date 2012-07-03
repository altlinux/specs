Name: rezerwar
Summary: A big mess of networked blocks and pipes
Version: 0.4.2
Release: alt1
License: BSD
Group: Games/Puzzles
Source: http://tamentis.com/projects/rezerwar/files/%name-%version.tar.gz
Source1: %name.desktop
Source2: %name.png
Url: http://tamentis.com/projects/rezerwar/

# Automatically added by buildreq on Thu Jun 17 2010
BuildRequires: libSDL_mixer-devel

%description
rezerwar is a puzzle game that could be quickly described as the
illegitimate child of a known tetromino game and the average pipe game.

Authors: Bertrand Janin <tamentis@neopulsar.org>

%prep
%setup -q

TARGET_BIN="%_bindir" TARGET_DATA="%_datadir/%name" TARGET_DOC="%_docdir/%name" ./configure Linux
sed -i -e "1i CFLAGS += $RPM_OPT_FLAGS" src/Makefile

%build
%make_build
strip src/%name

%install
%makeinstall DESTDIR="%buildroot"
install -D -m 644 %SOURCE1 %buildroot/%_desktopdir/%name.desktop
install -D -m 644 %SOURCE2 %buildroot/%_niconsdir/%name.png

%files
%_bindir/%name
%dir %_datadir/%name/
%doc %_docdir/%name
%_datadir/%name/*
%_desktopdir/%name.desktop
%_niconsdir/%name.png

%changelog
* Thu Jun 17 2010 Fr. Br. George <george@altlinux.ru> 0.4.2-alt1
- Initial build from SuSE

* Tue May 11 2010 PVince81@yahoo.fr
- Updated to version 0.4.2
* Mon Jan  4 2010 PVince81@yahoo.fr
- Changed SDL dependencies to SDL instead of libSDL
- Changed summary
* Fri Sep 18 2009 PVince81@yahoo.fr
- Updated to version 0.4.1
* Sun Jul 12 2009 PVince81@yahoo.fr
- Initial package
