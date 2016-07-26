%define oldname faience-icon-theme
%global themes Faience Faience-Azur Faience-Ocre Faience-Claire

Name:           icon-theme-faience
Version:        0.5
Release:        alt1_5
Summary:        Faience icon theme
Group:          Graphical desktop/Other

License:        GPLv3
URL:            https://code.google.com/p/faience-theme
Source0:        http://raveit65.fedorapeople.org/Others/Source/%{oldname}_%{version}.tar.xz

# source0 is re-released and cleaned from icons with copyrighted trademarks
# Therefore we use this script to remove them before shipping it.
# runtime require faenza-icon-theme is also removed from index.theme.
# Invoke this script to generate the faience-icon-theme tarball
Source1:        faience-icon-theme-generate-tarball.sh
BuildArch:      noarch
Source44: import.info

%description
The faience icon theme include Faience, Faience-Azur,
Faience-Claire and Faience-Ocre theme.
It is cleaned from any nonfree icons.


%prep
%setup -q -n %{oldname}_%{version}

# unpack the icon tarballs
for theme in %{themes}
do
    tar -zxvf ${theme}.tar.gz &>/dev/null
done

# fix permissions
find . -type d -exec chmod 0755 {} \;
find . -type f -exec chmod 0644 {} \;

# delete icon-cache from source
find -type f -name "icon-theme.cache" -delete -print


%build
# nothing to build


%install
install -dpm 755 $RPM_BUILD_ROOT%{_datadir}/icons

cp -ar %{themes} $RPM_BUILD_ROOT%{_datadir}/icons


%post
for theme in %{themes}
do
    touch --no-create %{_datadir}/icons/${theme} &>/dev/null ||:
done


%postun
if [ $1 -eq 0 ] ; then
    for theme in %{themes}
    do
        touch --no-create %{_datadir}/icons/${theme} &>/dev/null

    done
fi


%files
%doc AUTHORS ChangeLog COPYING README
%{_datadir}/icons/Faience/
%{_datadir}/icons/Faience-Azur/
%{_datadir}/icons/Faience-Claire/
%{_datadir}/icons/Faience-Ocre/


%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_4
- update to new release by fcimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_2
- update to new release by fcimport

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_1
- fc import

