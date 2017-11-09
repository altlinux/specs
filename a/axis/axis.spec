Group: Development/Other
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
Name:          axis
Version:       1.4
Release:       alt4_35jpp8
Epoch:         0
Summary:       SOAP implementation in Java
License:       ASL 2.0
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
Source4: axis-ant-MANIFEST.MF
Patch0:        %{name}-java16.patch
Patch1:        %{name}-manifest.patch
# CVE-2012-5784: Does not verify that the server hostname matches X.509 certificate name
# https://issues.apache.org/jira/secure/attachment/12560257/CVE-2012-5784-2.patch
Patch3:        %{name}-CVE-2012-5784.patch
# Patch to use newer xml-commons-apis
Patch4:        axis-xml-commons-apis.patch
BuildRequires: java-devel
BuildRequires: javapackages-local
BuildRequires: ant
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
BuildRequires: log4j12
BuildRequires: javax.wsdl
BuildRequires: xalan-j2
BuildRequires: xmlbeans
BuildRequires: xml-security
BuildRequires: zip

Requires:      apache-commons-discovery
Requires:      apache-commons-logging
Requires:      jakarta-commons-httpclient >= 1:3.0
Requires:      log4j12
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
find . -name "*.jar" -delete
find . -name "*.zip" -delete
find . -name "*.class" -delete

%patch0 -b .orig
%patch1 -b .orig

cp %{SOURCE1} %{SOURCE2} %{SOURCE3} .

%patch3 -p1 -b .orig
%patch4 -p1 -b .orig

# Disable doclinting for java 8
sed -i '/doctitle/a additionalparam="-Xdoclint:none"' build.xml

# Use correct encoding
sed -i '/<javac/a encoding="iso-8859-1"' build.xml
sed -i '/<javadoc/a encoding="iso-8859-1"' build.xml

# Use JRE version of xml-apis
sed -i -e '/javax\.xml\.parsers\./d' axis.properties xmls/properties.xml xmls/targets.xml

%build
pushd lib
build-jar-repository -s -p . \
  bea-stax-api bsf castor commons-discovery commons-httpclient commons-logging commons-net httpunit \
  log4j-1 oro xalan-j2 xml-security xmlbeans/xbean wsdl4j javamail/mail glassfish-servlet-api
popd

ant \
    -Dant.build.javac.source=1.4 \
    -Dtest.functional.fail=no \
    -Dcommons-discovery.jar=$(build-classpath commons-discovery) \
    -Dcommons-logging.jar=$(build-classpath commons-logging) \
    -Dlog4j-core.jar=$(build-classpath log4j-1) \
    -Dwsdl4j.jar=$(build-classpath wsdl4j) \
    clean war javadocs # junit

# inject axis-ant OSGi manifest
mkdir -p META-INF
cp -p %{SOURCE4} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip build/lib/%{name}-ant.jar META-INF/MANIFEST.MF

%install
for i in axis axis-ant axis-jaxrpc axis-saaj axis-schema ; do
  if [ -f "build/lib/${i}.jar" ] ; then
    %mvn_artifact "org.apache.axis:$i:%{version}" build/lib/${i}.jar
  else
    %mvn_artifact "org.apache.axis:$i:%{version}" build/lib/${i#axis-}.jar
  fi
  %mvn_alias "org.apache.axis:$i" "axis:$i"
done
%mvn_file ":axis" axis/axis javax.xml.rpc/axis
%mvn_file ":axis-jaxrpc" axis/jaxrpc javax.xml.rpc/jaxrpc
%mvn_file ":axis-saaj" axis/saaj
%mvn_install -J build/javadocs

# Install webapp
install -d -m 755 %{buildroot}%{_datadir}/axis/webapps
install -m 644 build/axis.war \
    %{buildroot}%{_datadir}/axis/webapps

# J2EE API dir
build-jar-repository -s -p %{buildroot}%{_javadir}/javax.xml.rpc/ javax.wsdl \
              javax.mail apache-commons-logging apache-commons-discovery \
              jakarta-commons-httpclient log4j-1


%files -f .mfiles
%doc LICENSE
%doc README release-notes.html changelog.html
%{_javadir}/javax.xml.rpc
%{_datadir}/%{name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%files manual
%doc LICENSE
%doc --no-dereference docs/*

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt4_35jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt4_32jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt4_29jpp8
- new fc release

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
