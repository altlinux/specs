Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           derby
Version:        10.9.1.0
Release:        alt1_2jpp7
Summary:        Relational database implemented entirely in Java

Group:          Databases
License:        ASL 2.0
URL:            http://db.apache.org/derby/
Source0:        http://archive.apache.org/dist/db/%{name}/db-%{name}-%{version}/db-%{name}-%{version}-src.tar.gz
Source1:        derby-script
Source2:        derby.service

Source10:       http://repo1.maven.org/maven2/org/apache/%{name}/derby/%{version}/derby-%{version}.pom
Source11:       http://repo1.maven.org/maven2/org/apache/%{name}/derby-project/%{version}/derby-project-%{version}.pom
Source12:       http://repo1.maven.org/maven2/org/apache/%{name}/derbyLocale_cs/%{version}/derbyLocale_cs-%{version}.pom
Source13:       http://repo1.maven.org/maven2/org/apache/%{name}/derbyLocale_de_DE/%{version}/derbyLocale_de_DE-%{version}.pom
Source14:       http://repo1.maven.org/maven2/org/apache/%{name}/derbyLocale_es/%{version}/derbyLocale_es-%{version}.pom
Source15:       http://repo1.maven.org/maven2/org/apache/%{name}/derbyLocale_fr/%{version}/derbyLocale_fr-%{version}.pom
Source16:       http://repo1.maven.org/maven2/org/apache/%{name}/derbyLocale_hu/%{version}/derbyLocale_hu-%{version}.pom
Source17:       http://repo1.maven.org/maven2/org/apache/%{name}/derbyLocale_it/%{version}/derbyLocale_it-%{version}.pom
Source18:       http://repo1.maven.org/maven2/org/apache/%{name}/derbyLocale_ja_JP/%{version}/derbyLocale_ja_JP-%{version}.pom
Source19:       http://repo1.maven.org/maven2/org/apache/%{name}/derbyLocale_ko_KR/%{version}/derbyLocale_ko_KR-%{version}.pom
Source20:       http://repo1.maven.org/maven2/org/apache/%{name}/derbyLocale_pl/%{version}/derbyLocale_pl-%{version}.pom
Source21:       http://repo1.maven.org/maven2/org/apache/%{name}/derbyLocale_pt_BR/%{version}/derbyLocale_pt_BR-%{version}.pom
Source22:       http://repo1.maven.org/maven2/org/apache/%{name}/derbyLocale_ru/%{version}/derbyLocale_ru-%{version}.pom
Source23:       http://repo1.maven.org/maven2/org/apache/%{name}/derbyLocale_zh_CN/%{version}/derbyLocale_zh_CN-%{version}.pom
Source24:       http://repo1.maven.org/maven2/org/apache/%{name}/derbyLocale_zh_TW/%{version}/derbyLocale_zh_TW-%{version}.pom
Source25:       http://repo1.maven.org/maven2/org/apache/%{name}/derbyclient/%{version}/derbyclient-%{version}.pom
Source26:       http://repo1.maven.org/maven2/org/apache/%{name}/derbynet/%{version}/derbynet-%{version}.pom
Source27:       http://repo1.maven.org/maven2/org/apache/%{name}/derbytools/%{version}/derbytools-%{version}.pom

# https://issues.apache.org/jira/browse/DERBY-5125
Patch1: derby-javacc5.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=830661
Patch2: derby-net.patch

BuildRequires:  jpackage-utils
BuildRequires:  servlet25
BuildRequires:  jakarta-oro
BuildRequires:  javacc
BuildRequires:  junit4
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
BuildRequires:  ant
Requires:       jpackage-utils
Requires(pre):  shadow-utils

BuildArch:      noarch
Source44: import.info

%description
Apache Derby, an Apache DB sub-project, is a relational database implemented
entirely in Java. Some key advantages include a small footprint, conformance
to Java, JDBC, and SQL standards and embedded JDBC driver.


