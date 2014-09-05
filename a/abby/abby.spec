# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libqt4-devel
# END SourceDeps(oneline)
Name:           abby
Version:        0.4.8
Release:        alt3
Summary:        Front-end for cclive and clive
Packager: Ilya Mashkin <oddity@altlinux.ru>
Group:          Video
License:        GPLv3+
URL:            http://code.google.com/p/abby/
Source0:        http://%{name}.googlecode.com/files/%{name}-%{version}.tar.bz2

BuildRequires:  qt4-devel desktop-file-utils
Requires:       cclive
Source44: import.info

%description
abby is a front-end for clive and cclive, allowing users unfamiliar with
command-line interfaces to make most of cclive using a graphical
user-interface. abby is written in C++. 

%prep
%setup -q
echo "[Desktop Entry]" > %{name}.desktop
echo "Name=abby" >> %{name}.desktop
echo "GenericName=abby" >> %{name}.desktop
echo "Comment=Front-end for cclive and clive" >> %{name}.desktop
echo "Exec=abby" >> %{name}.desktop
echo "Terminal=false" >> %{name}.desktop
echo "Type=Application" >> %{name}.desktop
echo "Categories=Network;FileTransfer;Qt;" >> %{name}.desktop


%build
qmake-qt4
make %{?_smp_mflags}


%install
install -d $RPM_BUILD_ROOT%{_bindir}
install -Dm 755 -p %{name} $RPM_BUILD_ROOT%{_bindir}
desktop-file-install --vendor=""   \
       --dir=%{buildroot}%{_datadir}/applications/   \
       %{name}.desktop


%files
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop


%changelog
* Fri Sep 05 2014 Ilya Mashkin <oddity@altlinux.ru> 0.4.8-alt3
- build for Sisyphus

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt2_6
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt2_5
- update to new release by fcimport

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt2_4
- update to new release by fcimport

* Tue May 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt2_3
- regenerated with 0.46 R::S::C

* Fri May 18 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.8-alt1_3
- converted for Sisyphus

