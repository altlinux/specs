# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-interceptors-1.2-api
%define version 1.0.0
%global namedreltag .Alpha3
%global namedversion %{version}%{?namedreltag}
%global oname jboss-interceptors-api_1.2_spec
Name:          jboss-interceptors-1.2-api
Version:       1.0.0
Release:       alt1_0.1.Alpha3jpp7
Summary:       Java(TM) EE Interceptors 1.2 API
Group:         Development/Java
License:       CDDL or GPLv2 with exceptions
URL:           https://github.com/jboss/jboss-interceptors-api_spec
Source0:       https://github.com/jboss/jboss-interceptors-api_spec/archive/%{namedversion}.tar.gz

BuildRequires: jboss-parent

BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-resources-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-plugin

BuildArch:     noarch
Source44: import.info

%description
The Java(TM) EE  Interceptors 1.2 API classes from JSR 318.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n jboss-interceptors-api_spec-%{namedversion}

%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId ='maven-bundle-plugin']" \
 "<version>any</version>"

# Fix incorrect-fsf-address
sed -i "s,59,51,;s,Temple Place,Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301," LICENSE

%build

mvn-rpmbuild package javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}/%{name}
install -m 644 target/%{oname}-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE README

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE

%changelog
* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.1.Alpha3jpp7
- new version

