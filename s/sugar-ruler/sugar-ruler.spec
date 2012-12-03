# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-macros-fedora-compat
BuildRequires: python-devel
# END SourceDeps(oneline)
Name:           sugar-ruler
Version:        19
Release:        alt1_1
Summary:        Simple collection of measurement tools

Group:          Graphical desktop/Sugar
License:        GPLv3+
URL:            http://wiki.sugarlabs.org/go/Activities/Ruler
Source0:        http://download.sugarlabs.org/sources/honey/Ruler/Ruler-%{version}.tar.bz2

BuildRequires:  sugar-toolkit gettext
BuildArch:      noarch
Requires:       sugar
Source44: import.info

%description
Ruler is a simple collection of measurement tools that are displayed 
on the screen. Since the OLPC XO computer has a 200 DPI display, the 
rulers are quite accurate. One other hardware, where the display 
resolution is not known, their is a spinner to let the user set the DPI. 
Ruler saves this value to the Journal, so it need not be set on 
subsequent uses of the Activity.

%prep
%setup -q -n Ruler-%{version}


%build
%{__python} ./setup.py build

%install
%{__python} ./setup.py install --prefix=%{buildroot}/%{_prefix}

%find_lang com.laptop.Ruler


%files -f com.laptop.Ruler.lang
%doc COPYING NEWS
%{sugaractivitydir}/Ruler.activity/


%changelog
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 19-alt1_1
- new version; import from fc17 updates

