# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-macros-fedora-compat
BuildRequires: python-devel
# END SourceDeps(oneline)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

Name:           sugar-record
Version:        96
Release:        alt1_1
Summary:        Recording tool for Sugar

Group:          Graphical desktop/Sugar
License:        MIT
URL:            http://wiki.laptop.org/go/Record
Source0:        http://mirrors.ibiblio.org/pub/mirrors/sugar/activities/4081/record-%{version}.xo

BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  sugar-toolkit

Requires:       sugar
Requires:       gst-plugins-good
Source44: import.info

%description
Record is the basic rich-media capture activity for the laptop. It 
lets you capture still images, video, and/or audio. It has a simple 
interface and works in both laptop and ebook mode. An interface for 
sharing pictures among multi XOs during a picture-taking session is
a hallmark of the Record activity

%prep
%setup -q -n Record.activity

%build
python ./setup.py build

%install
python ./setup.py install --prefix=%{buildroot}/%{_prefix}

%find_lang org.laptop.RecordActivity

%files -f org.laptop.RecordActivity.lang
%doc COPYING NEWS
%{sugaractivitydir}/Record.activity/

%changelog
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 96-alt1_1
- new version; import from fc17 updates

