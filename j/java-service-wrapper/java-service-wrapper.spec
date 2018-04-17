Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-generic-compat rpm-macros-java
BuildRequires: gcc-c++ rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name java-service-wrapper
%global javaver 1.7
%global hgrev   3290d306074a
%global pname yaja-wrapper

# rpmbuild < 4.6 support

%global __provides_exclude_from ^%{_libdir}/%{name}/.*\.so$

# Whether to build docs too - by default this is not done as Cocoon is not
# available in Fedora.  Instead we ship a prebuilt archive of the docs
# (the doc/english dir).
%bcond_with     docs
%global cocoon  cocoon-2.0.4

Name:           java-service-wrapper
Version:        3.2.5
Release:        alt2_31jpp8
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
Patch98:        Use-RPM_OPT_FLAGS-on-s390x.patch
Patch99:        ppc64le-support.patch
BuildRequires:  ant
BuildRequires:  javapackages-local
BuildRequires:  gcc
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
sed -e 's|@LIBPATH@|%{_libdir}/%{name}|' %{PATCH1} | patch -p1 -F 0
%patch2 -p0
%patch3
%patch98 -p1
%patch99 -p1
%if %{with docs}
mkdir tools ; cd tools
tar xf %{SOURCE3}
unzip -q %{cocoon}/cocoon.war ; mv WEB-INF/lib %{cocoon}/
cd ..
%endif
(cd src/c; cp Makefile-linux-ppc64le-64.make Makefile-linux-aarch64-64.make)
(cd src/c; cp Makefile-linux-arm-32.make Makefile-linux-aarch32-32.make)
# e2k support
(cd src/c; cp Makefile-linux-ppc64le-64.make Makefile-linux-e2k-64.make)
# e2k: lcc is not --pedantic
perl -i -npe 's,--pedantic,,' src/c/Makefile-linux-*
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

install -dm 755 $RPM_BUILD_ROOT%{_libdir}/%{name}
install -pm 755 lib/libwrapper.so $RPM_BUILD_ROOT%{_libdir}/%{name}

%mvn_file : %{name} %{_libdir}/%{name}/wrapper
%mvn_artifact pom.xml lib/wrapper.jar

%mvn_install -J javadoc

%files -f .mfiles
%doc AboutThisRepository.txt doc/
%{_sbindir}/java-service-wrapper
%{_libdir}/%{name}/
%doc --no-dereference doc/license.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference doc/license.txt

%changelog
* Tue Apr 17 2018 Igor Vlasenko <viy@altlinux.ru> 3.2.5-alt2_31jpp8
- e2k support

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 3.2.5-alt1_31jpp8
- regenerated to fix __isa_bits definition

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.2.5-alt1_27jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 3.2.5-alt1_26jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.2.5-alt1_23jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 3.2.5-alt1_22jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 3.2.5-alt1_19jpp7
- new release

