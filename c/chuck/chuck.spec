%define mAname miniAudicle
%define mAversion 0.2.0

Name: chuck
Version: 1.2.1.3
Release: alt2.qa1

Summary: Strongly-timed, Concurrent, and On-the-fly Audio Programming Language
License: %gpl2plus
Group: Sound
Url: http://chuck.cs.princeton.edu/

Packager: Ilya Mashkin <oddity@altlinux.ru>
Source0: %name-%version.tar.bz2
Source1: %mAname.tar.bz2
Source2: chuck-alsa.alternatives
Source3: chuck-jack.alternatives
Source4: miniAudicle-alsa.alternatives
Source5: miniAudicle-jack.alternatives
Source6: miniAudicle.desktop

BuildPreReq: rpm-build-licenses
BuildRequires: gcc-c++ flex libsndfile-devel libalsa-devel jackit-devel wxGTK-devel wxGTK-contrib-stc-devel libpango-devel ImageMagick-tools
Requires: chuck-common chuck-alsa chuck-jack chuck-doc
BuildRequires: desktop-file-utils

%description
ChucK is a new (and developing) audio programming language for real-time
synthesis, composition, performance, and now, analysis - fully supported on
MacOS X, Windows, and Linux. ChucK presents a new time-based, concurrent
programming model that's highly precise and expressive (we call this
strongly-timed), as well as dynamic control rates, and the ability to add and
modify code on-the-fly. In addition, ChucK supports MIDI, OSC, HID device, and
multi-channel audio. It's fun and easy to learn, and offers composers,
researchers, and performers a powerful programming tool for building and
experimenting with complex audio synthesis/analysis programs, and real-time
interactive control.

This metapackage installs the full list of ChucK packages.

%package common
Summary: Common files for ChucK
Group: Sound

%description common
ChucK is a new (and developing) audio programming language for real-time
synthesis, composition, performance, and now, analysis - fully supported on
MacOS X, Windows, and Linux. ChucK presents a new time-based, concurrent
programming model that's highly precise and expressive (we call this
strongly-timed), as well as dynamic control rates, and the ability to add and
modify code on-the-fly. In addition, ChucK supports MIDI, OSC, HID device, and
multi-channel audio. It's fun and easy to learn, and offers composers,
researchers, and performers a powerful programming tool for building and
experimenting with complex audio synthesis/analysis programs, and real-time
interactive control.

This package contains common files for ChucK

%package doc
Summary: Documentation for ChucK
Group: Sound
Requires: chuck-common = %version-%release

%description doc
ChucK is a new (and developing) audio programming language for real-time
synthesis, composition, performance, and now, analysis - fully supported on
MacOS X, Windows, and Linux. ChucK presents a new time-based, concurrent
programming model that's highly precise and expressive (we call this
strongly-timed), as well as dynamic control rates, and the ability to add and
modify code on-the-fly. In addition, ChucK supports MIDI, OSC, HID device, and
multi-channel audio. It's fun and easy to learn, and offers composers,
researchers, and performers a powerful programming tool for building and
experimenting with complex audio synthesis/analysis programs, and real-time
interactive control.

This package contains documentation for ChucK

%package alsa
Summary: ChucK with ALSA interface
Group: Sound
Requires: chuck-common = %version-%release

%description alsa
ChucK is a new (and developing) audio programming language for real-time
synthesis, composition, performance, and now, analysis - fully supported on
MacOS X, Windows, and Linux. ChucK presents a new time-based, concurrent
programming model that's highly precise and expressive (we call this
strongly-timed), as well as dynamic control rates, and the ability to add and
modify code on-the-fly. In addition, ChucK supports MIDI, OSC, HID device, and
multi-channel audio. It's fun and easy to learn, and offers composers,
researchers, and performers a powerful programming tool for building and
experimenting with complex audio synthesis/analysis programs, and real-time
interactive control.

This package contains ALSA version of ChucK

%package jack
Summary: ChucK with JACK interface
Group: Sound
Requires: chuck-common = %version-%release

%description jack
ChucK is a new (and developing) audio programming language for real-time
synthesis, composition, performance, and now, analysis - fully supported on
MacOS X, Windows, and Linux. ChucK presents a new time-based, concurrent
programming model that's highly precise and expressive (we call this
strongly-timed), as well as dynamic control rates, and the ability to add and
modify code on-the-fly. In addition, ChucK supports MIDI, OSC, HID device, and
multi-channel audio. It's fun and easy to learn, and offers composers,
researchers, and performers a powerful programming tool for building and
experimenting with complex audio synthesis/analysis programs, and real-time
interactive control.

This package contains JACK version of ChucK

%package -n %mAname-common
Summary: Integrated development + performance environment for ChucK
License: %gpl2plus
Group: Sound
Url: http://audicle.cs.princeton.edu/mini/
Version: %mAversion

%description -n %mAname-common
The miniAudicle is a light-weight integrated development environment for the
ChucK digital audio programming language. It can be used as a standalone ChucK
development + runtime + on-the-fly programming environment, or in conjunction
with traditional command-line modes of 'chuck' operation and with other chuck
tools.

This package contains common files for miniAudicle

%package -n %mAname-alsa
Summary: Integrated development + performance environment for ChucK
License: %gpl2plus
Group: Sound
Url: http://audicle.cs.princeton.edu/mini/
Version: %mAversion
Requires: %mAname-common = %mAversion-%release
Provides: miniAudicle

