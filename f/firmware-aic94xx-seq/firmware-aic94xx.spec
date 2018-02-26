%define firmware_name aic94xx-seq
%define realname aic94xx_sequencer_fw

Name: firmware-%firmware_name
Version: 17
Release: alt1
Packager: L.A. Kostis <lakostis@altlinux.ru>
License: GPL
Group: System/Kernel and hardware
Summary: firmware for Aic94xx SAS/SATA driver
Source0: http://ftp.kernel.org/pub/linux/kernel/people/jejb/%realname.tar.bz2
Url: http://ftp.kernel.org/pub/linux/kernel/people/jejb
BuildArch: noarch

%description
link sequencer code for AIC-94xx

Compile options: RAZOR BYPASS_OOB SATA_II_NCQ TARGET_MODE CONCURR_CONNECTION

%prep
%setup -q -n %realname

%build
gcc $RPM_BUILD_OPTIONS main.c -o main
./main
chmod 644 *.fw

%install
install -d $RPM_BUILD_ROOT/lib/firmware
install -p *.fw $RPM_BUILD_ROOT/lib/firmware/

%files
%defattr(644,root,root,755)
/lib/firmware/*.fw

%changelog
* Thu Oct 16 2008 L.A. Kostis <lakostis@altlinux.ru> 17-alt1
- initial release for ALTLinux.
- contains reference firmware V17/10c6 (covered by GPL).

