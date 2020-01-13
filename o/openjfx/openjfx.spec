Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: java-devel-default perl(Class/Struct.pm) perl(Compress/Zlib.pm) perl(Config.pm) perl(English.pm) perl(Exporter.pm) perl(FindBin.pm) perl(IO/File.pm) perl(JSON/PP.pm) perl(List/Util.pm) perl(Term/ANSIColor.pm) perl(Text/ParseWords.pm) zip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name openjfx
%global openjfxdir %{_jvmdir}/%{name}

Name:           openjfx
Version:        8.0.202
Release:        alt1_8.b07jpp8
Summary:        Rich client application platform for Java

#fxpackager is BSD
License:        GPL v2 with exceptions and BSD
URL:            http://openjdk.java.net/projects/openjfx/

Source0:        http://hg.openjdk.java.net/openjfx/8u-dev/rt/archive/8u202-b07.tar.bz2
Source1:        README.fedora

Patch0:         0000-Fix-wait-call-in-PosixPlatform.patch
Patch1:         0001-Change-SWT-and-Lucene.patch
Patch2:         0002-Allow-build-to-work-on-newer-gradles.patch
Patch3:         0003-fix-cast-between-incompatible-function-types.patch
Patch4:         0004-Fix-Compilation-Flags.patch
Patch5:         0005-fxpackager-extract-jre-accept-symlink.patch
Patch6:         0006-Drop-SWT-32bits-and-Lucene.patch

ExclusiveArch:  %{ix86} x86_64

Requires:       java

BuildRequires:  gradle-local
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel-static
BuildRequires:  mvn(antlr:antlr)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.antlr:antlr:3.1.3)
BuildRequires:  mvn(org.antlr:stringtemplate)
BuildRequires:  mvn(org.apache.ant:ant)
%ifarch s390x x86_64 aarch64 ppc64le
BuildRequires:  mvn(org.eclipse.swt:swt)
%endif

BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(gl)

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gperf
Source44: import.info

%description
JavaFX/OpenJFX is a set of graphics and media APIs that enables Java
developers to design, create, test, debug, and deploy rich client
applications that operate consistently across diverse platforms.

The media and web module have been removed due to missing dependencies.

%package devel
Group: Development/Java
Requires: %{name} = %{version}-%{release}
Summary: OpenJFX development tools and libraries

%description devel
%{summary}.

%package src
Group: Development/Java
Requires: %{name} = %{version}-%{release}
Summary: OpenJFX Source Bundle

%description src
%{summary}.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
#BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n rt-8u202-b07
%patch0 -p1
%ifarch s390 %{arm} %{ix86}
%patch -P 6 -p1
%else
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
 
cp %{SOURCE1} .

cat > gradle.properties << EOF
COMPILE_WEBKIT = false
COMPILE_MEDIA = false
%ifarch s390 %{arm} %{ix86}
COMPILE_SWT = false
%endif 
BUILD_JAVADOC = true
BUILD_SRC_ZIP = true
GRADLE_VERSION_CHECK = false
CONF = DebugNative
EOF

find -name '*.class' -delete
find -name '*.jar' -delete

#Bundled libraries
rm -rf modules/media/src/main/native/gstreamer/3rd_party/glib
rm -rf modules/media/src/main/native/gstreamer/gstreamer-lite

#Drop SWT for 32 bits build
%ifarch s390 %{arm} %{ix86}
rm -rf modules/swt
rm -rf modules/graphics/src/main/java/com/sun/glass/ui/swt
rm -rf modules/builders/src/main/java/javafx/embed/swt
%endif 

sed -i 's,"-Werror","-Wsized-deallocation",' buildSrc/*.gradle

%build
#Tests do not run by default, tests in web fails and one test in graphics fail:
#UnsatisfiedLinkError: libjavafx_iio.so: undefined symbol: jpeg_resync_to_restart
gradle-local --no-daemon --offline --info

%install
install -d -m 755 %{buildroot}%{openjfxdir}
cp -a build/sdk/{bin,lib,rt} %{buildroot}%{openjfxdir}

install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 build/sdk/man/man1/* %{buildroot}%{_mandir}/man1

install -d -m 755 %{buildroot}%{_mandir}/ja_JP/man1
install -m 644 build/sdk/man/ja_JP.UTF-8/man1/* %{buildroot}%{_mandir}/ja_JP/man1

install -m 644 build/sdk/javafx-src.zip %{buildroot}%{openjfxdir}/javafx-src.zip

install -d 755 %{buildroot}%{_javadocdir}/%{name}
cp -a build/sdk/docs/api/. %{buildroot}%{_javadocdir}/%{name}

mkdir -p %{buildroot}%{_bindir}
ln -s %{openjfxdir}/bin/javafxpackager %{buildroot}%{_bindir}
ln -s %{openjfxdir}/bin/javapackager %{buildroot}%{_bindir}

%files
%dir %{openjfxdir}
%{openjfxdir}/rt
%doc --no-dereference LICENSE
%doc README
%doc README.fedora

%files devel
%{openjfxdir}/lib
%{openjfxdir}/bin
%{_bindir}/javafxpackager
%{_bindir}/javapackager
%{_mandir}/man1/javafxpackager.1*
%{_mandir}/man1/javapackager.1*
%{_mandir}/ja_JP/man1/javafxpackager.1*
%{_mandir}/ja_JP/man1/javapackager.1*
%doc --no-dereference LICENSE
%doc README
%doc README.fedora

%files src
%{openjfxdir}/javafx-src.zip

%files javadoc
%{_javadocdir}/%{name}
%doc --no-dereference LICENSE

%changelog
* Mon Jan 13 2020 Igor Vlasenko <viy@altlinux.ru> 8.0.202-alt1_8.b07jpp8
- fixed build

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 8.0.202-alt1_5.b07jpp8
- new version

* Sat Apr 06 2019 Igor Vlasenko <viy@altlinux.ru> 8.0.152-alt1_17.b05jpp8
- new version (closes: #35634)

