%set_verify_elf_method textrel=relaxed
%define rev	5426

Name:           jitsi
Version:        2.8.%rev
Release:        alt1

Summary:        Multiprotocol (SIP, XMPP/Jabber, ecc.) VoIP and instant messaging software
Group:          Networking/Instant messaging
License:        LGPL-2.1+
URL:            http://www.jitsi.org
# VCS:          https://github.com/jitsi/jitsi.git

Packager:	Andrey Cherepanov <cas@altlinux.org>

Source0:        jitsi-%{version}.tar
Source1:        jitsi.sh
Source2:        jitsi.desktop

BuildRequires(pre): rpm-build-java
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

%description
Jitsi is an audio/video and chat communicator that supports protocols
such as SIP, XMPP/Jabber, AIM/ICQ, Windows Live, Yahoo!, Bonjour and
many other useful features such as voice and chat encryption.

%prep
%setup
sed -i "s/0\.build\.by\.SVN/%rev/" src/net/java/sip/communicator/impl/version/NightlyBuildID.java

%build
#Build main program
%ant rebuild

%install
find lib/ lib/bundle/ -maxdepth 1 -type f -exec install -Dm644 {} "%buildroot%_libdir/%name/"{} \;
%ifarch x86_64
find lib/native/linux-64/ -maxdepth 1 -type f -execdir install -Dm644 {} "%buildroot%_libdir/%name/lib/native/"{} \;
%else
find lib/native/linux/ -maxdepth 1 -type f -execdir install -Dm644 {} "%buildroot%_libdir/%name/lib/native/"{} \;
%endif
find sc-bundles/{,os-specific/linux/} -maxdepth 1 -type f -execdir install -Dm644 {} "%buildroot%_libdir/%name/sc-bundles/"{} \;

# Install executable start script and desktop file
install -Dm0755 %SOURCE1 %buildroot%_bindir/jitsi
install -Dm0644 %SOURCE2 %buildroot%_desktopdir/%name.desktop

# Install icons
cd resources/install/debian/
for _file in *.{svg,xpm}; do
  install -Dm644 "$_file" "%buildroot%_pixmapsdir/${_file}"
done

%files
%_bindir/jitsi
%_libdir/%name
%_pixmapsdir/*.xpm
%_pixmapsdir/%name.svg
%_desktopdir/jitsi.desktop

%changelog
* Sun May 03 2015 Andrey Cherepanov <cas@altlinux.org> 2.8.5426-alt1
- Initial build in Sisyphus

