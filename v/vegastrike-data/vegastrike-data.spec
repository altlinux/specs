%filter_from_requires /^python2...Briefing.$/d
%filter_from_requires /^python2...Director.$/d
%filter_from_requires /^python2...VS.$/d

%define _unpackaged_files_terminate_build 1
%add_python_req_skip Base
Name:           vegastrike-data
Version:        0.5.1
Release:        alt2_1.r1
Summary:        Data files for Vega Strike
Group:          Games/Other
License:        GPLv2+
URL:            http://vegastrike.sourceforge.net/
#Source0:        %{name}-%{version}.tar.bz2
Source0:        http://downloads.sourceforge.net/vegastrike/vegastrike-data-0.5.1.r1.tar.bz2
Source1:        http://downloads.sourceforge.net/vegastrike/vegastrike-extra-0.5.1.r1.tar.bz2
# Remove Falik's songs from playlists (no longer needed, kept for reference)
Patch0:         vegastrike-data-0.5.0-playlists.patch
BuildArch:      noarch
Requires:       vegastrike >= %{version}
Source44: import.info

%description
Data files for Vega Strike, a GPL 3D OpenGL Action RPG space sim that allows
a player to trade and bounty hunt.

%package -n vegastrike-extra
Summary:        Extra textures for Vega Strike
Group:          Games/Other
Requires:       vegastrike-data >= %{version}

%description -n vegastrike-extra
Extra texture files for Vega Strike. These files are *not* essential to
play Vega Strike.

%prep
%setup -q -b1 -n vegastrike-extra-%{version}.r1
cd ..
%setup -q -n %{name}-%{version}.r1
# some cleanup
# hack due to rpm -bi autocleanup of *.orig
find .. -name "*.orig" -delete
rm -rf cockpits/bomber-cockpit.cpt/#cockpit.xmesh# \
  modules/.cvsignore modules/builtin `find -name "*.xmesh"`
find . -type f -print0 | xargs -0 chmod -x
chmod +x units/findunits.py modules/webpageize.py
sed -i 's/\r//g' documentation/mission_howto.txt
# remove the stale included manpages and the .xls abonimation
rm documentation/*.1 documentation/*.xls
find .vegastrike ai animations bases cockpits communications \
         history meshes mission modules movies programs sectors sounds \
         sprites techniques textures units universe \
         *.xml *.csv *.config *.cur *.xpm New_Game Version.txt \
        -type d | sed -e 's;^;%dir "%{_datadir}/vegastrike/;;s;$;";' | sort -u > data.dirs
find .vegastrike ai animations bases cockpits communications \
         history meshes mission modules movies programs sectors sounds \
         sprites techniques textures units universe \
         *.xml *.csv *.config *.cur *.xpm New_Game Version.txt \
        -type f | sed -e 's;^;"%{_datadir}/vegastrike/;;s;$;";' | sort -u > data.files
cd ..
cp -a vegastrike-extra-%{version}.r1/* %{name}-%{version}.r1
cd %{name}-%{version}.r1
find .vegastrike ai animations bases cockpits communications \
         history meshes mission modules movies programs sectors sounds \
         sprites techniques textures units universe \
         *.xml *.csv *.config *.cur *.xpm New_Game Version.txt \
        -type f | sed -e 's;^;"%{_datadir}/vegastrike/;;s;$;";' | sort -u | \
        comm -2 -3 - data.files > extra.files

# pyc and pyo files are going to be built automatically after the
# install step and we need to list those files.

grep '\.py"$' data.files | sed -e 's;\.py"$;.pyc";' > data.pyc
grep '\.py"$' data.files | sed -e 's;\.py"$;.pyo";' > data.pyo
grep '\.py"$' extra.files | sed -e 's;\.py"$;.pyc";' > extra.pyc
grep '\.py"$' extra.files | sed -e 's;\.py"$;.pyo";' > extra.pyo

%build
# nothing to build data only


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/vegastrike
for i in .vegastrike ai animations bases cockpits communications \
         history meshes mission modules movies programs sectors sounds \
         sprites techniques textures units universe \
         *.xml *.csv *.config *.cur *.xpm New_Game Version.txt; do
  cp -a $i $RPM_BUILD_ROOT%{_datadir}/vegastrike
done
ln -s ../doc/%{name}-%{version} \
  $RPM_BUILD_ROOT%{_datadir}/vegastrike/documentation

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 vegastrike.xpm \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
# multiple -f flags in %files: merging -f extra.pyc into -f extra.files
#cat extra.pyc >> extra.files
# multiple -f flags in %files: merging -f extra.pyo into -f extra.files
#cat extra.pyo >> extra.files
# multiple -f flags in %files: merging -f data.dirs into -f data.files
cat data.dirs >> data.files
# multiple -f flags in %files: merging -f data.pyc into -f data.files
#cat data.pyc >> data.files
# multiple -f flags in %files: merging -f data.pyo into -f data.files
#cat data.pyo >> data.files
# multiple -f flags in %files: merging -f data.dirs into -f data.files
cat data.dirs >> data.files


%files -n vegastrike-extra -f extra.files

%files -f data.files 
%{_datadir}/vegastrike/documentation
%doc vega-license.txt documentation/*
%{_datadir}/icons/hicolor/128x128/apps/vegastrike.xpm


%changelog
* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt2_1.r1
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt2_0.3.beta1.2
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_0.3.beta1.2
- update to new release by fcimport

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt1_0.2.beta1.2.1
- Rebuild with Python-2.7

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_0.2.beta1.2
- update to new release by fcimport

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_6
- converted from Fedora by srpmconvert script

