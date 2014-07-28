# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%define fedora 21
Name:          littleproxy
Version:       0.4
Release:       alt1_4jpp7
Summary:       High Performance HTTP Proxy
Group:         Development/Java
License:       ASL 2.0
URL:           http://www.littleshoot.org/littleproxy/
# git clone git://github.com/adamfisk/LittleProxy.git littleproxy-0.4
# cd littleproxy-0.4 &&  git archive --format=tar --prefix=littleproxy-0.4/ littleproxy-0.4 | xz > ../littleproxy-0.4-src-git.tar.xz
Source0:       %{name}-%{version}-src-git.tar.xz
# add netty 3.5.x support
Patch0:        %{name}-%{version}-netty35.patch
# remove: maven-assembly-plugin, maven-gpg-plugin
Patch1:        %{name}-%{version}-pom.patch

BuildRequires: jpackage-utils
BuildRequires: sonatype-oss-parent

BuildRequires: apache-commons-codec
BuildRequires: apache-commons-io
BuildRequires: apache-commons-lang
BuildRequires: ehcache-core
BuildRequires: log4j
BuildRequires: netty
BuildRequires: slf4j

# test deps
BuildRequires: junit

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4

Requires:      apache-commons-codec
Requires:      apache-commons-io
Requires:      apache-commons-lang
Requires:      ehcache-core
Requires:      log4j
Requires:      netty
Requires:      slf4j

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
LittleProxy is a high performance HTTP proxy written in Java and
using the Netty networking framework.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%if %{?fedora} > 17
%patch0 -p1
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin
%else
%patch1 -p0
%endif

%build

mvn-rpmbuild install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc COPYRIGHT.txt LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc COPYRIGHT.txt LICENSE.txt

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_4jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_2jpp7
- new version

