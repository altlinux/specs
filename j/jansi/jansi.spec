Name: jansi
Version: 1.11
Summary: Jansi is a java library for generating and interpreting ANSI escape sequences
License: ASL 2.0
Url: http://jansi.fusesource.org/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jansi = 1.11-9.fc23
Provides: mvn(org.fusesource.jansi:jansi) = 1.11
Provides: mvn(org.fusesource.jansi:jansi-project:pom:) = 1.11
Provides: mvn(org.fusesource.jansi:jansi:pom:) = 1.11
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.fusesource.hawtjni:hawtjni-runtime)
Requires: mvn(org.fusesource.jansi:jansi-native)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jansi-1.11-9.fc23.cpio

%description
Jansi is a small java library that allows you to use ANSI escape sequences
in your Java console applications. It implements ANSI support on platforms
which don't support it like Windows and provides graceful degradation for
when output is being sent to output devices which cannot support ANSI sequences.

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
ln -s jansi/jansi.jar %buildroot/usr/share/java/jansi.jar

%files -f %name-list
/usr/share/java/jansi.jar

%changelog
* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.11-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt1_3jpp7
- new release

* Thu Oct 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt1_1jpp7
- new release

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt3_4jpp7
- added Requires: fusesource-pom

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_4jpp7
- added jansi:jansi depmap for jpp packages

* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_2jpp7
- fixed pom

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_2jpp7
- fc version

* Sat Feb 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_1jpp6
- new version

