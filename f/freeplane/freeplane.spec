%define _unpackaged_files_terminate_build 1

Name: freeplane
Version: 1.13.2
Release: alt1

Summary: Application for Mind Mapping
Group: Office
License: GPL-2.0
Url: https://www.freeplane.org/
Vcs: https://github.com/freeplane/freeplane
ExclusiveArch: x86_64 aarch64

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: /proc
BuildRequires: jpackage-17-compat
BuildRequires: xgradle
BuildRequires: mnemonicsetter
BuildRequires: svgsalamander
BuildRequires: data-url
BuildRequires: flatlaf-core
BuildRequires: twelvemonkeys-common
BuildRequires: apache-commons-lang
BuildRequires: apache-commons-io
BuildRequires: apache-commons-codec
BuildRequires: jgoodies-forms
BuildRequires: jgoodies-common
BuildRequires: SimplyHTML
BuildRequires: idw-gpl
BuildRequires: freeplane-twemoji
BuildRequires: ant
BuildRequires: batik
BuildRequires: fop
BuildRequires: fontbox
BuildRequires: biz-aQute-bnd-gradle-plugins
BuildRequires: knopflerfish-framework
BuildRequires: xml-commons-apis
Requires: java-openjdk >= 1.8.0
Requires: java-openjdk <= 22.0.0

%description
Freeplane is a free and open source software application that supports
thinking, sharing information, getting things done at work, in school
and at home. It provides you a set of tools for mind mapping (also
known as concept mapping or information mapping) and navigating the
mapped information. Freeplane is also a more robust and superior
alternative to Xmind, Mindmeister, and similar mind mapping software.

%prep
%setup
%autopatch -p1

%build
gradle dist \
    -x check \
    -x :freeplane:copyFlatLafDll\
    -Dmaven.poms.dir=/usr/share/maven-poms \
    -Djava.library.dir=/usr/share/java,/usr/lib/java \
    -PuseSystemJarSymlinks \

%install
install -Dpm 0644 -t %buildroot%_datadir/freeplane BIN/*.*
install -Dpm 0755 -t %buildroot%_datadir/freeplane BIN/freeplane.sh
install -Dpm 0644 -t %buildroot%_datadir/freeplane/core/org.freeplane.core/META-INF BIN/core/org.freeplane.core/META-INF/*
install -Dpm 0644 -t %buildroot%_datadir/freeplane/doc BIN/doc/*.*
install -Dpm 0644 -t %buildroot%_datadir/freeplane/doc/Images BIN/doc/Images/*.png
install -Dpm 0644 -t %buildroot%_datadir/freeplane/doc/Images/doc BIN/doc/Images/doc/*
install -Dpm 0644 -t %buildroot%_datadir/freeplane/doc/Images/mouse BIN/doc/Images/mouse/*
install -Dpm 0644 -t %buildroot%_datadir/freeplane/doc/latestFreeplaneFeatures_files BIN/doc/latestFreeplaneFeatures_files/*
install -Dpm 0644 -t %buildroot%_datadir/freeplane/plugins/org.freeplane.plugin.bugreport/META-INF BIN/plugins/org.freeplane.plugin.bugreport/META-INF/*
install -Dpm 0644 -t %buildroot%_datadir/freeplane/plugins/org.freeplane.plugin.svg/META-INF BIN/plugins/org.freeplane.plugin.svg/META-INF/*
install -Dpm 0644 -t %buildroot%_datadir/freeplane/resources BIN/resources/*.*
install -Dpm 0644 -t %buildroot%_datadir/freeplane/resources/ortho BIN/resources/ortho/*
install -Dpm 0644 -t %buildroot%_datadir/freeplane/resources/templates BIN/resources/templates/*
install -Dpm 0644 -t %buildroot%_datadir/freeplane/resources/xml BIN/resources/xml/*
install -Dpm 0644 -t %buildroot%_datadir/freeplane/resources/xslt BIN/resources/xslt/*
install -Dpm 0644 -t %buildroot%_iconsdir/hicolor/scalable/apps freeplane_framework/script/freeplane.svg
install -Dpm 0644 -t %buildroot%_desktopdir debian-meta-data/freeplane.desktop
install -Dpm 0644 debian-meta-data/freeplane.sharedmimeinfo %buildroot%_datadir/mime/packages/freeplane.xml
# Packaging symlinks to system JARs so as not to make the package heavier.
install -d %buildroot%_datadir/freeplane/core/org.freeplane.core/lib
cp -a BIN/core/org.freeplane.core/lib/. %buildroot%_datadir/freeplane/core/org.freeplane.core/lib/
install -d %buildroot%_datadir/freeplane/plugins/org.freeplane.plugin.bugreport/lib
cp -a BIN/plugins/org.freeplane.plugin.bugreport/lib/. %buildroot%_datadir/freeplane/plugins/org.freeplane.plugin.bugreport/lib/
install -d %buildroot%_datadir/freeplane/plugins/org.freeplane.plugin.svg/lib
cp -a BIN/plugins/org.freeplane.plugin.svg/lib/. %buildroot%_datadir/freeplane/plugins/org.freeplane.plugin.svg/lib/
install -d %buildroot%_bindir
ln -s %_datadir/freeplane/freeplane.sh %buildroot%_bindir/freeplane

%files
%doc README.md license.txt
%_bindir/freeplane
%_desktopdir/freeplane.desktop
%_datadir/freeplane/
%_iconsdir/hicolor/scalable/apps/freeplane.svg
%_datadir/mime/packages/freeplane.xml

%changelog
* Fri Apr 24 2026 Arseniy Kostevich <faux@altlinux.org> 1.13.2-alt1
- Initial build for ALT.
