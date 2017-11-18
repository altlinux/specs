BuildRequires: maven-remote-resources-plugin
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.1.30
%global namedreltag .Fork2
%global namedversion %{version}%{?namedreltag}

Name:           netty-tcnative
Version:        1.1.30
Release:        alt3_8jpp8
Summary:        Fork of Tomcat Native with improved OpenSSL and mavenized build
License:        ASL 2.0
URL:            https://github.com/netty/netty/wiki/Forked-Tomcat-Native
Source0:        https://github.com/netty/netty-tcnative/archive/%{name}-%{namedversion}.tar.gz
Source1:        CheckLibrary.java
Patch1:         fixLibNames.patch.in
Patch2:         i388aprFix.patch

BuildRequires:  maven-local
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  glibc-devel
BuildRequires:  libapr1-devel
%if 0%{?fedora} >= 26
BuildRequires:  libssl-devel
%else
BuildRequires:  libssl-devel
%endif
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-hawtjni-plugin
BuildRequires:  maven-plugin-build-helper
BuildRequires:  maven-plugin-bundle
BuildRequires:  maven-source-plugin
#parent pom is needed
BuildRequires:  netty
BuildRequires:  sonatype-oss-parent
BuildRequires: mvn(kr.motd.maven:os-maven-plugin)
Source44: import.info


%description
netty-tcnative is a fork of Tomcat Native. It includes a set of changes
contributed by Twitter, Inc, such as:
 *  Simplified distribution and linkage of native library
 *  Complete mavenization of the project
 *  Improved OpenSSL support
To minimize the maintenance burden, we create a dedicated branch for each stable
upstream release and apply our own changes on top of it, while keeping the
number of maintained branches to minimum


%package javadoc
Summary:   API documentation for %{name}
Group:     Development/Java
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{name}-%{namedversion}
patch=`mktemp`
sed "s;@PATH@;%{_libdir}/%{name};g" < %{PATCH1} > $patch
patch -p1 < $patch
%patch2 -p1


%build
%mvn_build -f

%install
%mvn_install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}/
cp target/native-build/target/lib/lib%{name}-%{namedversion}.so $RPM_BUILD_ROOT%{_libdir}/%{name}/lib%{name}.so


%check
javac -d . -cp $RPM_BUILD_ROOT%{_jnidir}/%{name}/%{name}.jar %{SOURCE1}
#don't know how to test load(path) without more and more patching, however the test class can be used for manual testing
#java -cp .:$RPM_BUILD_ROOT%%{_jnidir}/%%{name}/%%{name}.jar CheckLibrary


%files -f .mfiles
%dir %{_libdir}/%{name}
%dir %{_jnidir}/%{name}
%dir %{_mavenpomdir}/%{name}
%{_libdir}/%{name}/lib%{name}.so

%files javadoc -f .mfiles-javadoc

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.30-alt3_8jpp8
- added BR: maven-remote-resources-plugin for javapackages 5

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.30-alt2_8jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.30-alt2_6jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.30-alt2_3jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.30-alt2_2jpp8
- %%_jnidir set to /usr/lib/java

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.30-alt1_2jpp8
- new version

