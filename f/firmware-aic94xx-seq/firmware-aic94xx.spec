%define firmware_name aic94xx-seq
%define pkg_name aic94xx_seq

Name: firmware-%firmware_name
Version: 30
Release: alt1
Packager: L.A. Kostis <lakostis@altlinux.ru>
License: Adaptec Proprietary License
Group: System/Kernel and hardware
Summary: firmware for Aic94xx SAS/SATA driver
Source0: http://download.adaptec.com/scsi/linux/%{firmware_name}-%version-1.tar.gz
Url: https://storage.microsemi.com/en-us/speed/scsi/linux/%{firmware_name}-%version-1_tar_gz.php
BuildArch: noarch

%description
Adaptec SAS 44300, 48300, 58300 Sequencer Firmware for AIC94xx driver

%prep
%setup -qcn %firmware_name-%version

%build
rpm2cpio %pkg_name-%version-1.noarch.rpm|cpio -idvm --no-absolute-filenames

%install
chmod 644 lib/firmware/*.fw
mkdir -p %buildroot/lib/firmware
install -m644 lib/firmware/*.fw %buildroot/lib/firmware

%files
%defattr(644,root,root,755)
/lib/firmware/*.fw
%doc README-94xx.pdf

%changelog
* Wed Mar 21 2018 L.A. Kostis <lakostis@altlinux.ru> 30-alt1
- Updated to v30 from adaptec site (as in RHEL7).
- Change License to Proprietary (IANAL, but if CentOS7 does, why we can't?).

* Thu Oct 16 2008 L.A. Kostis <lakostis@altlinux.ru> 17-alt1
- initial release for ALTLinux.
- contains reference firmware V17/10c6 (covered by GPL).

