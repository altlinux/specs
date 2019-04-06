Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gettext gcc-c++ libcxx-devel libicu-devel libpng-devel libsqlite3-devel perl(Archive/Zip.pm) perl(CGI.pm) perl(Class/Struct.pm) perl(Compress/Zlib.pm) perl(Config.pm) perl(Digest/MD5.pm) perl(English.pm) perl(Exporter.pm) perl(Fcntl.pm) perl(File/Spec/Functions.pm) perl(File/stat.pm) perl(FindBin.pm) perl(HTTP/Date.pm) perl(HTTP/Request.pm) perl(IO/File.pm) perl(IPC/Open2.pm) perl(IPC/Open3.pm) perl(JSON/PP.pm) perl(LWP/Simple.pm) perl(LWP/UserAgent.pm) perl(List/Util.pm) perl(MIME/Base64.pm) perl(Term/ANSIColor.pm) perl(Term/ReadKey.pm) perl(Test/Harness.pm) perl(Test/More.pm) perl(Test/Simple.pm) perl(Text/ParseWords.pm) perl(Time/HiRes.pm) perl(Time/gmtime.pm) perl(XML/Simple.pm) perl(base.pm) perl(sigtrap.pm) zip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name openjfx
%global openjfxdir %{_jvmdir}/%{name}

Name:           openjfx
Version:        8.0.152
Release:        alt1_17.b05jpp8
Summary:        Rich client application platform for Java

#fxpackager is BSD
License:        GPL v2 with exceptions and BSD
URL:            http://openjdk.java.net/projects/openjfx/

Source0:        http://hg.openjdk.java.net/openjfx/8u-dev/rt/archive/8u152-b05.tar.bz2
Source1:        README.fedora

Patch0:         0001-Fix-wait-call-in-PosixPlatform.patch
Patch1:         0002-Bulid-in-Gradle-local-mode.patch
Patch2:         0003-Allow-build-to-work-on-newer-gradles.patch
Patch3:         0004-fix-cast-between-incompatible-function-types.patch

ExclusiveArch:  %{ix86} x86_64

Requires:       javapackages-tools
Requires:       java

BuildRequires:  gradle-local
BuildRequires:  mvn(antlr:antlr)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.antlr:antlr:3.1.3)
BuildRequires:  mvn(org.antlr:stringtemplate)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.eclipse.swt:swt)

BuildRequires:  pkgconfig(gtk+-2.0)
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
BuildArch: noarch
Summary: Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.


%prep
%setup -q -n rt-8u152-b05
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

cp %{SOURCE1} .

cat > gradle.properties << EOF
COMPILE_WEBKIT = false
COMPILE_MEDIA = false
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
rm -rf modules/graphics/src/main/native-iio/libjpeg*

%build
#Tests do not run by default, tests in web fails and one test in graphics fail:
#UnsatisfiedLinkError: libjavafx_iio.so: undefined symbol: jpeg_resync_to_restart
gradle-local --no-daemon --offline


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
* Sat Apr 06 2019 Igor Vlasenko <viy@altlinux.ru> 8.0.152-alt1_17.b05jpp8
- new version (closes: #35634)

