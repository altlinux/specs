Name:           ember-media
Version:        0.7.0
# No dist tag because this is large noarch game data
Release:        alt1_3
Summary:        Media files for the ember WorldForge client

Group:          Games/Other
License:        GPLv2+ or GFDL
URL:            http://www.worldforge.org/dev/eng/clients/ember
Source0:        http://downloads.sourceforge.net/worldforge/%{name}-%{version}.tar.bz2
BuildArch:      noarch

Requires:       ember >= 0.7.0 ember < 0.7.1 fonts-ttf-dejavu

Obsoletes:      sear-media < 0.6-11
Source44: import.info

%description
Media files for the ember WorldForge client.


%prep
%setup -q


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
%doc media/user/COPYING.txt media/user/LICENSING.txt media/user/README
%dir %{_datadir}/ember
%{_datadir}/ember/media



%changelog
* Sat Jun 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_3
- new fc release

* Wed May 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_2
- initial fc import

