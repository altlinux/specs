%define _unpackaged_files_terminate_build 1
%global bundle org.apache.felix.framework
%global felix_source_base https://downloads.apache.org/felix/

Name: felix-framework
Version: 8.0.0
Release: alt1

Summary: Apache Felix OSGi Framework
License: Apache-2.0
Group: Development/Java
URL: https://felix.apache.org/
VCS: https://github.com/apache/felix-dev.git
BuildArch: noarch

Source0: %{felix_source_base}%{bundle}-%{version}-source-release.tar.gz

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:felix-parent:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.felix:org.apache.felix.resolver)
BuildRequires: mvn(org.osgi:org.osgi.annotation)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.ow2.asm:asm-tree)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.codehaus.mojo:animal-sniffer-annotations)
BuildRequires: mvn(org.moditect:moditect-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)

%description
Apache Felix Framework is an implementation of the OSGi Core specification.

%package javadoc
Summary: Javadoc for %{name}
Group: Development/Java
BuildArch: noarch

%description javadoc
Javadoc for the Apache Felix Framework API.

%prep
%setup -q -n %{bundle}-%{version}
sed -i '/<artifactId>felix-parent<\/artifactId>/{
    n
    s#<version>8</version>#<version>7</version>#
}' pom.xml
sed -i \
    -e '/maven-source-plugin/a\        <version>3.2.1</version>' \
    -e 's#<version>6.0.0</version>#<version>8.0.1</version>#' \
    -e 's#<version>9.8</version>#<version>9.11.1</version>#' \
    -e 's#<version>5.12.1</version>#<version>5.14.4</version>#' \
    -e 's#<version>5.18.0</version>#<version>5.20.0</version>#' \
    -e 's#<version>3.27.7</version>#<version>3.27.3</version>#' \
    -e 's#<version>1.9</version>#<version>1.28</version>#' \
    -e 's#<version>5.1.1</version>#<version>5.1.9</version>#' \
    -e 's#<version>1.0.0.RC1</version>#<version>1.3.0</version>#' pom.xml
%pom_remove_plugin org.apache.rat:apache-rat-plugin

%build
%mvn_build -- \
    -Dsource=11 \
    -Dmaven.compiler.release=11 \
    -Dxmvn.javadoc.ignoreJPMS=true

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE
%doc DEPENDENCIES

%files javadoc -f .mfiles-javadoc

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 8.0.0-alt1
- New version.
* Tue May 18 2021 Igor Vlasenko <viy@altlinux.org> 5.6.0-alt2_8jpp8
- fixed build
* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 5.6.0-alt1_8jpp8
- fc update
* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 5.6.0-alt1_6jpp8
- new version
* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 5.6.0-alt1_5jpp8
- fc29 update
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 5.6.0-alt1_4jpp8
- java update
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 5.6.0-alt1_3jpp8
- fc27 update
* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 5.6.0-alt1_2jpp8
- new jpp release
* Wed Dec 07 2016 Igor Vlasenko <viy@altlinux.ru> 5.4.0-alt1_3jpp8
- new version
* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1_1jpp8
- java 8 mass update
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies
* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt1_1jpp7
- new version
* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.2-alt1_4jpp7
- new version
* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.2-alt1_3jpp7
- new release
* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt1_3jpp6
- new jpp release
