Name:         kmhtconvert
Version:      0.6
Release:      alt2.1
URL:          http://users.otenet.gr/~geosp/kmhtconvert/
License:      GPL
Group:        Networking/WWW
Summary:      convert mht files to war files.
Source:       %name-%version.tar.gz
Patch:        kmhtconvert-0.6-alt-DSO.patch

BuildRequires: gcc-c++ kdelibs-devel

%description
kmhtConvert is a utility to convert mht (Windows Web Archive) files to
war (KDE Web Archive) files. I decided to write this utility because for
a number of years I have been using Windows (who hasn't) and was used to
saving data acquired from the net in  mht files. Since I started using
Linux, if I wanted to read or use these files, I had to load Windows and
extract the file(s). The same thing also happened when friends send me
mht files by email.

%prep
%setup
%patch -p2

%build
%add_optflags -I%_includedir/tqtinterface
%__subst 's,\.la,.so,' configure
%K3configure --disable-rpath
%make_build

%install
%K3install

%K3find_lang --with-kde %name

%post
if [ ! -d /var/lib/klinpopup ] ; then
    mkdir -vp /var/lib/klinpopup
    chmod 777 /var/lib/klinpopup
fi

%files -f %name.lang 
%doc TODO ChangeLog README COPYING INSTALL AUTHORS NEWS
%defattr(-,root,root)
%_K3bindir/*
%_K3applnk/Utilities/*
%_K3applnk/.hidden/*
%_K3apps/%name
%_K3apps/konqueror/*/*
%_kde3_iconsdir/*/*/*/*

%changelog
* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt2.1
- Fixed build

* Wed Apr 20 2011 Andrey Cherepanov <cas@altlinux.org> 0.6-alt2
- Adapt to new KDE3 placement
- Cleanup requires

* Thu Jan 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.6-alt1.1
- Rebuilt with libstdc++.so.6.

* Tue Jan 11 2005 Nick S. Grechukh <gns@altlinux.ru> 0.6-alt1
- initial ALT build
