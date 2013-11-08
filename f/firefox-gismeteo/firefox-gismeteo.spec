%define rname	gismeteo
%define cid	extensions@gismeteo.com
%define ciddir %firefox_noarch_extensionsdir/%cid

Summary: Weather forecast extension for Firefox by Gismeteo.Ru
Name:	firefox-%rname
Version: 5.0.0.6
Release: alt2.1
Source0: %rname-%version.xpi
License: Free
Group: Networking/WWW
URL: https://addons.mozilla.org/ru/firefox/addon/gismeteobar/

BuildArch: noarch
BuildRequires(pre): rpm-build-firefox
BuildRequires: unzip

%description 	
Summary: Weather forecast extension for Firefox by Gismeteo.Ru.

%prep
%setup -c
rm -fR .gear *.spec
subst 's/23\.0/24.*/' install.rdf

%install
mkdir -p %buildroot/%ciddir
cp -r * %buildroot/%ciddir

%postun
if [ "$1" = 0 ]; then
    [ ! -d "%ciddir" ] || rm -rf "%ciddir"
fi
	
%files
%ciddir

%changelog
* Wed Oct 30 2013 Andrey Cherepanov <cas@altlinux.org> 5.0.0.6-alt2.1
- Adapt for Firefox 24.x

* Sun Oct 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.0.6-alt2
- Change URL

* Sun Oct 20 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.0.6-alt1
- Version 5.0.0.6

* Wed Dec 19 2012 Andrey Cherepanov <cas@altlinux.org> 5.0.0.5-alt1
- New version 5.0.0.5

* Mon Aug 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.0.3-alt1
- Initial build for ALT Linux

