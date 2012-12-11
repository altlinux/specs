# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
%define date 20090128

Name:           sugar-xomail
Version:        0
Release:        alt1_0.7.20090128
Summary:        Xomail for Sugar

Group:          Graphical desktop/Sugar
License:        GPLv2+
URL:            http://wiki.laptop.org/go/Projects/xomail
Source0:        Xomail-%{version}.%{date}.tar.bz2
Source1:        %{name}-checkout.sh
BuildArch:      noarch

BuildRequires:  sugar-toolkit

Requires:       sugar
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity


%description
Mail activity for the Sugar Desktop.


%prep
%setup -q -n Xomail-%{version}.%{date}


%build
python ./setup.py build
chmod -x mailactivity.py


%install
python ./setup.py install --prefix=%{buildroot}/%{_prefix}


%files
%{sugaractivitydir}/Mail.activity/


%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.7.20090128
- new version; import from fc18

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.6.20090128
- new version; import from fc17 updates

