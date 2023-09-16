Name: rpm-macros-R
Version: 1.0
Release: alt1
Summary: RPM helper macros to build R packages
License: ALT-Public-Domain
Group: Development/Other
BuildArch: noarch

Source: %name.macros

%description
These helper macros facilitate creation of RPM packages containing R code.

%prep
%setup -cT

%install
install -pD -m644 %SOURCE0 %buildroot%_rpmlibdir/macros.d/R

%files
%_rpmlibdir/macros.d/R

%changelog
* Sat Sep 16 2023 Igor Vlasenko <viy@altlinux.org> 1.0-alt1
- initial build for ALT Linux Sisyphus
