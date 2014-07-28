Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global oname jamon

Name:       jamonapi
Version:    2.73
Release:    alt2_7jpp7
Summary:    A Java monitoring API
Group:      Development/Java
License:    BSD
URL:        http://jamon.sourceforge.net

# cvs -d:pserver:anonymous@jamonapi.cvs.sourceforge.net:/cvsroot/jamonapi login
# cvs -z3 -d:pserver:anonymous@jamonapi.cvs.sourceforge.net:/cvsroot/jamonapi co -P -r v2_73 jamonapi/src
# tar caf jamonapi-2.73.tar.gz jamonapi
Source0:    jamonapi-2.73.tar.gz
# This POM is completely Fedora-specific
Source1:    jamonapi-2.73.pom
Patch0:     jamonapi-buildxml.patch
Patch1:     jamonapi-jetty8.patch

BuildRequires:   jpackage-utils
BuildRequires:   ant
BuildRequires:   tomcat-lib
BuildRequires:   tomcat-servlet-3.0-api
BuildRequires:   tomcat-el-2.2-api
BuildRequires:   jetty
BuildRequires:   geronimo-interceptor
BuildRequires:   log4j
BuildRequires:   dos2unix
Requires:        jpackage-utils
Requires:        tomcat-lib
Requires:        tomcat-servlet-3.0-api
Requires:        tomcat-el-2.2-api
Requires:        jetty
Requires:        geronimo-interceptor
Requires:        log4j
BuildArch:       noarch
Source44: import.info

%description
A Java monitoring API

%package javadoc
Summary:         API documentation for %{name}
Group:           Development/Java
Requires:        jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}
%patch0 -p0
%patch1 -p1
mkdir dist
mkdir lib

%build
pushd src/ant
ant JAR
ant javadoc
popd

# Remove spurious executable permissions
find src/JAMonUsersGuide -type f | xargs chmod -x
find src/JAMonUsersGuide -regex '.*\(xml\|css\|js\)' -o -name package-list | xargs dos2unix

# Remove pregenerated javadoc files in the source tree
rm -rf src/JAMonUsersGuide/javadoc/
# Remove zip file which contains a proprietary binary
rm src/JAMonUsersGuide/JAMon_PB.zip

# There should be a shorter way to do an iconv task, but I do not know of one
pushd src/JAMonUsersGuide/presentation/jamon_files/
mv master04_stylesheet.css master04_stylesheet.css.iso8859-1
iconv -f ISO-8859-1 -t UTF-8 master04_stylesheet.css.iso8859-1 > master04_stylesheet.css
rm master04_stylesheet.css.iso8859-1
popd

%install
install -d -m 0755 ${RPM_BUILD_ROOT}/%{_javadir}
install -m 0644 dist/%{oname}-%{version}.jar ${RPM_BUILD_ROOT}/%{_javadir}/%{name}.jar
ln -s %{name}.jar ${RPM_BUILD_ROOT}/%{_javadir}/%{oname}.jar

install -d -m 0755 ${RPM_BUILD_ROOT}/%{_mavenpomdir}
install -m 0644 %{SOURCE1} ${RPM_BUILD_ROOT}/%{_mavenpomdir}/JPP-%{oname}.pom

install -d -m 0755 ${RPM_BUILD_ROOT}%{_javadocdir}
cp -rp src/doc/javadoc ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}

%add_maven_depmap JPP-%{oname}.pom %{oname}.jar

%files
%doc src/JAMonUsersGuide
%{_javadir}/%{oname}.jar
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{oname}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc src/JAMonUsersGuide/JAMonLicense.html
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.73-alt2_7jpp7
- new release

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.73-alt2_6jpp7
- use fc geronimo

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.73-alt1_6jpp7
- new version

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.7-alt3_2jpp6
- built with java 6 due to abstract getParentLogger

* Fri Jan 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.7-alt2_2jpp6
- converted from JPackage by jppimport script

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.7-alt2_1jpp5
- selected java5 compiler explicitly

* Sat Oct 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.7-alt1_1jpp5
- new jpp5.0 build

* Tue Jun 05 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_2jpp1.7
- converted from JPackage by jppimport script

