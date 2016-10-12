# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define oldname caja-terminal
# package include only on python file
# in result debuginfo is empty
%global debug_package %{nil}

Name:           mate-file-manager-terminal
Version:        0.9.1
Release:        alt1_1
Summary:        Terminal embedded in Caja
Group:          Shells
License:        GPLv3+
URL:            https://github.com/yselkowitz/%{oldname}
Source0:        https://github.com/yselkowitz/caja-terminal/archive/%{oldname}-%{version}.tar.gz

BuildRequires: gettext gettext-tools gettext-tools-python python-devel

# needed for run caja-terminal
Requires: python-module-pygtk python-module-pygtk-demo python-module-caja libvte python-module-vte python-module-pyxdg
Source44: import.info
BuildArch: noarch

%description
Caja Terminal is a terminal embedded in Caja, the MATE file browser.
It is always open in the current folder, and follows the navigation
(like an automated "cd" command).

%prep
%setup -n %{oldname}-%{version} -q
sed -i -e 's~#!/usr/bin/python~#!%{__python}~g' code/caja-terminal.py

%build
# no build needed

%install
mkdir -p $RPM_BUILD_ROOT
%{makeinstall_std}

bash install.sh --package $RPM_BUILD_ROOT

#rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

%find_lang %{oldname} --with-gnome --all-name


%files -f %{oldname}.lang
%doc COPYING AUTHORS README
%{_datadir}/%{oldname}/
%{_datadir}/caja-python/extensions/%{oldname}.*


%changelog
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

