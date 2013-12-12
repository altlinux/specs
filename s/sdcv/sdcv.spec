Name: sdcv
Version: 0.5.0
Release: alt1

Summary: A console version of StarDict the international dictionary

Group: System/Internationalization
License: GPLv2
Url: http://sdcv.sourceforge.net/

Packager: Paul Wolneykien <manowar@altlinux.org>

Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: zlib-devel
BuildRequires: libreadline-devel
BuildRequires: glib2-devel >= 2.6.1

%description
The console version of StarDict the cross-platform and international
dictionary.

%prep
%setup -q -n %name-%version

%build
cmake -DCMAKE_INSTALL_PREFIX=%_usr

%make_build VERBOSE=1

mkdir locale
pushd po
for f in *.po; do \
    mkdir -m 0755 -p "../locale/${f%%.po}/LC_MESSAGES"; \
    msgfmt -o "../locale/${f%%.po}/LC_MESSAGES/%name.mo" "$f"; \
done
popd

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/*
%_man1dir/*
%_mandir/uk/man1/*

%changelog
* Thu Dec 12 2013 Paul Wolneykien <manowar@altlinux.org> 0.5.0-alt1
- Freshed up to v0.5.0 with the help of cronbuild and update-source-functions.

* Thu Dec 12 2013 Paul Wolneykien <manowar@altlinux.org> 0.4.2-alt1
- Freshed up to v0.4.2 with the help of cronbuild and update-source-functions.

