%define _unpackaged_files_terminate_build 1

Name: latencyutils
Version: 2.0.3
Release: alt1

Summary: Latency recording and reporting utilities
License: CC0-1.0
Group: Development/Java
Url: https://latencyutils.github.io/LatencyUtils
VCS: https://github.com/LatencyUtils/LatencyUtils.git

Source: %name-%version.tar
Patch: wait-for-pause-notification.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.hdrhistogram:HdrHistogram)

%description
LatencyUtils provides latency recording and reporting utilities, including
pause detection and interval estimation for coordinated omission correction.

%prep
%setup
%patch -p1
%pom_remove_parent
%pom_remove_plugin :maven-dependency-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-gpg-plugin

%build
# JDK 8 javac preserves the upstream Java 6 bytecode target while XMvn
# itself runs on the system JDK 17.
%mvn_build -s -j -- -Dmaven.compiler.fork=true \
    -Dmaven.compiler.executable=%_jvmdir/java-1.8.0-openjdk/bin/javac

%install
%mvn_install

%files -f .mfiles-LatencyUtils
%doc LICENSE README.md

%changelog
* Fri Oct 30 2026 Ivan Khanas <xeno@altlinux.org> 2.0.3-alt1
- Initial build for ALT.
