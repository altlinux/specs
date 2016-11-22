Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# READ BEFORE UPDATING: After updating this package to new upstream
# version eclipse-ecf should be rebuilt.  For more info, see:
# https://fedoraproject.org/wiki/SIGs/Java#Package_Update.2FRebuild_Notes

%global base_name  logging
%global short_name commons-%{base_name}

Name:           apache-%{short_name}
Version:        1.2
Release:        alt1_5jpp8
Summary:        Apache Commons Logging
License:        ASL 2.0
URL:            http://commons.apache.org/%{base_name}
Source0:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Source2:        http://mirrors.ibiblio.org/pub/mirrors/maven2/%{short_name}/%{short_name}-api/1.1/%{short_name}-api-1.1.pom

Patch0:         0001-Generate-different-Bundle-SymbolicName-for-different.patch

BuildRequires:  maven-local
BuildRequires:  mvn(avalon-framework:avalon-framework-api)
BuildRequires:  mvn(avalon-framework:avalon-framework-impl)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(log4j:log4j)
BuildRequires:  mvn(logkit:logkit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

BuildArch:      noarch
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
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
%{summary}.

# -----------------------------------------------------------------------------

%prep
%setup -q -n %{short_name}-%{version}-src
%patch0 -p1

# Sent upstream https://issues.apache.org/jira/browse/LOGGING-143
%pom_remove_dep :avalon-framework
%pom_add_dep avalon-framework:avalon-framework-api:4.3:provided
%pom_add_dep avalon-framework:avalon-framework-impl:4.3:test

%pom_xpath_inject "pom:dependency[pom:artifactId='logkit']" '<scope>provided</scope>'

%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :maven-scm-publish-plugin

sed -i 's/\r//' RELEASE-NOTES.txt LICENSE.txt NOTICE.txt

# for compatibility reasons
%mvn_file ":%{short_name}{*}" "%{short_name}@1" "%{name}@1"
%mvn_alias ":%{short_name}{*}" "org.apache.commons:%{short_name}@1" "apache:%{short_name}@1"

# Remove log4j12 tests
rm -rf src/test/java/org/apache/commons/logging/log4j/log4j12


%build
%mvn_build

# -----------------------------------------------------------------------------

%install
%mvn_install

install -p -m 644 target/%{short_name}-api-%{version}.jar %{buildroot}/%{_javadir}/%{name}-api.jar
install -p -m 644 target/%{short_name}-adapters-%{version}.jar %{buildroot}/%{_javadir}/%{name}-adapters.jar

pushd %{buildroot}/%{_javadir}
for jar in %{name}-*; do
    ln -sf ${jar} `echo ${jar}| sed "s|apache-||g"`
done
popd

install -pm 644 %{SOURCE2} %{buildroot}/%{_mavenpomdir}/JPP-%{short_name}-api.pom

%add_maven_depmap JPP-%{short_name}-api.pom %{short_name}-api.jar -a "org.apache.commons:commons-logging-api"

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt
%doc PROPOSAL.html RELEASE-NOTES.txt
%{_javadir}/*%{short_name}-api.jar
%{_javadir}/*%{short_name}-adapters.jar


%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

# -----------------------------------------------------------------------------

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_5jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_4jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt1_2jpp7
- new version

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
