Group: System/Configuration/Other
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Font/TTF/Font.pm) perl(Unicode/UCD.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 0
%define fedora 29
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name fontpackages
%global spectemplatedir %{_sysconfdir}/rpmdevtools/
%global ftcgtemplatedir %{_datadir}/fontconfig/templates/

# Use the same directory of the main package for subpackage licence and docs
%global _docdir_fmt %{name}

Name:    fontpackages
Version: 1.44
Release: alt7_24
Summary: Common directory and macro definitions used by font packages

# Mostly means the scriptlets inserted via this package do not change the
# license of the packages they're inserted in
License:   LGPLv3+
URL:       http://fedoraproject.org/wiki/fontpackages
Source0:   http://fedorahosted.org/releases/f/o/%{name}/%{name}-%{version}.tar.xz
Patch0:    dnf.patch
Patch1:    %{name}-drop-fccache.patch
Patch2:    %{name}-add-ghost-uuid.patch

BuildArch: noarch
BuildRequires: rpm-build-perl
Source44: import.info
Patch33: macros.fonts.diff


%description
This package contains the basic directory layout, spec templates, rpm macros
and other materials used to create font packages.


%package filesystem
Group: System/Configuration/Other
Summary: Directories used by font packages
License: Public Domain

%description filesystem
This package contains the basic directory layout used by font packages,
including the correct permissions for the directories.


%package devel
Group: System/Configuration/Other
Summary: Templates and macros used to create font packages

Requires: fontconfig
Requires: rpm-macros-fontpackages rpm-build-fonts xorg-font-encodings

%description devel
This package contains spec templates, rpm macros and other materials used to
create font packages.


%package tools
Group: System/Configuration/Other
Summary: Tools used to check fonts and font packages

Requires: fontconfig fontforge libfontforge
Requires: curl, make, mutt
Requires: dnf-command(repoquery)
Requires: createrepo_c

# repo-font-audit script need to run fedoradev-pkgowners command
# which is available on Fedora only and not on RHEL.
%if 0%{?fedora}
Requires: fedora-packager
%endif

%description tools
This package contains tools used to check fonts and font packages.

%package -n rpm-macros-%{name}
Summary: Set of RPM macros for packaging %name-based applications
Group: Development/Other
BuildArch: noarch

%description -n rpm-macros-%{name}
Set of RPM macros for packaging %name-based applications for ALT Linux.
Install this package if you want to create RPM packages that use %name.

%files -n rpm-macros-%{name}
%_rpmmacrosdir/*



%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%if 0%{?rhel}
sed -i 's|/usr/bin/fedoradev-pkgowners|""|g' bin/repo-font-audit
%endif

# Drop obosolete %defattr (#1047031)
sed -i '/^%%defattr/d' rpm/macros.fonts
%patch33 -p0

%build
sed -i "s|^DATADIR\([[:space:]]*\)\?=\(.*\)$|DATADIR=%{_datadir}/%{name}|g" \
  bin/repo-font-audit bin/compare-repo-font-audit

%install
# Pull macros out of macros.fonts and emulate them during install
for dir in fontbasedir        fontconfig_masterdir \
           fontconfig_confdir fontconfig_templatedir ; do
  export _${dir}=$(rpm --eval $(grep -E "^%_${dir}\b" \
    rpm/macros.fonts | gawk '{ print $2 }'))
done

install -m 0755 -d %{buildroot}${_fontbasedir} \
                   %{buildroot}${_fontconfig_masterdir} \
                   %{buildroot}${_fontconfig_confdir} \
                   %{buildroot}${_fontconfig_templatedir} \
                   %{buildroot}%{spectemplatedir} \
                   %{buildroot}%{_rpmmacrosdir} \
                   %{buildroot}%{_datadir}/fontconfig/templates \
                   %{buildroot}/%_datadir/%{name} \
                   %{buildroot}%{_bindir}
install -m 0644 -p spec-templates/*.spec       %{buildroot}%{spectemplatedir}
install -m 0644 -p fontconfig-templates/*      %{buildroot}%{ftcgtemplatedir}
install -m 0644 -p rpm/macros*                 %{buildroot}%{_rpmmacrosdir}
install -m 0644 -p private/repo-font-audit.mk  %{buildroot}/%{_datadir}/%{name}
install -m 0755 -p private/core-fonts-report \
                   private/font-links-report \
                   private/fonts-report \
                   private/process-fc-query \
                   private/test-info           %{buildroot}/%{_datadir}/%{name}
install -m 0755 -p bin/*                       %{buildroot}%{_bindir}

cat <<EOF > %{name}-%{version}.files
%dir ${_fontbasedir}
%dir ${_fontconfig_masterdir}
%dir ${_fontconfig_confdir}
%dir ${_fontconfig_templatedir}
%ghost ${_fontbasedir}/.uuid
EOF
rm -rf %buildroot%{spectemplatedir}
# rename macros.xxx
mv %buildroot%_rpmmacrosdir/macros.fonts  %buildroot%_rpmmacrosdir/%name

%files devel
%doc --no-dereference license.txt
%doc readme.txt
%dir %{ftcgtemplatedir}
%{ftcgtemplatedir}/*conf
%{ftcgtemplatedir}/*txt

%changelog
* Sun Feb 06 2022 Igor Vlasenko <viy@altlinux.org> 1.44-alt7_24
- restored as compat package

* Sun Feb 17 2019 Igor Vlasenko <viy@altlinux.ru> 1.44-alt6_24
- fc update

* Thu Jul 12 2018 Igor Vlasenko <viy@altlinux.ru> 1.44-alt6_21
- merged repocop patch

* Thu Jul 12 2018 Igor Vlasenko <viy@altlinux.ru> 1.44-alt5_21.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * altlinux-policy-rpm-macros-packaging for fontpackages-devel

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.44-alt5_21
- update to new release by fcimport

* Tue Nov 07 2017 Igor Vlasenko <viy@altlinux.ru> 1.44-alt5_19
- cleaned up dependencies (closes: #33161)

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.44-alt4_19
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.44-alt4_18
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.44-alt4_17
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.44-alt4_15
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.44-alt4_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.44-alt4_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.44-alt4_9
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.44-alt4_8
- update to new release by fcimport

* Tue Mar 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.44-alt4_7
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.44-alt4_6
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.44-alt4_5
- update to new release by fcimport

* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.44-alt4_4
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.44-alt4_3
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.44-alt3_3
- update to new release by fcimport

* Mon Aug 08 2011 Igor Vlasenko <viy@altlinux.ru> 1.44-alt3_2
- added req: xorg-font-encodings

* Thu Aug 04 2011 Igor Vlasenko <viy@altlinux.ru> 1.44-alt2_2
- added dependency on rpm-build-fonts

* Mon Aug 01 2011 Igor Vlasenko <viy@altlinux.ru> 1.44-alt1_2
- new version

