# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: python-devel
# END SourceDeps(oneline)
%filter_from_requires /^python....PeriodicSaveThread.$/d
%filter_from_requires /^python....defs.$/d
Name:           sugar-labyrinth
Version:	14
Release:        alt1_2
Summary:        A lightweight mind-mapping activity for Sugar

Group:          Graphical desktop/Sugar
License:        GPLv2+
URL:            http://wiki.sugarlabs.org/go/Activities/Labyrinth
Source0:        http://download.sugarlabs.org/sources/honey/Labyrinth/Labyrinth-%{version}.tar.bz2

BuildRequires:  gettext sugar-toolkit
BuildArch:      noarch
Requires:       sugar
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity

%description
A lightweight mind-mapping activity based on an Open Source project called
Labyrinth. It allows creating mind maps from a mixture of text, freehand
drawings, and images from your Journal. There is an infinite sized canvas
for your map that can be panned and zoomed while you work. Maps can be
"Kept to PDF" for uploading to web sites, sharing, and printing by others
who may not be using Sugar. 


%prep
%setup -q -n Labyrinth-%{version}

# remove these shebangs to calm rpmlint down
for Files in src/TextThought.py src/MMapArea.py labyrinthactivity.py src/labyrinth.py; do
  %{__sed} -i.orig -e 1d ${Files}
  touch -r ${Files}.orig ${Files}
  %{__rm} ${Files}.orig
done


%build
python ./setup.py build


%install
python ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}

%find_lang org.gnome.Labyrinth

# Remove empty file
rm $RPM_BUILD_ROOT/%{_datadir}/sugar/activities/Labyrinth.activity/port/TODO

%files -f org.gnome.Labyrinth.lang
%doc AUTHORS COPYING NEWS README
%{sugaractivitydir}/Labyrinth.activity/


%changelog
* Wed Dec 12 2012 Igor Vlasenko <viy@altlinux.ru> 14-alt1_2
- new version; import from fc18

