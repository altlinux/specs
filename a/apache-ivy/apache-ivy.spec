Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_without  ssh
%bcond_without  bouncycastle

Name:           apache-ivy
Version:        2.4.0
Release:        alt1_10jpp8
Summary:        Java-based dependency manager

License:        ASL 2.0
URL:            http://ant.apache.org/ivy
Source0:        http://www.apache.org/dist/ant/ivy/%{version}/%{name}-%{version}-src.tar.gz
BuildArch:      noarch

# Non-upstreamable.  Add /etc/ivy/ivysettings.xml at the end list of
# settings files Ivy tries to load.  This file will be used only as
# last resort, when no other setting files exist.
Patch0:         %{name}-global-settings.patch
# sent upstream: IVY-1521
Patch1:         port-to-bc-1.52.patch

Provides:       ivy = %{version}-%{release}

BuildRequires:  ant
BuildRequires:  ant-contrib
BuildRequires:  ant-testutil
BuildRequires:  apache-commons-vfs
BuildRequires:  apache-commons-lang
%if %{with bouncycastle}
BuildRequires:  bouncycastle
BuildRequires:  bouncycastle-pg
%endif
BuildRequires:  apache-commons-httpclient
BuildRequires:  jsch
BuildRequires:  jakarta-oro
BuildRequires:  apache-commons-parent
BuildRequires:  sonatype-oss-parent
BuildRequires:  apache-parent
BuildRequires:  ivy-local >= 4
%if %{with ssh}
BuildRequires:  jsch-agent-proxy-connector-factory
BuildRequires:  jsch-agent-proxy-core
BuildRequires:  jsch-agent-proxy-jsch
%endif
Source44: import.info
AutoReqProv: yes,noosgi
Obsoletes: ivy < 2

%description
Apache Ivy is a tool for managing (recording, tracking, resolving and
reporting) project dependencies.  It is designed as process agnostic and is
not tied to any methodology or structure. while available as a standalone
tool, Apache Ivy works particularly well with Apache Ant providing a number
of powerful Ant tasks ranging from dependency resolution to dependency
reporting and publication.

%package javadoc
Group: Development/Java
Summary:        API Documentation for ivy
BuildArch: noarch

%description javadoc
JavaDoc documentation for %{name}

%prep
%setup -q
%patch0
%patch1 -p1

# Don't hardcode sysconfdir path
sed -i 's:/etc/ivy/:%{_sysconfdir}/ivy/:' src/java/org/apache/ivy/ant/IvyAntSettings.java

%if %{without ssh}
%pom_remove_dep :jsch
%pom_remove_dep :jsch.agentproxy
%pom_remove_dep :jsch.agentproxy.connector-factory
%pom_remove_dep :jsch.agentproxy.jsch
rm -r src/java/org/apache/ivy/plugins/repository/{ssh,sftp}
rm src/java/org/apache/ivy/plugins/resolver/*{Ssh,SFTP}*.java
%endif

%if %{without bouncycastle}
%pom_remove_dep org.bouncycastle
rm src/java/org/apache/ivy/plugins/signer/bouncycastle/OpenPGPSignatureGenerator.java
%endif

%mvn_alias : jayasoft:ivy
%mvn_file : %{name}/ivy ivy

# Fix messed-up encodings
for F in README LICENSE NOTICE
do
        sed 's/\r//' $F |iconv -f iso8859-1 -t utf8 >$F.utf8
        touch -r $F $F.utf8
        mv $F.utf8 $F
done
# ant-trax has been obsoleted, use main ant package
sed -i s/ant-trax/ant/ ivy.xml

# Fedora bouncycastle packages provide -jdk16 artifacts only
sed -i /bouncycastle/s/jdk14/jdk16/ ivy.xml

# Port from commons-vfs 1.x to 2.x
sed -i "s/commons.vfs/&2/" src/java/org/apache/ivy/plugins/repository/vfs/*

# Remove prebuilt documentation
rm -rf doc build/doc

# Publish artifacts through XMvn
sed -i /ivy:publish/s/local/xmvn/ build.xml

# girar noarch diff
sed -i -e s,yyyyMMddHHmmss,yyyyMMddHH, build.xml


%build
%ant -Divy.mode=local -Dtarget.ivy.bundle.version=%{version} -Dtarget.ivy.bundle.version.qualifier= -Dtarget.ivy.version=%{version} jar javadoc publish-local


%install
%mvn_install -J build/doc/reports/api

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ant.d
echo "apache-ivy/ivy" > $RPM_BUILD_ROOT%{_sysconfdir}/ant.d/%{name}

%files -f .mfiles
%{_sysconfdir}/ant.d/%{name}
%doc README
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Wed May 09 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt1_10jpp8
- java update

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt1_9jpp8
- new fc release

* Mon Nov 28 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt1_5jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt1_4jpp8
- java 8 mass update

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt1_1jpp7
- new version

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt3_5jpp7
- fc release

* Sat Sep 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt3_1jpp6
- build with new commons-vfs2

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt2_1jpp6
- fixed build

* Wed Sep 07 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt1_1jpp6
- new version

* Mon Sep 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.0-alt1_2jpp6
- new version

