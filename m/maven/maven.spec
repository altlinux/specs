Name: maven
Version: 3.0.4
Summary: Java project management and project comprehension tool
License: ASL 2.0 and MIT and BSD
Url: http://maven.apache.org/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven2
Provides: /etc/mavenrc
Requires: aether
Requires: animal-sniffer
Requires: apache-commons-cli
Requires: apache-commons-parent
Requires: async-http-client
Requires: atinject
Requires: google-guice
Requires: guava
Requires: hamcrest
Requires: java
Requires: maven-parent
Requires: maven-wagon
Requires: maven2-common-poms
Requires: mojo-parent
Requires: nekohtml
Requires: plexus-cipher
Requires: plexus-classworlds
Requires: plexus-containers-component-annotations
Requires: plexus-containers-container-default
Requires: plexus-interpolation
Requires: plexus-sec-dispatcher
Requires: plexus-utils
Requires: sisu
Requires: sonatype-oss-parent
Requires: xbean
Requires: xerces-j2

BuildArch: noarch
Group: Development/Java
Release: alt4jpp
Source: maven-3.0.4-21.fc18.cpio

%description
Maven is a software project management and comprehension tool. Based on the
concept of a project object model (POM), Maven can manage a project's build,
reporting and documentation from a central piece of information.

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



%files -f %name-list

%changelog
* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.4-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

%changelog
* Wed Oct 10 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0.4-alt3_10jpp7
- fix for upgrade from 5.1 (closes: #27807)

* Fri Sep 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0.4-alt2_10jpp7
- restored requires: apache-commons-parent

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0.4-alt1_10jpp7
- complete build

* Wed Aug 22 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0.4-alt0.4jpp
- require maven-filesystem; now noarch

* Thu Jun 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0.4-alt0.3jpp
- restored mvn

* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0.4-alt0.2jpp
- use system atinject

* Sat Mar 03 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0.4-alt0.1jpp
- bootstrap maven3 package
