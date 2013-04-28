# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Name:           sugar-words
Version:        19
Release:        alt1_3
Summary:        A multi lingual dictionary with speech synthesis

Group:          Graphical desktop/Sugar
License:        GPLv3+
URL:            http://activities.sugarlabs.org/en-US/sugar/addon/4315
Source0:        http://mirrors.rit.edu/sugarlabs/activities/4315/words-%{version}.xo

BuildRequires:  python-devel sugar-toolkit-gtk3 gettext
BuildArch:      noarch
Requires:       sugar >= 0.97.0
Source44: import.info

%description
Words is a multi lingual dictionary for sugar. It is enabled 
with speech synthesis.

%prep
%setup -q -n Words.activity
rm po/aym.po
rm po/cpp.po
rm po/nah.po
rm po/son.po

%build
%{__python} ./setup.py build

%install
%{__python} ./setup.py install --prefix=%{buildroot}/%{_prefix}

%find_lang org.laptop.Words

%files -f org.laptop.Words.lang
%doc NEWS AUTHORS HACKING
%{sugaractivitydir}/Words.activity/

%changelog
* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 19-alt1_3
- initial fc import

