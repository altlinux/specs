Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# The version of Subversion that we are compatible with
%global svn_version 1.8.1

Epoch:   1
Name:    svnkit
Version: 1.8.12
Release: alt1_2jpp8
Summary: Pure Java library to manage Subversion working copies and repositories

# License located at https://svnkit.com/license.html
License:        TMate and ASL 2.0
URL:            https://www.svnkit.com/
Source0:        https://www.svnkit.com/org.tmatesoft.svn_%{version}.src.zip

# POMs
Source1:        http://repo1.maven.org/maven2/org/tmatesoft/svnkit/svnkit/%{version}/svnkit-%{version}.pom
Source2:        http://repo1.maven.org/maven2/org/tmatesoft/svnkit/svnkit-cli/%{version}/svnkit-cli-%{version}.pom
Source3:        http://repo1.maven.org/maven2/org/tmatesoft/svnkit/svnkit-javahl16/%{version}/svnkit-javahl16-%{version}.pom

# Custom aggregator pom to avoid reliance on gradle
Source4:        svnkit-parent.pom

# SVNKit provides a pure-Java implementation of the Subversion JavaHL API, but it only provides an older
# Subversion JavaHL API, so we need an old version of the JavaHL source to build against. This is that:
#  $ svn export https://svn.apache.org/repos/asf/subversion/tags/1.8.1/subversion/bindings/javahl/src/ javahl-1.8.1
Source5:        javahl-%{svn_version}.tar.gz

# Just in SRPM due to nailgun comes included in svnkit upstream sources:
Source10:       https://www.apache.org/licenses/LICENSE-2.0.txt
Source11:       https://www.apache.org/licenses/LICENSE-1.1.txt

# svnkit's trilead-ssh2 does not throw InterruptedException from Session.waitForCondition()
# Fedora's trilead-ssh2 trhows ...
Patch1:         svnkit-1.8.5-SshSession-unreported-exception.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.jcraft:jsch.agentproxy.connector-factory)
BuildRequires:  mvn(com.jcraft:jsch.agentproxy.svnkit-trilead-ssh2)
BuildRequires:  mvn(com.trilead:trilead-ssh2)
BuildRequires:  mvn(de.regnis.q.sequence:sequence-library) >= 1.0.3
BuildRequires:  mvn(net.java.dev.jna:jna)
BuildRequires:  mvn(net.java.dev.jna:jna-platform)
BuildRequires:  mvn(org.tmatesoft.sqljet:sqljet)
Source44: import.info

%description
SVNKit is a pure java Subversion client library. You would like to use SVNKit
when you need to access or modify Subversion repository from your Java
application, as a standalone program and plugin or web application. Being a
pure java program, SVNKit doesn't need any additional configuration or native
binaries to work on any OS that runs java.

%package cli
Group: Development/Java
Summary: SVNKit based Subversion command line client

%description cli
%{summary}.

%package javahl
Group: Development/Java
Summary: SVNKit based Subversion JavaHL API implementation

%description javahl
%{summary}.

%package javadoc
Group: Development/Java
Summary: Javadoc for SVNKit
BuildArch: noarch

%description javadoc
API documentation for SVNKit.

%prep
%setup -q -n %{name}-%{version}

%patch1 -p1

# Delete all pre-built binaries, except for "template.jar" which is important
# for the function of svnkit and contains no actual bytecode:
find -name *.class -delete
find -name *.jar -a ! -name template.jar -delete

cp -pr %{SOURCE1} svnkit/pom.xml
cp -pr %{SOURCE2} svnkit-cli/pom.xml
cp -pr %{SOURCE3} svnkit-javahl16/pom.xml
cp -pr %{SOURCE4} pom.xml

# Build against the bundled version of the JavaHL API source
(cd svnkit-javahl16/src/main/java/ &&  tar xf %{SOURCE5} --strip-components=1 --skip-old-files)
%pom_remove_dep ":svn-javahl-api" svnkit-javahl16
%pom_remove_dep ":svn-javahl-tests" svnkit-javahl16

rev="t$(date -u +%Y%m%d%H%M)"
cat > svnkit/src/main/resources/svnkit.build.properties <<EOF
svnkit.version=%{version}
build.number=$rev

svnkit.version.string=SVN/%{svn_version} SVNKit/%{version} (http://svnkit.com/) $rev
svnkit.version.major=$(echo "%{version}" | cut -f1 -d.)
svnkit.version.minor=$(echo "%{version}" | cut -f2 -d.)
svnkit.version.micro=$(echo "%{version}" | cut -f3 -d.)
svnkit.version.revision=$rev

svnkit.svn.version=%{svn_version}
EOF

# Don't install our custom aggregator pom
%mvn_package ":parent" __noinstall

%build
# Upstream builds with ignore test failures set to true, so I guess we shouldn't expect them to work...
# Let's skip tests for now.
%mvn_build -s -f -- -Dproject.buildVersion.baseVersion=%{version}

%install
%mvn_install

# Generate scripts for command line tools
for class in SVN SVNAdmin SVNDumpFilter SVNLook SVNSync SVNVersion ; do
  mainclass=org.tmatesoft.svn.cli.$class
  script=j$(echo $class | tr '[:upper:]' '[:lower:]')
  %jpackage_script "$mainclass" "-Dsun.io.useCanonCaches=false" "" "svnkit:sequence-library:sqljet:antlr32/antlr-runtime-3.2:trilead-ssh2" "$script" true
done

mkdir -p $RPM_BUILD_ROOT`dirname /etc/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/%{name}.conf

%files -f .mfiles-svnkit
%doc --no-dereference LICENSE.txt README.txt CHANGES.txt
%config(noreplace,missingok) /etc/%{name}.conf

%files cli -f .mfiles-svnkit-cli
%{_bindir}/*

%files javahl -f .mfiles-svnkit-javahl16

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Fri Apr 20 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.8.12-alt1_2jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.6-alt2_7jpp7
- new release

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.7.6-alt2_6jpp7
- target 5 build

* Mon Mar 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.7.6-alt1_6jpp7
- replaced by fc package

* Wed Jan 27 2010 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_1jpp6
- new version

* Fri Nov 30 2007 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt1_2jpp5.0
- converted from JPackage by jppimport script

