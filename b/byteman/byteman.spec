Name: byteman
Version: 2.1.4.1
Summary: Java agent-based bytecode injection tool
License: LGPLv2+
Url: http://www.jboss.org/byteman
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: byteman = 2.1.4.1-5.fc23
Provides: mvn(org.jboss.byteman:byteman) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman-bmunit) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman-bmunit::javadoc:) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman-bmunit::sources:) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman-bmunit:pom:) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman-download:pom:) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman-dtest) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman-dtest::javadoc:) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman-dtest::sources:) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman-dtest:pom:) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman-install) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman-install::javadoc:) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman-install::sources:) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman-install:pom:) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman-root:pom:) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman-rulecheck-maven-plugin) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman-rulecheck-maven-plugin::javadoc:) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman-rulecheck-maven-plugin::sources:) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman-rulecheck-maven-plugin:pom:) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman-sample) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman-sample::javadoc:) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman-sample::sources:) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman-sample:pom:) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman-submit) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman-submit::javadoc:) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman-submit::sources:) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman-submit:pom:) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman::javadoc:) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman::sources:) = 2.1.4.1
Provides: mvn(org.jboss.byteman:byteman:pom:) = 2.1.4.1
Requires: /bin/bash
Requires: /bin/sh
Requires: java-devel
Requires: java-headless
Requires: jpackage-utils
Requires: jpackage-utils
Requires: mvn(asm:asm-all)
Requires: mvn(com.sun:tools)
Requires: mvn(java_cup:java_cup)
Requires: mvn(org.apache.maven:maven-core)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.apache.maven:maven-project)
Requires: mvn(org.codehaus.plexus:plexus-utils)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: byteman-2.1.4.1-5.fc23.cpio

%description
Byteman is a tool which simplifies tracing and testing of Java programs.
Byteman allows you to insert extra Java code into your application,
either as it is loaded during JVM startup or even after it has already
started running. The injected code is allowed to access any of your data
and call any application methods, including where they are private.
You can inject code almost anywhere you want and there is no need to
prepare the original source code in advance nor do you have to recompile,
repackage or redeploy your application. In fact you can remove injected
code and reinstall different code while the application continues to execute.

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
* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.4.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.4-alt1_3jpp7
- new version

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_5jpp7
- new fc release

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_4jpp7
- fc build

