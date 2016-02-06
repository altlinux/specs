Name: antlr3-java-bootstrap
Version: 3.5.2
Summary: Java run-time support for ANTLR-generated parsers
License: BSD
Url: http://www.antlr3.org/
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: antlr3-java = 1:3.5.2-9.fc23
Provides: mvn(org.antlr:antlr-runtime) = 3.5.2
Provides: mvn(org.antlr:antlr-runtime:pom:) = 3.5.2
Requires: java-headless
Requires: jpackage-utils
Obsoletes: antlr3-java < 3.5.2

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: antlr3-java-3.5.2-9.fc23.cpio

%description
Java run-time support for ANTLR-generated parsers

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
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.5.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Jul 31 2014 Igor Vlasenko <viy@altlinux.ru> 3.4-alt3_14jpp7
- new release

* Thu Jul 17 2014 Igor Vlasenko <viy@altlinux.ru> 3.4-alt3_12jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 3.4-alt2_12jpp7
- NMU rebuild to move poms and fragments

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 3.4-alt1_12jpp7
- fixed requires for antlr3-java

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 3.4-alt1_11jpp7
- new version

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1_10jpp6
- new jpp relase

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1_9jpp6
- new version

