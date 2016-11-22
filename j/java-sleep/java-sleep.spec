# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
Name:		java-sleep
Version:	2.1
Release:	alt1_11jpp8
Summary:	Multi-paradigm scripting language for Java

Group:		Development/Other
License:	LGPLv2+ and BSD
URL:		http://sleep.dashnine.org/
Source0:	http://sleep.dashnine.org/download/sleep21-lgpl.tgz
# Patch to allow bootstrapping sleep.jar without sleep-engine.jar
Patch0:		sleep-bootstrap.patch
BuildArch:	noarch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:	ant-contrib
Requires: javapackages-tools rpm-build-java
%if 0%{?fedora} >= 20 || 0%{?rhel} >= 7
%else
%endif
Source44: import.info

%description
Sleep ...

 - is a multi-paradigm scripting language for the Java Platform
 - easy to learn with Perl and Objective-C inspired syntax
 - executes scripts fast with a small package size (~250KB)
 - excels at data manipulation, component integration, and distributed
   communication
 - seamlessly uses Java objects and 3rd party libraries


%package javadoc
Summary:	Javadocs for %{name}
Group:		Development/Java
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n sleep
%patch0 -p1 -b .bootstrap
find -name \*.jar -delete
sed -i -e 's/\r//' *.txt
# Fix FSF address
sed -i -e 's/59 Temple Place, Suite 330/51 Franklin Street, Fifth Floor/' \
       -e 's/MA  02111-1307/MA  02110-1301/' license.txt


%build
# Build without sleep-engine components
ant -Dbootstrap=true
# Build sleep-engine.jar
ant -f jsr223/build.xml
# Build in the sleep-engine components
ant
# Build the test data jars
ant -f tests/data/build.xml
ant -f tests/data2/build.xml
ant -f tests/data3/build.xml
# Build docs
ant docs


%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p sleep.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}.jar $RPM_BUILD_ROOT%{_javadir}/sleep.jar
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
mv docs/api docs_api
cp -rp docs_api $RPM_BUILD_ROOT%{_javadocdir}/%{name}/api


%check
java -jar sleep.jar runtests.sl


%files
%doc *.txt docs
%{_javadir}/%{name}.jar
%{_javadir}/sleep.jar


%files javadoc
%{_javadocdir}/%{name}


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_11jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_10jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_6jpp7
- new release

