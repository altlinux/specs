# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%define svndate 20101024
%define snapshot 63

Name:           bluecove
Version:        2.1.1
Release:        alt1_0.3.20101024snap63jpp7
Summary:        Implementation of JSR-82 Java Bluetooth API

Group:          System/Libraries
License:        ASL 2.0 and LGPLv2+ and GPLv3+
URL:            http://code.google.com/p/bluecove/

# Snapshot release sources
Source0:        http://snapshot.bluecove.org/distribution/download/%{version}-SNAPSHOT/%{version}-SNAPSHOT.%{snapshot}/bluecove-%{version}-SNAPSHOT-sources.tar.gz
Source1:        http://snapshot.bluecove.org/distribution/download/%{version}-SNAPSHOT/%{version}-SNAPSHOT.%{snapshot}/bluecove-gpl-%{version}-SNAPSHOT-sources.tar.gz
Source2:        http://snapshot.bluecove.org/distribution/download/%{version}-SNAPSHOT/%{version}-SNAPSHOT.%{snapshot}/bluecove-bluez-%{version}-SNAPSHOT-sources.tar.gz
Source3:        http://snapshot.bluecove.org/distribution/download/%{version}-SNAPSHOT/%{version}-SNAPSHOT.%{snapshot}/bluecove-emu-%{version}-SNAPSHOT-sources.tar.gz

# Official release sources
#Source0:        http://bluecove.googlecode.com/files/bluecove-%{version}-sources.tar.gz
#Source1:        http://bluecove.googlecode.com/files/bluecove-gpl-%{version}-sources.tar.gz
#Source2:        http://bluecove.googlecode.com/files/bluecove-bluez-%{version}-sources.tar.gz
#Source3:        http://bluecove.googlecode.com/files/bluecove-emu-%{version}-sources.tar.gz

Source4:        README.dist


BuildRequires:  jpackage-utils
BuildRequires:  ant
BuildRequires:  libbluez-devel
BuildRequires:  ant-nodeps
BuildRequires:  libmatthew-java
BuildRequires:  dbus-java >= 2.5.1
Requires:       jpackage-utils
Requires:       libmatthew-java
Requires:       dbus-java >= 2.5.1
Source44: import.info

%description
BlueCove is a JSR-82 implementation on Java Standard Edition (J2SE) that 
currently interfaces with the Mac OS X, WIDCOMM, BlueSoleil and Microsoft 
Bluetooth stack. Originally developed by Intel Research and currently 
maintained by volunteers.

This package adds additional support for:
- Linux with BlueZ (bluecove-gpl)
- Linux with BlueZ using DBUS for device discovery (bluecove-bluez)
- Emulator for use with MicroEmulator (bluecove-emu)

%prep
%setup -q -n bluecove-%{version}-SNAPSHOT
# unpack bluecove-gpl
tar zxf %{SOURCE1}
# unpack bluecove-bluez
tar zxf %{SOURCE2}
# unpack bluecove-emu
tar zxf %{SOURCE3}

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

cp -p bluecove-gpl-%{version}-SNAPSHOT/AUTHORS.txt AUTHORS-gpl.txt
cp -p bluecove-gpl-%{version}-SNAPSHOT/LICENSE.txt LICENSE-gpl.txt
 
# add README.dist
cp -p %{SOURCE4} .

%build
# build main bluecove
ant jar -Dproduct_version=%{version}

# build bluecove-gpl
cd bluecove-gpl-%{version}-SNAPSHOT
ant jar -Dproduct_version=%{version} \
        -Dbluecove_main_dist_dir=../target \
        -Dbluecove.native.resources.skip=true \
        -Dbluecove.native.linker.options="" \
        -DCC_compiler_options="${RPM_OPT_FLAGS} -fPIC -fno-stack-protector"

# build bluecove-bluez
cd ../bluecove-bluez-%{version}-SNAPSHOT
ant jar -Dproduct_version=%{version} \
        -Dbluecove_main_dist_dir=../target \
        -Ddbus_java_jar=%{_javadir}/dbus-java/dbus.jar \
        -Dlibmatthew_java_debug_jar=%{_libdir}/libmatthew-java/unix.jar \
        -Dbluecove.native.resources.skip=true \
        -Dbluecove.native.linker.options="" \
        -DCC_compiler_options="${RPM_OPT_FLAGS} -fPIC -fno-stack-protector"

# build bluecove-emu
cd ../bluecove-emu-%{version}-SNAPSHOT
ant jar -Dproduct_version=%{version} \
        -Dbluecove_main_dist_dir=../target

%install

mkdir -p $RPM_BUILD_ROOT%{_javadir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}/%{version}-SNAPSHOT

############
# BlueCove #
############
cp -p target/bluecove-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
# create symlink without version
(cd $RPM_BUILD_ROOT%{_javadir}/ && ln -sf %{name}-%{version}.jar %{name}.jar)

################
# BlueCove GPL #
################
cp -p bluecove-gpl-%{version}-SNAPSHOT/target/bluecove-gpl-%{version}.jar \
        $RPM_BUILD_ROOT%{_libdir}/%{name}/%{name}-gpl-%{version}.jar
# create symlink without version
(cd $RPM_BUILD_ROOT%{_libdir}/%{name} && ln -sf %{name}-gpl-%{version}.jar %{name}-gpl.jar)

# copy the GPL JNI library to library directory
cp -p bluecove-gpl-%{version}-SNAPSHOT/target/*.so $RPM_BUILD_ROOT%{_libdir}/%{name}/%{version}-SNAPSHOT

#######################
# BlueCove BlueZ DBUS #
#######################
cp -p bluecove-bluez-%{version}-SNAPSHOT/target/bluecove-bluez-%{version}.jar \
        $RPM_BUILD_ROOT%{_libdir}/%{name}/%{name}-bluez-%{version}.jar
# create symlink without version
(cd $RPM_BUILD_ROOT%{_libdir}/%{name} && ln -sf %{name}-bluez-%{version}.jar %{name}-bluez.jar)

# copy the BlueZ JNI library to library directory
cp -p bluecove-bluez-%{version}-SNAPSHOT/target/*.so $RPM_BUILD_ROOT%{_libdir}/%{name}/%{version}-SNAPSHOT

################
# BlueCove Emu #
################
cp -p bluecove-emu-%{version}-SNAPSHOT/target/bluecove-emu-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-emu-%{version}.jar
# create symlink without version
(cd $RPM_BUILD_ROOT%{_javadir}/ && ln -sf %{name}-emu-%{version}.jar %{name}-emu.jar)

%files
%{_javadir}/*
%{_libdir}/%{name}
%doc AUTHORS.txt README.txt LICENSE.txt stacks.txt todo.txt AUTHORS-gpl.txt LICENSE-gpl.txt README.dist

%changelog
* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt1_0.3.20101024snap63jpp7
- fc build

