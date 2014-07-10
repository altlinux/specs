Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global upstream    talios
%global groupId     com.theoryinpractise
%global artifactId  clojure-maven-plugin
%global commit_hash 48bc0ce

Name:           %{artifactId}
Version:        1.3.10
Release:        alt1_4jpp7
Summary:        Clojure plugin for Maven

License:        EPL
URL:            https://github.com/%{upstream}/%{name}
# wget --content-disposition %%{url}/tarball/%%{version}
Source0:        %{upstream}-%{name}-%{name}-%{version}-0-g%{commit_hash}.tar.gz

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

BuildRequires:  apache-commons-exec
BuildRequires:  fest-assert
BuildRequires:  maven-invoker-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  mockito

Requires:       maven
# non-test dependency
Requires:       apache-commons-exec

Requires:       jpackage-utils
%if 0%{?rhel}
Requires(post):   jpackage-utils
Requires(postun): jpackage-utils
%endif
Source44: import.info


%description
This plugin has been designed to make working with clojure as easy as
possible, when working in a mixed language, enterprise project.


%prep
%setup -q -n %{upstream}-%{artifactId}-d03beed


%build
# test1.clj does not get discovered if LANG=C
# also, using 'package' instead of 'install' to avoid
# running integration tests - they do installation tests
# for a lot of packages*versions we do not currently have
export LANG=en_US.utf8
%if 0%{?rhel}
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

mvn-jpp \
    -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
%else
mvn-rpmbuild \
%endif
    package


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
%doc epl-v10.html README.markdown
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom
%{_javadir}/%{name}.jar


%changelog
* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.10-alt1_4jpp7
- update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.10-alt1_2jpp7
- new version

