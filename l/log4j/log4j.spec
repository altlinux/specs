# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
%filter_from_requires /^.usr.bin.run/d
BuildRequires: /proc
BuildRequires: jpackage-compat

%global bootstrap %{?_with_bootstrap:1}%{!?_with_bootstrap:%{?_without_bootstrap:0}%{!?_without_bootstrap:%{?_bootstrap:%{_bootstrap}}%{!?_bootstrap:0}}}

Name:           log4j
Version:        1.2.17
Release:        alt4_10jpp7
Epoch:          0
Summary:        Java logging package
BuildArch:      noarch
License:        ASL 2.0
Group:          Development/Java
URL:            http://logging.apache.org/%{name}
Source0:        http://www.apache.org/dist/logging/%{name}/%{version}/%{name}-%{version}.tar.gz
# Converted from src/java/org/apache/log4j/lf5/viewer/images/lf5_small_icon.gif
Source101:      %{name}-logfactor5.png
Source102:      %{name}-logfactor5.sh
Source103:      %{name}-logfactor5.desktop
Source104:      %{name}-logfactor5.1
# Converted from docs/images/logo.jpg
Source111:      %{name}-chainsaw.png
Source112:      %{name}-chainsaw.sh
Source113:      %{name}-chainsaw.desktop
Source114:      %{name}-chainsaw.1
Source200:      %{name}.catalog
Patch0:         0001-logfactor5-changed-userdir.patch
Patch1:         0006-Remove-mvn-clirr-plugin.patch
Patch2:         0009-Remove-ant-run-of-tests.patch
Patch3:         0010-Fix-javadoc-link.patch
Patch4:         0011-Remove-openejb.patch
Patch5:         0012-Add-proper-bundle-symbolicname.patch

BuildRequires:  maven-local
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
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-idea-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  ant-junit
BuildRequires:  ant-contrib
Source44: import.info


%description
Log4j is a tool to help the programmer output log statements to a
variety of output targets.

%package        manual
Summary:        Developer manual for %{name}
Group:          Development/Java
Requires:       %{name}-javadoc = %{version}-%{release}
BuildArch: noarch

%description    manual
%{summary}.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
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
%pom_remove_plugin :maven-site-plugin

sed -i "s|groupId>ant<|groupId>org.apache.ant<|g" pom.xml

sed -i 's/\r//g' LICENSE NOTICE site/css/*.css site/xref/*.css \
    site/xref-test/*.css

# fix encoding of mailbox files
for i in contribs/JimMoore/mail*;do
    iconv --from=ISO-8859-1 --to=UTF-8 "$i" > new
    mv new "$i"
done

# remove all the stuff we'll build ourselves
find -name "*.jar" -o -name "*.class" -delete
rm -rf docs/api


%build
%mvn_file : %{name}
%mvn_build -f

%install
%mvn_install

# scripts
install -pD -T -m 755 %{SOURCE102} %{buildroot}%{_bindir}/logfactor5
install -pD -T -m 755 %{SOURCE112} %{buildroot}%{_bindir}/chainsaw

# freedesktop.org menu entries and icons
install -pD -T -m 644 %{SOURCE101} \
        %{buildroot}%{_datadir}/pixmaps/logfactor5.png
desktop-file-install \
     --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
     %{SOURCE103}

install -pD -T -m 644 %{SOURCE111} \
        %{buildroot}%{_datadir}/pixmaps/chainsaw.png
desktop-file-install \
     --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
     %{SOURCE113}

# Manual pages
install -d -m 755 ${RPM_BUILD_ROOT}%{_mandir}/man1
install -p -m 644 %{SOURCE104} ${RPM_BUILD_ROOT}%{_mandir}/man1/logfactor5.1
install -p -m 644 %{SOURCE114} ${RPM_BUILD_ROOT}%{_mandir}/man1/chainsaw.1

# DTD and the SGML catalog (XML catalog handled in scriptlets)
install -pD -T -m 644 src/main/javadoc/org/apache/log4j/xml/doc-files/log4j.dtd \
  %{buildroot}%{_datadir}/sgml/%{name}/log4j.dtd
install -pD -T -m 644 %{SOURCE200} \
  %{buildroot}%{_datadir}/sgml/%{name}/catalog

# fix perl location
%__perl -p -i -e 's|/opt/perl5/bin/perl|%{__perl}|' \
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

%files -f .mfiles
%doc LICENSE NOTICE
%{_bindir}/*
%{_mandir}/*/*
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
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.17-alt4_10jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.17-alt4_3jpp7
- rebuild with maven-local

* Tue Jul 22 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.17-alt3_3jpp7
- osgi fix

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

