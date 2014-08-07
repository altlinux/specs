Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat

%global base_name  logging
%global short_name commons-%{base_name}

Name:           apache-%{short_name}
Version:        1.1.1
Release:        alt8_20jpp7
Summary:        Apache Commons Logging
License:        ASL 2.0
Group:          Development/Java
URL:            http://commons.apache.org/%{base_name}
Source0:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Source1:        %{short_name}.depmap
Source2:        http://mirrors.ibiblio.org/pub/mirrors/maven2/%{short_name}/%{short_name}-api/1.1/%{short_name}-api-1.1.pom
# Sent upstream https://issues.apache.org/jira/browse/LOGGING-143
Patch0:         %{short_name}-avalon-update.patch

Patch1:         %{short_name}-eclipse-manifest.patch
Patch33:	commons-logging-alt-avalon-logkit.patch
BuildArch:      noarch
BuildRequires:  maven-local
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  avalon-framework >= 4.3
BuildRequires:  avalon-logkit
BuildRequires:  apache-commons-parent
BuildRequires:  maven-plugin-build-helper
BuildRequires:  maven-release-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  servlet

Requires:       jpackage-utils >= 0:1.6

# This should go away with F-17
Provides:       jakarta-%{short_name} = 0:%{version}-%{release}
Obsoletes:      jakarta-%{short_name} <= 0:1.0.4
Source44: import.info

%description
The commons-logging package provides a simple, component oriented
interface (org.apache.commons.logging.Log) together with wrappers for
logging systems. The user can choose at runtime which system they want
to use. In addition, a small number of basic implementations are
provided to allow users to use the package standalone.
commons-logging was heavily influenced by Avalon's Logkit and Log4J. The
commons-logging abstraction is meant to minimize the differences between
the two, and to allow a developer to not tie himself to a particular
logging implementation.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils

Obsoletes:      jakarta-%{short_name}-javadoc <= 0:1.0.4
BuildArch: noarch

%description    javadoc
%{summary}.

# -----------------------------------------------------------------------------

%prep
%setup -q -n %{short_name}-%{version}-src

%patch0 -p1
%patch1
%patch33 -p1

sed -i 's/\r//' RELEASE-NOTES.txt LICENSE.txt

# -----------------------------------------------------------------------------

%build
# fails with recent surefire for some reason
rm src/test/org/apache/commons/logging/logkit/StandardTestCase.java
rm src/test/org/apache/commons/logging/servlet/BasicServletTestCase.java

# These files have names suggesting they are test cases but they are not.
# They should probably be renamed/excluded from surefire run properly
rm src/test/org/apache/commons/logging/log4j/log4j12/*StandardTestCase.java

mvn-rpmbuild -Dmaven.local.depmap.file="%{SOURCE1}" \
    install javadoc:aggregate

# -----------------------------------------------------------------------------

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 644 target/%{short_name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -p -m 644 target/%{short_name}-api-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-api.jar
install -p -m 644 target/%{short_name}-adapters-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-adapters.jar

pushd $RPM_BUILD_ROOT%{_javadir}
for jar in %{name}*; do
    ln -sf ${jar} `echo $jar| sed "s|apache-||g"`
done
popd

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{short_name}.pom
install -pm 644 %{SOURCE2} $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{short_name}-api.pom

%add_to_maven_depmap org.apache.commons %{short_name} %{version} JPP %{short_name}
%add_to_maven_depmap org.apache.commons %{short_name}-api %{version} JPP %{short_name}-api
%add_to_maven_depmap org.apache.commons %{short_name}-adapters %{version} JPP %{short_name}-adapters

# following lines are only for backwards compatibility. New packages
# should use proper groupid org.apache.commons and also artifactid
%add_to_maven_depmap %{short_name} %{short_name} %{version} JPP %{short_name}
%add_to_maven_depmap %{short_name} %{short_name}-api %{version} JPP %{short_name}-api
%add_to_maven_depmap %{short_name} %{short_name}-adapters %{version} JPP %{short_name}-adapters


# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc PROPOSAL.html STATUS.html LICENSE.txt RELEASE-NOTES.txt
%{_javadir}/*
%{_mavenpomdir}/JPP-%{short_name}.pom
%{_mavenpomdir}/JPP-%{short_name}-api.pom
%{_mavendepmapfragdir}/*


%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}

# -----------------------------------------------------------------------------

%changelog
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt8_20jpp7
- rebuild with maven-local

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt7_20jpp7
- fixed build

* Tue Jul 15 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt6_20jpp7
- fixed build

* Wed Aug 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt5_20jpp7
- added jakarta cpmpat symlinks

* Wed Aug 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt4_20jpp7
- no not package repolib in main commons-logging

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt3_20jpp7
- new release

* Sat Feb 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt3_6jpp6
- fixed build

* Sun Feb 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt2_6jpp6
- synced osgi manifest

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt1_6jpp6
- new version

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt1_2jpp6
- new version

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_8jpp5
- updated OSGi manifest

* Fri Jul 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_7jpp5
- rebuild with osgi provides

* Mon May 26 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_4jpp1.7
- updated to new jpackage release

* Mon Dec 03 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_3jpp1.7
- added eclipse manifest

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_3jpp1.7
- updated to new jpackage release

* Fri Nov 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_2jpp1.7
- updated to new jpackage release

* Fri Apr 27 2007 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt4
- added JPackage compatibility stuff

* Sun Aug 29 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.4-alt3
- Disabled check by default due to a circular build dependency

* Thu Jul 15 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.4-alt2
- Disabled avalon by default

* Thu Jun 17 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.4-alt1
- New upstream release
- Patch0 obsoleted

* Thu Feb 26 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.3-alt1
- Adapted for Sisyphus from the JPackage project
