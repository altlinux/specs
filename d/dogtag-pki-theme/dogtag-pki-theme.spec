Group: System/Base
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-java
BuildRequires: java-devel-default perl(APR/Const.pm) perl(CGI.pm) perl(CGI/Carp.pm) perl(Exporter.pm) perl(FileHandle.pm) perl(LWP/UserAgent.pm) perl(MIME/Base64.pm) perl(ModPerl/Registry.pm) perl(Mozilla/LDAP/Conn.pm) perl(Mozilla/LDAP/LDIF.pm) perl(Parse/RecDescent.pm) perl(URI/Escape.pm) perl(URI/URL.pm) perl(XML/Simple.pm) perl(subs.pm) rpm-build-java zlib-devel
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
################################################################################
Name:             dogtag-pki-theme
################################################################################

Summary:          Dogtag PKI Theme Package
URL:              http://www.dogtagpki.org/
License:          GPLv2

%if 0%{?rhel}
Version:          10.6.0
Release:          alt1_1jpp8
%else
Version:          10.6.0
Release:          alt1_1jpp8
%endif

Source:           https://github.com/dogtagpki/pki/archive/v%{version}/pki-%{version}.tar.gz

BuildArch:        noarch

################################################################################
# Build Dependencies
################################################################################

BuildRequires:    ctest cmake
BuildRequires:    gcc-c++
BuildRequires:    java-1.8.0-openjdk-devel
BuildRequires:    jpackage-utils >= 1.7.5
Source44: import.info

%description
Several PKI packages utilize a "virtual" theme component.  These
"virtual" theme components are "Provided" by various theme "flavors"
including "dogtag" or a user customized theme package.  Consequently,
all "dogtag" and any customized theme components MUST be mutually
exclusive!

################################################################################
%package -n       dogtag-pki-server-theme
Group: System/Base
################################################################################

Summary:          Dogtag PKI Server Theme Package

Obsoletes:        dogtag-pki-common-theme <= %{version}-%{release}
Obsoletes:        dogtag-pki-common-ui
Obsoletes:        dogtag-pki-ca-theme <= %{version}-%{release}
Obsoletes:        dogtag-pki-ca-ui
Obsoletes:        dogtag-pki-kra-theme <= %{version}-%{release}
Obsoletes:        dogtag-pki-kra-ui
Obsoletes:        dogtag-pki-ocsp-theme <= %{version}-%{release}
Obsoletes:        dogtag-pki-ocsp-ui
Obsoletes:        dogtag-pki-tks-theme <= %{version}-%{release}
Obsoletes:        dogtag-pki-tks-ui
Obsoletes:        dogtag-pki-ra-theme <= %{version}-%{release}
Obsoletes:        dogtag-pki-ra-ui
Obsoletes:        dogtag-pki-tps-theme <= %{version}-%{release}
Obsoletes:        dogtag-pki-tps-ui

Provides:         dogtag-pki-common-theme = %{version}-%{release}
Provides:         pki-server-theme = %{version}-%{release}
Provides:         pki-common-theme = %{version}-%{release}
Provides:         pki-common-ui = %{version}-%{release}

Provides:         dogtag-pki-ca-theme = %{version}-%{release}
Provides:         pki-ca-theme = %{version}-%{release}
Provides:         pki-ca-ui = %{version}-%{release}

Provides:         dogtag-pki-kra-theme = %{version}-%{release}
Provides:         pki-kra-theme = %{version}-%{release}
Provides:         pki-kra-ui = %{version}-%{release}

Provides:         dogtag-pki-ocsp-theme = %{version}-%{release}
Provides:         pki-ocsp-theme = %{version}-%{release}
Provides:         pki-ocsp-ui = %{version}-%{release}

Provides:         dogtag-pki-tks-theme = %{version}-%{release}
Provides:         pki-tks-theme = %{version}-%{release}
Provides:         pki-tks-ui = %{version}-%{release}

