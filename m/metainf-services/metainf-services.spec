BuildRequires: maven2-plugin-compiler maven2-plugin-jar maven2-plugin-install maven2-plugin-javadoc
BuildRequires: /proc
BuildRequires: jpackage-compat

Name: metainf-services
Version: 1.4
Release: alt1_0jpp6
Summary: A Java META-INF/services generator

Group: Development/Java
License: MIT
Url: http://metainf-services.kohsuke.org/

Source0: %name-%version.tar
Source1: settings.xml

Patch0: fix-extra-deps.patch

BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: maven2 >= 0:2.0.8
BuildRequires: maven2-plugin-resources
BuildRequires: junit4

Requires: jpackage-utils >= 0:5.0.0

Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0

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
cp -p %SOURCE1 settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
mkdir external_repo
ln -s %_javadir external_repo/JPP

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL
export MAVEN_OPTS="-Dmaven2.jpp.mode=true -Dmaven.repo.local=$MAVEN_REPO_LOCAL -Djava.awt.headless=true -Daggregate=true -Dallow.test.failure.ignore=true -Dmaven.test.failure.ignore=true"
export MAVEN_SETTINGS=$(pwd)/settings.xml

mvn-jpp -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $MAVEN_SETTINGS \
        install javadoc:javadoc

%install
%__rm -rf %buildroot

# jar
%__mkdir_p %buildroot%_javadir
%__install -m 644 target/%name-%version.jar %buildroot%_javadir
(cd %buildroot%_javadir && for jar in *-%{version}*; do \
%__ln_s ${jar} ${jar/-%version/}; done)

# poms
%__mkdir_p %buildroot%_datadir/maven2/poms
%__install -m 644 pom.xml \
               $RPM_BUILD_ROOT%_datadir/maven2/poms/JPP-%name.pom
%add_to_maven_depmap %name %name %version JPP %name

# javadoc
%__mkdir_p %buildroot%_javadocdir/%name-%version
%__cp -a target/site/apidocs/* \
               %buildroot%_javadocdir/%name-%version
%__ln_s %name-%version %buildroot%_javadocdir/%name

%files
%_javadir/*.jar
%_datadir/maven2/poms/*
%_mavendepmapfragdir/*

%files javadoc
%_javadocdir/%name-%version
%_javadocdir/%name

%changelog
* Thu Feb 28 2013 Paul Wolneykien <manowar@altlinux.org> 1.4-alt1_0jpp6
- Initial build for ALT Linux.
