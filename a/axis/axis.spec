# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          axis
Version:       1.4
Release:       alt4_28jpp8
Epoch:         0
Summary:       SOAP implementation in Java
License:       ASL 2.0
Group:         Development/Other
URL:           http://ws.apache.org/axis/
Source0:       axis-1.4-src.tar.gz
# svn export http://svn.apache.org/repos/asf/webservices/axis/branches/AXIS_1_4_FINAL/
# Build only
# cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/tools export -r v1_1_0 org.eclipse.orbit/javax.xml.rpc/META-INF/MANIFEST.MF
# mv org.eclipse.orbit/javax.xml.rpc/META-INF/MANIFEST.MF xmlrpc-MANIFEST.MF
Source1: xmlrpc-MANIFEST.MF
# cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/tools export -r v1_4_0 org.eclipse.orbit/org.apache.axis/META-INF/MANIFEST.MF
# mv org.eclipse.orbit/org.apache.axis/META-INF/MANIFEST.MF axis-MANIFEST.MF
Source2: axis-MANIFEST.MF
# cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/tools export -r v1_3_0 org.eclipse.orbit/javax.xml.soap/META-INF/MANIFEST.MF
# mv org.eclipse.orbit/javax.xml.soap/META-INF/MANIFEST.MF saaj-MANIFEST.MF
Source3: saaj-MANIFEST.MF
Source4: http://repo1.maven.org/maven2/org/apache/axis/axis/1.4/axis-1.4.pom
Source5: http://repo1.maven.org/maven2/org/apache/axis/axis-ant/1.4/axis-ant-1.4.pom
Source6: http://repo1.maven.org/maven2/org/apache/axis/axis-jaxrpc/1.4/axis-jaxrpc-1.4.pom
Source7: http://repo1.maven.org/maven2/org/apache/axis/axis-saaj/1.4/axis-saaj-1.4.pom
# This POM is not present upstream, so a placeholder was created
Source8: axis-schema-1.4.pom
Source9: axis-ant-MANIFEST.MF
Patch0:        %{name}-java16.patch
Patch1:        %{name}-manifest.patch
Patch2:        axis-1.4-wsdl-pom.patch
# CVE-2012-5784: Does not verify that the server hostname matches X.509 certificate name
# https://issues.apache.org/jira/secure/attachment/12560257/CVE-2012-5784-2.patch
Patch3:        %{name}-CVE-2012-5784.patch
# Patch to use newer xml-commons-apis
Patch4:        axis-xml-commons-apis.patch
BuildRequires: javapackages-tools rpm-build-java
BuildRequires: ant >= 0:1.6
BuildRequires: ant-junit
BuildRequires: httpunit
BuildRequires: junit
BuildRequires: xmlunit
# Main requires
BuildRequires: bea-stax-api
BuildRequires: bsf
BuildRequires: castor
BuildRequires: javax.mail
BuildRequires: glassfish-servlet-api
BuildRequires: apache-commons-discovery
BuildRequires: jakarta-commons-httpclient >= 1:3.0
BuildRequires: apache-commons-logging
BuildRequires: apache-commons-net
BuildRequires: jakarta-oro
BuildRequires: regexp
BuildRequires: log4j
BuildRequires: javax.wsdl
BuildRequires: xalan-j2
BuildRequires: xerces-j2
BuildRequires: xml-commons-apis
BuildRequires: xmlbeans
BuildRequires: xml-security
BuildRequires: zip
# optional requires
#BuildRequires: jimi

Requires: javapackages-tools rpm-build-java
Requires:      apache-commons-discovery
Requires:      apache-commons-logging
Requires:      jakarta-commons-httpclient >= 1:3.0
Requires:      log4j
Requires:      javax.mail
Requires:      javax.wsdl

BuildArch:     noarch

Provides:      javax.xml.rpc
Source44: import.info

%description
Apache AXIS is an implementation of the SOAP ("Simple Object Access Protocol")
submission to W3C.

From the draft W3C specification:

SOAP is a lightweight protocol for exchange of information in a decentralized,
distributed environment. It is an XML based protocol that consists of three
parts: an envelope that defines a framework for describing what is in a message
and how to process it, a set of encoding rules for expressing instances of
application-defined datatypes, and a convention for representing remote
procedure calls and responses.

This project is a follow-on to the Apache SOAP project.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package manual
Group: Development/Java
Summary:        Manual for %{name}
BuildArch: noarch

%description manual
Documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}-src
ln -s %{_javadocdir}/%{name} docs/apiDocs

# Remove provided binaries
#find . -name "*.jar" -exec rm -f {} \;
for f in $(find . -name "*.jar"); do mv $f $f.no; done
#find . -name "*.zip" -exec rm -f {} \;
for f in $(find . -name "*.zip"); do mv $f $f.no; done
#find . -name "*.class" -exec rm -f {} \;
for f in $(find . -name "*.class"); do mv $f $f.no; done

%patch0 -b .orig
%patch1 -b .orig

cp %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .

# %patch2 -b .orig
%patch3 -p1 -b .orig
%patch4 -p1 -b .orig

%build
pushd lib
ln -sf $(build-classpath bea-stax-api) .
ln -sf $(build-classpath bsf) .
ln -sf $(build-classpath castor) .
ln -sf $(build-classpath commons-discovery) .
ln -sf $(build-classpath commons-httpclient) .
ln -sf $(build-classpath commons-logging) .
ln -sf $(build-classpath commons-net) .
ln -sf $(build-classpath httpunit) .
ln -sf $(build-classpath log4j) .
ln -sf $(build-classpath oro) .
ln -sf $(build-classpath xalan-j2) .
ln -sf $(build-classpath xml-security) .
ln -sf $(build-classpath xmlbeans/xbean) .
ln -sf $(build-classpath wsdl4j) .
pushd endorsed
ln -sf $(build-classpath xerces-j2) .
ln -sf $(build-classpath xml-commons-apis) .
popd
ln -sf $(build-classpath javamail/mail) .
popd