Provides:         dogtag-pki-tps-theme = %{version}-%{release}
Provides:         pki-tps-theme = %{version}-%{release}
Provides:         pki-tps-ui = %{version}-%{release}

%description -n   dogtag-pki-server-theme
This PKI Server Framework User Interface contains
Dogtag textual and graphical user interface for PKI Server.

################################################################################
%package -n       dogtag-pki-console-theme
Group: System/Base
################################################################################

Summary:          Dogtag PKI Console Theme Package

Requires:         java-1.8.0-openjdk

%if 0%{?rhel}
# EPEL version of Dogtag "theme" conflicts with all versions of Red Hat "theme"
Conflicts:        redhat-pki-console-theme
Conflicts:        redhat-pki-console-ui
%endif

Obsoletes:        dogtag-pki-console-ui <= 9

Provides:         pki-console-theme = %{version}-%{release}
Provides:         pki-console-ui = %{version}-%{release}

%description -n   dogtag-pki-console-theme
This PKI Console Theme Package contains
Dogtag textual and graphical user interface for PKI Console.

################################################################################
%prep
################################################################################

%setup -q -n pki-%{version}
sed -i -e s,/usr/bin/ln,/bin/ln,g dogtag/common-ui/CMakeLists.txt


################################################################################
%build
################################################################################

mkdir -p build
cd build
%{fedora_cmake} \
    -DVERSION=%{version}-%{release} \
    -DVAR_INSTALL_DIR:PATH=/var \
    -DJAVA_LIB_INSTALL_DIR=%{_jnidir} \
    -DBUILD_DOGTAG_PKI_THEME:BOOL=ON \
    ..

################################################################################
%install
################################################################################

cd build

# Do not use _smp_mflags to preserve build order
make \
    VERBOSE=%{?_verbose} \
    DESTDIR=%{buildroot} \
    INSTALL="install -p" \
    all install

# NOTE:  Several "theme" packages require ownership of the "/usr/share/pki"
#        directory because the PKI subsystems (CA, KRA, OCSP, TKS, TPS)
#        which require them may be installed either independently or in
#        multiple combinations.

################################################################################
%files -n dogtag-pki-server-theme
################################################################################

%doc dogtag/common-ui/LICENSE
%{_datadir}/pki/common-ui/
%{_datadir}/pki/server/webapps/pki/ca
%{_datadir}/pki/server/webapps/pki/css
%{_datadir}/pki/server/webapps/pki/esc
%{_datadir}/pki/server/webapps/pki/fonts
%{_datadir}/pki/server/webapps/pki/images
%{_datadir}/pki/server/webapps/pki/kra
%{_datadir}/pki/server/webapps/pki/ocsp
%{_datadir}/pki/server/webapps/pki/pki.properties
%{_datadir}/pki/server/webapps/pki/tks
%dir %{_datadir}/pki/server/webapps/pki
%dir %{_datadir}/pki/server/webapps
%dir %{_datadir}/pki/server

################################################################################
%files -n dogtag-pki-console-theme
################################################################################

%doc dogtag/console-ui/LICENSE
%{_javadir}/pki/pki-console-theme.jar

################################################################################
%changelog
* Fri Apr 20 2018 Igor Vlasenko <viy@altlinux.ru> 10.6.0-alt1_1jpp8
- java update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 10.5.1-alt1_1jpp8
- new version

* Wed Nov 15 2017 Igor Vlasenko <viy@altlinux.ru> 10.4.8-alt1_3jpp8
- new version

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 10.3.5-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 10.3.5-alt1_1jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 10.3.1-alt1_1jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 10.2.6-alt1_1jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 10.1.0-alt1_1jpp7
- new release

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 10.0.6-alt1_1jpp7
- new version

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 10.0.0-alt1_1jpp7
- fc update

* Tue Dec 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.0.0-alt1_0.1.a1jpp7.1
- new version

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 10.0.0-alt1_0.1.a1jpp7
- new version

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 9.0.11-alt1_2jpp7
- new version

