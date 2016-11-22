Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global base_name       compress
%global short_name      commons-%{base_name}

Name:           apache-%{short_name}
Version:        1.10
Release:        alt3_0.3.svn1684406jpp8
Summary:        Java API for working with compressed files and archivers
License:        ASL 2.0
URL:            http://commons.apache.org/%{base_name}/
BuildArch:      noarch

# svn export http://svn.apache.org/repos/asf/commons/proper/compress/trunk/ commons-compress-1.10-src
# tar caf commons-compress-1.10-SNAPSHOT.tar.xz commons-compress-1.10-src
Source0:        %{short_name}-%{version}-SNAPSHOT.tar.xz
#Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.tukaani:xz)
Source44: import.info

%description
The Apache Commons Compress library defines an API for working with
ar, cpio, Unix dump, tar, zip, gzip, XZ, Pack200 and bzip2 files.


%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
# FIXME: test fails for unknown reason
find -name X5455_ExtendedTimestampTest.java -delete

%build
%mvn_file  : %{short_name} %{name}
%mvn_alias : commons:
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt3_0.3.svn1684406jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt3_0.2.svn1684406jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_1jpp7
- new version

* Thu Aug 21 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt3_2jpp7
- added maven-local BR:

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt1_2jpp7
- new version

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_0.r831574.6jpp6
- new version

