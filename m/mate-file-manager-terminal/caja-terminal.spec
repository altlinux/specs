# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define oldname caja-terminal
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# package include only on python file
# in result debuginfo is empty
%global debug_package %{nil}

Name:           mate-file-manager-terminal
Version:        0.10
Release:        alt1_3
Summary:        Terminal embedded in Caja
Group:          Shells
License:        GPLv3+
URL:            https://github.com/yselkowitz/%{oldname}
Source0:        https://github.com/yselkowitz/caja-terminal/archive/%{oldname}-%{version}.tar.gz

# only for rhel
Patch0:         caja-terminal_rhel-doc-dir-with-version.patch

BuildRequires:  gettext gettext-tools python-devel

# needed for run caja-terminal
Requires:       python-module-pygobject3 python-module-caja vte3 python-module-pyxdg
Source44: import.info
BuildArch: noarch

%description
Caja Terminal is a terminal embedded in Caja, the MATE file browser.
It is always open in the current folder, and follows the navigation
(like an automated "cd" command).

%prep
%setup -n %{oldname}-%{version} -q

sed -i -e 's~#!/usr/bin/python~#!%{__python}~g' code/caja-terminal.py
# move doc dir for rhel
%if 0%{?rhel}
%patch0 -p1 -b .rhel-doc-dir
%endif

%build
# no build needed

%install
mkdir -p $RPM_BUILD_ROOT
%{makeinstall_std}

bash install.sh --package $RPM_BUILD_ROOT

%if 0%{?rhel}
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc
%endif

%find_lang %{oldname} --with-gnome --all-name


%files -f %{oldname}.lang
%doc COPYING AUTHORS README
%{_datadir}/%{oldname}/
%{_datadir}/caja-python/extensions/%{oldname}.*


%changelog
* Wed Sep 06 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.10-alt1_3
- new fc release

* Wed Oct 12 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.1-alt1_1
- update to mate 1.16

* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_1
- new version

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1_5
- new fc release

* Sat Mar 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1_0
- new fc release

* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_0101
- initial import

