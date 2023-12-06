Epoch: 1
Group: System/Base
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global base_name   daemon
%global short_name  commons-%{base_name}

Name:           apache-commons-daemon
Summary:        Defines API to support an alternative invocation mechanism
Version:        1.2.4
Release:        alt3_1jpp11
License:        ASL 2.0

URL:            https://commons.apache.org/%{base_name}
Source0:        https://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz

Patch0:         00-configure-java-os.patch

BuildRequires:  autoconf
BuildRequires:  dos2unix
BuildRequires:  gcc
BuildRequires:  xmlto

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
Source44: import.info
Patch33: apache-commons-daemon-1.2.0-e2k.patch
Patch34: apache-commons-daemon-1.2.0-riscv64.patch
Patch35: apache-commons-daemon-1.2.4-loongarch64.patch

%description
The scope of this package is to define an API in line with the current
Java Platform APIs to support an alternative invocation mechanism
which could be used instead of the public static void main(String[])
method.  This specification covers the behavior and life cycle of what
we define as Java daemons, or, in other words, non interactive
Java applications.


%package        jsvc
Group: System/Base
Summary:        Java daemon launcher
Provides:       jsvc = 1:%{version}-%{release}

%description    jsvc
Java daemon launcher.


%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
Requires:       jpackage-utils
BuildArch:      noarch

%description    javadoc
API documentation for apache-commons-daemon.


%prep
%setup -q -n %{short_name}-%{version}-src
%patch0 -p1

%patch33 -p1
%patch34 -p1
%patch35 -p1

# mark example files as non-executable
chmod 644 src/samples/*

# convert to correct end-of-line format
dos2unix -k -n src/samples/ProcrunServiceInstall.cmd src/samples/ProcrunServiceInstall.cmd.new
rm src/samples/ProcrunServiceInstall.cmd
mv src/samples/ProcrunServiceInstall.cmd.new src/samples/ProcrunServiceInstall.cmd

# build manpage for jsvc
cd src/native/unix
xmlto man man/jsvc.1.xml


%build
# build native jsvc
pushd src/native/unix
sh support/buildconf.sh

%configure --with-java=%{java_home}
%make_build
popd

# build jars
%mvn_file  : %{short_name} %{name}
%mvn_alias : org.apache.commons:%{short_name}
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8


%install
# install native jsvc
install -Dpm 755 src/native/unix/jsvc $RPM_BUILD_ROOT%{_bindir}/jsvc
install -Dpm 644 src/native/unix/jsvc.1 $RPM_BUILD_ROOT%{_mandir}/man1/jsvc.1

%mvn_install


%files -f .mfiles
%doc LICENSE.txt PROPOSAL.html NOTICE.txt RELEASE-NOTES.txt src/samples
%doc src/docs/*

%files jsvc
%doc LICENSE.txt NOTICE.txt
%{_bindir}/jsvc
%{_mandir}/man1/jsvc.1*

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt


%changelog
* Wed Dec 06 2023 Ivan A. Melnikov <iv@altlinux.org> 1:1.2.4-alt3_1jpp11
- loongarch64 support

* Mon Feb 21 2022 Ivan A. Melnikov <iv@altlinux.org> 1:1.2.4-alt2_1jpp11
- riscv64 support

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1:1.2.4-alt1_1jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1:1.2.2-alt1_5jpp8
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1:1.0.15-alt3_19jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1:1.0.15-alt3_18jpp8
- restored jpp patches

* Mon Feb 04 2019 Igor Vlasenko <viy@altlinux.ru> 1:1.0.15-alt2_18jpp8
- java update

* Tue Apr 17 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.0.15-alt2_17jpp8
- e2k support

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.0.15-alt1_17jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.0.15-alt1_16jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.0.15-alt1_13jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.15-alt1_11jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.15-alt1_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.15-alt1_4jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.13-alt1_1jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.11-alt2_1jpp7
- rebuild with maven-local

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.0.11-alt1_1jpp7
- fc update

* Mon Oct 08 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0.10-alt1_4jpp7
- new version

* Sat Jan 01 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt1_0.r831676.4jpp6
- new version

