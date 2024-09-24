%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%def_without check

%if "%(rpmvercmp '%{get_version ImageMagick-tools}' '7.0')" <= "0"
%def_disable IM7
%else
%def_enable IM7
%endif

Name: ravada
Version: 2.3.0
Release: alt2
Summary: Remote Virtual Desktops Manager
License: AGPL-3.0
Group: Development/Perl
Url: https://ravada.upc.edu/
Vcs: https://github.com/UPC/ravada.git
BuildArch: noarch

Source: %name-%version.tar

Requires: perl-DBD-mysql perl-DBD-SQLite perl-Mojolicious-Plugin-I18N
Requires: bridge-utils iproute2 iptables iptstate net-tools
Requires: libvirt qemu-img qemu-kvm openssl guestfs-tools lxc-core
# spice-vdagent @ VM

BuildRequires(pre): rpm-build-perl

BuildRequires: ImageMagick-tools
BuildRequires: bridge-utils iproute2 net-tools qemu-img wget

BuildRequires: perl-Authen-ModAuthPubTkt
BuildRequires: perl-Authen-Passphrase
BuildRequires: perl-DateTime-Format-DateParse
BuildRequires: perl-DateTime-Locale
BuildRequires: perl-DateTime
BuildRequires: perl-DBD-SQLite
BuildRequires: perl-DBIx-Connector
BuildRequires: perl-devel
BuildRequires: perl-File-Rsync
BuildRequires: perl-File-Tee
BuildRequires: perl-IO-Interface
BuildRequires: perl-IO-stringy
BuildRequires: perl-IPC-Run3
BuildRequires: perl-IPTables-ChainMgr
BuildRequires: perl-JSON-XS
BuildRequires: perl-ldap
BuildRequires: perl-Locale-Maketext
BuildRequires: perl-Locale-Maketext-Lexicon
BuildRequires: perl-Magick
BuildRequires: perl-Mojolicious >= 7.01
BuildRequires: perl-Mojolicious-Plugin-I18N
BuildRequires: perl-Moose
BuildRequires: perl-MooseX-Types
BuildRequires: perl-MooseX-Types-NetAddr-IP
BuildRequires: perl-Net-DNS
BuildRequires: perl-Net-OpenSSH
BuildRequires: perl-Net-Ping
BuildRequires: perl-PBKDF2-Tiny
BuildRequires: perl-Proc-PID-File
BuildRequires: perl-Sys-Virt
BuildRequires: perl-Test-Pod-Coverage
BuildRequires: perl-XML-LibXML
BuildRequires: perl-YAML
# NO Sys::Statistics::Linux

%if_with check
BuildRequires: /proc
BuildRequires: rpm-build-vm
BuildRequires: perl-Test-Moose-More
BuildRequires: perl-Test-Perl-Critic
BuildRequires: iptables
BuildRequires: libvirt libvirt-daemon libvirt-kvm
BuildRequires: mariadb-common
%endif

%define __spec_autodep_custom_pre export PERL5OPT='-I%buildroot%perl_vendor_privlib -MRavada'; export TZ=UTC
%set_perl_req_method relaxed
%global __find_requires export TZ=UTC; /usr/lib/rpm/find-requires

%description
Ravada is a software that allows the user to connect to a remote virtual desktop

%prep
%setup -q -n %name-%version
# ALT doesn't ship kvm-spice but qemu-kvm
# find . -type f -name "*.xml" -exec sed -i 's|kvm-spice|qemu-kvm|g' {} ';'

%build
%if_enabled IM7
sed -e 's/Image::Magick::Q16;/Image::Magick::Q16HDRI;/g' -i lib/Ravada.pm
%endif

