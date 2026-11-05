%define _unpackaged_files_terminate_build 1

Name: threeten-extra
Version: 1.11.0
Release: alt1

Summary: Additional date-time classes for Java
License: BSD-3-Clause
Group: Development/Java
URL: https://www.threeten.org/threeten-extra/
VCS: https://github.com/ThreeTen/threeten-extra.git

Source0: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-17-openjdk-devel
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.google.guava:guava-testlib)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.joda:joda-convert)
BuildRequires: mvn(org.jspecify:jspecify)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.junit-pioneer:junit-pioneer)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)

%description
ThreeTen-Extra adds date-time classes that complement the Java date and time
API with specialized functionality maintained by the ThreeTen project.

%javadoc_package

%prep
%setup
%autopatch -p1
%pom_remove_plugin org.jacoco:jacoco-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-checkstyle-plugin
%pom_xpath_inject \
    "pom:project/pom:profiles/pom:profile[pom:id='java9plus']/\
pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-dependency-plugin']/\
pom:executions/pom:execution[pom:id='copy-dependencies']/pom:configuration" \
    '<excludeArtifactIds>byte-buddy,byte-buddy-dep</excludeArtifactIds>'
%pom_xpath_remove \
    "pom:project/pom:profiles/pom:profile[pom:id='java9plus']/\
pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-surefire-plugin']/\
pom:executions/pom:execution[pom:id='default-test']/\
pom:configuration/pom:argLine"
%pom_xpath_inject \
    "pom:project/pom:profiles/pom:profile[pom:id='java9plus']/\
pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-surefire-plugin']/\
pom:executions/pom:execution[pom:id='default-test']/pom:configuration" \
    '<argLine>--add-modules org.joda.convert
--module-path ${project.build.directory}/dependencies</argLine>'

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-threeten-extra
%doc LICENSE.txt

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 1.11.0-alt1
- Initial build for ALT.
