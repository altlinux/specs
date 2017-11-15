# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: /usr/bin/desktop-file-install ImageMagick-tools
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           londonlaw
Version:        0.3.0
Release:        alt2_0.6.pre2
Summary:        Online multiplayer version of a well known detective boardgame
License:        GPLv2
Group:          Games/Other
URL:            http://github.com/anyc/londonlaw
Source0:        http://github.com/anyc/londonlaw/archive/v0.3.0_pre2.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}-server.desktop
BuildRequires:  python-devel python-module-wx3.0 ghostscript-utils ghostscript ImageMagick
BuildRequires:  /usr/bin/latex texlive-latex-recommended texlive-latex-recommended desktop-file-utils
BuildArch:      noarch
Requires:       python-module-twisted-conch python-module-twisted-conch-gui python-module-twisted-core python-module-twisted-core-gui python-module-twisted-core-gui-tk python-module-twisted-core-gui-wx python-module-twisted-core-test python-module-twisted-logger python-module-twisted-mail python-module-twisted-names python-module-twisted-news python-module-twisted-pair python-module-twisted-positioning python-module-twisted-runner python-module-twisted-web python-module-twisted-words icon-theme-hicolor
Source44: import.info

%description
London Law is an online multiplayer version of a well known detective
boardgame. The game is unusually asymmetric; one player controls the movements
of the criminal Mr. X as he tries to evade the detectives, while another one to
five players control five detectives trying to track him down. Mr. X has an
advantage in access to transportation routes, and his precise location remains
hidden for most of the game. The detectives have only the advantage of superior
numbers, so they must work in concert to limit the criminal's options. London
Law features an attractive map overlaid on high-resolution satellite imagery.


%prep
%setup -q -n %{name}-%{version}_pre2
chmod +x setup.py


%build
./setup.py build
make -C doc manual.pdf


%install
./setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
convert londonlaw/guiclient/images/playericon1.jpg -resize 48x48 \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE2}


%files
%doc COPYING doc/ChangeLog doc/TODO doc/*.pdf doc/readme.protocol
%{_bindir}/london-*
%{_datadir}/%{name}
%{python_sitelibdir_noarch}/%{name}
%{python_sitelibdir_noarch}/%{name}-%{version}*-py?.?.egg-info
%{_datadir}/applications/*%{name}*.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%changelog
* Wed Nov 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt2_0.6.pre2
- fixed build

* Thu Jun 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt2_0.3.pre2
- drop Req: python-module-twisted-core-gui-gnome

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_0.3.pre2
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_0.2.pre2
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt2_17
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt2_16
- update to new release by fcimport

* Mon Mar 18 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt2_15
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt2_12
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt2_11
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_11
- update to new release by fcimport

* Fri Oct 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.1-alt1_10.1
- Rebuild with Python-2.7

* Fri Jul 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_10
- initial release by fcimport

