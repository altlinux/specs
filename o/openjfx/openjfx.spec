Name: openjfx
Version: 25.0.4
Release: alt1
Epoch: 3
Summary: OpenJFX graphical user interface toolkit for Java

License: GPL-2.0-only WITH Classpath-exception-2.0 AND LGPL-2.1-or-later AND MIT AND IJG
Group: Development/Java
URL: https://openjfx.io/
VCS: https://github.com/openjdk/jfx25u
Source: %name.tar
Patch0: %name-ffmpeg8.patch
Patch1: %name-gradle9.patch
Patch2: %name-private-libs.patch
Patch3: %name-swscale.patch
ExcludeArch: %ix86

BuildRequires(pre): rpm-build-java
BuildRequires: java-25-openjdk-devel gradle antlr4 javapackages-local
BuildRequires: gcc-c++ make pkgconfig libgtk+3-devel libpango-devel
BuildRequires: libXtst-devel libXxf86vm-devel libalsa-devel libavcodec-devel libavformat-devel libavutil-devel libswscale-devel

%description
OpenJFX provides the JavaFX user interface toolkit, including graphics,
controls, FXML and multimedia support.

%prep
%setup -n %name
# Upstream FFmpeg 8 support, followed by system Gradle 9 compatibility.
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
# The system FFmpeg 9 uses ABI 63; the upstream decoder already compiles with it.
subst 's/61, 62 }/61, 62, 63 }/' modules/javafx.media/src/main/native/gstreamer/gstreamer-lite/gstreamer/gst/gstregistry.c

# SWT is an optional interoperation module, not used by the shipped toolkit.
subst 's/LINUX.compileSWT = true/LINUX.compileSWT = false/' buildSrc/linux.gradle
# Use the distribution shared C++ runtime.
subst 's/"-static-libgcc", "-static-libstdc++", //' buildSrc/linux.gradle
subst 's/-static-libgcc -static-libstdc++ //g' \
    modules/javafx.media/src/main/native/jfxmedia/projects/linux/Makefile \
    modules/javafx.media/src/main/native/gstreamer/projects/linux/*/Makefile

%mvn_file 'org.openjfx:javafx-{*}' %name/javafx.@1

%build
export JAVA_HOME=%_jvmdir/java-25-openjdk
export PATH="$JAVA_HOME/bin:$PATH"
export GRADLE_USER_HOME="$PWD/.gradle-home"
gradle --offline --no-daemon --max-workers=8 \
    -PGRADLE_VERSION_CHECK=false -PCOMPILE_MEDIA=true -PCOMPILE_WEBKIT=false \
    -PCONF=Release -PRELEASE_SUFFIX= -PPROMOTED_BUILD_NUMBER=3 sdk

# Publish only complete modules; WebKit and optional incubators are not built.
for module in base graphics controls fxml media swing; do
    cat > "build/javafx-$module.pom" <<EOF
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>
  <groupId>org.openjfx</groupId><artifactId>javafx-$module</artifactId>
  <version>%version</version>
  <dependencies>
EOF
    case "$module" in
        base) deps='' ;;
        graphics) deps='base' ;;
        *) deps='base graphics' ;;
    esac
    for dependency in $deps; do
        cat >> "build/javafx-$module.pom" <<EOF
    <dependency><groupId>org.openjfx</groupId>
      <artifactId>javafx-$dependency</artifactId><version>%version</version>
    </dependency>
EOF
    done
    echo '</dependencies></project>' >> "build/javafx-$module.pom"
    %mvn_artifact "build/javafx-$module.pom" "build/sdk/lib/javafx.$module.jar"
    mkdir -p legal
    cp -a "build/sdk/legal/javafx.$module" legal/
done

%install
%mvn_install
install -d %buildroot%_libdir/%name
install -m755 build/sdk/lib/*.so %buildroot%_libdir/%name/
install -d %buildroot%_jvmdir/%name
for module in base graphics controls fxml media swing; do
    ln -sr %buildroot%_javadir/%name/javafx.$module.jar %buildroot%_jvmdir/%name/javafx.$module.jar
done
for library in build/sdk/lib/*.so; do
    ln -sr %buildroot%_libdir/%name/"${library##*/}" %buildroot%_jvmdir/%name/"${library##*/}"
done

%files -f .mfiles
%doc LICENSE ADDITIONAL_LICENSE_INFO ASSEMBLY_EXCEPTION README.md legal
%_libdir/%name/
%_jvmdir/%name/

%changelog
* Wed Sep 09 2026 Vitaly Lipatov <lav@altlinux.ru> 3:25.0.4-alt1
- Restore to Sisyphus and update to 25.0.4.
- Build offline with system Gradle and register Maven artifacts.
- Enable multimedia with system FFmpeg and preserve the JVM library entry point.
- Fixes: CVE-2026-21947, CVE-2026-47013, CVE-2026-47034, CVE-2026-60166.

* Mon Apr 21 2025 Andrey Cherepanov <cas@altlinux.org> 3:21.0.13-alt1
- New version.
- Built using Java 21.

* Mon May 13 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 3:17.0.10.0.7-alt2
- Build for aarch64 and LoongArch (no changes required).

* Fri May 10 2024 Andrey Cherepanov <cas@altlinux.org> 3:17.0.10.0.7-alt1
- New version.
- Built from upstream tag.
- Built using openjdk17.

* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 3:11.0.9.2-alt1_6jpp11
- fixed build

* Mon Jan 18 2021 Igor Vlasenko <viy@altlinux.ru> 3:11.0.9.2-alt1_3jpp11
- new version

* Mon Jan 13 2020 Igor Vlasenko <viy@altlinux.ru> 8.0.202-alt1_8.b07jpp8
- fixed build

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 8.0.202-alt1_5.b07jpp8
- new version

* Sat Apr 06 2019 Igor Vlasenko <viy@altlinux.ru> 8.0.152-alt1_17.b05jpp8
- new version (closes: #35634)