%prep
%setup -q -c
pushd db-%{name}-%{version}-src
rm java/engine/org/apache/derby/impl/sql/compile/Token.java
%patch1 -p0
popd
%patch2 -p1

%build
cd db-%{name}-%{version}-src
find -name '*.jar' -delete

# tools/ant/properties/extrapath.properties
ln -sf $(build-classpath javacc) tools/java/javacc.jar
ln -sf $(build-classpath servlet25) \
        tools/java/geronimo-spec-servlet-2.4-rc4.jar
ln -sf $(build-classpath xalan-j2) tools/java/xalan.jar
ln -sf $(build-classpath oro) tools/java/jakarta-oro-2.0.8.jar
ln -sf $(build-classpath xerces-j2) tools/java/xercesImpl.jar
ln -sf $(build-classpath xalan-j2-serializer) tools/java/serializer.jar
ln -sf $(build-classpath junit4) tools/java/junit.jar

# Using generics
find -name build.xml |xargs sed '
        s/target="1.4"/target="1.6"/
        s/source="1.4"/source="1.6"/
        /Class-Path/d
' -i

# Fire
ant buildsource -Dderby.source.rpm=%{version}
ant buildjars -Dderby.source.rpm=%{version}


%install
cd db-%{name}-%{version}-src

# Library
install -d $RPM_BUILD_ROOT%{_javadir}/%{name}
for i in jars/sane/*.jar
do
        B=$(basename $i |sed 's/.jar$//')
        install -m644 $i $RPM_BUILD_ROOT%{_javadir}/%{name}/$B-%{version}.jar
        ln -sf $B-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/$B.jar
done

# We hardlink instead of symlinking so that default security policy
# applies to derbynet.jar
ln -f $RPM_BUILD_ROOT%{_javadir}/%{name}/derbynet-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}/derbynet.jar


# Wrapper scripts
install -d $RPM_BUILD_ROOT%{_bindir}
install -p -m755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}-ij
for P in sysinfo NetworkServerControl startNetworkServer stopNetworkServer
do
        ln $RPM_BUILD_ROOT%{_bindir}/%{name}-ij \
                $RPM_BUILD_ROOT%{_bindir}/%{name}-$P
done

# POMs
install -d $RPM_BUILD_ROOT%{_mavenpomdir}
install -p -m644 %{SOURCE10} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.derby-derby.pom
install -p -m644 %{SOURCE11} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.derby-derby-project.pom
install -p -m644 %{SOURCE12} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.derby-derbyLocale_cs.pom
install -p -m644 %{SOURCE13} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.derby-derbyLocale_de_DE.pom
install -p -m644 %{SOURCE14} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.derby-derbyLocale_es.pom
install -p -m644 %{SOURCE15} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.derby-derbyLocale_fr.pom
install -p -m644 %{SOURCE16} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.derby-derbyLocale_hu.pom
install -p -m644 %{SOURCE17} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.derby-derbyLocale_it.pom
install -p -m644 %{SOURCE18} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.derby-derbyLocale_ja_JP.pom
install -p -m644 %{SOURCE19} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.derby-derbyLocale_ko_KR.pom
install -p -m644 %{SOURCE20} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.derby-derbyLocale_pl.pom
install -p -m644 %{SOURCE21} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.derby-derbyLocale_pt_BR.pom
install -p -m644 %{SOURCE22} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.derby-derbyLocale_ru.pom
install -p -m644 %{SOURCE23} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.derby-derbyLocale_zh_CN.pom
install -p -m644 %{SOURCE24} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.derby-derbyLocale_zh_TW.pom
install -p -m644 %{SOURCE25} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.derby-derbyclient.pom
install -p -m644 %{SOURCE26} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.derby-derbynet.pom
install -p -m644 %{SOURCE27} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.derby-derbytools.pom

# Dependency maps
%add_to_maven_depmap org.apache.derby derby %{version} JPP/derby derby
%add_to_maven_depmap org.apache.derby derby-project %{version} JPP/derby derby-project
%add_to_maven_depmap org.apache.derby derbyLocale_cs %{version} JPP/derby derbyLocale_cs
%add_to_maven_depmap org.apache.derby derbyLocale_de_DE %{version} JPP/derby derbyLocale_de_DE
%add_to_maven_depmap org.apache.derby derbyLocale_es %{version} JPP/derby derbyLocale_es
%add_to_maven_depmap org.apache.derby derbyLocale_fr %{version} JPP/derby derbyLocale_fr
%add_to_maven_depmap org.apache.derby derbyLocale_hu %{version} JPP/derby derbyLocale_hu
%add_to_maven_depmap org.apache.derby derbyLocale_it %{version} JPP/derby derbyLocale_it
%add_to_maven_depmap org.apache.derby derbyLocale_ja_JP %{version} JPP/derby derbyLocale_ja_JP
%add_to_maven_depmap org.apache.derby derbyLocale_ko_KR %{version} JPP/derby derbyLocale_ko_KR
%add_to_maven_depmap org.apache.derby derbyLocale_pl %{version} JPP/derby derbyLocale_pl
%add_to_maven_depmap org.apache.derby derbyLocale_pt_BR %{version} JPP/derby derbyLocale_pt_BR
%add_to_maven_depmap org.apache.derby derbyLocale_ru %{version} JPP/derby derbyLocale_ru
%add_to_maven_depmap org.apache.derby derbyLocale_zh_CN %{version} JPP/derby derbyLocale_zh_CN
%add_to_maven_depmap org.apache.derby derbyLocale_zh_TW %{version} JPP/derby derbyLocale_zh_TW
%add_to_maven_depmap org.apache.derby derbyclient %{version} JPP/derby derbyclient
%add_to_maven_depmap org.apache.derby derbynet %{version} JPP/derby derbynet
%add_to_maven_depmap org.apache.derby derbytools %{version} JPP/derby derbytools

mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -p -m 644 %{SOURCE2} \
        $RPM_BUILD_ROOT%{_unitdir}/%{name}.service

mkdir -p $RPM_BUILD_ROOT`dirname /etc/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/%{name}.conf

%pre
getent group derby >/dev/null || groupadd -r derby
getent passwd derby >/dev/null || \
    useradd -r -g derby -d /var/lib/derby -s /sbin/nologin \
    -c "Apache Derby service account" derby
exit 0

%preun
%preun_service derby

%post
%post_service derby

%files
%{_bindir}/*
%{_javadir}/%{name}
%doc db-%{name}-%{version}-src/LICENSE
%doc db-%{name}-%{version}-src/NOTICE
%doc db-%{name}-%{version}-src/published_api_overview.html
%doc db-%{name}-%{version}-src/RELEASE-NOTES.html
%doc db-%{name}-%{version}-src/README
%{_mavenpomdir}/*.pom
%{_mavendepmapfragdir}/%{name}
%{_unitdir}/%{name}.service
%config(noreplace,missingok) /etc/%{name}.conf


%changelog
* Wed Jul 09 2014 Igor Vlasenko <viy@altlinux.ru> 0:10.9.1.0-alt1_2jpp7
- converted from JPackage by jppimport script

* Thu Mar 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:10.6.2.1-alt3_2jpp6
- dropped felix dependency

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:10.6.2.1-alt2_2jpp6
- built with java 6

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:10.6.2.1-alt1_2jpp6
- new version

* Sat Feb 28 2009 Igor Vlasenko <viy@altlinux.ru> 0:10.3.3.0-alt2_1jpp6
- packaged jdbc driver

* Thu Jan 29 2009 Igor Vlasenko <viy@altlinux.ru> 0:10.3.3.0-alt1_1jpp6
- new version

* Wed Nov 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:10.1.1.0-alt2_1jpp1.7
- force build with java4

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:10.1.1.0-alt1_1jpp1.7
- converted from JPackage by jppimport script

