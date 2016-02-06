Name: c3p0
Version: 0.9.5
Summary: JDBC DataSources/Resource Pools
License: LGPLv2 or EPL
Url: https://github.com/swaldman/c3p0
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: c3p0 = 0.9.5-0.2.pre8.fc23
Provides: mvn(c3p0:c3p0) = 0.9.5
Provides: mvn(c3p0:c3p0:pom:) = 0.9.5
Provides: mvn(com.mchange:c3p0) = 0.9.5
Provides: mvn(com.mchange:c3p0:pom:) = 0.9.5
Requires: java-headless
Requires: jpackage-utils
Requires: mchange-commons
Requires: mvn(com.mchange:mchange-commons-java)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: c3p0-0.9.5-0.2.pre8.fc23.cpio

%description
c3p0 is an easy-to-use library for augmenting traditional JDBC drivers with
JNDI-bindable DataSources, including DataSources that implement Connection
and Statement Pooling, as described by the jdbc3 spec and jdbc2 standard
extension.

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
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.9.2.1-alt1_4jpp7
- new release

* Sat Aug 02 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.9.2.1-alt1_2jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.2-alt2_0.9.pre1jpp7
- new fc release

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.2-alt2_0.7.pre1jpp7
- fc version

* Thu Jan 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.2-alt1_0.pre1.1jpp6
- converted from JPackage by jppimport script

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.1.2-alt3_2jpp5
- selected java5 compiler explicitly

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.9.1.2-alt2_2jpp5
- fixed docdir ownership

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.1.2-alt1_2jpp5
- converted from JPackage by jppimport script

* Mon Mar 24 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.0-alt2_2jpp1.7
- fixed alternatives intersection

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.9.0-alt1_2jpp1.7
- converted from JPackage by jppimport script

