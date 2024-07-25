Name:           dia-shapes-user
Version:        0.0.2
Release:        alt1
Summary:        Additional Dia shapes for UI design
Group:          Office
BuildArch:      noarch

License:        BSD
Source:         %name-%version.tar

%description
%summary

%prep
%setup

%install
mkdir -p %buildroot%_datadir/dia/shapes %buildroot%_datadir/dia/sheets
cp -a shapes/*[^ya~] %buildroot%_datadir/dia/shapes/
cp -a sheets/*[^y~] %buildroot%_datadir/dia/sheets/

%files
%_datadir/dia/*/*

%changelog
* Thu Jul 25 2024 Fr. Br. George <george@altlinux.org> 0.0.2-alt1
- Add MenuText shape

* Thu Jul 25 2024 Fr. Br. George <george@altlinux.org> 0.0.1-alt2
- Remove unneeded .dia files from package

* Fri Jun 14 2024 Fr. Br. George <george@altlinux.org> 0.0.1-alt1
- Initial build for ALT
