%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           autoarchive
Version:        0.2.0
Release:        alt2_3
Summary:        A simple backup tool that uses tar

Group:          File tools
License:        GPLv3
URL:            http://autoarchive.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-module-setuptools

Requires:       xz
Requires:       tar
Requires:       gzip
Requires:       bzip2
Requires:       xz
Source44: import.info


%description
AutoArchive is a simple utility for making backups more easily. It
uses tar for creating archives. The idea of the program is that every 
information needed for making a backup is in one file - the archive 
spec file. Path to this file is passed as a parameter to 'aa' command 
which reads informations from it and creates desired backup.


%prep
%setup -q


%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}


%files
%doc COPYING NEWS README README.sk src/doc/examples/
%{_mandir}/man?/*.*
%{_bindir}/autoarchive
%{_bindir}/aa
%{python_sitelib}/AutoArchive/
%{python_sitelib}/%{name}*.egg-info


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_3
- rebuild to get rid of #27020

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.0-alt1_3.1
- Rebuild with Python-2.7

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_3
- initial release by fcimport

