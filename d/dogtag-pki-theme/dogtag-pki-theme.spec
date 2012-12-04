# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++ rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%define fedora 18
# for a pre-release, define the prerel field e.g. .a1 .rc2 - comment out for official release
# also remove the space between % and global - this space is needed because
# fedpkg verrel stupidly ignores comment lines
%global prerel .a1
# also need the relprefix field for a pre-release e.g. .0 - also comment out for official release
%global relprefix 0.

Name:             dogtag-pki-theme
Version:          10.0.0
Release:          alt1_0.1.a1jpp7.1
Summary:          Certificate System - Dogtag PKI Theme Components
URL:              http://pki.fedoraproject.org/
License:          GPLv2
Group:            System/Base

BuildArch:        noarch


BuildRequires:    ctest cmake
%if 0%{?fedora} >= 16
BuildRequires:    jpackage-utils >= 1.7.5-10
%else
BuildRequires:    jpackage-utils
%endif

Source0:          http://pki.fedoraproject.org/pki/sources/%{name}/%{name}-%{version}%{?prerel}.tar.gz

%if 0%{?rhel}
ExcludeArch:      ppc ppc64 s390 s390x
%endif

%global overview                                                       \
Several PKI packages require a "virtual" theme component.  These       \
"virtual" theme components are "Provided" by various theme "flavors"   \
including "dogtag", "redhat", and "ipa".  Consequently,                \
all "dogtag", "redhat", and "ipa" theme components MUST be             \
mutually exclusive!                                                    \
                                                                       \
On Fedora systems, the "dogtag" theme packages are the ONLY available  \
theme components.                                                      \
                                                                       \
Similarly, the "ipa" theme packages are ONLY available on RHEL         \
systems, and represent the default theme components.                   \
                                                                       \
Alternatively, on RHEL systems, if the "dogtag" theme packages are     \
available as EPEL packages, while they may be used as a transparent    \
replacement for their corresponding "ipa" theme package, they are not  \
intended to be used as a replacement for their corresponding "redhat"  \
theme components.                                                      \
                                                                       \
Finally, if available for a RHEL system (e. g. - RHCS subscription),   \
each "redhat" theme package MUST be used as a transparent replacement  \
for its corresponding "ipa" theme package or "dogtag" theme package.   \
%{nil}
Source44: import.info

%description %{overview}


%package -n       dogtag-pki-common-theme
Summary:          Certificate System - PKI Common Framework User Interface
Group:            System/Base

%if 0%{?rhel}
# EPEL version of Dogtag "theme" conflicts with all versions of Red Hat "theme"
Conflicts:        redhat-pki-common-theme
Conflicts:        redhat-pki-common-ui

# EPEL version of Dogtag "theme" ALWAYS replaces ALL versions of IPA "theme"
Obsoletes:        ipa-pki-common-theme <= 9999
Provides:         ipa-pki-common-theme = %{version}-%{release}
%endif

Obsoletes:        dogtag-pki-common-ui <= 9

Provides:         pki-common-theme = %{version}-%{release}
Provides:         pki-common-ui = %{version}-%{release}

%description -n   dogtag-pki-common-theme
This PKI Common Framework User Interface contains
the Dogtag textual and graphical user interface for the PKI Common Framework.

This package is used by the Dogtag Certificate System.

%{overview}


%package -n       dogtag-pki-ca-theme
Summary:          Certificate System - Certificate Authority User Interface
Group:            System/Base

Requires:         dogtag-pki-common-theme = %{version}-%{release}

%if 0%{?rhel}
# EPEL version of Dogtag "theme" conflicts with all versions of Red Hat "theme"
Conflicts:        redhat-pki-ca-theme
Conflicts:        redhat-pki-ca-ui

# EPEL version of Dogtag "theme" ALWAYS replaces ALL versions of IPA "theme"
Obsoletes:        ipa-pki-ca-theme <= 9999
Provides:         ipa-pki-ca-theme = %{version}-%{release}
%endif

Obsoletes:        dogtag-pki-ca-ui <= 9

