# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-macros-fedora-compat
BuildRequires: gcc-c++ pkgconfig(gtk+-2.0) pkgconfig(x11) python-devel
# END SourceDeps(oneline)
Name:           sugar-xoirc
Version:        10
Release:        alt1_2
Summary:        IRC client for Sugar

Group:          Graphical desktop/Sugar
License:        GPLv2+
URL:            http://git.sugarlabs.org/projects/irc
Source0:        http://download.sugarlabs.org/sources/honey/IRC/IRC-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  sugar-toolkit
Requires:       sugar
Source44: import.info


%description
This activity allows you to contact other OLPC users and enthusiasts
on the internet, and chat with them. 


%prep
%setup -q -n IRC-%{version}

chmod -x {purk/scripts/ignore.py,purk/scripts/console.py,purk/scripts/timeout.py,purk/scripts/alias.py}
chmod +x setup.py
rm -rf NEWS

%build
python ./setup.py build


%install
python ./setup.py install --prefix=%{buildroot}/%{_prefix}


%files
%doc README TODO
%{sugaractivitydir}/IRC.activity/


%changelog
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 10-alt1_2
- new version; import from fc17 updates

