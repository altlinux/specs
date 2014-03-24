%define oldname dmz-cursor-themes
Name:           x-cursor-themes-dmz
Version:        0.4
Release:        alt2_8
Summary:        X cursors themes

Group:          Graphical desktop/Other
License:        CC-BY-SA
URL:            http://jimmac.musichall.cz/themes.php?skin=7

%define checkout 0359f226

# NB: The tarball needs to be generated first, so the first download will fail.
#     Generating takes about 30s - 1 minute.
# wget http://gitorious.org/opensuse/art/archive-tarball/%{checkout}
# tar xzf %{checkout}
# cd opensuse-art/cursors
# tar chof - dmz dmz-aa | bzip2 -9 -c > dmz-cursor-themes-%{checkout}.tar.bz2
Source0:        dmz-cursor-themes-%{checkout}.tar.bz2

BuildArch:      noarch
Source44: import.info

%description
An X cursors theme by Jakub Steiner used by OpenSUSE.

%prep
%setup -n %{oldname}-%{version} -q -c dmz-cursor-themes-%{version}

%build

%install

mkdir -p %{buildroot}/%{_datadir}/icons/dmz
cp -pr dmz/xcursors %{buildroot}/%{_datadir}/icons/dmz/cursors
mkdir -p %{buildroot}/%{_datadir}/icons/dmz-aa
cp -pr dmz-aa/xcursors %{buildroot}/%{_datadir}/icons/dmz-aa/cursors

%files
%doc dmz/COPYING
%{_datadir}/icons/dmz/
%{_datadir}/icons/dmz-aa/

%changelog
* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_8
- moved to Sisyphus for mate-themes-extras

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_8
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_7
- update to new release by fcimport

* Fri Dec 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_6
- fc import

