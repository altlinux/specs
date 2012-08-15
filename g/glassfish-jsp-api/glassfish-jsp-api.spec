BuildRequires:  maven-enforcer-plugin
BuildRequires: /proc
BuildRequires: jpackage-compat
%global artifactId javax.servlet.jsp-api
%global jspspec 2.2


Name:       glassfish-jsp-api
Version:    2.2.1
Release:    alt1_2jpp7
Summary:    Glassfish J2EE JSP API specification

Group:      Development/Java
License:    CDDL and GPLv2 with exceptions
URL:        http://glassfish.org
Source0:    %{artifactId}-%{version}.tar.xz
# no source releases, but this will generate tarball for you from an
# SVN tag
Source1:    generate_tarball.sh

BuildArch:  noarch

BuildRequires:  maven
BuildRequires:  maven-plugin-bundle
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  jvnet-parent
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(javax.el:javax.el-api)

Requires:       jvnet-parent
Requires:       mvn(javax.servlet:javax.servlet-api)
Requires:       mvn(javax.el:javax.el-api)
Source44: import.info

%description
This project provides a container independent specification of JSP
2.2. Note that this package doesn't contain implementation of this
specification. See glassfish-jsp for one of implementations

%package javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils >= 0:1.7.5
BuildArch:      noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{artifactId}-%{version}


%build
mvn-rpmbuild install javadoc:javadoc


%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 target/%{artifactId}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar


install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap

%files
%{_javadir}/%{name}.jar
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Wed Aug 15 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_2jpp7
- full version

