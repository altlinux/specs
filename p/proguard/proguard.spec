Name: proguard
Summary: Java class file shrinker, optimizer, obfuscator, and preverifier
Version: 4.11
Release: alt1
License: GPL
Group: Development/Java
BuildArch: noarch
BuildRequires: ant checkstyle4 tzdata log4j slf4j
BuildRequires: /proc
Packager: Denis Smirnov <mithraen@altlinux.ru>
Source: %name-%version.tar
Url: http://proguard.sourceforge.net/

Patch: %name-%version-%release.patch
Source100: %name.watch

%description
Java class file shrinker, optimizer, obfuscator, and preverifier


%prep
%setup
%patch -p1

%build
pushd build
ant \
	-Djdk.javadoc=%{_javadocdir}/java

%install
for s in proguard proguardgui retrace; do
	install -D -m 0644 lib/$s.jar %buildroot%_datadir/java/$s.jar
	install -D -m 0755 $s %buildroot%_bindir/$s
done

%files
%_datadir/java/proguard.jar
%_datadir/java/proguardgui.jar
%_datadir/java/retrace.jar
%_bindir/proguard
%_bindir/proguardgui
%_bindir/retrace

%changelog
* Sun Dec 29 2013 Cronbuild Service <cronbuild@altlinux.org> 4.11-alt1
- new version 4.11

* Fri Aug 16 2013 Denis Smirnov <mithraen@altlinux.ru> 4.10-alt1
- new version 4.10
- add cronbuild support

* Wed Apr 10 2013 Denis Smirnov <mithraen@altlinux.ru> 4.9-alt1
- 4.9

* Fri Jan 25 2013 Denis Smirnov <mithraen@altlinux.ru> 4.8-alt2
- add Url tag

* Fri Oct 12 2012 Denis Smirnov <mithraen@altlinux.ru> 4.8-alt1
- 4.8

* Tue Oct 04 2011 Denis Smirnov <mithraen@altlinux.ru> 4.6-alt1
- 4.6

* Mon Nov 09 2009 Denis Smirnov <mithraen@altlinux.ru> 4.4-alt1
- first build for Sisyphus

