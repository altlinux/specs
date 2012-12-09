# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: python-devel
# END SourceDeps(oneline)
Name:           sugar-analyze
Version:        8
Release:        alt1_10
Summary:        Analysing tool for Sugar

Group:          Graphical desktop/Sugar
License:        GPLv2+
URL:            http://wiki.laptop.org/go/Analyze
Source0:        http://dev.laptop.org/pub/sugar/sources/Analyze/Analyze-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  sugar-toolkit
Requires:       sugar
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity


%description
The Analyze activity helps developers analyze their system. Along with 
Log Viewer and Terminal, one of three activities that used to make up 
the developer console.

%prep
%setup -q -n Analyze-%{version}


%build
python ./setup.py build

%install
./setup.py install --prefix=%{buildroot}/%{_prefix}


%files
%doc README NEWS
%{sugaractivitydir}/Analyze.activity/


%changelog
* Sun Dec 09 2012 Igor Vlasenko <viy@altlinux.ru> 8-alt1_10
- new version; import from fc18

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 8-alt1_9
- new version; import from fc17 updates

