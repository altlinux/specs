# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# SVN info
%global svnRev 96

# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

Name:    bindex
Version: 2.2
Release: alt3_7.svn96jpp7
Summary: Bundle Manifest Header Mapper

Group:   Development/Java
License: ASL 2.0
URL:     http://www.osgi.org/Repository/BIndex

# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  svn export -r ${svnRev} \
#    http://www.osgi.org/svn/public/trunk/org.osgi.impl.bundle.bindex \
#    bindex
#  tar -czvf bindex.r${svnRev}.svn.tar.gz bindex
Source0: %{name}.r%{svnRev}.svn.tar.gz

BuildArch: noarch

BuildRequires: ant
BuildRequires: aqute-bnd
BuildRequires: felix-osgi-obr
BuildRequires: felix-osgi-core
BuildRequires: jpackage-utils
BuildRequires: junit4
BuildRequires: kxml

Requires: jpackage-utils
Source44: import.info

%description
A Java program that implements the manifest header to repository 
format mapping as described in the RFC-0112 Bundle Repository.

%prep
%setup -q -n %{name}
find . -type f -iname "*.jar" | xargs -t %__rm -f ;
%__mkdir_p bin

%build
export CLASSPATH=$(build-classpath ant kxml junit \
                                   felix/org.osgi.service.obr \
                                   felix/org.osgi.core)
javac -d bin $(find src -name *.java)
pushd jar
  %__ln_s $(build-classpath ant.jar)
  %__ln_s $(build-classpath kxml.jar) kxml2-min.jar
  %__ln_s $(build-classpath felix/org.osgi.service.obr.jar)
popd
java -jar $(build-classpath aqute-bnd.jar) \
     build -output %{name}-%{version}.jar bindex.bnd

%install
%__install -d -m 0755 %{buildroot}%{_javadir}
%__install -m 644 %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && %__ln_s %{name}-%{version}.jar %{name}.jar)

%files
%doc LICENSE.txt README
%{_javadir}/*

%changelog
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

