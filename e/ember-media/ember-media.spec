Name:           ember-media
Version:        0.7.2.1
# No dist tag because this is large noarch game data
Release:        alt1_4
Summary:        Media files for the ember WorldForge client

Group:          Games/Other
License:        GPLv2+ or GFDL
URL:            http://www.worldforge.org/dev/eng/clients/ember
Source0:        http://downloads.sourceforge.net/worldforge/%{name}-%{version}.tar.bz2
BuildArch:      noarch
Requires:       ember >= 0.7.2 ember < 0.7.3 fonts-ttf-dejavu
Obsoletes:      sear-media < 0.6-11
Source44: import.info

%description
Media files for the ember WorldForge client.


%prep
#FIXME
%setup -qn %{name}-0.7.2


%build
# Nothing to build!


%install
install -d $RPM_BUILD_ROOT%{_datadir}/ember/media

# In 0.5.6 media got moved to media subdir
cd media

cp -a * $RPM_BUILD_ROOT%{_datadir}/ember/media

# Remove doc files from installed media files
rm -f $RPM_BUILD_ROOT%{_datadir}/ember/media/shared/{COPYING.txt,LICENSING.txt,README}
rm -f $RPM_BUILD_ROOT%{_datadir}/ember/media/user/{COPYING.txt,LICENSING.txt,README}

# Use system DejaVu fonts
rm -f $RPM_BUILD_ROOT%{_datadir}/ember/media/shared/common/themes/ember/gui/fonts/{DejaVuSans,DejaVuSans-Bold}.ttf
cd $RPM_BUILD_ROOT%{_datadir}/ember/media/shared/common/themes/ember/gui/fonts/
ln -s ../../../../../../../../fonts/ttf/dejavu/{DejaVuSans,DejaVuSans-Bold}.ttf .
rm -f $RPM_BUILD_ROOT%{_datadir}/ember/media/shared/core/DejaVuSans.ttf
cd $RPM_BUILD_ROOT%{_datadir}/ember/media/shared/core/
ln -s ../../../../fonts/ttf/dejavu/DejaVuSans.ttf .


%files
%doc media/shared/COPYING.txt media/shared/LICENSING.txt media/shared/core/LICENSE media/shared/core/AUTHORS
%dir %{_datadir}/ember
%{_datadir}/ember/media


%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.2.1-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.7.2.1-alt1_3
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.2.1-alt1_2
- update to new release by fcimport

* Thu Sep 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2.1-alt1
- Version 0.7.2.1

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_4
- update to new release by fcimport

* Sat Jun 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_3
- new fc release

* Wed May 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_2
- initial fc import

