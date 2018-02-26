Name: libbluray-plugin-xine
Version: 0.2.2
Release: alt1
Summary: Xine BD plugin

Group: Video
License: LGPL
Url: http://www.videolan.org/developers/libbluray.html

Source: %name-%version-%release.tar

BuildRequires: libbluray-devel libxine-devel

%description
%summary

%prep
%setup

%build
make

%install
%makeinstall DESTDIR=%buildroot

%files
%_libdir/xine/plugins/*/*

%changelog
* Wed Mar 21 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.2-alt1
- 0.2.2 released

* Fri Dec 02 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.1-alt1
- 0.2.1 released

* Wed Oct 26 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt0.3
- updated from git.e037110f

* Fri Aug 26 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt0.2
- updated from git.8e5d241e

* Wed May 11 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt0.1
- initial
