Group: Graphical desktop/MATE
%define _libexecdir %_prefix/libexec
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
#%%global _internal_version  c147867

Name:           mate-icon-theme-faenza
Version:        1.20.0
Release:        alt1_1
#Release:        0.1.git%{_internal_version}%{?dist}
Summary:        Extra set of icon themes for MATE Desktop
License:        GPLv2+
URL:            http://mate-desktop.org

# To generate tarball
# wget http://git.mate-desktop.org/%%{name}/snapshot/%%{name}-{_internal_version}.tar.xz -O %%{name}-%%{version}.git%%{_internal_version}.tar.xz
#Source0: http://raveit65.fedorapeople.org/Mate/git-upstream/%{name}-%{version}.git%{_internal_version}.tar.xz

Source0:        http://pub.mate-desktop.org/releases/1.20/%{name}-%{version}.tar.xz

BuildRequires: hardlink
BuildRequires: mate-common

BuildArch: noarch
Source44: import.info

%description
Provides a complimentary set of icon themes for MATE Desktop


%prep
%setup -q


# nedded for git snapshots
NOCONFIGURE=1 ./autogen.sh

%build
%configure
%make_build V=1

%install
%{makeinstall_std}

# save space by linking identical images
hardlink -c -v %{buildroot}%{_datadir}/icons


%postun
if [ $1 -eq 0 ] ; then

    /bin/touch --no-create %{_datadir}/icons//matefaenzadark &> /dev/null

    /bin/touch --no-create %{_datadir}/icons//matefaenzagray &> /dev/null

fi

%files
%{_datadir}/icons/matefaenzagray
%{_datadir}/icons/matefaenzadark
%{_datadir}/icons/matefaenza
%doc AUTHORS COPYING README NEWS


%changelog
* Thu Feb 22 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release

* Mon Oct 16 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.19.0-alt1_1
- new fc release

* Wed Sep 06 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.18.1-alt1_2
- new fc release

* Wed Oct 12 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.16.0-alt1_1
- update to mate 1.16

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.0-alt1_1
- new version

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.0-alt1_2
- new fc release

* Sat Mar 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

