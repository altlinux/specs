Name: proguard
Summary: Java class file shrinker, optimizer, obfuscator, and preverifier
Version: 4.6
Release: alt1
License: GPL
Group: Development/Java
BuildArch: noarch
BuildRequires: ant checkstyle4 tzdata log4j slf4j
BuildRequires: /proc
Packager: Denis Smirnov <mithraen@altlinux.ru>
Source: %name-%version.tar

%description
Java class file shrinker, optimizer, obfuscator, and preverifier


%prep
%setup

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
* Tue Oct 04 2011 Denis Smirnov <mithraen@altlinux.ru> 4.6-alt1
- 4.6

* Mon Nov 09 2009 Denis Smirnov <mithraen@altlinux.ru> 4.4-alt1
- first build for Sisyphus

