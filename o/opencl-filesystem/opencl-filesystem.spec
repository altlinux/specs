Name: opencl-filesystem
Version: 1.0
Release: alt1

Summary: OpenCL filesystem layout

Group: System/Libraries
License: Public Domain
Url: http://www.khronos.org/registry/cl/

BuildArch: noarch

%description
This package provides some directories required by packages which use OpenCL.

%prep

%install
# ICD Loader Vendor Enumeration
# http://www.khronos.org/registry/cl/extensions/khr/cl_khr_icd.txt
mkdir -p %buildroot/%_sysconfdir/OpenCL/vendors/

%files
%_sysconfdir/OpenCL/

%changelog
* Sat Jun 17 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Sisyphus

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 28 2013 Fabian Deutsch <fabiand@fedoraproject.org> - 1.0-1
- Initial package
