Group: Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
BuildRequires: /usr/bin/git
Name:             adobe-mappings-cmap
Summary:          CMap resources for Adobe's character collections
Version:          20230118
Release:          alt1_1
License:          BSD

URL:              https://www.adobe.com/
Source:           https://github.com/adobe-type-tools/cmap-resources/archive/%{version}.tar.gz#/cmap-resources-%{version}.tar.gz

BuildArch:        noarch
BuildRequires:    git

# The cmap-resources package duplicated this one (albeit with different
# installation paths). It was retired for F36. Provide an upgrade path.
%global crversion %(echo '%{version}' | \
    awk '{print substr($0,1,4)"."substr($0,5,2)"."substr($0,7)}')
Provides:         cmap-resources = %{crversion}-6.%{release}
Obsoletes:        cmap-resources < 2019.07.30-6
Provides:         cmap-resources-cns1-6 = %{crversion}-6.%{release}
Obsoletes:        cmap-resources-cns1-6 < 2019.07.30-6
Provides:         cmap-resources-cns1-7 = %{crversion}-6.%{release}
Obsoletes:        cmap-resources-cns1-7 < 2019.07.30-6
Provides:         cmap-resources-gb1-5 = %{crversion}-6.%{release}
Obsoletes:        cmap-resources-gb1-5 < 2019.07.30-6
Provides:         cmap-resources-japan1-7 = %{crversion}-6.%{release}
Obsoletes:        cmap-resources-japan1-7 < 2019.07.30-6
Provides:         cmap-resources-korea1-2 = %{crversion}-6.%{release}
Obsoletes:        cmap-resources-korea1-2 < 2019.07.30-6
Provides:         cmap-resources-identity-0 = %{crversion}-6.%{release}
Obsoletes:        cmap-resources-identity-0 < 2019.07.30-6
Provides:         cmap-resources-kr-9 = %{crversion}-6.%{release}
Obsoletes:        cmap-resources-kr-9 < 2019.07.30-6
Source44: import.info

%description
CMap (Character Map) resources are used to unidirectionally map character codes,
such as Unicode encoding form, to CIDs (Character IDs -- meaning glyphs) of a
CIDFont resource.

These CMap resources are useful for some applications (e.g. Ghostscript) to
correctly display text containing Japanese, (Traditional) Chinese, or Korean
characters.

# === SUBPACKAGES =============================================================

%package deprecated
Group: Other
Summary:          Deprecated CMap resources for Adobe's character collections
Requires:         %{name} = %{version}-%{release}

Provides:         cmap-resources-japan2-0 = %{crversion}-6.%{release}
Obsoletes:        cmap-resources-japan2-0 < 2019.07.30-6

%description deprecated
This sub-package contains currently deprecated CMap resources that some
applications might still require to function properly.

%package devel
Group: Other
Summary:          RPM macros for Adobe's CMap resources for character collections
Requires:         %{name} = %{version}-%{release}
Requires:         %{name}-deprecated = %{version}-%{release}

%description devel
This package is useful for development purposes only. It installs RPM
macros useful for building packages against %{name},
as well as all the fonts contained in this font set.

# === BUILD INSTRUCTIONS ======================================================

# NOTE: This package provides only resource files, which are already
#       "pre-compiled" to smallest size possible, but they still remain in
#       postscript format as intended. That's why there is no %%build phase.

%prep
%setup -q -n cmap-resources-%{version}
git init -q
git config user.name "rpmbuild"
git config user.email "<rpmbuild>"
git config gc.auto 0
git add --force .
git commit -q --allow-empty -a --author "rpmbuild <rpmbuild>" -m "%{NAME}-%{VERSION} base"


%install
%makeinstall_std prefix=%{_prefix}

# Generate the macro containing the root path to our mappings files:
install -m 0755 -d %{buildroot}%{_rpmmacrosdir}

cat > %{buildroot}%{_rpmmacrosdir}/macros.%{name} << _EOF
%%adobe_mappings_rootpath     %{_datadir}/adobe/resources/mapping/
_EOF

# === PACKAGING INSTRUCTIONS ==================================================

%files
%doc README.md VERSIONS.txt
%doc --no-dereference LICENSE.md

# Necessary directories ownership (to remove them correctly when uninstalling):
%dir %{_datadir}/adobe
%dir %{_datadir}/adobe/resources
%dir %{_datadir}/adobe/resources/mapping

%{_datadir}/adobe/resources/mapping/CNS1
%{_datadir}/adobe/resources/mapping/GB1
%{_datadir}/adobe/resources/mapping/Identity
%{_datadir}/adobe/resources/mapping/Japan1
%{_datadir}/adobe/resources/mapping/Korea1
%{_datadir}/adobe/resources/mapping/KR

%files deprecated
%{_datadir}/adobe/resources/mapping/deprecated

%files devel
%{_rpmmacrosdir}/macros.%{name}

# =============================================================================

%changelog
* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 20230118-alt1_1
- update to new release by fcimport

* Mon Oct 25 2021 Igor Vlasenko <viy@altlinux.org> 20190730-alt1_2
- update to new release by fcimport

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 20171205-alt1_9
- update to new release by fcimport

* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 20171205-alt1_6
- new version

