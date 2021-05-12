Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global artifactId javax.servlet.jsp
%global jspspec 2.3

Name:       glassfish-jsp
Version:    2.3.4
Release:    alt1_3jpp8
Summary:    Glassfish J2EE JSP API implementation
# Classes in package "org.apache.jasper" are Apache licensed
License:    (CDDL-1.1 or GPLv2 with exceptions) and ASL 2.0
URL:        https://github.com/javaee/javaee-jsp-api

Source0:    https://github.com/javaee/javaee-jsp-api/archive/%{artifactId}-%{version}.tar.gz
Source1:    http://www.apache.org/licenses/LICENSE-2.0.txt

# JSP can do byte-code compilation at runtime, if we enable the Eclipse compiler support
Patch0:     %{name}-build-eclipse-compilers.patch
# Fix compilation errors due to unimplemented interfaces in newer servlet APIs
Patch1:     %{name}-port-to-servlet-3.1.patch

BuildArch:  noarch

BuildRequires:  maven-local
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(javax.servlet.jsp:javax.servlet.jsp-api)
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.eclipse.jdt:core)
BuildRequires:  mvn(org.glassfish:javax.el)

Provides:   jsp = %{jspspec}
Provides:   jsp%{jspspec}
Provides:   javax.servlet.jsp
Source44: import.info

%description
This project provides a container independent implementation of JSP
specification %{jspspec}.

%package javadoc
Group: Development/Java
Summary: API documentation for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n javaee-jsp-api-%{artifactId}-%{version}

cp -p %{SOURCE1} LICENSE-ASL-2.0.txt

pushd impl
%patch0 -p1
%patch1 -p1

%pom_add_dep org.eclipse.jdt:core::provided

%mvn_alias : "org.eclipse.jetty.orbit:org.apache.jasper.glassfish"

# compat symlink
%mvn_file : %{name}/javax.servlet.jsp %{name}

# Plugins not needed for RPM builds:
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-source-plugin
popd

%build
pushd impl
%mvn_build
popd

%install
pushd impl
%mvn_install
popd

# Install j2ee api symlinks
install -d -m 755 %{buildroot}%{_javadir}/javax.servlet.jsp/
pushd %{buildroot}%{_javadir}/javax.servlet.jsp/
for jar in ../%{name}/*jar; do
    ln -sf $jar .
done
# Copy jsp-api so that deps can be included as well
build-jar-repository -p . glassfish-jsp-api
xmvn-subst -R %{buildroot} -s .
popd

%files -f impl/.mfiles
%{_javadir}/javax.servlet.jsp
%doc --no-dereference LICENSE-ASL-2.0.txt LICENSE

%files javadoc -f impl/.mfiles-javadoc
%doc --no-dereference LICENSE-ASL-2.0.txt LICENSE

%changelog
* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 2.3.4-alt1_3jpp8
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 2.3.3-alt1_0.14.b02jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 2.3.3-alt1_0.13.b02jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.3.3-alt1_0.12.b02jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.3-alt1_0.11.b02jpp8
- new fc release

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.3-alt1_0.10.b02jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.3-alt1_0.7.b02jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.3-alt1_0.5.b02jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.3-alt1_0.4.b02jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.3-alt1_0.3.b02jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.6-alt2_11jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.6-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.6-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.6-alt1_2jpp7
- new release

* Mon Aug 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.5-alt1_1jpp7
- full version

