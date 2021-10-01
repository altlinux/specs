Group: Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# spec file for package battray
#

Name:           battray
Version:        2.3
Release:        alt1_19
Summary:        Tool for displaying a laptop's battery status in the system traiy
License:        MIT
URL:            http://arp242.net/code/battray/
Source0:        https://github.com/Carpetsmoker/battray/archive/version-%{version}/%{name}-version-%{version}.tar.bz2

BuildArch:      noarch
BuildRequires:  python3-module-distribute
BuildRequires:  python3-devel
Requires:       python3
Requires:       python3-module-notify2
Source44: import.info

%description
Battray is a fairly simple tray icon to show a laptopa.'s battery status. Ita.'s 
simple, easy, fairly environment-independent, and a.'just worksa.' without tons of
{Gnome,KDE,..} dependencies.

One can also configure it to play annoying sounds if your battery is getting 
low, dim the screen when you switch from AC to battery, etc.

%prep
%setup -q -n %{name}-version-%{version}

%build
%python3_build

%install
%python3_install

%files
%{python3_sitelibdir_noarch}/*
%{_bindir}/%{name}
%{_datadir}/%{name}
%doc README.markdown
%doc --no-dereference LICENSE

%changelog
* Fri Oct 01 2021 Igor Vlasenko <viy@altlinux.org> 2.3-alt1_19
- update to new release by fcimport

* Thu Oct 17 2019 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_11
- update to new release by fcimport

* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_10
- new version

