Name:		avoision
Version:	0.6
Release:	alt2_5
Summary:	Arcade style game of evade and capture
Group:		Text tools
# Code is GPLv2+, music and graphics are CC-BY-SA
License:	GPLv2+ and CC-BY-SA
URL:		http://avsn.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/avsn/%{name}-%{version}.tar.gz
Source1:	%{name}.png
Source2:	%{name}.desktop
BuildRequires:	radius-engine-devel desktop-file-utils zip
Source44: import.info

%description
Avoision is a straightforward, yet captivating distillation of vintage arcade 
entertainment requiring strategy, precision, and perseverance with a singular 
objective: capture the red square while evading innumerable cruel, spiteful 
white squares.

%prep
%setup -q
chmod -x License.txt ChangeLog *.c

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/pixmaps/
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications	%{SOURCE2}

%files
%doc License.txt ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_5
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_5
- update to new release by fcimport

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_4
- update to new release by fcimport

* Sat Dec 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_3
- update to new release by fcimport

* Fri Jul 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_2
- initial release by fcimport

