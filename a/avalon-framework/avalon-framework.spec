Name: avalon-framework
Version: 4.3
Summary: Java components interfaces
License: ASL 2.0
Url: http://avalon.apache.org/framework/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: avalon-framework = 0:4.3-14.fc23
Provides: mvn(avalon-framework:avalon-framework) = 4.3
Provides: mvn(avalon-framework:avalon-framework-api) = 4.3
Provides: mvn(avalon-framework:avalon-framework-api:pom:) = 4.3
Provides: mvn(avalon-framework:avalon-framework-impl) = 4.3
Provides: mvn(avalon-framework:avalon-framework-impl:pom:) = 4.3
Provides: mvn(avalon-framework:avalon-framework:pom:) = 4.3
Provides: mvn(org.apache.avalon.framework:avalon-framework-api) = 4.3
Provides: mvn(org.apache.avalon.framework:avalon-framework-api:pom:) = 4.3
Provides: mvn(org.apache.avalon.framework:avalon-framework-impl) = 4.3
Provides: mvn(org.apache.avalon.framework:avalon-framework-impl:pom:) = 4.3
Requires: apache-commons-logging
Requires: avalon-logkit
Requires: java-headless
Requires: jpackage-utils
Requires: log4j
Requires: xalan-j2

BuildArch: noarch
Group: Development/Java
Release: alt3jpp
Source: avalon-framework-4.3-14.fc23.cpio

%description
The Avalon framework consists of interfaces that define relationships
between commonly used application components, best-of-practice pattern
enforcements, and several lightweight convenience implementations of the
generic components.
What that means is that we define the central interface Component. We
also define the relationship (contract) a component has with peers,
ancestors and children.

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
* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt2_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt2_8jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt1_7jpp7
- new release

* Tue May 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt1_5jpp7
- fc build

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.1.5-alt3_2jpp5
- fixed build with moved maven1

* Sun Feb 20 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.1.5-alt2_2jpp5
- fixed build

* Sat Jan 24 2009 Igor Vlasenko <viy@altlinux.ru> 0:4.1.5-alt1_2jpp5
- restored in separate package due to repolib

