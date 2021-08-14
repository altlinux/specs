Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
%define oldname material-icons-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define _fontstem material-icons
Version:        4.0.0
Release:        alt1_0
URL:            https://google.github.io/material-design-icons/

Source0:        https://github.com/google/material-design-icons/archive/%{version}/material-design-icons-%{version}.tar.gz
Source1:        65-%{oldname}.conf
Source2:        %{oldname}.metainfo.xml

%global fontlicense     ASL 2.0
%global fontlicenses    LICENSE
%global fontdocs        README.md
%global fontfamily      Material Icons
%global fontsummary     Google material design system icons
%global fonts           font/*.otf font/*.ttf
%global fontconfs       65-%{oldname}.conf

%global fontdescription \
Material design icons is the official icon set from Google.  The icons\
are designed under the material design guidelines.

BuildRequires:  fontpackages-devel

Name:           fonts-ttf-material-icons
Summary:        %{fontsummary}
License:        %{fontlicense}
BuildArch:      noarch
BuildRequires:  rpm-macros-fonts
Source44: import.info

%description -n fonts-ttf-material-icons
%{?fontdescription}

%prep
%setup -q -n material-design-icons-%{version}

%build

%install
mkdir -p %{buildroot}%{_fontbasedir}/{ttf,otf}/%{_fontstem}/
install -m 644 font/*.ttf %{buildroot}%{_fontbasedir}/ttf/%{_fontstem}/
install -m 644 font/*.otf %{buildroot}%{_fontbasedir}/otf/%{_fontstem}/
install -D -m644 %SOURCE2 %{buildroot}%{_metainfodir}/%{oldname}.metainfo.xml
install -D -m644 %SOURCE1 %{buildroot}%{_fontconfig_templatedir}/%{fontconfs}
mkdir -p %{buildroot}%{_fontconfig_confdir}
ln -s %{_fontconfig_templatedir}/%{fontconfs} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconfs}

%files -n fonts-ttf-material-icons
%doc README.md
%{_fontconfig_templatedir}/%{fontconfs}
%config(noreplace) %{_fontconfig_confdir}/%{fontconfs}
%{_fontbasedir}/ttf/%{_fontstem}/*.ttf
%{_fontbasedir}/otf/%{_fontstem}/*.otf
%{_metainfodir}/%{oldname}.metainfo.xml

%changelog
* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 4.0.0-alt1_0
- new version

