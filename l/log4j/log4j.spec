Name: log4j
Version: 2.3
Summary: Java logging package
License: ASL 2.0
Url: http://logging.apache.org/log4j
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: log4j = 2.3-2.fc23
Provides: mvn(log4j:log4j) = 2.3
Provides: mvn(log4j:log4j:pom:) = 2.3
Provides: mvn(org.apache.logging.log4j:log4j-1.2-api) = 2.3
Provides: mvn(org.apache.logging.log4j:log4j-1.2-api:pom:) = 2.3
Provides: mvn(org.apache.logging.log4j:log4j-api) = 2.3
Provides: mvn(org.apache.logging.log4j:log4j-api:pom:) = 2.3
Provides: mvn(org.apache.logging.log4j:log4j-core) = 2.3
Provides: mvn(org.apache.logging.log4j:log4j-core:pom:) = 2.3
Provides: mvn(org.apache.logging.log4j:log4j-iostreams) = 2.3
Provides: mvn(org.apache.logging.log4j:log4j-iostreams:pom:) = 2.3
Provides: mvn(org.apache.logging.log4j:log4j-jul) = 2.3
Provides: mvn(org.apache.logging.log4j:log4j-jul:pom:) = 2.3
Provides: mvn(org.apache.logging.log4j:log4j:pom:) = 2.3
Requires: /bin/sh
Requires: /bin/sh
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: log4j-2.3-2.fc23.cpio

%description
Log4j is a tool to help the programmer output log statements to a
variety of output targets.

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none
%prep
cpio -idmu --quiet --no-absolute-filenames < %{SOURCE0}

%build
cpio --list < %{SOURCE0} | sed -e 's,^\.,,' > %name-list

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done

%preun
if [ $1 -eq 0 ]; then
  if [ -x xmlcatalog -a -w /etc/xml/catalog ]; then
    xmlcatalog --noout --del \
      file:///usr/share/sgml/log4j/log4j.dtd \
      /etc/xml/catalog > /dev/null || :
  fi
fi

# TODO: Remove this in F-24

%postun
# Note that we're using versioned catalog, so this is always ok.
if [ -x install-catalog -a -d /etc/sgml ]; then
  install-catalog --remove \
    /etc/sgml/log4j-2.3-2.fc23.cat \
    /usr/share/sgml/log4j/catalog > /dev/null || :
fi


%files -f %name-list

%changelog
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.17-alt4_14jpp7
- new release

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

