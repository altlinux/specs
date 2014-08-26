# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global artifactId javax.el

Name:           glassfish-el
Version:        2.2.5
Release:        alt1_2jpp7
Summary:        J2EE Expression Language Implementation
Group:          Development/Java
License:        CDDL or GPLv2 with exceptions
URL:            http://uel.java.net
# svn export https://svn.java.net/svn/uel~svn/tags/javax.el-2.2.5/ javax.el-2.2.5
# tar cvJf javax.el-2.2.5.tar.xz javax.el-2.2.5/
Source0:        %{artifactId}-%{version}.tar.xz
BuildArch:      noarch

BuildRequires:  jvnet-parent
BuildRequires:  maven-local
BuildRequires:  maven
BuildRequires:  maven-source-plugin
BuildRequires:  mvn(javax.el:javax.el-api)
Requires:       mvn(javax.el:javax.el-api)
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

%build
mvn-rpmbuild \
        install javadoc:javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{artifactId}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap -a "org.eclipse.jetty.orbit:com.sun.el"

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/
rm -rf target/site/api*

%files -f .mfiles

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.5-alt1_2jpp7
- new release

