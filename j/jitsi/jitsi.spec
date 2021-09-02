%set_verify_elf_method textrel=relaxed
%define buildrev	5630

Name:           jitsi
Version:        2.11.%buildrev
Release:        alt2.1

Summary:        Multiprotocol (SIP, XMPP/Jabber, ecc.) VoIP and instant messaging software
Group:          Networking/Instant messaging
License:        LGPL-2.1+
URL:            http://www.jitsi.org
# VCS:          https://github.com/jitsi/jitsi.git

Packager:	Andrey Cherepanov <cas@altlinux.org>

#ExclusiveArch:  %ix86 x86_64 aarch64

Source0:        jitsi-%{version}.tar
Source1:        jitsi.sh
Source2:        jitsi.desktop

# --- mageia patches from 2.10.5550-8 ----
#Patch0:		jitsi-2.9-mga-fix_bin_file_path.patch
#Patch1:		jitsi-2.9-mga-fix_man_file_package-name.patch
#Patch2:		jitsi-2.9-mga-fix_desktop_file_package-name.patch
Patch3:		jitsi-2.10-harfbuzz-header-path.patch
#Patch100:	jitsi-2.9-build-native-modules.patch
# --- mageia patches from 2.10.5550-8 ----
# based on jitsi-2.9-build-native-modules.patch from mageia, see .gear/*diff
Patch100:	jitsi-2.11-alt-build-native-modules.patch

BuildRequires(pre): rpm-build-java
BuildRequires:  java-1.8.0-devel
BuildRequires:  ant
BuildRequires:  gcc-c++
BuildRequires:  gnome-vfs-devel
BuildRequires:  libdbus-devel
BuildRequires:  libexpat-devel
BuildRequires:  libgnome-devel
BuildRequires:  libgtk+2-devel
BuildRequires:  libmatthew-java
BuildRequires:  libportaudio2-devel
BuildRequires:  libsane-devel
BuildRequires:  libspeex-devel
BuildRequires:  libssl-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXt-devel
BuildRequires:  libXtst-devel
BuildRequires:  libXv-devel
BuildRequires:  unzip
BuildRequires:  xalan-j2
BuildRequires:  xorg-xproto-devel
BuildRequires:  xz

Requires:	java
Requires:	dnsjava

%description
Jitsi is an audio/video and chat communicator that supports protocols
such as SIP, XMPP/Jabber, AIM/ICQ, Windows Live, Yahoo!, Bonjour and
many other useful features such as voice and chat encryption.

%prep
%setup
sed -i "s/0\.build\.by\.SVN/%buildrev/" src/net/java/sip/communicator/impl/version/NightlyBuildID.java
# Version
#sed -n 's/^.*VERSION_M.*= \([0-9]*\);/\1/p' src/net/java/sip/communicator/impl/version/VersionImpl.java | tr '\n' '.' | sed 's/\.$/\n/'

%patch3 -p1
%patch100 -p1

# precompiled code
find . -name "*.so" -delete

%build
#Build main program
%ant -Dlabel=%{buildrev} rebuild

pushd src/native
for i in clean-native init-native galagonotification globalshortcut-linux hid hwaddressretriever sysactivity; do
  %ant $i
done

%install
find lib/ lib/bundle/ -maxdepth 1 -type f -exec install -Dm644 {} "%buildroot%_libdir/%name/"{} \;
find sc-bundles/{,os-specific/linux/} -maxdepth 1 -type f -execdir install -Dm644 {} "%buildroot%_libdir/%name/sc-bundles/"{} \;

# TODO: sync with mga
#define native_libs_dir %_libdir/%name/native
%define native_libs_dir %_libdir/%name/lib/native
# copy the native libs
mkdir -p %buildroot%native_libs_dir/
%ifarch %ix86 %arm
install -Dm644 lib/native/linux/* %buildroot%native_libs_dir/
%else
install -Dm644 lib/native/linux-64/* %buildroot%native_libs_dir/
%endif

# Install executable start script and desktop file
install -Dm0755 %SOURCE1 %buildroot%_bindir/jitsi
install -Dm0644 %SOURCE2 %buildroot%_desktopdir/%name.desktop

mkdir -p %buildroot%_man1dir
sed 's,_PACKAGE_NAME_,jitsi,g;s,_APP_NAME_,Jitsi,g' resources/install/debian/jitsi.1.tmpl > %buildroot%_man1dir/%name.1

# Install icons
install -Dm0644 resources/install/debian/jitsi-32.xpm %buildroot%_niconsdir/%name.xpm
install -Dm0644 resources/install/debian/jitsi-16.xpm %buildroot%_miconsdir/%name.xpm
install -Dm0644 resources/install/debian/jitsi.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

%files
%_bindir/jitsi
%_man1dir/%name.1*
%_libdir/%name
%_desktopdir/jitsi.desktop
%_niconsdir/%{name}.xpm
%_miconsdir/%{name}.xpm
%_iconsdir/hicolor/scalable/apps/%{name}.svg

%changelog
* Thu Sep 02 2021 Igor Vlasenko <viy@altlinux.org> 2.11.5630-alt2.1
- build with java8

* Fri Apr 17 2020 Igor Vlasenko <viy@altlinux.ru> 2.11.5630-alt2
- aarch64 support

* Wed Apr 08 2020 Igor Vlasenko <viy@altlinux.ru> 2.11.5630-alt1
- New version

* Wed Apr 08 2020 Igor Vlasenko <viy@altlinux.ru> 2.11.5614-alt1
- New version

* Tue Apr 07 2020 Igor Vlasenko <viy@altlinux.ru> 2.11.5553-alt3
- fixed build

* Thu Dec 14 2017 Denis Medvedev <nbr@altlinux.org> 2.11.5553-alt2
- add missing javadns library

* Tue Feb 14 2017 Andrey Cherepanov <cas@altlinux.org> 2.11.5553-alt1
- Set correct minor version for commit 5553

* Mon Feb 13 2017 Andrey Cherepanov <cas@altlinux.org> 2.9.5553-alt1
- New version

* Tue Jan 31 2017 Andrey Cherepanov <cas@altlinux.org> 2.9.5546-alt1
- New version

* Tue Jan 17 2017 Andrey Cherepanov <cas@altlinux.org> 2.9.5541-alt1
- New version

* Wed Nov 02 2016 Andrey Cherepanov <cas@altlinux.org> 2.9.5534-alt1
- New version

* Tue Jun 21 2016 Andrey Cherepanov <cas@altlinux.org> 2.9.5521-alt2
- Add ExclusiveArch for support architectures

* Sun Jun 19 2016 Andrey Cherepanov <cas@altlinux.org> 2.9.5521-alt1
- New version
- Return check arch for correct copy bundled libs

* Fri Jun 10 2016 Andrey Cherepanov <cas@altlinux.org> 2.9.5518-alt1
- New version
- Simplify copy by arch-independed way

* Sun May 03 2015 Andrey Cherepanov <cas@altlinux.org> 2.8.5426-alt1
- Initial build in Sisyphus

