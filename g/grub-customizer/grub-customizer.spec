Name:           grub-customizer
Version:        5.0.6
Release:        alt1
Summary:        Grub Customizer is a graphical interface to configure the grub2/burg settings

License:        GPLv3
Group: 		System/Configuration/Boot and Init
URL:            https://launchpad.net/grub-customizer

Source0:        https://launchpad.net/grub-customizer/4.0/%{version}/+download/%{name}_%{version}.tar.gz
Source1:	%name.watch

BuildRequires(pre): cmake
BuildRequires:  ctest
BuildRequires:  gcc-c++
BuildRequires:  libgtkmm3-devel
BuildRequires:  gettext
BuildRequires:  libssl-devel
BuildRequires:  libarchive-devel
BuildRequires:  desktop-file-utils

Requires:       grub2
Requires:       hwinfo

%description
Grub Customizer is a graphical interface to configure the grub2/burg settings
with focus on the individual list order - without losing the dynamical behavior
of grub.

The goal of this project is to create a complete and intuitive graphical
grub2/burg configuration interface. The main feature is the boot entry list
configuration - but not simply by modified the grub.cfg: to keep the dynamical
configuration, this application will only edit the script order and generate
proxies (script output filter), if required.

%prep
%setup -q

%build
%add_optflags -fpermissive -std=c++11
%cmake
%cmake_build

%install
%cmakeinstall_std

cat > grub.cfg << EOF
MKCONFIG_CMD=grub-mkconfig
INSTALL_CMD=grub-install
MKFONT_CMD=grub-mkfont
CFG_DIR=/etc/grub.d
OUTPUT_DIR=/boot/grub
OUTPUT_FILE=/boot/grub/grub.cfg
SETTINGS_FILE=/etc/sysconfig/grub2

EOF
mkdir -p %buildroot%_sysconfdir/%name
install -m 0644 grub.cfg %buildroot%_sysconfdir/%name/grub.cfg

%find_lang %name

%files -f %name.lang
%doc README COPYING changelog
%config(noreplace) %_sysconfdir/%name
%_bindir/%name
%_libdir/grubcfg-proxy
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_man1dir/%name.1*
%_datadir/polkit-1/actions/net.launchpad.danielrichter2007.pkexec.grub-customizer.policy


%changelog
* Tue Apr 26 2016 Andrey Cherepanov <cas@altlinux.org> 5.0.6-alt1
- New version

* Fri Apr 01 2016 Andrey Cherepanov <cas@altlinux.org> 5.0.5-alt1
- New version

* Tue Mar 29 2016 Andrey Cherepanov <cas@altlinux.org> 5.0.4-alt1
- New version

* Tue Oct 06 2015 Andrey Cherepanov <cas@altlinux.org> 4.0.6-alt2
- Fix build with gcc5

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.0.6-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Mon Jul 28 2014 Andrey Cherepanov <cas@altlinux.org> 4.0.6-alt1
- New version
- Add .watch file for update automation

* Wed Jul 16 2014 Andrey Cherepanov <cas@altlinux.org> 4.0.4-alt2
- Build in Sisyphus (ALT #30193)

* Tue Mar 04 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.4-alt1_1
- update to new release by fcimport

* Sat Jan 04 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.2-alt1_1
- update to new release by fcimport

* Mon Mar 25 2013 Igor Vlasenko <viy@altlinux.ru> 3.0.4-alt1_1
- update to new release by fcimport

* Tue Aug 14 2012 Igor Vlasenko <viy@altlinux.ru> 2.5.6-alt1_1
- new version

