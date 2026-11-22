%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
# END SourceDeps(oneline)

Name: pngencoder
Version: 0.16.0
Release: alt1

Summary: Fast PNG encoder library for Java
License: MIT
Group: Development/Java
URL: https://github.com/pngencoder/pngencoder
VCS: https://github.com/pngencoder/pngencoder

Source0: pngencoder-%version.tar.gz
Patch0: pngencoder-jdk21-imageio.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.hamcrest:hamcrest)
BuildRequires: mvn(org.openjdk.jmh:jmh-generator-annprocess)

BuildArch: noarch

%description
A Java library for encoding PNG images, supporting RGB, ARGB, grayscale
and indexed color images with optional predictor encoding.

%package javadoc
Group: Development/Java
Summary: Javadoc for %name

%description javadoc
API documentation for %name.

%prep
%setup -q
%patch0 -p1
find . -name '*.class' -delete
find . -name '*.jar' -delete
%pom_remove_plugin :maven-enforcer-plugin

%mvn_file com.pngencoder:pngencoder %name

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%name
%doc LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 0.16.0-alt1
- Initial build for ALT.
