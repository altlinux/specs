Name:           netty-jni-util
Version:        0.0.10
Release:        alt1

Summary:        Helper functions used by netty (and its subprojects) that use JNI
License:        Apache-2.0
Group:          Development/Java
URL:            https://github.com/netty/netty-jni-util
VCS:            https://github.com/netty/netty-jni-util

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local cmake
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)

BuildArch:      noarch

%description
%summary.

%javadoc_package

%package source
Summary:        Source files required for building dependent Netty native packages
Group:          Development/Java

%description source
Source files from netty-jni-util required to build dependent Netty native
packages.

%prep
%setup

%pom_remove_plugin :central-publishing-maven-plugin

%build
%mvn_build

%install
%mvn_install

install -d %buildroot%_usrsrc/%name/src/main
cp -a src/main/c %buildroot%_usrsrc/%name/src/main/

%files -f .mfiles
%doc *.md

%files source
%_usrsrc/%name/

%changelog
* Mon May 18 2026 Evgeniy Serov <scala@altlinux.org> 0.0.10-alt1
- Initial build for Sisyphus.
