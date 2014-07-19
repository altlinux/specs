Name: maven-plugin-tools
Version: 3.1
Summary: Maven Plugin Tools
License: ASL 2.0
Url: http://maven.apache.org/plugin-tools/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: java
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-plugin-tools-3.1-5.fc18.cpio

%description
The Maven Plugin Tools contains the necessary tools to be able to produce Maven
Plugins in a variety of languages.

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
* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

%changelog
* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.7-alt2_6jpp7
- fixed build

* Fri Sep 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.7-alt1_6jpp7
- new version

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.7-alt1_5jpp7
- new release; added org.apache.maven:maven-plugin-tools-api

* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.7-alt1_4jpp7
- complete build

* Sun Mar 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.7-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

