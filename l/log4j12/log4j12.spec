Name: log4j12
Version: 1.2.17
Summary: Java logging package
License: ASL 2.0
Url: http://logging.apache.org/log4j/1.2/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: log4j12 = 1.2.17-10.fc23
Provides: mvn(log4j:log4j:1.2.12) = 1.2.17
Provides: mvn(log4j:log4j:1.2.17) = 1.2.17
Provides: mvn(log4j:log4j:12) = 1.2.17
Provides: mvn(log4j:log4j:pom:1.2.12) = 1.2.17
Provides: mvn(log4j:log4j:pom:1.2.17) = 1.2.17
Provides: mvn(log4j:log4j:pom:12) = 1.2.17
Requires: /bin/sh
Requires: /bin/sh
Requires: /bin/sh
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: log4j12-1.2.17-10.fc23.cpio

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
  if [ -x /usr/bin/xmlcatalog -a -w /etc/xml/catalog ]; then
    /usr/bin/xmlcatalog --noout --del \
      file:///usr/share/sgml/log4j/log4j.dtd \
      /etc/xml/catalog > /dev/null || :
  fi
fi

%post
# Note that we're using versioned catalog, so this is always ok.
if [ -x /usr/bin/install-catalog -a -d /etc/sgml ]; then
  /usr/bin/install-catalog --add \
    /etc/sgml/log4j-1.2.17-10.fc23.cat \
    /usr/share/sgml/log4j/catalog > /dev/null || :
fi
if [ -x /usr/bin/xmlcatalog -a -w /etc/xml/catalog ]; then
  /usr/bin/xmlcatalog --noout --add public "-//APACHE//DTD LOG4J 1.2//EN" \
    file:///usr/share/sgml/log4j/log4j.dtd /etc/xml/catalog \
    > /dev/null
  /usr/bin/xmlcatalog --noout --add system log4j.dtd \
    file:///usr/share/sgml/log4j/log4j.dtd /etc/xml/catalog \
    > /dev/null || :
fi

%postun
# Note that we're using versioned catalog, so this is always ok.
if [ -x /usr/bin/install-catalog -a -d /etc/sgml ]; then
  /usr/bin/install-catalog --remove \
    /etc/sgml/log4j-1.2.17-10.fc23.cat \
    /usr/share/sgml/log4j/catalog > /dev/null || :
fi


%files -f %name-list

%changelog
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.17-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