# set environment variable to make sure DateTime::TimeZone::Local
# could determine timezone during tests
export TZ=UTC
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
export TZ=UTC
%perl_vendor_install
install -D -m755 script/rvd_back %buildroot%_sbindir/rvd_back
install -D -m755 script/rvd_front %buildroot%_sbindir/rvd_front
mkdir -p %buildroot%_localstatedir/%name
cp -aR etc/xml %buildroot%_localstatedir/%name/
mkdir -p %buildroot%_datadir/%name
cp -aR public %buildroot%_datadir/%name/
cp -aR templates %buildroot%_datadir/%name/
mkdir -p %buildroot%_sysconfdir
install -p -m644 etc/%name.conf %buildroot%_sysconfdir/%name.conf
install -p -m644 etc/rvd_front.conf.example %buildroot%_sysconfdir/rvd_front.conf
mkdir -p %buildroot%_unitdir
install -p -m644 etc/systemd/*.service %buildroot%_unitdir
mkdir -p %buildroot%_docdir/%name
cp -aR sql %buildroot%_docdir/%name
rm -f %buildroot%_docdir/%name/sql/mysql/Makefile

mkdir -p %buildroot%_bindir
cat > %buildroot%_bindir/kvm-spice <<_EOF
#!/bin/sh

# Libvirt introspects the binary using -M none. In that case, don't try
# to init KVM, which will fail and be noisy if the host has kvm disabled
opts="-machine accel=kvm"
if echo "\$@" | grep -q " -M none "; then
    opts=
fi

if echo "\$@" | grep -q -E -e '(^|\s)-machine\s.*accel=' -e '(^|\s)-accel\s' -e '(^|\s)-enable-kvm'; then
    # acceleration already set via commandline option
    opts=
fi

arch="\$(uname -m)"
case "\$arch" in
	i?86) arch="i386" ;;
	x86_64) arch="x86_64" ;;
	aarch64) arch=aarch64 ;;
	arm*) arch=arm ;;
	ppc64|ppc64le) arch=ppc64 ;;
	ppc) arch=ppc ;;
esac

exec /usr/bin/qemu-system-"\$arch" "\$@"
_EOF
chmod 0755 %buildroot%_bindir/kvm-spice

# Remove empty files
find %buildroot -size 0 -delete

%check
export TZ=UTC
export PATH=$PATH:/sbin
vm-run --kvm=cond "mount -t tmpfs tmp /var/run; service libvirtd start; make test"

%preun
%preun_service rvd_back
%preun_service rvd_front

%post
%post_service rvd_back
# First installation, not upgrade.
systemctl=/bin/systemctl
if [ $1 -eq 1 -a -f "$systemctl" ]; then
    $systemctl enable rvd_back.service ||:
fi

%post_service rvd_front
# First installation, not upgrade.
if [ $1 -eq 1 ]; then
    %_sbindir/useradd --system ravada ||:
fi
systemctl=/bin/systemctl
if [ $1 -eq 1 -a -f "$systemctl" ]; then
    $systemctl enable rvd_front.service ||:
fi

%files
%doc LICENSE MANIFEST README.md
%perl_vendor_privlib/*
%_bindir/kvm-spice
%_sbindir/*
%_datadir/%name
%_localstatedir/%name
%_unitdir/*.service
%_docdir/%name
%config(noreplace)%_sysconfdir/%name.conf
%config(noreplace)%_sysconfdir/rvd_front.conf

%changelog
* Tue Sep 24 2024 Anton Farygin <rider@altlinux.ru> 2.3.0-alt2
- use the ImageMagick version check instead of checking
  the version of the branch to fix Magick perl module name

* Tue Sep 10 2024 Andrew A. Vasilyev <andy@altlinux.org> 2.3.0-alt1
- 2.3.0

* Fri May 03 2024 Andrew A. Vasilyev <andy@altlinux.org> 2.2.2-alt1
- 2.2.2

* Mon Mar 11 2024 Andrew A. Vasilyev <andy@altlinux.org> 2.2.1-alt1
- 2.2.1

* Tue Mar 05 2024 Andrew A. Vasilyev <andy@altlinux.org> 2.2.0-alt1
- 2.2.0

* Wed Feb 28 2024 Andrew A. Vasilyev <andy@altlinux.org> 2.1.9-alt1
- 2.1.9

* Thu Feb 08 2024 Andrew A. Vasilyev <andy@altlinux.org> 2.1.8-alt1
- 2.1.8

* Thu Dec 14 2023 Andrew A. Vasilyev <andy@altlinux.org> 2.1.7-alt1
- 2.1.7

* Thu Nov 02 2023 Andrew A. Vasilyev <andy@altlinux.org> 2.1.5-alt1
- 2.1.5

* Thu Oct 26 2023 Andrew A. Vasilyev <andy@altlinux.org> 2.1.3-alt1
- 2.1.3

* Mon Oct 09 2023 Andrew A. Vasilyev <andy@altlinux.org> 2.1.2-alt1
- 2.1.2
- use "fix for using HDRI version of the ImageMagick" hack only for
  Sisyphus/p11

* Tue Sep 26 2023 Andrew A. Vasilyev <andy@altlinux.org> 2.1.1-alt1
- 2.1.1

* Thu Aug 31 2023 Andrew A. Vasilyev <andy@altlinux.org> 2.0.6-alt1
- 2.0.6

* Thu Aug 31 2023 Anton Farygin <rider@altlinux.ru> 2.0.5-alt2
- added fix for using HDRI version of the ImageMagick

* Mon May 29 2023 Andrew A. Vasilyev <andy@altlinux.org> 2.0.5-alt1
- 2.0.5

* Wed May 24 2023 Andrew A. Vasilyev <andy@altlinux.org> 2.0.4-alt1
- 2.0.4

* Thu Mar 23 2023 Andrew A. Vasilyev <andy@altlinux.org> 2.0.3-alt1
- 2.0.3

* Mon Feb 13 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.8.8-alt1
- 1.8.8

* Thu Feb 09 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.8.7-alt1
- 1.8.7

* Tue Jan 24 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.8.6-alt1
- 1.8.6

* Tue Jan 10 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.8.4-alt1
- 1.8.4

* Tue Dec 20 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.8.3-alt1
- 1.8.3

* Tue Nov 29 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.8.2-alt1
- 1.8,2

* Thu Nov 10 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.8.0-alt1
- 1.8.0

* Tue Oct 18 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.7.7-alt1
- 1.7.7

* Thu Sep 22 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.7.5-alt1
- 1.7.5
- remove explicit dependancy on mariadb-common

* Tue Sep 06 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.7.3-alt1
- 1.7.3

* Wed Jul 27 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.7.2-alt1
- 1.7.2

* Fri Jul 22 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.7.1-alt1
- 1.7.1

* Fri Jul 15 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.7.0-alt1
- 1.7.0

* Tue Jul 05 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.6.0-alt1
- 1.6.0

* Wed Jun 08 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.5.3-alt1
- 1.5.3

* Thu Jun 02 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.5.2-alt1
- 1.5.2
- add qcow2 files detection
- add kvm-spice script
- add "Do not try LDAP if not available" fix

* Wed May 25 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.5.1-alt1
- 1.5.1
- fix path to ss

* Sun May 22 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.5.0-alt2
- package sql scripts
- add missed Requires

* Fri May 20 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.5.0-alt1
- 1.5.0

* Tue Mar 29 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.4.0-alt1
- 1.4.0

* Tue Feb 22 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.3.4-alt1
- 1.3.4

* Tue Feb 08 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.3.3-alt1
- 1.3.3

* Thu Feb 03 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.3.2-alt1
- 1.3.2

* Tue Jan 11 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.3.0-alt1
- 1.3.0

* Fri Dec 31 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.2.0-alt1
- 1.2.0

* Mon Nov 29 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.1.2-alt1
- 1.1.2

* Tue Oct 26 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.1.1-alt1
- 1.1.1

* Wed Sep 29 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.1.0-alt1
- 1.1.0

* Thu Sep 16 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.0.5-alt1
- 1.0.5

* Thu Sep 09 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.0.4-alt1
- 1.0.4

* Thu Jul 01 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.0.3-alt1
- 1.0.3

* Sat Jun 19 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.0.2-alt1
- 1.0.2

* Tue Jun 08 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.0.1-alt2
- FTBFS: BR: perl-DateTime-Locale

* Tue May 18 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.0.1-alt1
- 1.0.1

* Fri Apr 23 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.0.0-alt1
- 1.0.0

* Wed Mar 03 2021 Andrew A. Vasilyev <andy@altlinux.org> 0.11.4-alt1
- 0.11.4

* Thu Feb 25 2021 Andrew A. Vasilyev <andy@altlinux.org> 0.11.2-alt1
- 0.11.2

* Fri Feb 12 2021 Andrew A. Vasilyev <andy@altlinux.org> 0.11.1-alt1
- 0.11.1

* Tue Feb 02 2021 Andrew A. Vasilyev <andy@altlinux.org> 0.11.0-alt1
- 0.11.0

* Mon Dec 21 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.10.5-alt1
- 0.10.5

* Mon Dec 14 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.10.4-alt1
- 0.10.4

* Wed Dec 09 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.10.3-alt1
- 0.10.3

* Wed Dec 02 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.10.2-alt1
- 0.10.2

* Wed Nov 25 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.10.1-alt1
- 0.10.1

* Wed Nov 11 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.10.0-alt1
- 0.10.0

* Thu Oct 08 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.9.0-alt1
- 0.9.0

* Wed Aug 05 2020 Andrew A. Vasilyev <andy@altlinux.org> 0.8.3-alt1
- initial build for ALT Linux Sisyphus

