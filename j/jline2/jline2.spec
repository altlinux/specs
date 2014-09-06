Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             jline2
Version:          2.10
Release:          alt1_8jpp7
Summary:          JLine is a Java library for handling console input
Group:            Development/Java
License:          BSD and ASL 2.0
URL:              https://github.com/jline/jline2

# git clone git://github.com/jline/jline2.git
# cd jline2/ && git archive --format=tar --prefix=jline-2.10/ jline-2.10 | xz > jline-2.10.tar.xz
Source0:          jline-%{version}.tar.xz

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    junit4
BuildRequires:    jansi
BuildRequires:    fusesource-pom
BuildRequires:    maven-surefire-provider-junit4

Requires:         jpackage-utils
Requires:         jansi
Source44: import.info

%description
JLine is a Java library for handling console input. It is similar
in functionality to BSD editline and GNU readline. People familiar
with the readline/editline capabilities for modern shells (such as
bash and tcsh) will find most of the command editing features of
JLine to be familiar. 

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jline-%{version}

# Remove maven-shade-plugin usage
%pom_remove_plugin "org.apache.maven.plugins:maven-shade-plugin"
# Remove animal sniffer plugin in order to reduce deps
%pom_remove_plugin "org.codehaus.mojo:animal-sniffer-maven-plugin"

# Remove unavailable and unneeded deps
%pom_xpath_remove "pom:build/pom:extensions"
%pom_xpath_remove "pom:build/pom:pluginManagement/pom:plugins/pom:plugin[pom:artifactId = 'maven-site-plugin']"

# Do not import non-existing internal package
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-bundle-plugin']/pom:executions/pom:execution/pom:configuration/pom:instructions/pom:Import-Package"
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-bundle-plugin']/pom:executions/pom:execution/pom:configuration/pom:instructions" "<Import-Package>javax.swing;resolution:=optional,!org.fusesource.jansi.internal</Import-Package>"

# Let maven bundle plugin figure out the exports.
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-bundle-plugin']/pom:executions/pom:execution/pom:configuration/pom:instructions/pom:Export-Package"

%build
mvn-rpmbuild -Dmaven.test.failure.ignore=true install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
cp -p target/jline-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# Uh, oh...
# http://sourceforge.net/mailarchive/message.php?msg_id=27330388
# https://github.com/jline/jline2/commit/7a4d27430999706f0fd30b4548d5879275a88de2#pom.xml
%add_maven_depmap -v "" -a "jline:jline"

# add_maven_depmap moves actual jar into its %{_javadir}/%{name}-%{version}.jar
ln -s %{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*
%doc CHANGELOG.md README.md LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.10-alt1_8jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt3_7jpp7
- rebuild with maven-local

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt2_7jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_7jpp7
- fc update

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_6jpp7
- new fc release

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_5jpp7
- fc version

* Sat Jan 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_3jpp6
- new jpp relase

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_2jpp6
- new version

