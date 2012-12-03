# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

Name: sugar-abacus
Version: 35
Release: alt1_1
Summary: A simple abacus activity for Sugar

Group: Graphical desktop/Sugar
License: LGPLv3+
URL: http://activities.sugarlabs.org/addon/4293
Source0: http://download.sugarlabs.org/sources/honey/Abacus/Abacus-%{version}.tar.bz2

BuildArch: noarch
BuildRequires: python-devel
BuildRequires: sugar-base
BuildRequires: sugar-toolkit-gtk3
BuildRequires: gettext
Requires: sugar >= 0.95.0
Source44: import.info

%description
Abacus lets the learner explore different representations of numbers using 
different mechanical counting systems developed by the ancient Romans and 
Chinese. There are several different variants available for exploration: a 
suanpan, the traditional Chinese abacus with 2 beads on top and 5 beads below; 
a soroban, the traditional Japanese abacus with 1 bead on top and 4 beads below;
the schety, the traditional Russian abacus, with 10 beads per column, with the 
exception of one column with just 4 beads used for counting in fourths; and the 
nepohualtzintzin, the traditional Mayan abacus, with 3 beads on top and 4 beads 
below (it uses base 20).

%prep
%setup -q -n Abacus-%{version}

%build
python ./setup.py build

# %find_lang org.sugarlabs.AbacusActivity

%install
python ./setup.py install --prefix=%{buildroot}/%{_prefix}

%find_lang org.sugarlabs.AbacusActivity

%files -f org.sugarlabs.AbacusActivity.lang
%doc COPYING NEWS
%{sugaractivitydir}/Abacus.activity/

%changelog
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 35-alt1_1
- new version; import from fc17 updates

