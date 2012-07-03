Name: maven-shade-plugin
Version: 1.5
Summary: This plugin provides the capability to package the artifact in an uber-jar
License: ASL 2.0
Url: http://maven.apache.org/plugins/maven-shade-plugin
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven2-plugin-shade
Requires: ant
Requires: java
Requires: jdependency
Requires: jpackage-utils
Requires: maven

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: maven-shade-plugin-1.5-2.fc17.cpio

%description
This plugin provides the capability to package the artifact in an
uber-jar, including its dependencies and to shade - i.e. rename - the
packages of some of the dependencies.

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
* Thu Apr 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2jpp
- reverted to bootstrap pack due to regression

* Tue Apr 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_2jpp7
- complete build

* Tue Mar 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

