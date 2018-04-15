# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# SVN info
%global svnRev 96

# Prevent brp-java-repack-jars from being run.
%global __jar_repack %{nil}

Name:    bindex
Version: 2.2
Release: alt3_18.svn96jpp8
Summary: Bundle Manifest Header Mapper

Group:   Development/Other
License: ASL 2.0
URL:     http://www.osgi.org/Repository/BIndex

# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  svn export -r ${svnRev} \
#    http://www.osgi.org/svn/public/trunk/org.osgi.impl.bundle.bindex \
#    bindex
#  tar -czvf bindex.r${svnRev}.svn.tar.gz bindex
Source0: %{name}.r%{svnRev}.svn.tar.gz
Patch0: add-classpath.patch

BuildArch: noarch

BuildRequires: ant
BuildRequires: aqute-bnd
BuildRequires: felix-osgi-obr
BuildRequires: felix-osgi-core
BuildRequires: java-devel >= 1.6.0
BuildRequires: junit
BuildRequires: kxml
BuildRequires: xpp3

Requires: javapackages-tools
Source44: import.info

%description
A Java program that implements the manifest header to repository 
format mapping as described in the RFC-0112 Bundle Repository.

%prep
%setup -q -n %{name}
find . -type f -iname "*.jar" | xargs -t rm -f ;
mkdir -p bin
%patch0 -p1

%build
export CLASSPATH=$(build-classpath ant kxml junit xpp3 \
                                   felix/org.osgi.service.obr \
                                   felix/org.osgi.core)
javac -d bin $(find src -name *.java)
pushd jar
  ln -s $(build-classpath ant.jar)
  ln -s $(build-classpath kxml.jar) kxml2-min.jar
  ln -s $(build-classpath felix/org.osgi.service.obr.jar)
  ln -s $(build-classpath xpp3.jar)
popd
bnd buildx --output %{name}.jar bindex.bnd

%install
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 %{name}.jar %{buildroot}%{_javadir}/%{name}.jar

%files
%doc README
%doc --no-dereference LICENSE.txt
%{_javadir}/*

%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_18.svn96jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_17.svn96jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_16.svn96jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_15.svn96jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_14.svn96jpp8
- java8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_8.svn96jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_7.svn96jpp7
- new release

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_6.svn96jpp7
- added jpp compatible symlink

* Thu Mar 29 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_1jpp6
- dropped felix dependency

* Wed Jan 18 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_1jpp6
- added felix-osgi-obr dep

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_1jpp6
- new version

