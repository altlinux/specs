
# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none

Name: xmvn-connector-ivy
Version: 3.1.0
Summary: XMvn Connector for Apache Ivy
License: ASL 2.0
Url: https://fedora-java.github.io/xmvn/
Group: Development/Java
Release: alt0.1jpp

Packager: Igor Vlasenko <viy@altlinux.org>
Provides: mvn(org.fedoraproject.xmvn:xmvn-connector-ivy) = 3.1.0
Provides: mvn(org.fedoraproject.xmvn:xmvn-connector-ivy:pom:) = 3.1.0
Requires: javapackages-filesystem
Requires: mvn(org.fedoraproject.xmvn:xmvn-api)
Requires: mvn(org.slf4j:slf4j-api)

BuildArch: noarch
Source: xmvn-connector-ivy-3.1.0-2.fc32.cpio


%description
This package provides XMvn Connector for Apache Ivy, which provides
integration of Apache Ivy with XMvn.  It provides an adapter which
allows XMvn resolver to be used as Ivy resolver.

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
* Thu May 27 2021 Igor Vlasenko <viy@altlinux.org> 3.1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu May 13 2021 Igor Vlasenko <viy@altlinux.org> 3.0.0-alt2_26jpp8
- build w/o gradle

* Sun May 09 2021 Igor Vlasenko <viy@altlinux.org> 3.0.0-alt1_26jpp8
- update

* Mon Jul 15 2019 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_23jpp8
- build with new gradle

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_21jpp8
- new version

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_18jpp8
- java fc28+ update

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_14jpp8
- support for maven-javadoc-plugin-3.0.0

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_8jpp8
- support for gradle 4.3
- no support for maven-javadoc-plugin >= 3.0.0 yet

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_7jpp8
- rebuild with guava20

* Tue Nov 21 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_6jpp8
- new version (unbootstrap build)

* Tue Nov 21 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Oct 30 2017 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_21jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_11jpp8
- new fc release

* Fri Dec 09 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_6jpp8
- unbootstrup build

* Fri Dec 09 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt1_5jpp8
- unbootsrap build

* Tue Jan 19 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt4_4jpp7
- rebuild to update symlinks

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt3_4jpp7
- fixed bin
- nobootstrap build

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_5jpp7
- nobootstrap build

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Mar 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