ant \
    -Dant.build.javac.source=1.4 \
    -Dtest.functional.fail=no \
    -Dcommons-discovery.jar=$(build-classpath commons-discovery) \
    -Dcommons-httpclient.jar=$(build-classpath commons-httpclient) \
    -Dcommons-logging.jar=$(build-classpath commons-logging) \
    -Dlog4j-core.jar=$(build-classpath log4j) \
    -Dwsdl4j.jar=$(build-classpath wsdl4j) \
    -Dregexp.jar=$(build-classpath regexp) \
    -Dxmlunit.jar=$(build-classpath xmlunit) \
    -Dmailapi.jar=$(build-classpath javamail/mail) \
    -Dservlet.jar=$(build-classpath glassfish-servlet-api) \
    -Dbsf.jar=$(build-classpath bsf) \
    -Dcastor.jar=$(build-classpath castor) \
    -Dcommons-net.jar=$(build-classpath commons-net) \
    -Dsecurity.jar=$(build-classpath xml-security) \
    -Dxmlbeans.jar=$(build-classpath xmlbeans) \
    -Dhttpunit.jar=$(build-classpath httpunit) \
    clean war javadocs # junit

#    -Djimi.jar=$(build-classpath jimi) \

# inject axis-ant OSGi manifest
mkdir -p META-INF
cp -p %{SOURCE9} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u build/lib/%{name}-ant.jar META-INF/MANIFEST.MF


%install
### Jar files

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

pushd build/lib
# install axis-schema.jar when xmlbeans is available
   install -m 644 axis.jar axis-ant.jar saaj.jar jaxrpc.jar axis-schema.jar \
           $RPM_BUILD_ROOT%{_javadir}/%{name}
popd

### Javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/webapps
install -m 644 build/axis.war \
    $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/webapps

# POMs
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -m 644 axis-1.4.pom $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-axis.pom
%add_maven_depmap JPP.%{name}-axis.pom %{name}/axis.jar -a "axis:axis"
install -m 644 %{S:5} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-axis-ant.pom
%add_maven_depmap JPP.%{name}-axis-ant.pom %{name}/axis-ant.jar -a "axis:axis-ant"
install -m 644 %{S:6} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-jaxrpc.pom
%add_maven_depmap JPP.%{name}-jaxrpc.pom %{name}/jaxrpc.jar -a "axis:axis-jaxrpc"
install -m 644 %{S:7} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-saaj.pom
%add_maven_depmap JPP.%{name}-saaj.pom %{name}/saaj.jar -a "axis:axis-saaj"
install -m 644 %{S:8} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-axis-schema.pom
%add_maven_depmap JPP.%{name}-axis-schema.pom %{name}/axis-schema.jar -a "axis:axis-schema"

# J2EE API dir
install -d -m 755 %{buildroot}%{_javadir}/javax.xml.rpc/
ln -sf ../%{name}/jaxrpc.jar %{buildroot}%{_javadir}/javax.xml.rpc/
ln -sf ../%{name}/%{name}.jar %{buildroot}%{_javadir}/javax.xml.rpc/
build-jar-repository %{buildroot}%{_javadir}/javax.xml.rpc/ javax.wsdl \
              javax.mail apache-commons-logging apache-commons-discovery \
              jakarta-commons-httpclient log4j


%files -f .mfiles
%doc LICENSE README release-notes.html changelog.html
%dir %{_javadir}/%{name}
%{_javadir}/javax.xml.rpc
%{_datadir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}

%files manual
%doc --no-dereference docs/*

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt4_28jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt4_27jpp8
- added osgi provides

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_27jpp8
- new version

* Wed Jul 09 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_20jpp7
- converted from JPackage by jppimport script

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_6jpp6
- new jpp relase

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_5jpp6
- new jpp release

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_4jpp5
- selected java5 compiler explicitly

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_4jpp5
- new jpp release

* Mon Feb 23 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_2jpp5
- fixed build

* Tue Oct 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_2jpp1.7
- removed jaf conflict

* Wed Aug 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_2jpp1.7
- updated to new jpackage version

* Mon Jul 04 2005 Vladimir Lettiev <crux@altlinux.ru> 1.2.1-alt1
- 1.2.1
- changed dependency: jakarta-oro -> jakarta-regexp
- changed rpmgroup of packages with documentation

* Sun Mar 27 2005 Vladimir Lettiev <crux@altlinux.ru> 1.2-alt0.2
- rpm-build-java macroces
- version from cvs 20050327

* Tue Sep 21 2004 Vladimir Lettiev <crux@altlinux.ru> 1.2-alt0.1.beta3
- 1.2beta3
- Rebuild for ALT Linux Sisyphus
- spec cleanup

* Fri Aug 20 2004 Ralph Apel <r.apel at r-apel.de>  0:1.1-3jpp
- Build with ant-1.6.2

* Thu Jun 26 2003 Nicolas Mailhot <Nicolas.Mailhot at laPoste.net>  0:1.1-2jpp
- fix javadoc versionning

* Thu Jun 26 2003 Nicolas Mailhot <Nicolas.Mailhot at laPoste.net>  0:1.1-1jpp
- Initial packaging
- no xml security for now since xml-security is not packaged yet
- functional tests not executed yet - seems they need some setup and do not
  run out of the box
- no webapp right now - file layout is too messy if hidden into a war file
  since jpp installs webapps expanded, this matters
