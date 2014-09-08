# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
%global artifactId javax.servlet.jsp
%global jspspec 2.2


Name:       glassfish-jsp
Version:    2.2.6
Release:    alt2_11jpp7
Summary:    Glassfish J2EE JSP API implementation

Group:      Development/Java
License:    (CDDL or GPLv2 with exceptions) and ASL 2.0
URL:        http://glassfish.org
Source0:    %{artifactId}-%{version}.tar.xz
# no source releases, but this will generate tarball for you from an
# SVN tag
Source1:    generate_tarball.sh
Source2:    http://www.apache.org/licenses/LICENSE-2.0.txt
Source3:    https://svn.java.net/svn/glassfish~svn/tags/legal-1.1/src/main/resources/META-INF/LICENSE.txt

Patch0:     %{name}-build-eclipse-compilers.patch

BuildArch:  noarch

BuildRequires:  maven-local
BuildRequires:  glassfish-jsp-api
BuildRequires:  mvn(javax.el:javax.el-api)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(net.java:jvnet-parent)
BuildRequires:  mvn(org.eclipse.jdt:core)

Provides:   jsp = %{jspspec}
Provides:   jsp%{jspspec}

Provides:   javax.servlet.jsp
# make sure the symlinks will be correct
Requires:  glassfish-jsp-api
Source44: import.info

%description
This project provides a container independent implementation of JSP
2.2. The main goals are:
  * Improves current implementation: bug fixes and performance
    improvements
  * Provides API for use by other tools, such as Netbeans
  * Provides a sandbox for new JSP features; provides a reference
    implementation of next JSP spec.


%package javadoc
Summary:    API documentation for %{name}
Group:      Development/Java
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{artifactId}-%{version}
%patch0
cp -p %{SOURCE2} LICENSE
cp -p %{SOURCE3} cddllicense.txt

%mvn_alias : "javax.servlet:jsp-api" "org.eclipse.jetty.orbit:org.apache.jasper.glassfish"

# compat symlink
%mvn_file : %{name}/javax.servlet.jsp %{name}

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
if [ -f %{_javadir}/%{name}-api*.jar ];then
   cp %{_javadir}/glassfish-jsp-api*.jar .
else
   cp %{_javadir}/glassfish-jsp-api/*.jar .
fi
xmvn-subst .
popd

%files -f .mfiles
%dir %{_javadir}/%{name}
%{_javadir}/javax.servlet.jsp
%doc LICENSE cddllicense.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE cddllicense.txt


%changelog
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

