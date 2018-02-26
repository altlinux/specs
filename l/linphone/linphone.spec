Name: linphone
Version: 3.5.2
Release: alt1
License: GPLv2+
Url: http://www.linphone.org/

Summary: Open source video SIP phone
Group: Communications

Packager: Alexei Takaseev <taf@altlinux.ru>

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildPreReq: libortp-devel >= 0.16
BuildRequires: gcc-c++
BuildRequires: doxygen intltool libexosip2-devel libglade-devel libgsm-devel
BuildRequires: libnotify-devel libssl-devel
BuildRequires: libmediastreamer-devel libreadline-devel libspeex-devel
BuildRequires: libSDL-devel libosip2-devel >= 3.5.0 libncurses-devel
Requires: %name-gui = %version-%release
Requires: %name-cli = %version-%release

%description
Linphone is a SIP compliant audio & video phone. It can be used to run calls 
over the internet. It has a gtk+ and console interface.

%package common
Summary: Common files for %name
Group: Communications

%description common
Linphone is a SIP compliant audio & video phone. It can be used to run calls 
over the internet. It has a gtk+ and console interface.

This package contains common files for %name.

%package gui
Summary: Open source video SIP phone, graphical interface
Group: Communications
Requires: %name-common = %version-%release

%description gui
Linphone is a SIP compliant audio & video phone. It can be used to run calls 
over the internet. It has a gtk+ and console interface.

This package contains graphical interface of %name.

%package cli
Summary: Open source video SIP phone, console interface
Group: Communications
Requires: %name-common = %version-%release

%description cli
Linphone is a SIP compliant audio & video phone. It can be used to run calls 
over the internet. It has a gtk+ and console interface.

This package contains console interface for %name.

%package devel
Summary: Development files for %name
Group: Communications

%description devel
Linphone is a SIP compliant audio & video phone. It can be used to run calls 
over the internet. It has a gtk+ and console interface.

This package contains development files for %name.

%prep
%setup
%patch0 -p1
./autogen.sh

%build
%configure --enable-external-ortp \
 --enable-external-mediastreamer \
 --enable-notify \
 --enable-ssl \
 --disable-static
%make_build

%install
%makeinstall_std
%find_lang %name

%files

%files common
%doc AUTHORS ChangeLog NEWS README TODO
%_libdir/*.so.*
%exclude %_docdir/%name
%exclude %_datadir/gnome
%exclude %_mandir/cs
%exclude %_man1dir/sipomatic.1.gz

%files gui -f %name.lang
%_bindir/linphone
%_desktopdir/%name.desktop
%_pixmapsdir/%name
%_man1dir/linphone.1.gz
%_datadir/sounds/%name
%_datadir/%name

%files cli
%_bindir/linphonec
%_bindir/linphonecsh
%_man1dir/linphonec.1.gz
%_man1dir/linphonecsh.1.gz

%files devel
%doc coreapi/help/doc/html/*
%doc coreapi/help/*.c
%doc coreapi/help/java
%_pkgconfigdir/*
%_includedir/*
%_libdir/*.so

%changelog
* Sun Jun 24 2012 Alexei Takaseev <taf@altlinux.org> 3.5.2-alt1
- 3.5.2

* Sat Jan 28 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.5.0-alt1
- 3.5.0

* Fri Jul 22 2011 Egor Glukhov <kaman@altlinux.org> 3.4.3-alt1
- 3.4.3 (Closes: #25054)

* Sat Feb 12 2011 Egor Glukhov <kaman@altlinux.org> 3.4.0-alt1
- 3.4.0

* Wed Jul 28 2010 Egor Glukhov <kaman@altlinux.org> 3.3.2-alt1.git.88b8d036
- Initial build for Sisyphus
