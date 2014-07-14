Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
%global vendor      weavejester
%global groupId     clucy
%global artifactId  clucy
%global commit_hash 103a939

Name:           %{artifactId}
Version:        0.3.0
Release:        alt2_3jpp7
Summary:        Clojure interface to Lucene

License:        EPL
URL:            https://github.com/%{vendor}/%{name}/
# wget --content-disposition %%{url}/tarball/%%{version}
Source0:        %{vendor}-%{name}-%{version}-0-g%{commit_hash}.tar.gz
# generated using 'lein multi pom --with 1.2-lucene2' using Leiningen 1.7.1
# as we don't have leiningen packaged yet
# (Leiningen 2.x is needed as project.clj uses new-style profiles
#  not supported by Leiningen 1.x)
Source1:        %{name}-pom.xml
# Manifest file for our JAR generation
Source2:        %{name}-manifest.txt

BuildArch:      noarch

BuildRequires:  jpackage-utils


Requires:       jpackage-utils
%if 0%{?rhel}
Requires(post):   jpackage-utils
Requires(postun): jpackage-utils
%endif

Requires:       clojure-compat
Requires:       lucene-contrib
Source44: import.info


%description
Clucy is a Clojure interface to Lucene.


%prep
%setup -q -n %{vendor}-%{name}-ea39643
cp -p %{SOURCE1} pom.xml
cp -p %{SOURCE2} manifest.txt


%build
jar cmf manifest.txt %{name}.jar -C src .


%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 %{name}.jar \
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
%doc LICENSE.html README.md ChangeLog
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom
%{_javadir}/%{name}.jar


%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_3jpp7
- new version

