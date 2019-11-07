Name: pythia8
Version: 8.243
Release: alt1

Summary: The Lund Monte Carlo generator for High Energy Physics.

License: %gpl2plus
Group: Sciences/Physics
Url: http://home.thep.lu.se/~torbjorn/Pythia.html

Packager: Nikita Ermakov <arei@altlinux.org>

Source: %name-%version.tar
# Add DESTDIR, remove RPATH and add exclude MACOS include/._*
Patch1: alt-makefile.patch

BuildPreReq: rpm-build-licenses
BuildRequires: python3-dev gcc-c++ rsync

%description
The Pythia program is a standard tool for the generation of events in
high-energy collisions, comprising a coherent set of physics models
for the evolution from a few-body hard process to a complex
multiparticle final state.

%prep
%setup
%patch1 -p1

%build
%configure --prefix-lib=%_libdir --enable-optdebug --enable-shared
%make_build LOCAL_LIB=%_lib

%install
%makeinstall_std LOCAL_LIB=%_lib

%files
%_bindir/*
%dir %_includedir/Pythia8
%dir %_includedir/Pythia8Plugins
%_includedir/*
%_libdir/*.so
%dir %_datadir/Pythia8
%dir %_datadir/Pythia8/xmldoc
%dir %_datadir/Pythia8/phpdoc
%dir %_datadir/Pythia8/pdfdoc
%dir %_datadir/Pythia8/outref
%dir %_datadir/Pythia8/htmldoc
%_datadir/Pythia8/xmldoc/*
%_datadir/Pythia8/phpdoc/*
%_datadir/Pythia8/pdfdoc/*
%_datadir/Pythia8/outref/*
%_datadir/Pythia8/htmldoc/*
%doc AUTHORS COPYING GUIDELINES README

%changelog
* Thu Nov  7 2019 Nikita Ermakov <arei@altlinux.org> 8.243-alt1
- Initial build for ALT Linux Sisyphus.
