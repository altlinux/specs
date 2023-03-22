Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:	Java Simple Serial Connector
Name:		jssc
Version:	2.8.0
Release:	alt1_25jpp11
License:	GPLv3+
URL:		http://jssc.scream3r.org
Source:		https://github.com/scream3r/java-simple-serial-connector/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# lack of license file, reported upstream:
# https://github.com/scream3r/java-simple-serial-connector/issues/79
Source1:	http://www.gnu.org/licenses/gpl-3.0.txt
# jni load library patch
Patch0:		%{name}-loadlibrary.patch
# fixes jni header mismatch, reported upstream:
# https://github.com/scream3r/java-simple-serial-connector/issues/80
Patch1:		%{name}-jni-fix.patch


BuildRequires:	gcc-c++
BuildRequires:	javapackages-local

Requires:	jpackage-utils

%global jni		%{_libdir}/%{name}
%global jniFullSoName	libjSSC-%{version}.so
%global jniSoName	libjSSC.so
Source44: import.info


%description
jSSC (Java Simple Serial Connector) - library for working with serial ports
from Java.


%package javadoc
Group: System/Libraries
Summary:        Javadoc for %{name} package
BuildArch:      noarch
Requires:       %{name} = %{version}


%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n java-simple-serial-connector-%{version}
%patch0 -p1 -b .loadlibrary
%patch1 -p1 -b .jni-fix
cp -a %{SOURCE1} COPYING
# remove prebuild binaries and jni headers
rm -rf src/java/libs
rm -rf src/cpp/*.h


%build
# compile classes
mkdir -p classes/
(cd src/java; javac -h ../cpp -d ../../classes/ -encoding UTF-8 jssc/*.java)
(cd classes; jar -cf ../jssc.jar jssc/*.class)
# generate javadoc
mkdir -p javadoc/
(cd src/java; javadoc -Xdoclint:none -d ../../javadoc/ -encoding UTF-8 jssc/*.java)
# compile native library
g++ %{optflags} %{?__global_ldflags} -fPIC -shared \
    -D jSSC_NATIVE_LIB_VERSION=\"$(echo %{version} | sed 's/\([1-9]\.[0-9]\).*/\1/')\" \
    -I %{java_home}/include \
    -I %{java_home}/include/linux \
    -o %{jniFullSoName} src/cpp/_nix_based/jssc.cpp


%install
# create necessary directories
install -d %{buildroot}%{jni} \
           %{buildroot}%{_javadocdir}/%{name}
# install jni library and symlink
install -m 0755 -p %{jniFullSoName} %{buildroot}%{jni}
ln -srf %{buildroot}%{jni}/%{jniFullSoName} %{buildroot}%{jni}/%{jniSoName}
# install jar, pom files and java docs
%mvn_artifact org.scream3r:%{name}:%{version} %{name}.jar
%mvn_file org.scream3r:%{name}:%{version} %{name}
%mvn_install -J javadoc


%files -f .mfiles
%doc --no-dereference COPYING
%doc README.txt
%{jni}/


%files javadoc
%doc %{_javadocdir}/%{name}


%changelog
* Wed Mar 22 2023 Igor Vlasenko <viy@altlinux.org> 2.8.0-alt1_25jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 2.8.0-alt1_19jpp11
- fc34 update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 2.8.0-alt1_17jpp11
- update

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 2.8.0-alt1_14jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 2.8.0-alt1_12jpp8
- new version

* Mon Feb 04 2019 Igor Vlasenko <viy@altlinux.ru> 2.8.0-alt1_11jpp8
- java update

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 2.8.0-alt1_10jpp8
- java fc28+ update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 2.8.0-alt1_9jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.8.0-alt1_8jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.8.0-alt1_6jpp8
- new jpp release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.8.0-alt1_5jpp8
- new version

