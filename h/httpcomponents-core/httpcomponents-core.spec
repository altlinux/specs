Name: httpcomponents-core
Version: 4.4.1
Summary: Set of low level Java HTTP transport components for HTTP services
License: ASL 2.0 and CC-BY
Url: http://hc.apache.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: httpcomponents-core = 4.4.1-2.fc23
Provides: mvn(org.apache.httpcomponents:httpcomponents-core:pom:) = 4.4.1
Provides: mvn(org.apache.httpcomponents:httpcore) = 4.4.1
Provides: mvn(org.apache.httpcomponents:httpcore-nio) = 4.4.1
Provides: mvn(org.apache.httpcomponents:httpcore-nio:pom:) = 4.4.1
Provides: mvn(org.apache.httpcomponents:httpcore:pom:) = 4.4.1
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: httpcomponents-core-4.4.1-2.fc23.cpio

%description
HttpCore is a set of low level HTTP transport components that can be
used to build custom client and server side HTTP services with a
minimal footprint. HttpCore supports two I/O models: blocking I/O
model based on the classic Java I/O and non-blocking, event driven I/O
model based on Java NIO.

The blocking I/O model may be more appropriate for data intensive, low
latency scenarios, whereas the non-blocking model may be more
appropriate for high latency scenarios where raw data throughput is
less important than the ability to handle thousands of simultaneous
HTTP connections in a resource efficient manner.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 4.4.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.4-alt1_5jpp7
- new release

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.4-alt1_3jpp7
- new version

* Thu Aug 21 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.2-alt2_1jpp7
- added maven-local BR:

* Thu Oct 11 2012 Igor Vlasenko <viy@altlinux.ru> 4.2.2-alt1_1jpp7
- new release

* Sat Sep 08 2012 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt1_3jpp7
- new version

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt1_2jpp7
- full version

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

