%define _unpackaged_files_terminate_build 1
%define jbbuild 635.79
%define jbr_conf linux-%_target_cpu-server-release

Name: jbr-runtime
Version: 25.0.4.1b635.79
Release: alt1

Summary: JetBrains Runtime and build JDK for IntelliJ Platform
License: GPL-2.0-only with Classpath-exception-2.0
Group: Development/Java
URL: https://github.com/JetBrains/JetBrainsRuntime
VCS: https://github.com/JetBrains/JetBrainsRuntime.git

Source: %name-%version.tar.gz
Patch: jbr-alt-archive.patch

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-macros-java
BuildRequires: java-25-openjdk-devel
BuildRequires: gcc-c++
BuildRequires: autoconf
BuildRequires: zip
BuildRequires: unzip
BuildRequires: libalsa-devel
BuildRequires: libcups-devel
BuildRequires: fontconfig-devel
BuildRequires: libfreetype-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXrender-devel
BuildRequires: libXtst-devel
BuildRequires: libXt-devel
BuildRequires: libXi-devel
BuildRequires: libXrandr-devel
BuildRequires: libdbus-devel
BuildRequires: libspeechd-devel
BuildRequires: libwayland-client-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: wayland-devel
BuildRequires: wayland-protocols
BuildRequires: libxkbcommon-devel
BuildRequires: libvulkan-devel
BuildRequires: glslang

%description
JetBrains Runtime built from the official JBR release source. The runtime
uses the upstream module list and private versioned installation directory.

%package -n jbr-build-jdk
Summary: JetBrains Runtime development kit for IntelliJ Platform
Group: Development/Java

%description -n jbr-build-jdk
Full development kit built together with JetBrains Runtime. Includes javac,
jlink and JDK modules without changing the system Java alternatives.

%prep
%setup
%autopatch -p1

%build
# Whole-libjvm LTO exceeded 48 GiB of RAM.
%remove_optflags -flto=auto
export JDK_BUILD_NUMBER=1
bash -eu <<'BUILD'
source jb/project/tools/common/scripts/common.sh %jbbuild nomod
speechd_include=
for candidate in %_includedir %_includedir/speech-dispatcher; do
    if test -f "$candidate/libspeechd.h"; then
        speechd_include=$candidate
        break
    fi
done
test -n "$speechd_include"
bash configure \
    --with-debug-level=release \
    --with-vendor-name="$VENDOR_NAME" \
    --with-vendor-version-string="$VENDOR_VERSION_STRING" \
    --with-jvm-features=shenandoahgc \
    --with-version-pre= \
    --with-version-build="$JDK_BUILD_NUMBER" \
    --with-version-opt=b"$build_number" \
    --with-boot-jdk=%_jvmdir/java-25-openjdk \
    --build=%_target_cpu-unknown-linux-gnu \
    --openjdk-target=%_target_cpu-unknown-linux-gnu \
    --enable-cds=yes \
    --with-wayland-protocols=%_datadir/wayland-protocols \
    --with-speechd-include="$speechd_include" \
    --with-vulkan \
    --with-freetype=system \
    --with-extra-cflags="%optflags" \
    --with-extra-cxxflags="%optflags" \
    --with-extra-ldflags="%{?__global_ldflags}" \
    --with-native-debug-symbols=zipped \
    $STATIC_CONF_ARGS $REPRODUCIBLE_BUILD_OPTS
make JOBS=%_smp_build_ncpus images CONF=%jbr_conf
modules=$(xargs < jb/project/tools/common/modules.list | tr -d ' ')
build/%jbr_conf/images/jdk/bin/jlink \
    --module-path build/%jbr_conf/images/jmods \
    --no-man-pages --compress=2 --generate-cds-archive \
    --add-modules "$modules" --output build/runtime-image
grep -v '^JAVA_VERSION' build/%jbr_conf/images/jdk/release \
    | grep -v '^MODULES' >> build/runtime-image/release
BUILD

%install
mkdir -p %buildroot%_jvmdir/jbr-runtime-%version
cp -a build/runtime-image/. %buildroot%_jvmdir/jbr-runtime-%version/
mkdir -p %buildroot%_jvmdir/jbr-build-%version
cp -a build/%jbr_conf/images/jdk/. \
    %buildroot%_jvmdir/jbr-build-%version/
rm -f %buildroot%_jvmdir/jbr-build-%version/lib/src.zip
for image in jbr-runtime jbr-build; do
    ln -s server/libjvm.so %buildroot%_jvmdir/$image-%version/lib/libjvm.so
done

%files
%doc LICENSE ASSEMBLY_EXCEPTION ADDITIONAL_LICENSE_INFO
%_jvmdir/jbr-runtime-%version

%files -n jbr-build-jdk
%_jvmdir/jbr-build-%version

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 25.0.4.1b635.79-alt1
- Initial build for ALT.
