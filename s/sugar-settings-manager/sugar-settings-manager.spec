# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(gtk+-2.0) pkgconfig(x11)
# END SourceDeps(oneline)
Name:           sugar-settings-manager
Version:        0.87.2
Release:        alt1_6
Summary:        Settings manager for the Sugar environment

Group:          System/Servers
License:        MIT
URL:            http://git.sugarlabs.org/projects/sugar-settings-manager
Source0:        http://download.sugarlabs.org/sources/external/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gtk2-devel
BuildRequires:  libGConf-devel
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity

%description
A daemon which manages and monitors various UI related settings via the
XSETTINGS specifications.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc COPYING README
%{_bindir}/%{name}


%changelog
* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.87.2-alt1_6
- update from fc18 release

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.87.2-alt1_5
- new version; import from fc17 updates

