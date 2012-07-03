# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:           kitsune
Version:        2.0
Release:        alt3_9
Summary:        Program to solve mathematical problems

Group:          Games/Other
License:        GPLv2+
URL:            http://%{name}.tuxfamily.org/wiki/doku.php?id=homepage
Source0:        http://%{name}.tuxfamily.org/%{name}/%{name}%{version}/%{name}%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        http://%{name}.tuxfamily.org/download.php?url=icons/%{name}-icones.tar.gz

BuildRequires:  qt4-devel
BuildRequires:  desktop-file-utils
Source44: import.info

%description
Kitsune is a software aiming at solving digit problems 
of a famous television game show called "Countdown" in England 
and "Les chiffres et les lettres" in France.

%prep
%setup -q -a 2 -n %{name}%{version}

for f in Changelog.txt txt/gpl-fr.html txt/aide-fr.html txt/licence-fr.html ; do
   %{_bindir}/iconv -f iso8859-1 -t utf-8 ${f} > ${f}.conv && /bin/mv -f ${f}.conv ${f}
   /bin/sed -i -e "s/ISO-8859-1/UTF-8/" ${f} 
done

%build
qmake-qt4
lrelease-qt4 kitsune.pro
make %{?_smp_mflags}


%install

mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 0755 bin/kitsune $RPM_BUILD_ROOT%{_bindir}

for f in 16 22 32 48 64 ; do
  mkdir -p  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${f}x${f}/apps
  install -p -m 0644 %{name}-icones/%{name}-${f}X${f}.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${f}x${f}/apps/%{name}.png || \
  install -p -m 0644 %{name}-icones/%{name}-${f}x${f}.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${f}x${f}/apps/%{name}.png
done

desktop-file-install                                  \
       --dir=$RPM_BUILD_ROOT%{_datadir}/applications    \
       %{SOURCE1}


%files
%doc Changelog.txt txt/*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png


%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_9
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_8
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_8
- update to new release by fcimport

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_7
- converted from Fedora by srpmconvert script

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_7
- converted from Fedora by srpmconvert script

