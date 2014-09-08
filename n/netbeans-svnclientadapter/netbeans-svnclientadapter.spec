Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# Prevent brp-java-repack-jars from being run.
%global __jar_repack %{nil}

%global nb_            netbeans
%global nb_org         %{nb_}.org
%global nb_ver         7.3.1
%global nb_rel         RELEASE731
%global svnCA          svnClientAdapter
%global svnCA_ver      1.7.0
%global subclipse_ver  1.8.22

Name:           %{nb_}-svnclientadapter
Version:        %{nb_ver}
Release:        alt1_0.1.1.8.22jpp7
Summary:        Subversion Client Adapter
License:        ASL 2.0
Url:            http://subclipse.tigris.org/svnClientAdapter.html
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
# sh netbeans-svnclientadapter-create-tarball.sh
Source0:        %{svnCA}-%{svnCA_ver}-%{subclipse_ver}.tar.xz
Source1:        %{name}-create-tarball.sh
Source2:        http://bits.netbeans.org/nexus/content/groups/netbeans/org/netbeans/external/%{svnCA}-main/%{nb_rel}/%{svnCA}-main-%{nb_rel}.pom

#Source3:        http://bits.netbeans.org/nexus/content/groups/netbeans/org/netbeans/external/svnClientAdapter-javahl/RELEASE731/svnClientAdapter-javahl-RELEASE731.pom
#Source4:        http://bits.netbeans.org/nexus/content/groups/netbeans/org/netbeans/external/svnClientAdapter-svnkit/RELEASE731/svnClientAdapter-svnkit-RELEASE731.pom
# Add missing method stubs
Patch0:         %{svnCA}-%{svnCA_ver}-CmdLineClientAdapter.patch

BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  jpackage-utils
BuildRequires:  subversion-javahl
BuildRequires:  svnkit
BuildRequires:  svnkit-javahl

%if 0
BuildRequires:  antlr3-java
BuildRequires:  emma
BuildRequires:  jna
BuildRequires:  sequence-library
BuildRequires:  sqljet
BuildRequires:  svnkit-cli
BuildRequires:  trilead-ssh2
%endif

Requires:       jpackage-utils
Requires:       subversion
Source44: import.info

%description
SVNClientAdapter is a high-level Java API for Subversion.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{svnCA}-%{svnCA_ver}

%patch0 -p0

# remove all binary libs
find . -name "*.class" -print -delete
find . -name "*.jar" -print -delete

ln -sf $(build-classpath svn-javahl)       lib/svn-javahl.jar
ln -sf $(build-classpath svnkit)           lib/svnkit/svnkit-1.7.5-v1.jar
ln -sf $(build-classpath svnkit-javahl)    lib/svnkit/svnkit-javahl16-1.7.5-v1.jar
# Unused deps
#ln -sf $(build-classpath antlr3-runtime)   lib/svnkit/antlr-runtime-3.4.jar
#ln -sf $(build-classpath jna)              lib/svnkit/jna-3.4.0.jar
#ln -sf $(build-classpath sequence-library) lib/svnkit/sequence-library-1.0.2.jar
#ln -sf $(build-classpath svnkit-cli)       lib/svnkit/svnkit-cli-1.7.5-v1.jar
#ln -sf $(build-classpath sqljet)           lib/svnkit/sqljet-1.1.4.jar
#ln -sf $(build-classpath trilead-ssh2)     lib/svnkit/trilead-ssh2-1.0.0-build215.jar
# Tests suite deps
#ln -sf $(build-classpath emma)             test/lib/emma.jar
#ln -sf $(build-classpath emma_ant)         test/lib/emma_ant.jar

# fix non ASCII chars
for s in src/main/org/tigris/subversion/svnclientadapter/AbstractClientAdapter.java \
 src/main/org/tigris/subversion/svnclientadapter/ISVNDirEntry.java \
 src/main/org/tigris/subversion/svnclientadapter/ISVNNotifyListener.java \
 src/main/org/tigris/subversion/svnclientadapter/ISVNProperty.java \
 src/main/org/tigris/subversion/svnclientadapter/SVNClientAdapterFactory.java \
 src/main/org/tigris/subversion/svnclientadapter/SVNInfoUnversioned.java \
 src/main/org/tigris/subversion/svnclientadapter/SVNStatusUnversioned.java \
 src/main/org/tigris/subversion/svnclientadapter/SVNUrl.java \
 src/javahl/org/tigris/subversion/svnclientadapter/javahl/JhlClientAdapter.java \
 src/javahl/org/tigris/subversion/svnclientadapter/javahl/JhlInfo.java \
 src/javahl/org/tigris/subversion/svnclientadapter/javahl/JhlInfo2.java \
 src/commandline/org/tigris/subversion/svnclientadapter/commandline/CmdLineAnnotations.java \
 src/commandline/org/tigris/subversion/svnclientadapter/commandline/CmdLineInfoPart.java \
 src/commandline/org/tigris/subversion/svnclientadapter/commandline/CmdLineNotificationHandler.java \
 src/commandline/org/tigris/subversion/svnclientadapter/commandline/CmdLineStatusComposite.java \
 src/commandline/org/tigris/subversion/svnclientadapter/commandline/CmdLineStatuses.java \
 src/commandline/org/tigris/subversion/svnclientadapter/commandline/CommandLine.java \
 src/commandline/org/tigris/subversion/svnclientadapter/commandline/SvnAdminCommandLine.java \
 src/commandline/org/tigris/subversion/svnclientadapter/commandline/SvnCommandLine.java \
 src/commandline/org/tigris/subversion/svnclientadapter/commandline/parser/SvnActionRE.java \
 src/commandline/org/tigris/subversion/svnclientadapter/commandline/parser/SvnOutputParser.java \
 src/testcases/org/tigris/subversion/svnclientadapter/regression/CmdLineBugRegressionTest.java;do
  native2ascii -encoding UTF8 ${s} ${s}
done

%build
[ -z "$JAVA_HOME" ] && export JAVA_HOME=%{_jvmdir}/java
# Don't run tests suite because some part needs network
ant -verbose svnClientAdapter.jar javadoc

%install

install -dm 755 %{buildroot}%{_javadir} \
 %{buildroot}%{_mavenpomdir} \
 %{buildroot}%{_javadocdir}/%{name}

# jar
install -m 644 build/lib/svnClientAdapter.jar %{buildroot}%{_javadir}/%{name}.jar

# Pom and depmap
install -pm 644 %{SOURCE2} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "org.netbeans.external:svnClientAdapter-svnkit,org.netbeans.external:svnClientAdapter-javahl"

# Javadoc
cp -pr build/javadoc/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc changelog.txt license.txt readme.txt
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}
%doc license.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 7.3.1-alt1_0.1.1.8.22jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 6.7.1-alt1_6jpp7
- new release

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 6.7.1-alt1_5jpp7
- new version

* Tue Sep 13 2011 Igor Vlasenko <viy@altlinux.ru> 6.7.1-alt1_3jpp6
- update to new release by jppimport

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 6.7.1-alt1_2jpp6
- new version

* Thu Apr 30 2009 Igor Vlasenko <viy@altlinux.ru> 6.5-alt1_2jpp6
- new version

* Fri Dec 12 2008 Igor Vlasenko <viy@altlinux.ru> 6.1-alt1_3jpp6
- converted from JPackage by jppimport script

