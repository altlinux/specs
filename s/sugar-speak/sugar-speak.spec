# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-macros-fedora-compat
BuildRequires: pkgconfig(gtk+-2.0) pkgconfig(x11) python-devel
# END SourceDeps(oneline)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

Name:           sugar-speak
Version:        41
Release:        alt1_1
Summary:        Speak for Sugar

Group:          Graphical desktop/Sugar
License:        GPLv2+ and GPLv3+
URL:            http://wiki.laptop.org/go/Speak
Source0:        http://download.sugarlabs.org/activities/4038/speak-%{version}.xo
BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  sugar-toolkit
Requires:       sugar
Requires:       python-module-numpy
Requires:       espeak
Source44: import.info

%description
Speak is a talking face for the XO laptop. Anything you type will be spoken
aloud using the XO's speech synthesizer, espeak. You can adjust the accent,
rate and pitch of the voice as well as the shape of the eyes and mouth. This
is a great way to experiment with the speech synthesizer, learn to type or 
just have fun making a funny face for your XO.  

%prep
%setup -q -n Speak.activity
rm -rf .0sugar bot

%build
python ./setup.py build

%install
python ./setup.py install --prefix=%{buildroot}%{_prefix}
find  %{buildroot}%{sugaractivitydir}Speak.activity/activity.py  -type f -name \* -exec chmod 644 {} \;
%find_lang vu.lux.olpc.Speak

%files -f vu.lux.olpc.Speak.lang
%doc NEWS COPYING
%{sugaractivitydir}/Speak.activity/

%changelog
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 41-alt1_1
- new version; import from fc17 updates

