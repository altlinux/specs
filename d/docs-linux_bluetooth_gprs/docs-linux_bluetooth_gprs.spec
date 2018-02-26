# Generated File.
%setup_docs_module linux_bluetooth_gprs ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: GPRS over Bluetooth configuration with Siemens S55
Summary(ru_RU.KOI8-R): Настройка доступа в Internet через GPRS на Linux используя Siemens S55 и Bluetooth
License: distributable
Url: http://xtalk.msk.su/~ott/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3

# replace docs-LinuxBluetoothGPRS-kirill
Provides: docs-LinuxBluetoothGPRS-kirill
Obsoletes: docs-LinuxBluetoothGPRS-kirill

Source: %name-%version.tar

%description
Short story about GPRS configuration over Bluetooth

%description -l ru_RU.KOI8-R
небольшой рассказ о настройке GPRS over Bluetooth

%prep
%setup

%build
%docs_module_build "DocBook/XML" "linux-s55-bluetooth-gprs.ru.xml"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Mon Nov 10 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- fixed typo in Summary

* Sun Jun 01 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- package renamed: docs-LinuxBluetoothGPRS-kirill -> docs-linux_bluetooth_gprs
- build with rpm-build-docs-experimental
- added prev/next links

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 050411-alt3.1.1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Tue Oct 04 2005 Kirill Maslinsky <kirill@altlinux.ru> 050411-alt3.1.1
- Auto rebuild with new version.

* Fri Sep 23 2005 Kirill Maslinsky <kirill@altlinux.ru> 050411-alt3.1
- Auto rebuild with new version.

* Tue Jun 14 2005 Alexey Gladkov <legion@altlinux.ru> 050411-alt3
- Requires bugfix;

* Mon Jun 06 2005 Alexey Gladkov <legion@altlinux.ru> 050411-alt2
- rebuild with new rpm-build-docs.

* Mon Apr 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050411-alt1
- initial build

* Mon Apr 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.0.1-alt1
- initial build

