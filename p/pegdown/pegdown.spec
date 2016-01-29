Name: pegdown
Version: 1.4.2
Summary: Java library for Markdown processing
License: ASL 2.0
Url: http://pegdown.org
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.pegdown:pegdown) = 1.4.2
Provides: mvn(org.pegdown:pegdown:pom:) = 1.4.2
Provides: pegdown = 1.4.2-7.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.parboiled:parboiled-java)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: pegdown-1.4.2-7.fc23.cpio

%description
A pure-Java Markdown processor based on a parboiled PEG parser
supporting a number of extensions.

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
* Mon Jan 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt3_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt3_4jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt3_2jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_2jpp7
- new version

