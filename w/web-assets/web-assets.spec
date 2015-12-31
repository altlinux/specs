Group: Other
%filter_from_requires /^.usr.share.fonts$/d
#disable the httpd stuff while we're waiting on getting the path issues
#cleared up
%global enable_httpd 1

Name:           web-assets
Version:        5
Release:        alt3_3
Summary:        A simple framework for bits pushed to browsers
BuildArch:      noarch

License:        MIT
URL:            https://fedoraproject.org/wiki/User:Patches/PackagingDrafts/Web_Assets

Source1:        LICENSE
Source2:        macros.web-assets
Source3:        web-assets.conf
Source4:        README.devel
Source44: import.info

%description
%{summary}.

%package filesystem
Group: Other
Summary:        The basic directory layout for Web Assets
#there's nothing copyrightable about a few directories and symlinks
License:        Public Domain

%description filesystem
%{summary}.

%package devel
Group: Other
Summary:        RPM macros for Web Assets packaging
License:        MIT
Requires:       web-assets-filesystem = %{version}-%{release}

%description devel
%{summary}.

%if 0%{?enable_httpd}
%package httpd
Group: Other
Summary:        Web Assets aliases for the Apache HTTP daemon
License:        MIT
Requires:       web-assets-filesystem = %{version}-%{release}
Requires:       httpd

%description httpd
%{summary}.
%endif

%prep
%setup -c -T
cp %{SOURCE1} LICENSE
cp %{SOURCE4} README.devel

%build
#nothing to do

%install
mkdir -p %{buildroot}%{_datadir}/web-assets
mkdir -p %{buildroot}%{_datadir}/javascript

ln -sf ../javascript %{buildroot}%{_datadir}/web-assets/javascript
ln -sf ../javascript %{buildroot}%{_datadir}/web-assets/js
ln -sf ../fonts %{buildroot}%{_datadir}/web-assets/fonts

install -Dpm0644 %{SOURCE2} %{buildroot}%{_rpmmacrosdir}/macros.web-assets

%if 0%{?enable_httpd}
install -Dpm0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/httpd/conf.d/web-assets.conf

%endif
%files filesystem
%{_datadir}/web-assets
%{_datadir}/javascript

%files devel
%{_rpmmacrosdir}/macros.web-assets
%doc LICENSE README.devel

%if 0%{?enable_httpd}
%files httpd
%config(noreplace) %{_sysconfdir}/httpd/conf.d/web-assets.conf
%doc LICENSE
%endif

%changelog
* Thu Dec 31 2015 Igor Vlasenko <viy@altlinux.ru> 5-alt3_3
- to Sisyphus as BR: for mathjax

* Tue Nov 17 2015 Igor Vlasenko <viy@altlinux.ru> 5-alt2_3
- rebuild

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 5-alt1_3
- new version

