# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat

%global bootstrap %{?_with_bootstrap:1}%{!?_with_bootstrap:%{?_without_bootstrap:0}%{!?_without_bootstrap:%{?_bootstrap:%{_bootstrap}}%{!?_bootstrap:0}}}

Name:           log4j
Version:        1.2.17
Release:        alt2_3jpp7
Epoch:          0
Summary:        Java logging package
BuildArch:      noarch
License:        ASL 2.0
Group:          Development/Java
URL:            http://logging.apache.org/%{name}
Source0:        http://www.apache.org/dist/logging/%{name}/%{version}/%{name}-%{version}.tar.gz
# Converted from src/java/org/apache/log4j/lf5/viewer/images/lf5_small_icon.gif
Source1:        %{name}-logfactor5.png
Source2:        %{name}-logfactor5.sh
Source3:        %{name}-logfactor5.desktop
# Converted from docs/images/logo.jpg
Source4:        %{name}-chainsaw.png
Source5:        %{name}-chainsaw.sh
Source6:        %{name}-chainsaw.desktop
Source7:        %{name}.catalog
Patch0:         0001-logfactor5-changed-userdir.patch
Patch1:         0006-Remove-mvn-clirr-plugin.patch
Patch2:         0009-Remove-ant-run-of-tests.patch
Patch3:         0010-Fix-javadoc-link.patch
Patch4:         0011-Remove-openejb.patch
Patch5:         0012-Add-proper-bundle-symbolicname.patch

BuildRequires:  %{__perl}
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  javamail
BuildRequires:  geronimo-jms
BuildRequires:  geronimo-parent-poms
BuildRequires:  desktop-file-utils
BuildRequires:  jpackage-utils >= 0:1.7.2
BuildRequires:  maven-plugin-bundle
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-ant-plugin
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-changes-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-idea-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-skins
BuildRequires:  ant-junit
BuildRequires:  ant-contrib

Requires:       jpackage-utils >= 0:1.6
Source44: import.info

%description
Log4j is a tool to help the programmer output log statements to a
variety of output targets.

%package        manual
Summary:        Developer manual for %{name}
Group:          Development/Java
Requires:       %{name}-javadoc = %{?epoch:%epoch:}%{version}-%{release}
BuildArch: noarch

%description    manual
%{summary}.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n apache-%{name}-%{version}
# see patch files themselves for reasons for applying
%patch0 -p1 -b .logfactor-home
%patch1 -p1 -b .remove-mvn-clirr
%patch2 -p1 -b .remove-tests
%patch3 -p1 -b .xlink-javadoc
%patch4 -p1 -b .openejb
%patch5 -p1 -b .bundlename

sed -i "s|groupId>ant<|groupId>org.apache.ant<|g" pom.xml

sed -i 's/\r//g' LICENSE NOTICE site/css/*.css site/xref/*.css \
    site/xref-test/*.css

# fix encoding of mailbox files
for i in contribs/JimMoore/mail*;do
    iconv --from=ISO-8859-1 --to=UTF-8 "$i" > new
    mv new "$i"
done

# remove all the stuff we'll build ourselves
find . \( -name "*.jar" -o -name "*.class" \) -exec rm -f {} \;
rm -rf docs/api



%build
# we don't need javadoc:javadoc because build system is broken and
# builds javadoc when install-ing
# also note that maven.test.skip doesn't really work and we had to
# patch ant run of tests out of pom
mvn-rpmbuild verify

%install
# jars
#install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pD -T -m 644 target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# scripts
install -pD -T -m 755 %{SOURCE2} %{buildroot}%{_bindir}/logfactor5
install -pD -T -m 755 %{SOURCE5} %{buildroot}%{_bindir}/chainsaw

# freedesktop.org menu entries and icons
install -pD -T -m 644 %{SOURCE1} \
        %{buildroot}%{_datadir}/pixmaps/logfactor5.png
desktop-file-install \
     --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
     %{SOURCE3}

install -pD -T -m 644 %{SOURCE4} \
        %{buildroot}%{_datadir}/pixmaps/chainsaw.png
desktop-file-install \
     --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
     %{SOURCE6}


# DTD and the SGML catalog (XML catalog handled in scriptlets)
install -pD -T -m 644 src/main/javadoc/org/apache/log4j/xml/doc-files/log4j.dtd \
  %{buildroot}%{_datadir}/sgml/%{name}/log4j.dtd
install -pD -T -m 644 %{SOURCE7} \
  %{buildroot}%{_datadir}/sgml/%{name}/catalog

# fix perl location
perl -p -i -e 's|/opt/perl5/bin/perl|%{__perl}|' \
contribs/KitchingSimon/udpserver.pl

mkdir -p $RPM_BUILD_ROOT`dirname /etc/chainsaw.conf`
touch $RPM_BUILD_ROOT/etc/chainsaw.conf


%post
if [ -x %{_bindir}/install-catalog -a -d %{_sysconfdir}/sgml ]; then
  %{_bindir}/install-catalog --add \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{_datadir}/sgml/%{name}/catalog > /dev/null || :
fi
if [ -x %{_bindir}/xmlcatalog -a -w %{_sysconfdir}/xml/catalog ]; then
  %{_bindir}/xmlcatalog --noout --add system log4j.dtd \
    file://%{_datadir}/sgml/%{name}/log4j.dtd %{_sysconfdir}/xml/catalog \
    > /dev/null || :
fi


%preun
if [ $1 -eq 0 ]; then
  if [ -x %{_bindir}/xmlcatalog -a -w %{_sysconfdir}/xml/catalog ]; then
    %{_bindir}/xmlcatalog --noout --del log4j.dtd \
      %{_sysconfdir}/xml/catalog > /dev/null || :
  fi
fi


%postun
if [ -x %{_bindir}/install-catalog -a -d %{_sysconfdir}/sgml ]; then
  %{_bindir}/install-catalog --remove \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{_datadir}/sgml/%{name}/catalog > /dev/null || :
fi

%files
%doc LICENSE NOTICE
%{_bindir}/*
%{_javadir}/*
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/sgml/%{name}
%config(noreplace,missingok) /etc/chainsaw.conf

%files manual
%doc LICENSE NOTICE
%doc site/*.html site/css site/images/ site/xref site/xref-test contribs

%files javadoc
%doc LICENSE NOTICE
%doc %{_javadocdir}/%{name}


%changelog
* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.2.17-alt2_3jpp7
- applied repocop patches

* Sun Sep 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.17-alt1_3jpp7
- fc release

* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.15-alt2_7jpp6
- fixed repolib

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.15-alt1_7jpp6
- new version

* Sun Mar 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.14-alt8_15jpp5
- fixed missing org.apache.log4j.jmx

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.14-alt7_15jpp5
- new version

* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.14-alt7_4jpp5
- fixed missing org.apache.log4j.jmx

* Mon Nov 17 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.14-alt6_4jpp5
- removed obsolete update_menus

