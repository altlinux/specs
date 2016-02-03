%define __global_ldflags %nil
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name native-platform
%define version 0.10
%global debug_package %{nil}

%global namedreltag %{nil}
%global namedversion %{version}%{?namedreltag}

Name:          native-platform
Version:       0.10
Release:       alt1_7jpp8
Summary:       Java bindings for various native APIs
License:       ASL 2.0
URL:           https://github.com/adammurdoch/native-platform
Source0:       https://github.com/adammurdoch/native-platform/archive/%{namedversion}.tar.gz
# From Debian
Source4:       %{name}-0.7-Makefile
# Try to load native library from /usr/lib*/native-platform
# instead of extractDir or classpath.
Patch0:        %{name}-0.10-NativeLibraryLocator.patch
# Use generate libraries without arch references
# Add support for arm and other x64 arches
Patch1:        %{name}-0.10-native-libraries-name.patch

# build tools and deps
BuildRequires: javapackages-local
BuildRequires: ncurses-devel
BuildRequires: jopt-simple
Source44: import.info

%description
A collection of cross-platform Java APIs
for various native APIs.

These APIs support Java 5 and later. Some
of these APIs overlap with APIs available
in later Java versions.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch:     noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
find .  -name "*.jar" -delete
find .  -name "*.class" -delete

%patch0 -p0
%patch1 -p0

cp -p %{SOURCE4} Makefile

chmod 644 readme.md
sed -i 's/\r//' readme.md

# TODO
mv src/curses/cpp/*.cpp src/main/cpp
mv src/shared/cpp/* src/main/cpp

%build
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ;
CPPFLAGS="${CPPFLAGS:-%optflags}" ; export CPPFLAGS ;
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS ;
LDFLAGS="${LDFLAGS:-%__global_ldflags}"; export LDFLAGS;
make %{?_smp_mflags} JAVA_HOME=%{_jvmdir}/java

%mvn_artifact net.rubygrapefruit:%{name}:%{version} build/%{name}.jar
%mvn_file : %{name}

%install
%mvn_install -J build/docs/javadoc
mkdir -p %{buildroot}%{_libdir}/%{name}
install -pm 0755 build/binaries/libnative-platform-curses.so %{buildroot}%{_libdir}/%{name}/
install -pm 0755 build/binaries/libnative-platform.so %{buildroot}%{_libdir}/%{name}/

%files -f .mfiles
%{_libdir}/%{name}
%doc readme.md
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_7jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_0.2.rc2jpp7
- new release

