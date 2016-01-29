Name: jackson
Version: 1.9.11
Summary: Jackson Java JSON-processor
License: ASL 2.0 or LGPLv2
Url: http://jackson.codehaus.org
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jackson = 1.9.11-6.fc23
Provides: mvn(org.codehaus.jackson:jackson-core-asl) = 1.9.11
Provides: mvn(org.codehaus.jackson:jackson-core-asl:pom:) = 1.9.11
Provides: mvn(org.codehaus.jackson:jackson-jaxrs) = 1.9.11
Provides: mvn(org.codehaus.jackson:jackson-jaxrs:pom:) = 1.9.11
Provides: mvn(org.codehaus.jackson:jackson-mapper-asl) = 1.9.11
Provides: mvn(org.codehaus.jackson:jackson-mapper-asl:pom:) = 1.9.11
Provides: mvn(org.codehaus.jackson:jackson-mrbean) = 1.9.11
Provides: mvn(org.codehaus.jackson:jackson-mrbean:pom:) = 1.9.11
Provides: mvn(org.codehaus.jackson:jackson-smile) = 1.9.11
Provides: mvn(org.codehaus.jackson:jackson-smile:pom:) = 1.9.11
Provides: mvn(org.codehaus.jackson:jackson-xc) = 1.9.11
Provides: mvn(org.codehaus.jackson:jackson-xc:pom:) = 1.9.11
Requires: java-headless
Requires: java-headless
Requires: joda-time
Requires: jpackage-utils
Requires: jpackage-utils
Requires: jsr-311
Requires: objectweb-asm3
Requires: stax2-api

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jackson-1.9.11-6.fc23.cpio

%description
JSON processor (JSON parser + JSON generator) written in Java. Beyond basic
JSON reading/writing (parsing, generating), it also offers full node-based Tree
Model, as well as full OJM (Object/Json Mapper) data binding functionality.

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
* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 1.9.11-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.9.4-alt2_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.9.4-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.9.4-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.9.4-alt1_5jpp7
- new version

