Name: qpid-proton-java
Version: 0.10
Summary: Java libraries for Qpid Proton
License: ASL 2.0
Url: http://qpid.apache.org/proton/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.apache.qpid:proton-api) = 0.10
Provides: mvn(org.apache.qpid:proton-api:pom:) = 0.10
Provides: mvn(org.apache.qpid:proton-hawtdispatch) = 0.10
Provides: mvn(org.apache.qpid:proton-hawtdispatch:pom:) = 0.10
Provides: mvn(org.apache.qpid:proton-j) = 0.10
Provides: mvn(org.apache.qpid:proton-j-impl) = 0.10
Provides: mvn(org.apache.qpid:proton-j-impl:pom:) = 0.10
Provides: mvn(org.apache.qpid:proton-j-messenger-example) = 0.10
Provides: mvn(org.apache.qpid:proton-j-messenger-example:pom:) = 0.10
Provides: mvn(org.apache.qpid:proton-j-reactor-examples) = 0.10
Provides: mvn(org.apache.qpid:proton-j-reactor-examples:pom:) = 0.10
Provides: mvn(org.apache.qpid:proton-j:pom:) = 0.10
Provides: mvn(org.apache.qpid:proton-jms) = 0.10
Provides: mvn(org.apache.qpid:proton-jms:pom:) = 0.10
Provides: mvn(org.apache.qpid:proton-project:pom:) = 0.10
Provides: mvn(org.apache.qpid:proton-tests) = 0.10
Provides: mvn(org.apache.qpid:proton-tests:pom:) = 0.10
Provides: qpid-proton-java = 0.10-1.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.bouncycastle:bcpkix-jdk15on)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: qpid-proton-java-0.10-1.fc23.cpio

%description
Java language bindings for the Qpid Proton messaging framework.

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
* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

