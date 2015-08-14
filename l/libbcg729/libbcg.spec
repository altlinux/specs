Summary: Bcg729 codec plugin for mediastreamer2
Name: libbcg729
Version: 0.1
Release: alt2
License: GPL
Group: Communications
Url: http://www.belledonne-communications.com

Packager: Konstantin Artyushkin <akv@altlinux.org>

Source: %name-%version.tar
Requires: bash >= 2.0

%description
BCG729 codec plugin for mediastreamer2.

%package devel
Summary: Development libraries for bcg729
Group: Development/Other
Requires: %name = %version-%release

%description devel
BCG729 codec plugin for mediastreamer2.

%prep
%setup 


%build
sh ./autogen.sh
%configure --enable-static
%make_build

%install
%makeinstall

%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%_libdir/%name.*

%files devel
%_includedir/bcg729
%_includedir/*.h
%_pkgconfigdir/%name.pc

%changelog
* Fri Aug 14 2015 Konstantin Artyushkin <akv@altlinux.org> 0.1-alt2
- incrementing Release for Sisyphus. Must be +1 then p(7/6/5) 

* Mon Feb 16 2015 Konstantin Artyushkin <akv@altlinux.org> 0.1-alt1
- initial build for ALT Linux Sisyphus

* Mon Jan 12 2014 Margaux Clerc <margaux.clerc@belledonne-communications.com> 
- Creation of rpm for linphone
