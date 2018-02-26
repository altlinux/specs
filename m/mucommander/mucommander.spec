Name:           mucommander
Version:        0.8.5.svn3682
Release:        alt2
Summary:        File manager with Norton Commander interface written in Java
Packager:       Alex Negulescu <alecs@altlinux.org>
License:        GPLv3
Url:            http://www.mucommander.com
Group:          File tools
# svn export https://svn.mucommander.com/mucommander/tags/release_0_8_5/ mucommander-0.8.5
# tar cvjf muCommander-0.8.5.svn3682.tar.bz2 mucommander-0.8.5
Source0:        %name-%version.tar.bz2
Source1:        %name.desktop
BuildArch:      noarch
BuildRequires:  ant17 findbugs jtidy subversion java-1.6.0-sun java-1.6.0-sun-devel rpm-build-java

%description
muCommander is a lightweight, cross-platform file manager featuring a Norton Commander style interface and running on any operating system with Java support (Mac OS X, Windows, Linux, *BSD, Solaris...).

* Virtual filesystem with local volumes, FTP, SFTP, SMB, NFS, HTTP and Bonjour support
* Quickly copy, move, rename files, create directories, email files...
* Browse, create and uncompress ZIP, RAR, TAR, GZip, BZip2, ISO/NRG, AR/Deb and LST archives
* ZIP files can be modified on-the-fly, without having to recompress the whole archive
* Universal bookmarks and credentials manager
* Multiple windows support
* Full keyboard access
* Highly configurable
* Available in 22 languages : American & British English, French, German, Spanish, Czech, Simplified & Traditional Chinese, Polish, Hungarian, Russian, Slovenian, Romanian, Italian, Korean, Brazilian Portuguese, Dutch, Slovak, Japanese, Swedish, Danish and Ukrainian.
* Free Software (GPL)

%prep
%setup -q -n mucommander-0.8.5

%build
JAVA_HOME="/usr/lib/jvm/java-1.6.0-sun" ant17 obfuscate

echo '#!/bin/bash
java -jar %_javadir/%name.jar' > %name.sh

%install
install -D -m 644 ./tmp/compile/mucommander_unobf.jar %buildroot%_javadir/%name.jar
install -D -m 644 ./res/images/mucommander/icon16_24.png %buildroot%_miconsdir/%name.png
install -D -m 644 ./res/images/mucommander/icon32_24.png %buildroot%_iconsdir/%name.png
install -D -m 644 ./res/images/mucommander/icon48_24.png %buildroot%_liconsdir/%name.png
install -D -m 644 ./res/images/mucommander/icon128_24.png %buildroot/usr/share/pixmaps/%name.png
install -D -m 755 ./%name.sh %buildroot%_bindir/mucommander
install -D -m 644 %SOURCE1  %buildroot%_datadir/applications/%name.desktop

%files
%defattr(-,root,root,-)
%doc compile.txt license.txt readme.txt
%_javadir/%name.jar
%_datadir/applications/%name.desktop
%_miconsdir/%name.png
%_iconsdir/%name.png
%_liconsdir/%name.png
%_datadir/pixmaps/%name.png
%_bindir/%name

%changelog
* Sat Mar 10 2012 Alex Negulescu <alecs@altlinux.org> 0.8.5.svn3682-alt2
- fixed build issues with OpenJDK 7.0 installed
- fixed buildreqs

* Mon Sep 05 2011 Alex Negulescu <alecs@altlinux.org> 0.8.5.svn3682-alt1
- Initial package created
