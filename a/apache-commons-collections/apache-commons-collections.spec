Name: apache-commons-collections
Version: 3.2.1
Summary: Provides new interfaces, implementations and utilities for Java Collections
License: ASL 2.0
Url: http://commons.apache.org/collections/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: apache-commons-collections = 3.2.1-26.fc23
Provides: mvn(commons-collections:commons-collections) = 3.2.1
Provides: mvn(commons-collections:commons-collections:pom:) = 3.2.1
Provides: mvn(org.apache.commons:commons-collections) = 3.2.1
Provides: mvn(org.apache.commons:commons-collections:pom:) = 3.2.1
Requires: java-headless
Requires: java-headless
Requires: jpackage-utils
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt9jpp
Source: apache-commons-collections-3.2.1-26.fc23.cpio

%description
The introduction of the Collections API by Sun in JDK 1.2 has been a
boon to quick and effective Java programming. Ready access to powerful
data structures has accelerated development by reducing the need for
custom container classes around each core object. Most Java2 APIs are
significantly easier to use because of the Collections API.
However, there are certain holes left unfilled by Sun's
implementations, and the Jakarta-Commons Collections Component strives
to fulfill them. Among the features of this package are:
- special-purpose implementations of Lists and Maps for fast access
- adapter classes from Java1-style containers (arrays, enumerations) to
Java2-style collections.
- methods to test or create typical set-theory properties of collections
such as union, intersection, and closure.

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt9jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt8_19jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt8_16jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt8_14jpp7
- fc update

* Thu Mar 07 2013 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt8_6jpp6
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt7_6jpp6
- fixed build with new svgsalamander

* Sat Sep 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt6_6jpp6
- fixed build with lucene3

* Sat Jan 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt5_6jpp6
- new jpp relase

* Tue Jan 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt5_5jpp6
- fixed conflicts/obsoletes (closes: #24858)

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt4_5jpp6
- fixed repolib id

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt3_5jpp6
- fixed repolib

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt2_5jpp6
- add obsoletes

* Sat Jan 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt1_5jpp6
- new version

