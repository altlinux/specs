%define _unpackaged_files_terminate_build 1

Name: minlog
Version: 1.3.1
Release: alt1

Summary: Minimal overhead Java logging
License: BSD-3-Clause
Group: Development/Java
URL: https://github.com/EsotericSoftware/minlog
VCS: https://github.com/EsotericSoftware/minlog.git
BuildArch: noarch

Source0: %name-%version.tar.gz

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: rpm-build-java-osgi
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)

%description
MinLog is a small Java logging library. Logging statements below a constant
log level can be removed by the compiler. The API supports configurable log
levels and custom logger implementations.

%package javadoc
Summary: Javadoc for MinLog
Group: Development/Java

%description javadoc
API documentation for the MinLog Java logging library.

%prep
%setup -q -n minlog-minlog-%version
find . -type f \( -name '*.class' -o -name '*.jar' \) -delete
# Preserve the published package scope; sources stay in the SRPM.
%pom_remove_plugin :maven-source-plugin
# XMvn generates the documentation; avoid duplicate attached Javadocs.
%pom_remove_plugin :maven-javadoc-plugin

%mvn_file :minlog minlog
%mvn_alias :minlog com.googlecode:minlog com.esotericsoftware.minlog:minlog
%mvn_package :minlog minlog

%build
%mvn_build -s -- -Dmaven.compiler.source=8 -Dmaven.compiler.target=8

%install
%mvn_install

%files -f .mfiles-minlog
%doc license.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Oct 27 2026 Ivan Khanas <xeno@altlinux.org> 1.3.1-alt1
- New version.

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_8jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_6jpp8
- java update

* Wed Nov 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_5jpp8
- fc update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_4jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_3jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_2jpp8
- new version
