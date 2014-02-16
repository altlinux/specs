%set_verify_elf_method unresolved=strict

Name: gnustep-TalkSoup
Version: 1.0
Release: alt3.alpha
Summary: GNUstep IRC client
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://talksoup.aeruder.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-netclasses-devel

Requires: lib%name = %EVR
Requires: gnustep-netclasses
Requires: gnustep-back

%description
TalkSoup is a GNUstep IRC client with a minimalistic feel and by far one
of the most extensible designs in existence.

At the core is just a simple class which passes messages between bundles
or plugins. The rest of the IRC client is formed entirely by these
bundles. This means you can have multiple output bundles such as a GTK
output bundle, GNUstep bundle, even a ncurses bundle! And all of these
could use other bundles which can do everything from output your
incoming messages through a speech program or filter all your outgoing
messages through a spell checking bundle.

%package -n lib%name
Summary: Shared libraries of TalkSoup
Group: System/Libraries

%description -n lib%name
TalkSoup is a GNUstep IRC client with a minimalistic feel and by far one
of the most extensible designs in existence.

At the core is just a simple class which passes messages between bundles
or plugins. The rest of the IRC client is formed entirely by these
bundles. This means you can have multiple output bundles such as a GTK
output bundle, GNUstep bundle, even a ncurses bundle! And all of these
could use other bundles which can do everything from output your
incoming messages through a speech program or filter all your outgoing
messages through a spell checking bundle.

This package contains shared libraries of TalkSoup.

%package -n lib%name-devel
Summary: Development files of TalkSoup
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
TalkSoup is a GNUstep IRC client with a minimalistic feel and by far one
of the most extensible designs in existence.

At the core is just a simple class which passes messages between bundles
or plugins. The rest of the IRC client is formed entirely by these
bundles. This means you can have multiple output bundles such as a GTK
output bundle, GNUstep bundle, even a ncurses bundle! And all of these
could use other bundles which can do everything from output your
incoming messages through a speech program or filter all your outgoing
messages through a spell checking bundle.

This package contains development files of TalkSoup.

%prep
%setup

for i in $(find ./ -name GNUmakefile); do
	sed -i 's|Library/ApplicationSupport|Applications|g' $i
	sed -i 's|Library/Application Support|Applications|g' $i
	sed -i 's|Library/Frameworks|Frameworks|g' $i
done

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS="-I$PWD/Input" \
	CONFIG_SYSTEM_LIBS='-lgnustep-base -lobjc2'
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_INSTALLATION_DIR=%buildroot%_libdir/GNUstep

pushd %buildroot%_libdir
cp GNUstep/Frameworks/TalkSoupBundles.framework/Versions/Current/libTalkSoupBundles.so* \
	./
for j in TalkSoupBundles; do
	for i in lib$j.so*; do
		rm -f $i
		mv GNUstep/Frameworks/$j.framework/Versions/Current/$i ./
		for k in lib$j.so.*.*; do
			ln -s %_libdir/$k GNUstep/Frameworks/$j.framework/Versions/Current/$i
			rm GNUstep/Frameworks/$j.framework/Versions/0.990/$j
			ln -s %_libdir/$k GNUstep/Frameworks/$j.framework/Versions/Current/$j
		done
	done
done
popd

install -d %buildroot%_bindir
ln -s %_libdir/GNUstep/Applications/TalkSoup.app/TalkSoup \
	%buildroot%_bindir/

%files
%doc ChangeLog FAQ README
%_bindir/*
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/TalkSoupBundles.framework/Versions/0.990/Headers
%exclude %_libdir/GNUstep/Frameworks/TalkSoupBundles.framework/Headers
%exclude %_libdir/GNUstep/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_libdir/GNUstep/Frameworks/TalkSoupBundles.framework/Versions/0.990/Headers
%_libdir/GNUstep/Frameworks/TalkSoupBundles.framework/Headers
%_libdir/GNUstep/Headers

%changelog
* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3.alpha
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2.alpha
- Added Requires: gnustep-back

* Thu Jan 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.alpha
- Initial build for Sisyphus