%description -n %mAname-alsa
The miniAudicle is a light-weight integrated development environment for the
ChucK digital audio programming language. It can be used as a standalone ChucK
development + runtime + on-the-fly programming environment, or in conjunction
with traditional command-line modes of 'chuck' operation and with other chuck
tools.

This package contains ALSA version of miniAudicle

%package -n %mAname-jack
Summary: Integrated development + performance environment for ChucK
License: %gpl2plus
Group: Sound
Url: http://audicle.cs.princeton.edu/mini/
Version: %mAversion
Requires: %mAname-common = %mAversion-%release
Provides: miniAudicle

%description -n %mAname-jack
The miniAudicle is a light-weight integrated development environment for the
ChucK digital audio programming language. It can be used as a standalone ChucK
development + runtime + on-the-fly programming environment, or in conjunction
with traditional command-line modes of 'chuck' operation and with other chuck
tools.

This package contains JACK version of miniAudicle

%prep
%setup -a 1
cd miniAudicle
ln -sf .. chuck

%build
#	build jack version
pushd src
  %make_build linux-jack
  cp -a chuck chuck-jack
popd

pushd miniAudicle
  %make_build linux-jack
  mv wxw/miniAudicle %mAname-jack
  %make clean
popd

pushd src
  %make clean
popd 

#	build alsa version
pushd src
  %make_build linux-alsa
  cp -a chuck chuck-alsa
popd

pushd miniAudicle
  %make_build linux-alsa
  mv wxw/miniAudicle %mAname-alsa
  %make clean
popd

%install
#	install binaries
install -pDm0755 src/chuck-jack %buildroot%_bindir/chuck-jack
install -pDm0755 src/chuck-alsa %buildroot%_bindir/chuck-alsa
install -pDm0755 miniAudicle/%mAname-jack %buildroot%_bindir/%mAname-jack
install -pDm0755 miniAudicle/%mAname-alsa %buildroot%_bindir/%mAname-alsa

#	install alternatives
install -pDm0644 %SOURCE2 %buildroot%_altdir/chuck-alsa
install -pDm0644 %SOURCE3 %buildroot%_altdir/chuck-jack
install -pDm0644 %SOURCE4 %buildroot%_altdir/miniAudicle-alsa
install -pDm0644 %SOURCE5 %buildroot%_altdir/miniAudicle-jack

# 	install documentation
for file in AUTHORS DEVELOPER INSTALL PROGRAMMER QUICKSTART README THANKS TODO VERSIONS; do
  install -pDm0644 "$file" "%buildroot%_docdir/%name/$file"
done

pushd doc
  for file in *; do
    install -pDm0644 "$file" "%buildroot%_docdir/%name/$file"
  done
popd

for dir in $(find examples -type d); do
  pushd "$dir"
    mkdir -p "%buildroot%_docdir/%name/$dir"
    for file in *; do
      [ -f "$file" ] && install -pDm0644 "$file" "%buildroot%_docdir/%name/$dir"
    done
  popd
done

#	install .desktop and icon file
install -pDm0644 %SOURCE6 %buildroot%_datadir/applications/%mAname.desktop
install -dm 755 %buildroot%_liconsdir
convert -resize 48x48 miniAudicle/wxw/icons/miniAudicle.xpm %buildroot%_liconsdir/miniAudicle.png
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Music \
	%buildroot%_desktopdir/miniAudicle.desktop


%files

%files common
%doc %dir %_docdir/%name/
%doc %_docdir/%name/AUTHORS 
%doc %_docdir/%name/DEVELOPER 
%doc %_docdir/%name/INSTALL 
%doc %_docdir/%name/PROGRAMMER 
%doc %_docdir/%name/QUICKSTART 
%doc %_docdir/%name/README 
%doc %_docdir/%name/THANKS 
%doc %_docdir/%name/TODO 
%doc %_docdir/%name/VERSIONS

%files doc
%doc %_docdir/%name/GOTO 
%doc %_docdir/%name/ChucK_manual.pdf 
%doc %_docdir/%name/examples

%files alsa
%_bindir/chuck-alsa
%_altdir/chuck-alsa

%files jack
%_bindir/chuck-jack
%_altdir/chuck-jack

%files -n %mAname-common
%doc miniAudicle/BUGS miniAudicle/COPYING miniAudicle/LGPL miniAudicle/README.linux miniAudicle/VERSIONS miniAudicle/examples
%_datadir/applications/%mAname.desktop
%_liconsdir/miniAudicle.png

%files -n %mAname-alsa
%_bindir/%mAname-alsa
%_altdir/%mAname-alsa

%files -n %mAname-jack
%_bindir/%mAname-jack
%_altdir/%mAname-jack

%changelog
* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.1.3-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for miniAudicle-common

* Wed Mar 10 2010 Ilya Mashkin <oddity@altlinux.ru> 1.2.1.3-alt2
- rebuild with current wxGTK

* Tue Oct 06 2009 Timur Batyrshin <erthad@altlinux.org> 1.2.1.3-alt1
- updated ChucK to 1.2.1.3 
- updated miniAudicle to 0.2.0

* Sat Aug 29 2009 Timur Batyrshin <erthad@altlinux.org> 1.2.1.2-alt3
- miniAudicle build added

* Sat Aug 29 2009 Timur Batyrshin <erthad@altlinux.org> 1.2.1.2-alt2
- alternatives fixed

* Fri Aug 28 2009 Timur Batyrshin <erthad@altlinux.org> 1.2.1.2-alt1
- Initial build for sisyphus

