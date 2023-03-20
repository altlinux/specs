Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global srcname jsp-api

Name:           jakarta-server-pages
Version:        2.3.6
Release:        alt1_9jpp11
Summary:        Jakarta Server Pages (JSP)
# some files have Apache-2.0 license headers
# https://github.com/eclipse-ee4j/jsp-api/issues/180
License:        (EPL-2.0 or GPLv2 with exceptions) and ASL 2.0

# there's no code changes in jsp-api between 2.3.6 and IMPL-2.3.6 releases,
# so we're using the more recent one
%global upstream_version IMPL-%{version}-RELEASE

URL:            https://github.com/eclipse-ee4j/jsp-api
Source0:        https://github.com/eclipse-ee4j/jsp-api/archive/%{upstream_version}/%{srcname}-%{upstream_version}.tar.gz

# build with support for JDTJavaCompiler (for eclipse) and AntJavaCompiler
Patch1:         0001-enable-support-for-JDTJavaCompiler-and-AntJavaCompil.patch
# fix compilation errors due to unimplemented interfaces in newer servlet APIs
Patch2:         0002-Port-to-latest-version-of-Servlet-API.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(jakarta.el:jakarta.el-api)
BuildRequires:  mvn(jakarta.servlet:jakarta.servlet-api)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.eclipse.jdt:core)
BuildRequires:  mvn(org.glassfish:javax.el)

# package renamed in fedora 33, remove in fedora 35
Provides:       glassfish-jsp = %{version}-%{release}
Obsoletes:      glassfish-jsp < 2.3.4-9
Source44: import.info

%description
Jakarta Server Pages provides a container-independent implementation of
the JSP API.


%package api
Group: Development/Java
Summary:        Jakarta Server Pages (JSP) API

# package renamed in fedora 33, remove in fedora 35
Provides:       glassfish-jsp-api = %{version}-%{release}
Obsoletes:      glassfish-jsp-api < 2.3.3-6

%description api
Jakarta Server Pages provides a container-independent implementation of
the JSP API. This package contains the API only.


%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}

# package renamed in fedora 33, remove in fedora 35
Provides:       glassfish-jsp-javadoc = %{version}-%{release}
Obsoletes:      glassfish-jsp-javadoc < 2.3.4-9
Provides:       glassfish-jsp-api-javadoc = %{version}-%{release}
Obsoletes:      glassfish-jsp-api-javadoc < 2.3.3-6
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{srcname}-%{upstream_version}
%patch1 -p1
%patch2 -p1


# remove unnecessary dependency on parent POM
%pom_remove_parent . api impl

# do not build specification documentation
%pom_disable_module spec

# do not install useless parent POM
%mvn_package org.eclipse.ee4j.jsp:jsp-parent __noinstall

# reset jsp-api version from 2.3.7-SNAPSHOT to 2.3.6 (no code changes)
sed -i "s/2\.3\.7-SNAPSHOT/2.3.6/" api/pom.xml

# ant and ecj should be optional OSGi requirements
%pom_xpath_inject "pom:dependency[pom:groupId='org.apache.ant']" "<optional>true</optional>" impl
%pom_xpath_inject "pom:dependency[pom:groupId='org.eclipse.jdt']" "<optional>true</optional>" impl

# this source file is excluded by maven-compiler-plugin configuration;
# remove it entirely to fix building javadocs
rm impl/src/main/java/org/apache/jasper/runtime/PerThreadTagHandlerPool.java

# add aliases for old maven artifact coordinates
%mvn_alias org.glassfish.web:jakarta.servlet.jsp \
    org.eclipse.jetty.orbit:org.apache.jasper.glassfish \
    org.glassfish.web:javax.servlet.jsp

%mvn_alias jakarta.servlet.jsp:jakarta.servlet.jsp-api \
    javax.servlet.jsp:javax.servlet.jsp-api \
    javax.servlet.jsp:jsp-api \
    javax.servlet:jsp-api

# add compat symlinks for the old classpaths
%mvn_file :jakarta.servlet.jsp     %{name}/jakarta.servlet.jsp     glassfish-jsp     javax.servlet.jsp
%mvn_file :jakarta.servlet.jsp-api %{name}/jakarta.servlet.jsp-api glassfish-jsp-api


%build
%mvn_build -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8


%install
%mvn_install


%files -f .mfiles-jakarta.servlet.jsp
%doc --no-dereference LICENSE.md NOTICE.md
%doc README.md

%files api -f .mfiles-jakarta.servlet.jsp-api
%doc --no-dereference LICENSE.md NOTICE.md

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.md NOTICE.md


%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 2.3.6-alt1_9jpp11
- update

* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 2.3.6-alt1_3jpp11
- new version

