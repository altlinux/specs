Name: inkscape-psd
Version: 0.1.1
Release: alt3

Summary: Inkscape PSD Importer

License: BSD
Group: Graphics
Url: http://pernsteiner.org/inkscape/psd_import/

# Source-url: http://pernsteiner.org/inkscape/psd_import/inkscape-psd_import-%version.zip
Source: %name-%version.tar
Patch: inkscape-psd-python3.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%add_python3_lib_path %_datadir/inkscape/extensions/
# for debug only
%add_python3_req_skip pprint

Requires: inkscape

%description
This Inkscape extension allows you to load Photoshop PSD files.

%prep
%setup
%patch0 -p1

# Documentation of Licence (as it written in every file) :
cp psd_import/__init__.py LICENSE

%build
# Nothing to build.

%install
mkdir -p %buildroot%_datadir/inkscape/extensions
cp -p psd_import.inx %buildroot%_datadir/inkscape/extensions
cp -p psd_import_main.py %buildroot%_datadir/inkscape/extensions
cp -rp psd_import %buildroot%_datadir/inkscape/extensions

%files
%doc LICENSE
%_datadir/inkscape/extensions/*

%changelog
* Fri Aug 20 2021 Vitaly Lipatov <lav@altlinux.ru> 0.1.1-alt3
- manual build for ALT Sisyphus

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 0.1.1-alt2_15
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 0.1.1-alt2_14
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt2_13
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1_13
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1_12
- update to new release by fcimport

* Mon Sep 30 2019 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1_11
- new version

