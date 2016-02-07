Name: owasp-esapi-java
Version: 2.1.0
Summary: OWASP Enterprise Security API
License: BSD
Url: http://code.google.com/p/owasp-esapi-java/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.owasp.esapi:esapi) = 2.1.0
Provides: mvn(org.owasp.esapi:esapi:pom:) = 2.1.0
Provides: owasp-esapi-java = 2.1.0-2.fc22
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(commons-beanutils:commons-beanutils-core)
Requires: mvn(commons-collections:commons-collections)
Requires: mvn(commons-configuration:commons-configuration)
Requires: mvn(commons-fileupload:commons-fileupload)
Requires: mvn(log4j:log4j:12)
Requires: mvn(org.apache.tomcat:tomcat-jsp-api)
Requires: mvn(org.beanshell:bsh)
Requires: mvn(xom:xom)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: owasp-esapi-java-2.1.0-2.fc22.cpio

%description
OWASP ESAPI (The OWASP Enterprise Security API) is a free, open source,
web application security control library that makes it easier for programmers
to write lower-risk applications. The ESAPI for Java library is designed to
make it easier for programmers to retrofit security into existing applications.
ESAPI for Java also serves as a solid foundation for new development.

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
* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt3_9jpp7
- new release

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt3_7jpp7
- added BR: for xmvn

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_7jpp7
- new release

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_3jpp7
- fixed build

* Tue Feb 26 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_3jpp7
- fc update

