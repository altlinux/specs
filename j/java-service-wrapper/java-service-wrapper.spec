Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: gcc-c++ unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# fedora __isa_bits tmp hack
%ifarch x86_64
%define __isa_bits 64
%else
%define __isa_bits 32
%endif
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name java-service-wrapper
%define version 3.2.5
%global javaver 1.7
%global hgrev   3290d306074a
%global pname yaja-wrapper

# rpmbuild < 4.6 support
%if ! 0%{?__isa_bits}
%ifarch x86_64 ia64 ppc64 sparc64 s390x alpha ppc64le aarch64
%global __isa_bits 64
%else
%global __isa_bits 32
%endif
%endif

%global __provides_exclude_from ^%{_libdir}/%{name}/.*\.so$

# Whether to build docs too - by default this is not done as Cocoon is not
# available in Fedora.  Instead we ship a prebuilt archive of the docs
# (the doc/english dir).
#def_with docs
%bcond_with     docs
%global cocoon  cocoon-2.0.4

Name:           java-service-wrapper
Version:        3.2.5
Release:        alt1_23jpp8
Summary:        Java service wrapper
License:        MIT
URL:            https://bitbucket.org/ivertex/yaja-wrapper
# DO NOT TRY TO RELEASE NEW VERSION, see http://lists.fedoraproject.org/pipermail/legal/2011-August/001706.html
Source0:        https://bitbucket.org/ivertex/yaja-wrapper/get/release-3_2_5.tar.bz2
Source1:        %{name}.template.init
# this tar has been generated using --with-docs
Source2:        %{name}-%{version}-docs.tar.bz2
%if %{with docs}
Source3:        http://archive.apache.org/dist/cocoon/BINARIES/%{cocoon}-bin.tar.gz
%endif
# POM for version 3.2.5 is not available on central, so use version 3.2.3 instead.
Source4:        http://repo1.maven.org/maven2/tanukisoft/wrapper/3.2.3/wrapper-3.2.3.pom
Patch0:         %{name}-3.2.4-cflags.patch
Patch1:         %{name}-3.2.4-jnilibpath.patch
Patch2:         %{name}-3.2.4-docbuild.patch
# Use strcpy instead sprintf to copy C string
# Forwarded upstream: https://bitbucket.org/ivertex/yaja-wrapper/issue/6
Patch3:         %{name}-3.2.5-rhbz1037144.patch
Patch99:	ppc64le-support.patch
BuildRequires:  ant
BuildRequires: javapackages-tools rpm-build-java
Source44: import.info

%description
The Java Service Wrapper enables a Java application to be run as a
Unix daemon.  It also monitors the health of your application and JVM.

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch:      noarch

%description    javadoc
API documentation for %{name}.

%prep
%setup -q -n ivertex-%{pname}-%{hgrev}  -a 2
sed '/<version>/s/>.*</>%{version}</' %{SOURCE4} >pom.xml
install -pm 644 %{SOURCE1} doc/template.init
%patch0 -p1
sed -e 's|@LIBPATH@|%{_libdir}/%{name}|' %{PATCH1} | %{__patch} -p1 -F 0
%patch2 -p0
%patch3
%patch99 -p1
%if %{with docs}
mkdir tools ; cd tools
tar xf %{SOURCE3}
unzip -q %{cocoon}/cocoon.war ; mv WEB-INF/lib %{cocoon}/
cd ..
%endif
(cd src/c; cp Makefile-linux-ppc64le-64.make Makefile-linux-aarch64-64.make)
# -Wl,as-needed
perl -i -npe 's,(\$[({]COMPILE[)}](?: -pthread)?) -lm(.*)$,$1$2 -lm,' src/c/Makefile-linux-*


%build
%ant -Dbits=%{__isa_bits} -Djavac.target.version=%{javaver}
%javadoc -sourcepath src/java -Xdoclint:none -d javadoc -link %{_javadocdir}/java -author \
    -windowtitle "Java Service Wrapper API" -doctitle "Java Service Wrapper" \
    -version $(find src/java -name "*.java" -not -path "*/test/*")
%if %{with docs}
rm -r doc/english
%ant -Dbits=%{__isa_bits} doc
%endif


%install
install -Dpm 755 bin/wrapper $RPM_BUILD_ROOT%{_sbindir}/java-service-wrapper

install -dm 755 $RPM_BUILD_ROOT%{_jnidir}
install -dm 755 $RPM_BUILD_ROOT%{_libdir}/%{name}
install -pm 755 lib/libwrapper.so $RPM_BUILD_ROOT%{_libdir}/%{name}
install -pm 644 lib/wrapper.jar $RPM_BUILD_ROOT%{_jnidir}/%{name}.jar
ln -sf %{_jnidir}/%{name}.jar $RPM_BUILD_ROOT%{_libdir}/%{name}/wrapper.jar
    
install -dm 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}
cp -pR javadoc $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files -f .mfiles
%doc AboutThisRepository.txt doc/
%{_sbindir}/java-service-wrapper
%{_libdir}/%{name}/
%doc doc/license.txt

%files javadoc
%{_javadocdir}/%{name}
%doc doc/license.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.2.5-alt1_23jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 3.2.5-alt1_22jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 3.2.5-alt1_19jpp7
- new release

