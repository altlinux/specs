Group: Development/Other
%filter_from_requires /^.usr.share.fonts$/d
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_without httpd
%bcond_without nginx

Name:           web-assets
Version:        5
Release:        alt3_17
Summary:        A simple framework for bits pushed to browsers
License:        MIT
URL:            https://fedoraproject.org/wiki/User:Patches/PackagingDrafts/Web_Assets
Source0:        LICENSE
Source1:        README.devel
Source2:        macros.web-assets
Source3:        httpd-web-assets.conf
Source4:        nginx-web-assets.conf
BuildArch:      noarch
BuildRequires:  coreutils
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

%package -n rpm-macros-%name
Group: Other
Summary:        RPM macros for Web Assets packaging
License:        MIT
Provides: %name-devel = %{?epoch:%epoch:}%{version}-%{release}

%description -n rpm-macros-%name
%{summary}.

%if %{with httpd}
%package httpd
Group: Other
Summary:        Web Assets aliases for the Apache HTTP daemon
License:        MIT
Requires:       web-assets-filesystem = %{version}-%{release}
Requires:       apache2-base apache2-htcacheclean

%description httpd
%{summary}.
%endif

%if %{with nginx}
%package nginx
Group: Development/Other
Summary:        Web Assets aliases for the nginx daemon
License:        MIT
Requires:       web-assets-filesystem = %{version}-%{release}
Requires:       nginx

%description nginx
%{summary}.
%endif

%prep
%setup -c -T
cp %{SOURCE0} LICENSE
cp %{SOURCE1} README.devel

%build
#nothing to do

%install
mkdir -p %{buildroot}%{_datadir}/web-assets
mkdir -p %{buildroot}%{_datadir}/javascript
ln -sf ../javascript %{buildroot}%{_datadir}/web-assets/javascript
ln -sf ../javascript %{buildroot}%{_datadir}/web-assets/js
ln -sf ../fonts %{buildroot}%{_datadir}/web-assets/fonts
install -Dpm0644 %{SOURCE2} %{buildroot}%{_rpmmacrosdir}/web-assets
%if %{with httpd}
install -Dpm0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/httpd/conf.d/web-assets.conf
%endif
%if %{with nginx}
install -Dpm0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/nginx/default.d/web-assets.conf
%endif

%if %{with httpd}
%post httpd
[ -x %{_bindir}/systemctl ] && reload-or-try-restart httpd.service || :

%postun httpd
[ -x %{_bindir}/systemctl ] && reload-or-try-restart httpd.service || :
%endif

%if %{with nginx}
%post nginx
[ -x %{_bindir}/systemctl ] && systemctl reload-or-try-restart nginx.service || :

%postun nginx
[ -x %{_bindir}/systemctl ] && systemctl reload-or-try-restart nginx.service || :
%endif

%files filesystem
%{_datadir}/web-assets
%{_datadir}/javascript

%files -n rpm-macros-%name
%{_rpmmacrosdir}/web-assets
%doc --no-dereference LICENSE
%doc README.devel

%if %{with httpd}
%files httpd
%config(noreplace) %{_sysconfdir}/httpd/conf.d/web-assets.conf
%doc --no-dereference LICENSE
%endif

%if %{with nginx}
%files nginx
%config(noreplace) %{_sysconfdir}/nginx/default.d/web-assets.conf
%doc --no-dereference LICENSE
%endif

%changelog
* Thu May 12 2022 Igor Vlasenko <viy@altlinux.org> 5-alt3_17
- update

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 5-alt3_6
- update to new release by fcimport

* Fri Feb 19 2016 Igor Vlasenko <viy@altlinux.ru> 5-alt3_4
- added rpm-macros-web-assets

* Thu Dec 31 2015 Igor Vlasenko <viy@altlinux.ru> 5-alt3_3
- to Sisyphus as BR: for mathjax

* Tue Nov 17 2015 Igor Vlasenko <viy@altlinux.ru> 5-alt2_3
- rebuild

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 5-alt1_3
- new version

