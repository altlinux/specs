# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3 rpm-macros-fedora-compat
BuildRequires: python-devel
# END SourceDeps(oneline)
Name:           autoarchive
Version:        0.5.2
Release:        alt1_4
Summary:        A simple backup tool that uses tar

Group:          File tools
License:        GPLv3
URL:            http://autoarchive.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:         %{name}-0.5.2-coding.patch
BuildArch:      noarch

BuildRequires:  python3-devel

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
which reads information from it and creates desired backup.


%prep
%setup -q
%patch0 -p1


%build
%{__python3} setup.py build


%install
%{__python3} setup.py install -O1 --skip-build --root=%{buildroot}


%files
%doc COPYING NEWS README README.sk
%config(noreplace) %{_sysconfdir}/aa/
%{_mandir}/man?/*.*
%{_bindir}/autoarchive
%{_bindir}/aa
%{python3_sitelibdir_noarch}/AutoArchive/
%{python3_sitelibdir_noarch}/%{name}*.egg-info


%changelog
* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1_4
- new release

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_3
- rebuild to get rid of #27020

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.0-alt1_3.1
- Rebuild with Python-2.7

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_3
- initial release by fcimport

