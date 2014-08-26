# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global artifactId javax.el-api

Name:           glassfish-el-api
Version:        2.2.4
Release:        alt1_1jpp7
Summary:        Expression Language API 2.2.4

Group:          Development/Java
# Part of implementation files contain ASL 2.0 copyright
License:        CDDL and ASL 2.0
URL:            http://uel.java.net
# svn export https://svn.java.net/svn/uel~svn/tags/javax.el-api-2.2.4 javax.el-api-2.2.4
# tar cvJf javax.el-api-2.2.4.tar.xz javax.el-api-2.2.4/
Source0:        %{artifactId}-%{version}.tar.xz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  jvnet-parent
BuildRequires:  maven-local
BuildRequires:  maven
BuildRequires:  maven-source-plugin
Source44: import.info

%description
This project provides an implementation of the Expression Language (EL). 
The main goals are:
 * Improves current implementation: bug fixes and performance improvements
 * Provides API for use by other tools, such as Netbeans

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{artifactId}-%{version}
cp -p %{SOURCE1} .

%build
mvn-rpmbuild install javadoc:javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{artifactId}-%{version}.jar \
    %{buildroot}%{_javadir}/%{name}.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/
rm -rf target/site/api*

%files -f .mfiles
%doc LICENSE-2.0.txt

%files javadoc
%doc LICENSE-2.0.txt
%{_javadocdir}/%{name}

%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.4-alt1_1jpp7
- new release

