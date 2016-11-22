# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# SVN info
%global svnRev 96

# Prevent brp-java-repack-jars from being run.
%global __jar_repack %{nil}

Name:    bindex
Version: 2.2
Release: alt3_15.svn96jpp8
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
BuildRequires: junit
BuildRequires: kxml
BuildRequires: xpp3

Source44: import.info

%description
A Java program that implements the manifest header to repository 
format mapping as described in the RFC-0112 Bundle Repository.

%prep
%setup -q -n %{name}
find . -type f -iname "*.jar" | xargs -t %__rm -f ;
%__mkdir_p bin
%patch0 -p1

%build
export CLASSPATH=$(build-classpath ant kxml junit xpp3 \
                                   felix/org.osgi.service.obr \
                                   felix/org.osgi.core)
javac -d bin $(find src -name *.java)
pushd jar
  %__ln_s $(build-classpath ant.jar)
  %__ln_s $(build-classpath kxml.jar) kxml2-min.jar
  %__ln_s $(build-classpath felix/org.osgi.service.obr.jar)
  %__ln_s $(build-classpath xpp3.jar)
popd
bnd buildx --output %{name}.jar bindex.bnd

%install
%__install -d -m 0755 %{buildroot}%{_javadir}
%__install -m 644 %{name}.jar %{buildroot}%{_javadir}/%{name}.jar

%files
%doc README
%doc LICENSE.txt
%{_javadir}/*

%changelog
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

