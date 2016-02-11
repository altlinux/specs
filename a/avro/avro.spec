Name: avro
Version: 1.7.5
Summary: Data serialization system
License: ASL 2.0
Url: http://avro.apache.org
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: avro = 1.7.5-12.fc23
Provides: mvn(org.apache.avro:avro) = 1.7.5
Provides: mvn(org.apache.avro:avro:pom:) = 1.7.5
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.thoughtworks.paranamer:paranamer)
Requires: mvn(org.apache.commons:commons-compress)
Requires: mvn(org.codehaus.jackson:jackson-core-asl)
Requires: mvn(org.codehaus.jackson:jackson-mapper-asl)
Requires: mvn(org.slf4j:slf4j-api)
Requires: mvn(org.xerial.snappy:snappy-java)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: avro-1.7.5-12.fc23.cpio

%description
Apache Avro is a data serialization system.

Avro provides:

* Rich data structures.
* A compact, fast, binary data format.
* A container file, to store persistent data.
* Remote procedure call (RPC).
* Simple integration with dynamic languages. Code generation is not required
  to read or write data files nor to use or implement RPC protocols. Code
  generation as an optional optimization, only worth implementing for
  statically typed languages.

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
* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1.7.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt3_6jpp7
- new release

* Thu Jul 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt3_4jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_4jpp7
- new version

