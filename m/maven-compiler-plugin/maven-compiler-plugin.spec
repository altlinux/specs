Name: maven-compiler-plugin
Version: 3.0
Summary: Maven Compiler Plugin
License: ASL 2.0
Url: http://maven.apache.org/plugins/maven-compiler-plugin
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven2-plugin-compiler
Requires: java
Requires: maven-shared-incremental maven-shared-utils plexus-compiler

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-compiler-plugin-3.0-2.fc19.cpio

%description
The Compiler Plugin is used to compile the sources of your project.

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
* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 3.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.1-alt3_2jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.1-alt2_2jpp7
- fixed build

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 2.5.1-alt1_2jpp7
- new release

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1_5jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

