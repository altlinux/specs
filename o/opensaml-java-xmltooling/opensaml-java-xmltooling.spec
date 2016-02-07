Name: opensaml-java-xmltooling
Version: 1.3.4
Summary: Java XMLTooling library
License: ASL 2.0 and W3C
Url: http://www.opensaml.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.opensaml:xmltooling) = 1.3.4
Provides: mvn(org.opensaml:xmltooling:pom:) = 1.3.4
Provides: opensaml-java-xmltooling = 1.3.4-9.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(ca.juliusdavies:not-yet-commons-ssl)
Requires: mvn(commons-codec:commons-codec)
Requires: mvn(joda-time:joda-time)
Requires: mvn(net.jcip:jcip-annotations)
Requires: mvn(org.apache.santuario:xmlsec)
Requires: mvn(org.bouncycastle:bcprov-jdk16)
Requires: mvn(org.slf4j:jcl-over-slf4j)
Requires: mvn(org.slf4j:jul-to-slf4j)
Requires: mvn(org.slf4j:log4j-over-slf4j)
Requires: mvn(org.slf4j:slf4j-api)
Requires: mvn(xalan:xalan)
Requires: mvn(xerces:xercesImpl)
Requires: mvn(xml-resolver:xml-resolver)

BuildArch: noarch
Group: Development/Java
Release: alt3jpp
Source: opensaml-java-xmltooling-1.3.4-9.fc23.cpio

%description
Java XMLTooling is a low-level library that may be used to construct libraries
that allow developers to work with XML in a Java beans manner.

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
* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.4-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.4-alt2_7jpp7
- new release

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.4-alt2_5jpp7
- added BR: for xmvn

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.4-alt1_5jpp7
- new release

* Tue Feb 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.4-alt1_3jpp7
- fc update

