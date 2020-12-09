Name: dirb
Version: 2.22
Release: alt3

Summary: Web Content Scanner.

License: %gpl2only
Group: Networking/Other
Url: http://dirb.sourceforge.net/

Packager: Nikita Ermakov <arei@altlinux.org>

Source: %name-%version.tar
Patch1: Fix-DIRB-for-GCC-10.patch

BuildPreReq: rpm-build-licenses
BuildRequires: libcurl-devel autoconf

%description
DIRB is a Web Content Scanner. It looks for existing (and/or hidden)
Web Objects. It basically works by launching a dictionary based attack
against a web server and analizing the response.

%prep
%setup
%patch1 -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
mv %buildroot/%_bindir/gendict{,-dirb}
mkdir -p %buildroot/%_datadir/dirb/
find wordlists/ -maxdepth 1 -type f -exec install -m 0644 '{}' %buildroot/%_datadir/dirb/ \;
mkdir -p %buildroot/%_datadir/dirb/others
find wordlists/others -maxdepth 1 -type f -exec install -m 0644 '{}' %buildroot/%_datadir/dirb/others \;
mkdir -p %buildroot/%_datadir/dirb/stress
find wordlists/stress -maxdepth 1 -type f -exec install -m 0644 '{}' %buildroot/%_datadir/dirb/stress \;
mkdir -p %buildroot/%_datadir/dirb/vulns
find wordlists/vulns -maxdepth 1 -type f -exec install -m 0644 '{}' %buildroot/%_datadir/dirb/vulns \;

%files
%_bindir/*
%_man1dir/*
%dir %_datadir/%{name}
%dir %_datadir/%{name}/others
%dir %_datadir/%{name}/stress
%dir %_datadir/%{name}/vulns
%_datadir/%{name}/*
%doc LICENSE.txt README.txt docs/GENDICT.TXT docs/FAQ.txt docs/TRICKS.txt docs/CHANGES.txt

%changelog
* Wed Dec 09 2020 Nikita Ermakov <arei@altlinux.org> 2.22-alt3
- Fix DIRB for GCC 10.

* Tue Nov 12 2019 Nikita Ermakov <arei@altlinux.org> 2.22-alt2
- Rename gendict to gendict-dirb to avoid collisions with icu-utils.

* Tue Nov 12 2019 Nikita Ermakov <arei@altlinux.org> 2.22-alt1
- Initial build for ALT Linux Sisyphus.
