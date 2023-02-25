Group: Development/Other
BuildRequires: rpm-build-python3
%define oldname fonts-rpm-macros
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%oldname is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name fonts-rpm-macros
# SPDX-License-Identifier: MIT
%global forgeurl https://pagure.io/fonts-rpm-macros
Epoch: 1
Version: 2.0.5
# FedoraForgeMeta2ALT: generated meta
%global forgeurl https://pagure.io/fonts-rpm-macros
%global forgesource https://pagure.io/fonts-rpm-macros/archive/2.0.5/fonts-rpm-macros-2.0.5.tar.gz
%global archivename fonts-rpm-macros-2.0.5
%global archiveext tar.gz
%global archiveurl https://pagure.io/fonts-rpm-macros/archive/2.0.5/fonts-rpm-macros-2.0.5.tar.gz
%global topdir fonts-rpm-macros-2.0.5
%global extractdir fonts-rpm-macros-2.0.5
%global repo fonts-rpm-macros
#global owner %nil
#global namespace %nil
%global scm git
#global tag %nil
#global commit %nil
#global shortcommit %nil
#global branch %nil
%global version 2.0.5
#global date %nil
#global distprefix %nil
# FedoraForgeMeta2ALT: end generated meta

#https://src.fedoraproject.org/rpms/redhat-rpm-config/pull-request/51
%global _spectemplatedir %{_datadir}/rpmdevtools/fedora
%global _docdir_fmt     %{oldname}
%global ftcgtemplatedir %{_datadir}/fontconfig/templates

# Master definition that will be written to macro files
%global _fontbasedir            %{_datadir}/fonts
%global _fontconfig_masterdir   %{_sysconfdir}/fonts
%global _fontconfig_confdir     %{_sysconfdir}/fonts/conf.d
%global _fontconfig_templatedir %{_datadir}/fontconfig/conf.avail

BuildArch: noarch

Name:      rpm-build-fedora-compat-fonts
Release:   alt2_11
Summary:   Build-stage rpm automation for fonts packages

License:   GPL-3.0-or-later
URL:       https://docs.fedoraproject.org/en-US/packaging-guidelines/FontsPolicy/
Source:    %{forgesource}
Patch0:    %{oldname}-omit-foundry-in-family.patch


#Provides:  fontpackages-devel = %{?epoch:%{epoch}:}%{version}-%{release}
#Obsoletes: fontpackages-devel < %{?epoch:%{epoch}:}%{version}-%{release}
# Tooling dropped for now as no one was willing to maintain it
#Obsoletes: fontpackages-tools < %{?epoch:%{epoch}:}%{version}-%{release}

Requires:  fontconfig libfontconfig1
Requires:  libappstream-glib libappstream-glib-gir
Requires:  libuchardet uchardet

# For the experimental generator
Requires:  python3-module-ruamel-yaml
Requires:  python3-module-lxml
Source44: import.info
# for %%fontcheck
Requires: /usr/bin/appstream-util /usr/bin/xmllint
Source45: macros.fedora-fonts

Requires: rpm-build-fonts rpm-macros-fedora-compat-fonts

%description
This package provides build-stage rpm automation to simplify the creation of
fonts packages.

It does not need to be included in the default build root: fonts-srpm-macros
will pull it in for fonts packages only.

%package -n rpm-macros-fedora-compat-fonts
Summary: Set of RPM macros for packaging %name-based applications
Group: Development/Other
Requires: rpm-macros-fonts > 0.6
BuildArch: noarch

%description -n rpm-macros-fedora-compat-fonts
Set of RPM macros for packaging fedora-compat-fonts-based applications for ALT Linux.
Install this package if you want to create RPM packages that use %name.

%files -n rpm-macros-fedora-compat-fonts
%_rpmmacrosdir/fedora-compat-fonts

%package -n fonts-srpm-macros
Group: Development/Other
Summary:   Source-stage rpm automation for fonts packages

