Epoch: 0
Group: Development/Java
%filter_from_requires /^.usr.bin.run/d
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           derby
Version:        10.11.1.1
Release:        alt2_3jpp8
Summary:        Relational database implemented entirely in Java

License:        ASL 2.0
URL:            http://db.apache.org/derby/
Source0:        http://archive.apache.org/dist/db/derby/db-derby-%{version}/db-derby-%{version}-src.tar.gz
Source1:        derby-script
Source2:        derby.service

# https://issues.apache.org/jira/browse/DERBY-5125
Patch1: derby-javacc5.patch
# For compatibility with lucene >= 4.10
Patch2: derby-lucene.patch

BuildRequires:  apache-parent
BuildRequires:  javapackages-local
BuildRequires:  glassfish-servlet-api
BuildRequires:  jakarta-oro
BuildRequires:  javacc
BuildRequires:  lucene4
BuildRequires:  junit
BuildRequires:  ant
BuildRequires:  systemd
Requires(pre):  shadow-utils

BuildArch:      noarch
Source44: import.info

%description
Apache Derby, an Apache DB sub-project, is a relational database implemented
entirely in Java. Some key advantages include a small footprint, conformance
to Java, JDBC, and SQL standards and embedded JDBC driver.

%package javadoc
Group: Development/Java
Summary: API documentation for derby.
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -c

find -name '*.jar' -delete
find -name '*.class' -delete

pushd db-derby-%{version}-src

rm java/engine/org/apache/derby/impl/sql/compile/Token.java
%patch1 -p0
%patch2 -p0

# Don't use Class-Path in manifests
sed -i -e '/Class-Path/d' build.xml

# Don't download online packagelists
sed -e 's/initjars,set-doclint,install_packagelists/initjars,set-doclint/' \
    -e '/<link offline/,+1d' \
    -i build.xml

popd

%build
cd db-derby-%{version}-src

# tools/ant/properties/extrapath.properties
ln -sf $(build-classpath oro) tools/java/jakarta-oro-2.0.8.jar
ln -sf $(build-classpath glassfish-servlet-api) tools/java/geronimo-spec-servlet-2.4-rc4.jar
ln -sf $(build-classpath javacc) tools/java/javacc.jar
ln -sf $(build-classpath junit) tools/java/junit.jar
ln -sf $(build-classpath lucene4/lucene-core-4) tools/java/lucene-core.jar
ln -sf $(build-classpath lucene4/lucene-analyzers-common-4) tools/java/lucene-analyzers-common.jar
ln -sf $(build-classpath lucene4/lucene-queryparser-4) tools/java/lucene-queryparser.jar

# Fire
ant buildsource buildjars javadoc

# Generate maven poms
find maven2 -name pom.xml | xargs sed -i -e 's|ALPHA_VERSION|%{version}|'

# Request maven installation
%mvn_artifact maven2/pom.xml
for p in engine net client tools \
    derbyLocale_cs derbyLocale_de_DE derbyLocale_es derbyLocale_fr derbyLocale_hu \
    derbyLocale_it derbyLocale_ja_JP derbyLocale_ko_KR derbyLocale_pl derbyLocale_pt_BR \
    derbyLocale_ru derbyLocale_zh_CN derbyLocale_zh_TW ; do
  d=derby${p#derby}
  %mvn_artifact maven2/${p}/pom.xml jars/sane/${d%engine}.jar
done

%install
cd db-derby-%{version}-src

%mvn_install -J javadoc

# Wrapper scripts
install -d $RPM_BUILD_ROOT%{_bindir}
install -p -m755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}-ij
for P in sysinfo NetworkServerControl startNetworkServer stopNetworkServer
do
        ln $RPM_BUILD_ROOT%{_bindir}/%{name}-ij \
                $RPM_BUILD_ROOT%{_bindir}/%{name}-$P
done

# Systemd unit
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -p -m 644 %{SOURCE2} \
        $RPM_BUILD_ROOT%{_unitdir}/%{name}.service

# Derby home dir
install -dm 755 $RPM_BUILD_ROOT/var/lib/derby

mkdir -p $RPM_BUILD_ROOT`dirname /etc/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/%{name}.conf

%pre
getent group derby >/dev/null || groupadd -r derby
getent passwd derby >/dev/null || \
    useradd -r -g derby -d /var/lib/derby -s /sbin/nologin \
    -c "Apache Derby service account" derby
exit 0

%post
%post_service derby

%preun
%preun_service derby

%files -f  db-derby-%{version}-src/.mfiles
%{_bindir}/*
%doc db-%{name}-%{version}-src/published_api_overview.html
%doc db-%{name}-%{version}-src/RELEASE-NOTES.html
%doc db-%{name}-%{version}-src/README
%{_unitdir}/%{name}.service
%attr(755,derby,derby) %{_sharedstatedir}/%{name}
%doc db-derby-%{version}-src/LICENSE
%doc db-derby-%{version}-src/NOTICE
%config(noreplace,missingok) /etc/%{name}.conf

%files javadoc -f db-derby-%{version}-src/.mfiles-javadoc
%doc db-derby-%{version}-src/LICENSE
%doc db-derby-%{version}-src/NOTICE

%changelog
* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 0:10.11.1.1-alt2_3jpp8
- unbootstrap build

* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 0:10.11.1.1-alt1_3jpp8
- unbootstrap build

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0:10.11.1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sun Sep 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:10.9.1.0-alt1_6jpp7
- new release

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

