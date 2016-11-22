Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global short_name      taglibs-standard

Name:           tomcat-taglibs-standard
Version:        1.2.5
Release:        alt1_2jpp8
Epoch:          0
Summary:        Apache Standard Taglib
License:        ASL 2.0
URL:            http://tomcat.apache.org/taglibs/
Source0:        http://apache.cbox.biz/tomcat/taglibs/taglibs-standard-%{version}/taglibs-standard-%{version}-source-release.zip
Patch0: servlet31.patch

BuildArch:      noarch
BuildRequires:  maven-local
BuildRequires:  mvn(javax.el:el-api)
BuildRequires:  mvn(javax.servlet.jsp:jsp-api)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-checkstyle-plugin)
BuildRequires:  mvn(org.apache.taglibs:taglibs-parent:pom:)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(xalan:xalan)

Obsoletes: jakarta-taglibs-standard < 1.1.2-13
Source44: import.info

%description
An implementation of the JSP Standard Tag Library (JSTL).

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
Obsoletes: jakarta-taglibs-standard-javadoc < 1.1.2-13
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{short_name}-%{version}
%patch0 -b .sav
%mvn_alias org.apache.taglibs:taglibs-standard-impl javax.servlet:jstl
%mvn_alias org.apache.taglibs:taglibs-standard-impl org.eclipse.jetty.orbit:javax.servlet.jsp.jstl
%mvn_alias org.apache.taglibs:taglibs-standard-compat org.eclipse.jetty.orbit:org.apache.taglibs.standard.glassfish

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE
%doc README_src.txt README_bin.txt NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE
%doc NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2.5-alt1_2jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2.5-alt1_1jpp8
- java 8 mass update

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

