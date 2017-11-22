Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global artifactId javax.servlet.jsp
%global jspspec 2.3
%global reltag b02

Name:       glassfish-jsp
Version:    2.3.3
Release:    alt1_0.11.b02jpp8
Summary:    Glassfish J2EE JSP API implementation
License:    (CDDL-1.1 or GPLv2 with exceptions) and ASL 2.0
URL:        http://glassfish.org
BuildArch:  noarch

Source0:    %{artifactId}-%{version}-%{reltag}.tar.xz
# no source releases, but this will generate tarball for you from an
# SVN tag
Source1:    generate_tarball.sh
Source2:    http://www.apache.org/licenses/LICENSE-2.0.txt
Source3:    https://javaee.github.io/glassfish/LICENSE.html

Patch0:     %{name}-build-eclipse-compilers.patch
Patch1:     %{name}-port-to-servlet-3.1.patch

BuildRequires:  maven-local
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(javax.servlet.jsp:javax.servlet.jsp-api)
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.eclipse.jdt:core)
BuildRequires:  mvn(org.glassfish:javax.el)

Provides:   jsp = %{jspspec}
Provides:   jsp%{jspspec}

Provides:   javax.servlet.jsp
# make sure the symlinks will be correct
Requires:  glassfish-jsp-api
Source44: import.info

%description
This project provides a container independent implementation of JSP
2.3. The main goals are:
  * Improves current implementation: bug fixes and performance
    improvements
  * Provides API for use by other tools, such as Netbeans
  * Provides a sandbox for new JSP features; provides a reference
    implementation of next JSP spec.


%package javadoc
Group: Development/Java
Summary:    API documentation for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{artifactId}-%{version}-%{reltag}
%patch0 -p1
%patch1 -p1

%pom_add_dep org.eclipse.jdt:core::provided

cp -p %{SOURCE2} LICENSE-ASL-2.0.txt
cp -p %{SOURCE3} LICENSE-CDDL+GPLv2.html

%mvn_alias : "org.eclipse.jetty.orbit:org.apache.jasper.glassfish"

# compat symlink
%mvn_file : %{name}/javax.servlet.jsp %{name}

# javadoc generation fails due to strict doclint in JDK 8
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build

%install
%mvn_install

# install j2ee api symlinks
install -d -m 755 %{buildroot}%{_javadir}/javax.servlet.jsp/
pushd %{buildroot}%{_javadir}/javax.servlet.jsp/
for jar in ../%{name}/*jar; do
    ln -sf $jar .
done
# copy jsp-api so that build-classpath will include dep as well
build-jar-repository -p . glassfish-jsp-api
xmvn-subst -R %{buildroot} -s .
popd

%files -f .mfiles
%{_javadir}/javax.servlet.jsp
%doc LICENSE-ASL-2.0.txt LICENSE-CDDL+GPLv2.html

%files javadoc -f .mfiles-javadoc
%doc LICENSE-ASL-2.0.txt LICENSE-CDDL+GPLv2.html


%changelog
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

