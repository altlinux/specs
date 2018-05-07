Group: System/Fonts/True type
%define oldname glyphicons-halflings-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname glyphicons-halflings
%global githash 728067b586d2d989c07e8a6265f06fa8631c6b1f
%global gitshort 728067b
%global date 20140211
%global checkout %{date}git%{gitshort}

Name:           fonts-ttf-glyphicons-halflings
Epoch:          1
Version:        3.1.0
Release:        alt1_8.%{checkout}
Summary:        Precisely prepared monochromatic icons and symbols

License:        MIT
URL:            http://glyphicons.com/

Source0:        https://github.com/twbs/bootstrap/raw/%{githash}/fonts/glyphicons-halflings-regular.ttf
Source1:        https://github.com/twbs/bootstrap/raw/%{githash}/LICENSE
BuildArch:      noarch
BuildRequires:  fontpackages-devel 
BuildRequires:  ttembed
Source44: import.info

%description
GLYPHICONS is a library of precisely prepared monochromatic icons and symbols,
created with an emphasis on simplicity and easy orientation.

%prep
ttembed %{SOURCE0}
install -m 0644 -p %{SOURCE1} LICENSE

%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE0} %{buildroot}%{_fontdir}


%files
%doc LICENSE
%{_fontdir}


%changelog
* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1:3.1.0-alt1_8.20140211git728067b
- update to new release by fcimport

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.1.0-alt1_7.20140211git728067b
- update to new release by fcimport

* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.1.0-alt1_3.20140211git728067b
- converted for ALT Linux by srpmconvert tools

