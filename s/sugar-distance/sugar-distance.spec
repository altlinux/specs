# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Name:           sugar-distance
Version:        34
Release:        alt1_1.qa1
Summary:        Distance measurement for Sugar

Group:          Graphical desktop/Sugar
License:        GPLv2+
URL:            http://wiki.laptop.org/go/Distance
Source0:        http://mirrors.ibiblio.org/pub/mirrors/sugar/activities/4264/distance-%{version}.xo

BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  python-devel
BuildRequires:  sugar-toolkit-gtk3
Requires:       sugar >= 0.97.0
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity

%description
Distance (aka Acoustic Tape Measure) determines the physical distance 
between two XOs by measuring how long it takes sound pulses to travel 
between them. 

%prep
%setup -q -n Distance.activity


%build
python ./setup.py build


%install
mkdir -p %{buildroot}%{sugaractivitydir}
./setup.py install --prefix=%{buildroot}/%{_prefix}
find %{buildroot}%{sugaractivitydir}Distance.activity/arange.py -type f -name \* -exec chmod 644 {} \;

%find_lang org.laptop.AcousticMeasure

# It is the file in the package whose name matches the format emacs or vim uses 
# for backup and autosave files. It may have been installed by  accident.
find $RPM_BUILD_ROOT \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete
# failsafe cleanup if the file is declared as %%doc
find . \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete

%files -f org.laptop.AcousticMeasure.lang
%doc NEWS
%{sugaractivitydir}/Distance.activity/


%changelog
* Mon Apr 22 2013 Repocop Q. A. Robot <repocop@altlinux.org> 34-alt1_1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * backup-file-in-package for sugar-distance

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 34-alt1_1
- update from fc18 release

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 31-alt1_1
- new version; import from fc17 updates

