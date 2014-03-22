# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define oldname caja-terminal
# package include only on python file
# in result debuginfo is empty
%global debug_package %{nil}

Name:           mate-file-manager-terminal
Version:        0.8.1
Release:        alt1_0
Summary:        Terminal embedded in Caja

Group:          Shells
License:        GPLv3+
URL:            https://github.com/NiceandGently/%{oldname}
# upstream is located at github, but links from tag releases doesn't match copied link in
# web-browser, in result fedora-rewiew-tool will fail.
# so i decided to release on fedorapeople to have a valid download link
Source0:        http://raveit65.fedorapeople.org/Mate/SOURCE/%{oldname}-%{version}.tar.gz

BuildRequires:  gettext python-devel

# needed for run caja-terminal
Requires:       pygtk2 vte
Source44: import.info

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

%if %{_lib} == lib64
bash install-64.sh --package $RPM_BUILD_ROOT
%else
bash install.sh --package $RPM_BUILD_ROOT
%endif

rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

%find_lang %{oldname}

%files -f %{oldname}.lang
%doc COPYING AUTHORS README
%{_datadir}/%{oldname}/
%{_libdir}/caja/extensions-2.0/python/%{oldname}.py*

%changelog
* Sat Mar 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1_0
- new fc release

* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_0101
- initial import

