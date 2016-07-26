Summary:   Themes for Enlightenment, DR16
Name:      e16-themes
Version:   1.0.1
Release:   alt1_8
License:   MIT with advertising
Group:     Graphical desktop/Other
URL:       http://www.enlightenment.org/
#
# Use create-clean-tarball.sh script to create the cleaned tarball
# from the original tarball:
#   http://downloads.sourceforge.net/enlightenment/e16-themes-%{version}.tar.gz
#
Source0:   e16-themes-cleaned-%{version}.tar.gz
Source1:   create-clean-tarball.sh
BuildArch: noarch
Requires:  e16 >= 1.0.0
Source44: import.info

%description
The BlueSteel, BrushedMetal-Tigert, Ganymede and ShinyMetal themes
for Enlightenment, DR16.  

This is part of the Enlightenment distribution.

%prep
%setup -q

%build
%configure --enable-fsstd
%{__make}

%install
%{__make} install DESTDIR=%{buildroot} INSTALL="%{__install} -p"
%{__rm} -rfv %{buildroot}%{_datadir}/e16/themes/ShinyMetal/epplets/images/.xvpics
%{__chmod} 0755 %{buildroot}%{_datadir}/e16/themes/Ganymede/ACTIVATE_BUTTONS
# symlink all font configs to default theme
for theme in BlueSteel BrushedMetal-Tigert Ganymede ShinyMetal ; do
    %{__rm} -f %{buildroot}%{_datadir}/e16/themes/$theme/fonts.theme.cfg
    %{__ln_s} ../winter/fonts.theme.cfg \
       %{buildroot}%{_datadir}/e16/themes/$theme/fonts.theme.cfg
done
# Remove refs to removed fonts
%{__sed} -i -r -e 's/face=(aircut3,ganymede|rothwell|vixar|zirkle)/face=Vera/g' \
    %{buildroot}%{_datadir}/e16/themes/*/ABOUT/MAIN

%files
%doc AUTHORS COPYING
%{_datadir}/e16/themes

%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_8
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_4
- update to new release by fcimport

* Thu Dec 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_3
- fc import

