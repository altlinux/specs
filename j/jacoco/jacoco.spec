Name: jacoco
Version: 0.7.5
Summary: Java Code Coverage for Eclipse
License: EPL
Url: http://www.eclemma.org/jacoco/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jacoco = 0.7.5-2.fc23
Provides: mvn(org.jacoco:org.jacoco.agent) = 0.7.5.201505241946
Provides: mvn(org.jacoco:org.jacoco.agent.rt) = 0.7.5.201505241946
Provides: mvn(org.jacoco:org.jacoco.agent.rt:pom:) = 0.7.5.201505241946
Provides: mvn(org.jacoco:org.jacoco.agent::runtime:) = 0.7.5.201505241946
Provides: mvn(org.jacoco:org.jacoco.agent:pom:) = 0.7.5.201505241946
Provides: mvn(org.jacoco:org.jacoco.ant) = 0.7.5.201505241946
Provides: mvn(org.jacoco:org.jacoco.ant:pom:) = 0.7.5.201505241946
Provides: mvn(org.jacoco:org.jacoco.build:pom:) = 0.7.5.201505241946
Provides: mvn(org.jacoco:org.jacoco.core) = 0.7.5.201505241946
Provides: mvn(org.jacoco:org.jacoco.core:pom:) = 0.7.5.201505241946
Provides: mvn(org.jacoco:org.jacoco.report) = 0.7.5.201505241946
Provides: mvn(org.jacoco:org.jacoco.report:pom:) = 0.7.5.201505241946
Provides: mvn(org.jacoco:root:pom:) = 0.7.5.201505241946
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.ow2.asm:asm-debug-all)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jacoco-0.7.5-2.fc23.cpio

%description
JaCoCo is a free code coverage library for Java,
which has been created by the EclEmma team based on the lessons learned
from using and integration existing libraries over the last five years.

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
* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

