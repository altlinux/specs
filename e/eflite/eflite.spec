Name: eflite
Version: 0.4.2
Release: alt1

Summary: FLite Emacspeak server
License: GPL
Group: Sound
Url: http://cmuflite.org

Source: %name-%version-%release.tar
BuildRequires: flite-devel >= 1.3.9-alt1 libalsa-devel

Requires: flite >= 1.3.9-alt1

%description
This is a Emacspeak interface to Festival Lite speech synthesizer

%prep
%setup

%build
%autoreconf
%configure --with-vox=cmu_us_kal
make

%install
%makeinstall

%files
%doc README INSTALL
%_bindir/*
%_man1dir/*

%changelog
* Tue Aug  4 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.2-alt1
- 0.4.2 released

* Sun Jul 15 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt1
- 0.4.1 released

* Wed Oct 11 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.0-alt2
- braindamage64 symptoms weaken

* Tue Oct 10 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.0-alt1
- 0.4.0 released

* Mon Oct 31 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.9-alt1
- 0.3.9 released

* Sat May 15 2004 Ott Alex <ott@altlinux.ru> 0.3.6-alt2
- Fix build

* Sun May 18 2003 Ott Alex <ott@altlinux.ru> 0.3.6-alt1
- Initial build
