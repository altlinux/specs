BuildRequires: maven-compiler-plugin maven-jar-plugin maven-install-plugin maven-javadoc-plugin
BuildRequires: /proc
BuildRequires: jpackage-compat

Name: metainf-services
Version: 1.4
Release: alt4_0jpp6
Summary: A Java META-INF/services generator

Group: Development/Java
License: MIT
Url: http://metainf-services.kohsuke.org/

Source0: %name-%version.tar

Patch0: fix-extra-deps.patch

BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: maven-local
BuildRequires: maven-resources-plugin
BuildRequires: junit

Requires: jpackage-utils 

BuildArch: noarch

%description
This tiny library is an annotation processor that automatically
generates META-INF/services/* file from annotations that you placed on
your source code, thereby eliminating the need for you to do it by
yourself.

%package javadoc
Summary: Javadocs for %name
Group: Development/Java
Requires: %name = %version-%release
BuildArch: noarch

%description javadoc
%summary

This package contains generated documentation.

%prep
%setup
%patch0 -p2

%build
export MAVEN_OPTS="-Djava.awt.headless=true -Daggregate=true -Dallow.test.failure.ignore=true -Dmaven.test.failure.ignore=true"

mvn-rpmbuild -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        install javadoc:javadoc

%install
# jar
%__mkdir_p %buildroot%_javadir
%__install -m 644 target/%name-%version.jar %buildroot%_javadir
(cd %buildroot%_javadir && for jar in *-%{version}*; do \
%__ln_s ${jar} ${jar/-%version/}; done)

# poms
%__mkdir_p %buildroot%_mavenpomdir/
%__install -m 644 pom.xml \
               $RPM_BUILD_ROOT%_mavenpomdir/JPP-%name.pom
%add_to_maven_depmap org.kohsuke.metainf-services %name %version JPP %name

# javadoc
%__mkdir_p %buildroot%_javadocdir/%name-%version
%__cp -a target/site/apidocs/* \
               %buildroot%_javadocdir/%name-%version
%__ln_s %name-%version %buildroot%_javadocdir/%name

%files
%_javadir/*.jar
%_mavenpomdir/*
%_mavendepmapfragdir/*

%files javadoc
%_javadocdir/%name-%version
%_javadocdir/%name

%changelog
* Fri Aug 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt4_0jpp6
- NMU: BR: maven-local

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_0jpp6
- migrated to mvn-rpmbuild

* Thu Feb 28 2013 Paul Wolneykien <manowar@altlinux.ru> 1.4-alt2_0jpp6
- Fix the groupId in the generated POM part.

* Thu Feb 28 2013 Paul Wolneykien <manowar@altlinux.org> 1.4-alt1_0jpp6
- Initial build for ALT Linux.
