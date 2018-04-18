# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		java-sleep
Version:	2.1
Release:	alt1_14jpp8
Summary:	Multi-paradigm scripting language for Java

Group:		Development/Other
License:	LGPLv2+ and BSD
URL:		http://sleep.dashnine.org/
Source0:	http://sleep.dashnine.org/download/sleep21-lgpl.tgz
# Patch to allow bootstrapping sleep.jar without sleep-engine.jar
Patch0:		sleep-bootstrap.patch
BuildArch:	noarch

BuildRequires:	jpackage-utils
BuildRequires:	java-devel
BuildRequires:	ant-contrib
Requires:	jpackage-utils
%if 0%{?fedora} >= 20 || 0%{?rhel} >= 7
%else
Requires:	java
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
Requires:	jpackage-utils
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
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_14jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_13jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_12jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_11jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_10jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_6jpp7
- new release

