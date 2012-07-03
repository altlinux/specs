Name: flite
Version: 1.5.4
Release: alt1

Summary: flite - a small, fast speech synthesis engine
License: Custom, see COPYING
Group: Sound
Url: http://cmuflite.org

Source0: %name-%version-%release.tar

BuildRequires: ed libalsa-devel texi2html

%description
Flite - a small, fast speech synthesis engine. It is the latest addition to
the suite of free software synthesis tools including University of
Edinburgh's Festival Speech Synthesis System and Carnegie Mellon
University's FestVox project, tools, scripts and documentation for building
synthetic voices.  However, flite itself does not require either of these
systems to compile and run.

%package -n %name-devel
Summary: development files for flite
Group: Development/C
Requires: %name = %version-%release

%description -n %name-devel
development files for flite, a small, fast speech synthesis engine

%prep
%setup

%build
%autoreconf
%configure --enable-shared --with-vox=cmu_us_kal16
make

%install
%makeinstall \
	INSTALLBINDIR=%buildroot%_bindir \
	INSTALLLIBDIR=%buildroot%_libdir  \
	INSTALLINCDIR=%buildroot%_includedir 

%files
%doc ACKNOWLEDGEMENTS README COPYING doc/html
%_bindir/*
%_libdir/*.so.*

%files -n %name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Mon May 21 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.4-alt1
- 1.5.4 released

* Thu Nov 11 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.0-alt2
- rebuilt with set-versioned rpm

* Sat Feb  6 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.0-alt1
- 1.4.0 released

* Mon Apr 13 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.9-alt1
- 1.3.9 snapshot

* Sun Oct  8 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3-alt1
- 1.3 released
- resurrected alsa output (dropped by upstream now)

* Mon Apr 10 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2-alt6
- incomplete linking fixed

* Mon Oct 31 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2-alt5
- minor fixes in alsa support

* Fri Oct 28 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2-alt4
- rebuilt with alsa and 16-bit voice
- dropped static libs by default

* Sat May 15 2004 Ott Alex <ott@altlinux.ru> 1.2-alt3
- Fix build for gcc 3.3, thanks to Voins

* Sun May 09 2004 Ott Alex <ott@altlinux.ru> 1.2-alt2
- Fix build

* Sun Apr 27 2003 Ott Alex <ott@altlinux.ru> 1.2-alt1
- Initial release

