Provides: /etc/java/modello.conf
Name: modello
Version: 1.8.3
Summary: Modello Data Model toolkit
License: ASL 2.0 and BSD and MIT
Url: http://modello.codehaus.org/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: modello = 0:1.8.3-2.fc23
Provides: modello-maven-plugin = 0:1.8.3-2.fc23
Provides: mvn(org.codehaus.modello:modello-core) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-core:pom:) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-maven-plugin) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-maven-plugin:pom:) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-plugin-converters) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-plugin-converters:pom:) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-plugin-dom4j) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-plugin-dom4j:pom:) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-plugin-jackson) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-plugin-jackson:pom:) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-plugin-java) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-plugin-java:pom:) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-plugin-jdom) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-plugin-jdom:pom:) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-plugin-jsonschema) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-plugin-jsonschema:pom:) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-plugin-sax) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-plugin-sax:pom:) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-plugin-snakeyaml) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-plugin-snakeyaml:pom:) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-plugin-stax) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-plugin-stax:pom:) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-plugin-xdoc) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-plugin-xdoc:pom:) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-plugin-xml) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-plugin-xml:pom:) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-plugin-xpp3) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-plugin-xpp3:pom:) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-plugin-xsd) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-plugin-xsd:pom:) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-plugins:pom:) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-test) = 1.8.3
Provides: mvn(org.codehaus.modello:modello-test:pom:) = 1.8.3
Provides: mvn(org.codehaus.modello:modello:pom:) = 1.8.3
Requires: /bin/bash
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.fasterxml.jackson.core:jackson-annotations)
Requires: mvn(com.fasterxml.jackson.core:jackson-core)
Requires: mvn(com.fasterxml.jackson.core:jackson-databind)
Requires: mvn(junit:junit)
Requires: mvn(org.apache.maven:maven-core)
Requires: mvn(org.apache.maven:maven-model)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.codehaus.plexus:plexus-compiler-api)
Requires: mvn(org.codehaus.plexus:plexus-compiler-javac)
Requires: mvn(org.codehaus.plexus:plexus-container-default)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: mvn(org.sonatype.plexus:plexus-build-api)
Requires: mvn(org.yaml:snakeyaml)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: modello-1.8.3-2.fc23.cpio

%description
Modello is a Data Model toolkit in use by the Apache Maven Project.

Modello is a framework for code generation from a simple model.
Modello generates code from a simple model format based on a plugin
architecture, various types of code and descriptors can be generated
from the single model, including Java POJOs, XML
marshallers/unmarshallers, XSD and documentation.

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none
%prep
cpio -idmu --quiet --no-absolute-filenames < %{SOURCE0}

%build
cpio --list < %{SOURCE0} | sed -e 's,^\.,,' > %name-list

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done


%files -f %name-list

%changelog
* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_2jpp7
- new version

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_0jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt5_3jpp7
- rebuild with maven-local

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt4_3jpp7
- fixed build

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt3_3jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 10 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_3jpp7
- new version

* Fri Apr 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_1jpp6
- fixed build with new plexus-containers

* Fri Apr 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_1jpp6
- fixed build with maven3

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_1jpp6
- new jpp release

* Thu Sep 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.2.a15.5jpp6
- reverted to a15

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.a17.1jpp5
- fixes for java6 support

* Tue Feb 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.a17.1jpp5
- rebuild with maven

* Thu Jan 29 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a17.1jpp5
- new version a17

* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a15.1jpp5
- fixed build w/java5

* Fri Dec 21 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a15.1jpp1.7
- new version

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a8.6jpp1.7
- build with maven2

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a8.6jpp1.7
- converted from JPackage by jppimport script

