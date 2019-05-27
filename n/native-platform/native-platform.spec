Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 0.14
%global debug_package %{nil}

%global namedreltag %{nil}
%global namedversion %{version}%{?namedreltag}

Name:          native-platform
Version:       0.14
Release:       alt1_15jpp8
Summary:       Java bindings for various native APIs
License:       ASL 2.0
URL:           https://github.com/adammurdoch/native-platform
Source0:       https://github.com/adammurdoch/native-platform/archive/%{namedversion}.tar.gz
# From Debian
Source4:       %{name}-0.7-Makefile
# Try to load native library from /usr/lib*/native-platform
# instead of extractDir or classpath.
Patch0:        0001-Load-lib-from-system.patch
# Use generate libraries without arch references
# Add support for arm and other x64 arches
Patch1:        0002-Use-library-name-without-arch.patch

# build tools and deps
BuildRequires:  gcc-c++
BuildRequires: java-devel
BuildRequires: javapackages-local
BuildRequires: libncurses++-devel libncurses-devel libncursesw-devel libtic-devel libtinfo-devel
BuildRequires: jopt-simple
Source44: import.info
Patch33: native-platform-0.10-as-needed.patch

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

%patch0 -p1
%patch1 -p1

cp -p %{SOURCE4} Makefile

chmod 644 readme.md
sed -i 's/\r//' readme.md

# TODO
mv src/curses/cpp/*.cpp src/main/cpp
mv src/shared/cpp/* src/main/cpp
%patch33 -p1

%build
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ;
CPPFLAGS="${CPPFLAGS:-%optflags}" ; export CPPFLAGS ;
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS ;
%make_build JAVA_HOME=%{_jvmdir}/java

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
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_15jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_13jpp8
- java update

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1_12jpp8
- java update

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_11jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_9jpp8
- new jpp release

* Sat Feb 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_8jpp8
- fixed linkage

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_7jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_0.2.rc2jpp7
- new release

