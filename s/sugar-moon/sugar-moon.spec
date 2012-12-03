# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name: sugar-moon
Version: 14
Release: alt1_1
Summary: Moon phases activity for sugar

Group: Graphical desktop/Sugar
License: GPLv2+
BuildArch: noarch
URL: http://wiki.laptop.org/go/Moon
Source0: http://download.sugarlabs.org/sources/honey/Moon/Moon-%{version}.tar.bz2

BuildRequires: gettext
BuildRequires: python-devel
BuildRequires: sugar-toolkit
Requires: sugar
Requires: python-module-simplejson
Source44: import.info

%description
Moon is a simple Lunar phase activity for Sugar.

%prep
%setup -q -n Moon-%{version}

%build
python ./setup.py build

%install
mkdir -p $RPM_BUILD_ROOT%{sugaractivitydir}
python ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}

%find_lang com.garycmartin.Moon

%files -f com.garycmartin.Moon.lang
%doc COPYING AUTHORS
%{sugaractivitydir}/Moon.activity/

%changelog
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 14-alt1_1
- new version; import from fc17 updates

