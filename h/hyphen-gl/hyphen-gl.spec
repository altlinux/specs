# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name: hyphen-gl
Summary: Galician hyphenation rules
Version: 0.99
Release: alt1_4
Source: http://extensions.services.openoffice.org/files/2004/0/hyph_gl.oxt
Group: Text tools
URL: https://forxa.mancomun.org/projects/hyphenation-gl
License: GPLv3
BuildArch: noarch
Requires: libhyphen
Source44: import.info

%description
Galician hyphenation rules.

%prep
%setup -q -c -n hyphen-gl

%build
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_gl_ANY.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_gl_ES.dic

%files
%doc LEME-gl_ANY.txt LICENCES-gl.txt LICENSES-en.txt  
%{_datadir}/hyphen/*

%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1_4
- update to new release by fcimport

* Fri May 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1_3
- import by fcmass

