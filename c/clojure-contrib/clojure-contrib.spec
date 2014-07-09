Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global vendor      clojure
%global groupId     org.clojure
%global artifactId  clojure-contrib
%global commit_hash 2a4e52d

Name:           %{artifactId}
Version:        1.2.0
Release:        alt1_4jpp7
Summary:        User contributions library for Clojure

License:        EPL
URL:            http://richhickey.github.com/clojure-contrib/
# wget --content-disposition \
#      https://github.com/%%{vendor}/%%{name}/tarball/%%{version}
Source0:        %{vendor}-%{name}-%{version}-0-g%{commit_hash}.tar.gz

BuildArch:      noarch

BuildRequires:  jpackage-utils


BuildRequires:  maven-local

BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-release-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-plugin

BuildRequires:  clojure-compat
BuildRequires:  clojure-maven-plugin

Requires:       jpackage-utils
%if 0%{?rhel}
Requires(post):   jpackage-utils
Requires(postun): jpackage-utils
%endif

Requires:       clojure-compat
Source44: import.info

%description
The user contributions library, clojure-contrib, is a collection of
namespaces implementing features that may be useful to a large part of
the Clojure community.

It includes namespaces for math utilities, string manipulation,
sequence manipulation, json read and write and many more.


%prep
%setup -q -n %{vendor}-%{name}-c9572b3


%build
%if 0%{?rhel}
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

mvn-jpp \
    -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
%else
mvn-rpmbuild \
%endif
    install


%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 target/%{name}-%{version}.jar \
    $RPM_BUILD_ROOT/%{_javadir}/%{name}.jar

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml \
    $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom

%if 0%{?add_maven_depmap:1}
%add_maven_depmap JPP-%{name}.pom %{name}.jar
%else
%add_to_maven_depmap %{groupId} %{artifactId} %{version} JPP %{name}.jar
%endif


%files
%doc epl-v10.html README.txt
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom
%{_javadir}/%{name}.jar


%changelog
* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_4jpp7
- update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_2jpp7
- new version