%description -n fonts-srpm-macros
This package provides SRPM-stage rpm automation to simplify the creation of
fonts packages.

It limits itself to the automation subset required to create fonts SRPM
packages and needs to be included in the default build root.

The rest of the automation is provided by the fonts-rpm-macros package, that
fonts-srpm-macros will pull in for fonts packages only.

%package -n fonts-filesystem
Group: Development/Other
Summary:   Directories used by font packages
License:   MIT

Provides:  fontpackages-filesystem = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: fontpackages-filesystem < %{?epoch:%{epoch}:}%{version}-%{release}

%description -n fonts-filesystem
This package contains the basic directory layout used by font packages,
including the correct permissions for the directories.

%package -n fonts-rpm-templates
Group: Development/Other
Summary:   Example fonts packages rpm spec templates
License:   MIT

Requires:    rpm-build-fedora-compat-fonts = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n fonts-rpm-templates
This package contains documented rpm spec templates showcasing how to use the
macros provided by fonts-rpm-macros to create fonts packages.

%prep
%setup -q -n fonts-rpm-macros-2.0.5
for template in templates/rpm/*\.spec ; do
  target=$(echo "${template}" | sed "s|^\(.*\)\.spec$|\1-bare.spec|g")
  grep -v '^%%dnl' "${template}" > "${target}"
  touch -r "${template}" "${target}"
done
%patch0 -p1 -b .1-omit-foundry-in-family

%install
install -m 0755 -d    %{buildroot}%{_fontbasedir} \
                      %{buildroot}%{_fontconfig_masterdir} \
                      %{buildroot}%{_fontconfig_confdir} \
                      %{buildroot}%{_fontconfig_templatedir}

install -m 0755 -vd   %{buildroot}%{_spectemplatedir}
install -m 0644 -vp   templates/rpm/*spec \
                      %{buildroot}%{_spectemplatedir}
install -m 0755 -vd   %{buildroot}%{ftcgtemplatedir}
install -m 0644 -vp   templates/fontconfig/*{conf,txt} \
                      %{buildroot}%{ftcgtemplatedir}

install -m 0755 -vd   %{buildroot}%{_rpmmacrosdir}
install -m 0644 -vp   rpm/macros.d/macros.fonts-* \
                      %{buildroot}%{_rpmmacrosdir}
install -m 0755 -vd   %{buildroot}%{_rpmluadir}/fedora/srpm
install -m 0644 -vp   rpm/lua/srpm/*lua \
                      %{buildroot}%{_rpmluadir}/fedora/srpm
install -m 0755 -vd   %{buildroot}%{_rpmluadir}/fedora/rpm
install -m 0644 -vp   rpm/lua/rpm/*lua \
                      %{buildroot}%{_rpmluadir}/fedora/rpm

install -m 0755 -vd   %{buildroot}%{_bindir}
install -m 0755 -vp   bin/* %{buildroot}%{_bindir}
install -D -m644 %SOURCE45 %buildroot%_rpmmacrosdir/fedora-compat-fonts

%files
%doc --no-dereference LICENSE.txt
%{_bindir}/*

%doc --no-dereference LICENSE-templates.txt
%doc     *.md changelog.txt
%{_spectemplatedir}/*.spec
%dir %{ftcgtemplatedir}
%doc %{ftcgtemplatedir}/*conf
%doc %{ftcgtemplatedir}/*txt

%changelog
* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 1:2.0.5-alt2_11
- update to new release by fcimport

* Sun Feb 06 2022 Igor Vlasenko <viy@altlinux.org> 1:2.0.5-alt2_7
- do not obsolete fontpackages

* Sun Feb 06 2022 Igor Vlasenko <viy@altlinux.org> 1:2.0.5-alt1_7
- added dependencies

* Fri Jan 28 2022 Igor Vlasenko <viy@altlinux.org> 1:2.0.5-alt1_6
- new version

