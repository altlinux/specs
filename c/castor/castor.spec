Name: castor
Version: 1.3.3
Summary: An open source data binding framework for Java
License: BSD and ASL 2.0
Url: http://castor.codehaus.org
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: castor = 1.3.3-2.fc23
Provides: mvn(org.codehaus.castor:castor-archetype-codegen-testcase) = 1.3.3
Provides: mvn(org.codehaus.castor:castor-archetype-codegen-testcase:pom:) = 1.3.3
Provides: mvn(org.codehaus.castor:castor-codegen) = 1.3.3
Provides: mvn(org.codehaus.castor:castor-codegen:pom:) = 1.3.3
Provides: mvn(org.codehaus.castor:castor-core) = 1.3.3
Provides: mvn(org.codehaus.castor:castor-core:pom:) = 1.3.3
Provides: mvn(org.codehaus.castor:castor-xml) = 1.3.3
Provides: mvn(org.codehaus.castor:castor-xml-diff) = 1.3.3
Provides: mvn(org.codehaus.castor:castor-xml-diff:pom:) = 1.3.3
Provides: mvn(org.codehaus.castor:castor-xml-schema) = 1.3.3
Provides: mvn(org.codehaus.castor:castor-xml-schema:pom:) = 1.3.3
Provides: mvn(org.codehaus.castor:castor-xml:pom:) = 1.3.3
Provides: mvn(org.codehaus.castor:castor:pom:) = 1.3.3
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(commons-cli:commons-cli)
Requires: mvn(commons-collections:commons-collections)
Requires: mvn(commons-lang:commons-lang)
Requires: mvn(commons-logging:commons-logging)
Requires: mvn(javax.inject:javax.inject)
Requires: mvn(javax.xml.stream:stax-api)
Requires: mvn(org.springframework:spring-context)
Requires: mvn(stax:stax)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: castor-1.3.3-2.fc23.cpio

%description
Castor is an open source data binding framework for Java. It's basically
the shortest path between Java objects, XML documents and SQL tables.
Castor provides Java to XML binding, Java to SQL persistence, and more.

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
* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2-alt1_6jpp7
- new release

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.2-alt1_3jpp7
- new version

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2.1-alt3_4jpp5
- fixed build

* Tue May 11 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2.1-alt2_4jpp5
- fixes for java6 support

* Tue Feb 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2.1-alt1_4jpp5
- new version

* Tue Nov 25 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.9.1-alt1_2jpp5
- fixed build

* Sat Oct 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.9.1-alt1_2jpp1.7
- converted from JPackage by jppimport script