Provides:         pki-ca-theme = %{version}-%{release}
Provides:         pki-ca-ui = %{version}-%{release}

%description -n   dogtag-pki-ca-theme
This Certificate Authority (CA) User Interface contains
the Dogtag textual and graphical user interface for the CA.

This package is used by the Dogtag Certificate System.

%{overview}


%package -n       dogtag-pki-kra-theme
Summary:          Certificate System - Data Recovery Manager User Interface
Group:            System/Base

Requires:         dogtag-pki-common-theme = %{version}-%{release}

%if 0%{?rhel}
# EPEL version of Dogtag "theme" conflicts with all versions of Red Hat "theme"
Conflicts:        redhat-pki-kra-theme
Conflicts:        redhat-pki-kra-ui
%endif

Obsoletes:        dogtag-pki-kra-ui <= 9

Provides:         pki-kra-theme = %{version}-%{release}
Provides:         pki-kra-ui = %{version}-%{release}

%description -n   dogtag-pki-kra-theme
This Data Recovery Manager (DRM) User Interface contains
the Dogtag textual and graphical user interface for the DRM.

This package is used by the Dogtag Certificate System.

%{overview}


%package -n       dogtag-pki-ocsp-theme
Summary:          Certificate System - Online Certificate Status Protocol Manager User Interface
Group:            System/Base

Requires:         dogtag-pki-common-theme = %{version}-%{release}

%if 0%{?rhel}
# EPEL version of Dogtag "theme" conflicts with all versions of Red Hat "theme"
Conflicts:        redhat-pki-ocsp-theme
Conflicts:        redhat-pki-ocsp-ui
%endif

Obsoletes:        dogtag-pki-ocsp-ui <= 9

Provides:         pki-ocsp-theme = %{version}-%{release}
Provides:         pki-ocsp-ui = %{version}-%{release}

%description -n   dogtag-pki-ocsp-theme
This Online Certificate Status Protocol (OCSP) Manager User Interface contains
the Dogtag textual and graphical user interface for the OCSP Manager.

This package is used by the Dogtag Certificate System.

%{overview}


%package -n       dogtag-pki-ra-theme
Summary:          Certificate System - Registration Authority User Interface
Group:            System/Base

%if 0%{?rhel}
# EPEL version of Dogtag "theme" conflicts with all versions of Red Hat "theme"
Conflicts:        redhat-pki-ra-theme
Conflicts:        redhat-pki-ra-ui
%endif

Obsoletes:        dogtag-pki-ra-ui <= 9

Provides:         pki-ra-theme = %{version}-%{release}
Provides:         pki-ra-ui = %{version}-%{release}

%description -n   dogtag-pki-ra-theme
This Registration Authority (RA) User Interface contains
the Dogtag textual and graphical user interface for the RA.

This package is used by the Dogtag Certificate System.

%{overview}


%package -n       dogtag-pki-tks-theme
Summary:          Certificate System - Token Key Service User Interface
Group:            System/Base

Requires:         dogtag-pki-common-theme = %{version}-%{release}

%if 0%{?rhel}
# EPEL version of Dogtag "theme" conflicts with all versions of Red Hat "theme"
Conflicts:        redhat-pki-tks-theme
Conflicts:        redhat-pki-tks-ui
%endif

Obsoletes:        dogtag-pki-tks-ui <= 9

Provides:         pki-tks-theme = %{version}-%{release}
Provides:         pki-tks-ui = %{version}-%{release}

%description -n   dogtag-pki-tks-theme
This Token Key Service (TKS) User Interface contains
the Dogtag textual and graphical user interface for the TKS.

This package is used by the Dogtag Certificate System.

%{overview}


%package -n       dogtag-pki-tps-theme
Summary:          Certificate System - Token Processing System User Interface
Group:            System/Base

%if 0%{?rhel}
# EPEL version of Dogtag "theme" conflicts with all versions of Red Hat "theme"
Conflicts:        redhat-pki-tps-theme
Conflicts:        redhat-pki-tps-ui
%endif

Obsoletes:        dogtag-pki-tps-ui <= 9

