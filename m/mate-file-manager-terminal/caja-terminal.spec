%define _libexecdir %_prefix/libexec
%define oldname caja-terminal
Name:           mate-file-manager-terminal
Version:        0.7
Release:        alt1_0101
Summary:        Terminal embedded in Caja

Group:          Shells
License:        GPLv3+
URL:            https://github.com/NiceandGently/caja-terminal
Source0:        https://github.com/downloads/NiceandGently/caja-terminal/caja-terminal-%{version}.tar.xz


BuildRequires:  gettext python-devel

Requires:       pygtk2 vte
Source44: import.info

%description
Caja Terminal is a terminal embedded in Caja, the MATE's file browser.
It is always open in the current folder, and follows the navigation
(like an automated "cd" command).

%prep
%setup -n %{oldname}-%{version} -q
chmod -x AUTHORS
sed -i 's|/usr/lib/caja/extensions-2.0|%{_libdir}/caja/extensions-2.0|g' install.sh

%build

%install
mkdir -p $RPM_BUILD_ROOT
bash install.sh --package $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

%find_lang %{oldname}

%files -f %{oldname}.lang
%doc COPYING AUTHORS README
%{_datadir}/%{oldname}
%{_libdir}/caja/extensions-2.0/python/%{oldname}.py*

%changelog
* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_0101
- initial import

