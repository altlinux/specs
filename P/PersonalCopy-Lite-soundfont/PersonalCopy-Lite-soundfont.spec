Name:           PersonalCopy-Lite-soundfont
Version:        4.1
Release:        alt1_14
Summary:        Lite version of the PersonalCopy General Midi soundfont
Group:          Sound
License:        Redistributable, no modification permitted
URL:            http://www.personalcopy.com/sfarkfonts1.htm
# This is ftp://ftp.personalcopy.net/pub/PCLite.sfArk.exe after running this
# self extracting executable under wine
Source0:        PCLite.sf2
Source1:        LICENSE.txt
Source2:        license-permission.eml
BuildRequires:  soundfont-utils
BuildArch:      noarch
# Virtual soundfont2 provides for easy querying of all sf2 packages
Provides:       soundfont2
Source44: import.info

%description
Lite (smaller) version of the PersonalCopy General Midi soundfont in soundfont
2.0 (.sf2) format.


%prep
%setup -q -c -T
cp -p %{SOURCE1} %{SOURCE2} .


%build


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/soundfonts
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/soundfonts


%files
%doc LICENSE.txt license-permission.eml
%{_datadir}/soundfonts


%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_14
- update to new release by fcimport

* Fri Nov 06 2015 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_13
- new version