Provides:         pki-tps-theme = %{version}-%{release}
Provides:         pki-tps-ui = %{version}-%{release}

%description -n   dogtag-pki-tps-theme
This Token Processing System (TPS) User Interface contains
the Dogtag textual and graphical user interface for the TPS.

This package is used by the Dogtag Certificate System.

%{overview}


%package -n       dogtag-pki-console-theme
Summary:          Certificate System - PKI Console User Interface
Group:            System/Base


%if 0%{?rhel}
# EPEL version of Dogtag "theme" conflicts with all versions of Red Hat "theme"
Conflicts:        redhat-pki-console-theme
Conflicts:        redhat-pki-console-ui
%endif

Obsoletes:        dogtag-pki-console-ui <= 9

Provides:         pki-console-theme = %{version}-%{release}
Provides:         pki-console-ui = %{version}-%{release}

%description -n   dogtag-pki-console-theme
This PKI Console User Interface contains
the Dogtag textual and graphical user interface for the PKI Console.

This package is used by the Dogtag Certificate System.

%{overview}


%prep


%setup -q -n %{name}-%{version}%{?prerel}


%build
function runCmake () {
	%{fedora_cmake} \
		-DVAR_INSTALL_DIR:PATH=/var \
		-DBUILD_DOGTAG_PKI_THEME:BOOL=ON \
		-DJAVA_LIB_INSTALL_DIR=%{_jnidir} \
		..
}
%{__mkdir_p} build
cd build
runCmake ||:

# stage 2 for find CMakeJavaCompiler.cmake:
CMAKE_VER=$(rpm -q --queryformat="%{VERSION}" cmake)
cp CMakeFiles/CMakeJavaCompiler.cmake CMakeFiles/$CMAKE_VER/
runCmake

%{__make} VERBOSE=1 %{?_smp_mflags}


%install
cd build
%{__make} install DESTDIR=%{buildroot} INSTALL="install -p"

chmod 755 %{buildroot}%{_datadir}/pki/tps-ui/cgi-bin/sow/cfg.pl


# NOTE:  Several "theme" packages require ownership of the "/usr/share/pki"
#        directory because the PKI subsystems (CA, DRM, OCSP, TKS, RA, TPS)
#        which require them may be installed either independently or in
#        multiple combinations.
#
#        Since CA, DRM, OCSP, and TKS subsystems all require the
#        "dogtag-pki-common-theme" as well as their individual "themes",
#        only "dogtag-pki-common-theme" needs to require this directory.
#
#        However, RA and TPS subsystems still require their own individual
#        ownership of this directory.

%files -n dogtag-pki-common-theme
%doc dogtag/common-ui/LICENSE
%dir %{_datadir}/pki
%{_datadir}/pki/common-ui/


%files -n dogtag-pki-ca-theme
%doc dogtag/ca-ui/LICENSE
%{_datadir}/pki/ca-ui/


%files -n dogtag-pki-kra-theme
%doc dogtag/kra-ui/LICENSE
%{_datadir}/pki/kra-ui/


%files -n dogtag-pki-ocsp-theme
%doc dogtag/ocsp-ui/LICENSE
%{_datadir}/pki/ocsp-ui/


%files -n dogtag-pki-ra-theme
%doc dogtag/ra-ui/LICENSE
%dir %{_datadir}/pki
%{_datadir}/pki/ra-ui/


%files -n dogtag-pki-tks-theme
%doc dogtag/tks-ui/LICENSE
%{_datadir}/pki/tks-ui/


%files -n dogtag-pki-tps-theme
%doc dogtag/tps-ui/LICENSE
%dir %{_datadir}/pki
%{_datadir}/pki/tps-ui/


%files -n dogtag-pki-console-theme
%doc dogtag/console-ui/LICENSE
%{_javadir}/pki/


%changelog
* Tue Dec 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.0.0-alt1_0.1.a1jpp7.1
- new version

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 10.0.0-alt1_0.1.a1jpp7
- new version

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 9.0.11-alt1_2jpp7
- new version

