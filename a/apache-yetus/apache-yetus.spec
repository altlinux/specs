Name:           apache-yetus
Version:        0.15.1
Release:        alt1

Summary:        Apache Yetus
License:        Apache-2.0
Group:          Development/Java
URL:            https://yetus.apache.org/
VCS:            https://github.com/apache/yetus

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

Buildrequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)

BuildArch:      noarch

%description
Apache Yetus is a collection of libraries and tools that enable contribution and
release process for software projects.

%package -n     yetus-maven-plugin
Summary:        Apache Yetus - Maven Plugin
Group:          Development/Java

%description -n yetus-maven-plugin
Apache Yetus Maven Tools.

%prep
%setup

%pom_xpath_remove "//*[local-name()='plugin' and ./*[local-name()='artifactId']='flatten-maven-plugin']"
%pom_xpath_remove "//*[local-name()='plugin' and ./*[local-name()='artifactId']='maven-enforcer-plugin']"
%pom_xpath_remove "//*[local-name()='plugin' and ./*[local-name()='artifactId']='maven-assembly-plugin']" audience-annotations-component/audience-annotations

sed -i -e '/<module>precommit<\/module>/d' \
       -e '/<module>releasedocmaker<\/module>/d' \
       -e '/<module>shelldocs<\/module>/d' \
       -e '/<module>yetus-dist<\/module>/d' \
       -e '/<module>yetus-assemblies<\/module>/d' \
       -e '/<module>asf-site-src<\/module>/d' pom.xml

%mvn_package :yetus-maven-plugin maven-plugin

%build
%mvn_build -j -- -Dmaven.compiler.release=

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE README.md

%files -n yetus-maven-plugin -f .mfiles-maven-plugin

%changelog
* Fri Apr 17 2026 Evgeniy Serov <scala@altlinux.org> 0.15.1-alt1
- Initial build for Sisyphus.
