# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%define fedora 18
Name:             dogtag-pki-theme
Version:          10.0.0
Release:          alt1_1jpp7
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


%package -n       dogtag-pki-server-theme
Summary:          Certificate System - PKI Server Framework User Interface
Group:            System/Base

%if 0%{?rhel}
# EPEL version of Dogtag "theme" conflicts with all versions of Red Hat "theme"
Conflicts:        redhat-pki-server-theme
Conflicts:        redhat-pki-common-theme
Conflicts:        redhat-pki-common-ui
Conflicts:        redhat-pki-ca-theme
Conflicts:        redhat-pki-ca-ui
Conflicts:        redhat-pki-kra-theme
Conflicts:        redhat-pki-kra-ui
Conflicts:        redhat-pki-ocsp-theme
Conflicts:        redhat-pki-ocsp-ui
Conflicts:        redhat-pki-tks-theme
Conflicts:        redhat-pki-tks-ui
Conflicts:        redhat-pki-ra-theme
Conflicts:        redhat-pki-ra-ui
Conflicts:        redhat-pki-tps-theme
Conflicts:        redhat-pki-tps-ui

# EPEL version of Dogtag "theme" ALWAYS replaces ALL versions of IPA "theme"
Obsoletes:        ipa-pki-server-theme <= 9999
Obsoletes:        ipa-pki-common-theme <= 9999
Obsoletes:        ipa-pki-ca-theme <= 9999
Obsoletes:        ipa-pki-kra-theme <= 9999

Provides:         ipa-pki-server-theme = %{version}-%{release}
Provides:         ipa-pki-common-theme = %{version}-%{release}
Provides:         ipa-pki-ca-theme = %{version}-%{release}
Provides:         ipa-pki-kra-theme = %{version}-%{release}
%endif

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

Provides:         dogtag-pki-ra-theme = %{version}-%{release}
Provides:         pki-ra-theme = %{version}-%{release}
Provides:         pki-ra-ui = %{version}-%{release}

Provides:         dogtag-pki-tps-theme = %{version}-%{release}
Provides:         pki-tps-theme = %{version}-%{release}
Provides:         pki-tps-ui = %{version}-%{release}

%description -n   dogtag-pki-server-theme
This PKI Server Framework User Interface contains
the Dogtag textual and graphical user interface for the PKI Server Framework.

This package is used by the Dogtag Certificate System.

%%{overview}


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

%%{overview}


%prep


%setup -q -n %{name}-%{version}%{?prerel}


%build
%{__mkdir_p} build
cd build
%{fedora_cmake} -DVERSION=%{version}-%{release} \
	-DVAR_INSTALL_DIR:PATH=/var \
	-DBUILD_DOGTAG_PKI_THEME:BOOL=ON \
	-DJAVA_LIB_INSTALL_DIR=%{_jnidir} \
	..
%{__make} VERBOSE=1 %{?_smp_mflags}


%install
cd build
%{__make} install DESTDIR=%{buildroot} INSTALL="install -p"


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

%files -n dogtag-pki-server-theme
%doc dogtag/common-ui/LICENSE
%dir %{_datadir}/pki
%{_datadir}/pki/common-ui/


%files -n dogtag-pki-console-theme
%doc dogtag/console-ui/LICENSE
%{_javadir}/pki/


%changelog
* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 10.0.0-alt1_1jpp7
- fc update

* Tue Dec 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.0.0-alt1_0.1.a1jpp7.1
- new version

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 10.0.0-alt1_0.1.a1jpp7
- new version

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 9.0.11-alt1_2jpp7
- new version

